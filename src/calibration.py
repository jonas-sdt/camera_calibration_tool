import cv2
import os
import yaml
import time
import datetime
import numpy as np
from dataclasses import dataclass, field

def print_red(string):
    print(f"\033[91m{string}\033[0m")
def print_blue(string):
    print(f"\033[^4m{string}\033[0m")

@dataclass
class CharucoCalibrationSettings():
    """ Class to hold the calibration settings for charuco calibration
    """

    marker_size:float = 50.0    # in mm
    marker_no:tuple = (5,5)     # tuple (h, v)
    marker_dict:int = 0         # marker dictionary index
    
    def set_marker_dict(self, marker_dict:int):
        self._marker_dict = marker_dict
    
    def get_marker_dict(self):
        markers = { 1: cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50),
                    2: cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_100),
                    3: cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_250),
                    4: cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_1000),
                    5: cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_50),
                    6: cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_100),
                    7: cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_250),
                    8: cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_1000),
                    9: cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_50),
                    10: cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_100),
                    11: cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250),
                    12: cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_1000),
                    13: cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_7X7_50),
                    14: cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_7X7_100),
                    15: cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_7X7_250),
                    16: cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_7X7_1000)}
        return markers.get(self.marker_dict, "Invalid marker dictionary")

    marker_dict = property(get_marker_dict, set_marker_dict)

@dataclass
class ChessboardCalibrationSettings():
    """ Class to hold the calibration settings for chessboard calibration
    """
    square_size: float = 50.0  # in mm
    board_size: tuple = (9, 6)  # tuple (h, v)
    
@dataclass
class CalibrationParameters:
    """Class to hold the calibration parameters"""

    # * intrinsic parameters
    # focal length
    f_x:float = 0
    f_y:float = 0
    # pixel size
    # s_x:float = 0
    # s_y:float = 0
    # principal point
    c_x:float = 0
    c_y:float = 0
    # distortion coefficients
    k_1:float = 0
    k_2:float = 0
    p_1:float = 0
    p_2:float = 0
    k_3:float = 0


    def to_dict(self):
        """ Converts all parameter to a dictionary
        """
        return self.__dict__

    def __iter__(self):
        """ Iterator for the class
        """
        return iter(self.__dict__.keys())

    def __str__(self):
        """ String representation of the class in yaml format
        """
        def string_build(x): return f"{x}: {str(self.__dict__[x])}\n"
        return "".join(list(map(string_build, self.to_dict())))


class FrameGrabber():
    """FrameGrabber class for opencv camera
    """

    def __init__(self, cam_index: int) -> None:
        """Constructor

        Args:
            cam_index (int): index of the camera (starts from 0)
        """

        if cam_index is None:
            raise ValueError("Camera index must not be None")

        self.frame = self._open_camera(cam_index)

    def __del__(self):
        """releases the camera when the object is deleted
        """
        self.cap.release()

    def _open_camera(self, cam_index: int):
        """opens an opencv camera video capture

        Args:
            cam_index (int): index of the camera (starts from 0)

        Returns:
            image: first frame of the camera
        """

        self.cap = cv2.VideoCapture(cam_index)
        ret, frame = self.cap.read()
        self.frame = frame
        return frame

    def video_stream(self, fn_end, kwargs):
        """grabs frames from the camera continuously"""

        while not kwargs[0].stop_capture:
            ret, frame = self.cap.read()
            self.frame = frame
            kwargs[0].frame = frame
            if fn_end is not None:
                fn_end(frame, kwargs[1:])
        self.__del__()

    def get_frame_size(self):
        """gets the size of the frame

        Returns:
            tuple: size of the frame
        """

        return self.frame.shape


class CalibrationImages():
    """opencv frames for calibration
    """

    def __init__(self) -> None:
        """Constructor
        """
        self.frames = []

    def save_image(self, index: int, path: str):
        """saves an image to disk"""
        if path[-1] != "/":
            path += "/"
        cv2.imwrite(
            f"{path}img-{index}_{datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day}_{datetime.datetime.now().hour}-{datetime.datetime.now().minute}.png", self.frames[index])


def _calibrate_chessboard(settings: ChessboardCalibrationSettings, frames: list) -> CalibrationParameters:
    """calibrate the camera using chessboard

    Args:
        settings (ChessboardCalibrationSettings): chessboard calibration settings
        frames (list): list of frames to be used for calibration

    Returns:
        CalibrationParameters: calibration parameters
    """

    if settings is None or type(settings) != ChessboardCalibrationSettings:
        raise ValueError("Settings must be of type ChessboardCalibrationSettings")
    if frames is None:
        raise ValueError("Frames must not be None")

    # calibration with cv2
    gray_frames = [cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) for frame in frames]
    
    objp = np.zeros(((settings.board_size[0]-1)*(settings.board_size[1]-1), 3), np.float32)
    objp[:, :2] = np.mgrid[0:(settings.board_size[0]-1), 0:(settings.board_size[1]-1)].T.reshape(-1, 2)
    
    # Arrays to store object points and image points from all the images.
    objpoints = [] # 3d point in real world space
    imgpoints = [] # 2d points in image plane.
    failed_cnt = 0
    for frame in gray_frames:
        ret, corners = cv2.findChessboardCorners(frame, list((i-1 for i in settings.board_size)))
        
        if ret == True:
            objpoints.append(objp)
            corners2 = cv2.cornerSubPix(frame, corners, (11, 11), (-1, -1), (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
)
            imgpoints.append(corners2)
        else:
            failed_cnt += 1
    if len(frames) - failed_cnt < 10:
        print_red("Calibration failed: Chessboard Corners not found in enough images")
        raise cv2.error
    
    try:
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, frame.shape[0:2], None, None)
    except cv2.error as e:
        print_red("Calibration failed")
        raise e
    
    if not ret == False:
        calibration_parameters = CalibrationParameters()
        # * intrinsic parameters
        calibration_parameters.f_x = mtx[0][0]
        calibration_parameters.f_y = mtx[1][1]
        calibration_parameters.c_x = mtx[0][2]
        calibration_parameters.c_y = mtx[1][2]
        # calibration_parameters.s_x = mtx[0][1]
        # calibration_parameters.s_y = mtx[1][1]
        # distortion coefficients
        calibration_parameters.k_1 = dist[0][0]
        calibration_parameters.k_2 = dist[0][1]
        calibration_parameters.p_1 = dist[0][2]
        calibration_parameters.p_2 = dist[0][3]
        calibration_parameters.k_3 = dist[0][4]
        
        # * extrinsic parameters
        # R = rvecs[0]
        # t = (tvecs[0][0][0], tvecs[0][0][1], tvecs[0][0][2])
        
        return calibration_parameters

    else:
        print_red("Calibration failed")
        raise cv2.error


def _calibrate_charuco(settings: CharucoCalibrationSettings, frames: list) -> CalibrationParameters:
    """calibrate the camera using charuco

    Args:
        settings (CharucoCalibrationSettings): charuco calibration settings
        frames (list): list of frames to be used for calibration

    Returns:
        CalibrationParameters: calibration parameters
    """

    if settings is None or type(settings) != CharucoCalibrationSettings:
        raise ValueError("Settings must be of type CharucoCalibrationSettings")
    if frames is None:
        raise ValueError("Frames must not be None")

    # calibration with cv2
    board = cv2.aruco.CharucoBoard_create(
        squaresX=settings.marker_no[0],
        squaresY=settings.marker_no[1],
        squareLength=settings.marker_size*2,
        markerLength=settings.marker_size,
        dictionary=settings.marker_dict
    )
    
    gray_frames = [cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) for frame in frames]
        
    allCorners = []
    allIds = []
    decimator = 0
    for gray in gray_frames:

        res = cv2.aruco.detectMarkers(gray,settings.marker_dict)

        if len(res[0])>0:
            res2 = cv2.aruco.interpolateCornersCharuco(res[0],res[1],gray,board)
            if res2[1] is not None and res2[2] is not None and len(res2[1])>3 and decimator%3==0:
                allCorners.append(res2[1])
                allIds.append(res2[2])

        decimator+=1

    imsize = gray_frames[0].shape

    try:
        cal = cv2.aruco.calibrateCameraCharuco(allCorners,allIds,board,imsize,None,None)
        
        calibration_parameters = CalibrationParameters()
        calibration_parameters.f_x = cal[1][0][0]
        calibration_parameters.f_y = cal[1][1][1]
        calibration_parameters.c_x = cal[1][0][2]
        calibration_parameters.c_y = cal[1][1][2]
        # calibration_parameters.s_x = cal[1][0][1]
        # calibration_parameters.s_y = cal[1][1][1]
        calibration_parameters.k_1 = cal[2][0][0]
        calibration_parameters.k_2 = cal[2][0][1]
        calibration_parameters.p_1 = cal[2][0][2]
        calibration_parameters.p_2 = cal[2][0][3]
        calibration_parameters.k_3 = cal[2][0][4]
        calibration_parameters.R = cal[3]
        calibration_parameters.t = cal[4]
        
        return calibration_parameters
    
        
    except cv2.error as e:
        print_red("Calibration failed")
        raise e


def _print_chessboard_corners(settings: ChessboardCalibrationSettings, frame):
    """Visualizes the chessboard corners on the frame

    Args:
        settings (ChessboardCalibrationSettings): chessboard calibration settings
        frame (image): frame to be used for visualization

    Raises:
        RuntimeError: if chessboard corners are not found

    Returns:
        frame: frame with chessboard corners 
    """

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    painted_frame = frame.copy()

    ret, corners = cv2.findChessboardCorners(gray, list((i-1 for i in settings.board_size)), None)

    if ret:
        return cv2.drawChessboardCorners(painted_frame, list((i-1 for i in settings.board_size)), corners, ret)
    else:
        raise cv2.error()


def _print_charuco_corners(settings: CharucoCalibrationSettings, frame):
    """Visualizes the charuco corners on the frame

    Args:
        settings (CharucoCalibrationSettings): charuco calibration settings
        frame (image): frame to be used for visualization

    Raises:
        RuntimeError: if charuco corners are not found

    Returns:
        frame: frame with charuco corners 
    """

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    painted_frame = frame.copy()
    board = cv2.aruco.CharucoBoard_create(settings.marker_no[0], settings.marker_no[1], settings.marker_size*2, settings.marker_size, settings.marker_dict)
    res = cv2.aruco.detectMarkers(gray, settings.marker_dict)
    res2 = cv2.aruco.interpolateCornersCharuco(res[0], res[1], gray, board)
    cv2.aruco.drawDetectedCornersCharuco(painted_frame, res2[1], res2[2])
    cv2.aruco.drawDetectedMarkers(painted_frame, res[0], res[1])
    return painted_frame


class CameraCalibrator():
    """opencv camera calibration class for chessboard and charuco calibration
    """

    print_chessboard_corners = staticmethod(_print_chessboard_corners)

    print_charuco_corners = staticmethod(_print_charuco_corners)

    calibrate_chessboard = staticmethod(_calibrate_chessboard)

    calibrate_charuco = staticmethod(_calibrate_charuco)


def list_available_cameras(exception: list) -> list:
    """lists all available cameras

    Args:
        exception (list): list of camera indexes to be excluded from getting tested

    Returns:
        list: list of available cameras
    """

    non_working_ports = []
    dev_port = 0
    working_ports = []
    while len(non_working_ports) < 6:
        if not dev_port in exception:
            try:
                camera = cv2.VideoCapture(dev_port)
            except:
                pass
            if not camera.isOpened():
                non_working_ports.append(dev_port)
            else:
                is_reading, img = camera.read()
                w = camera.get(3)
                h = camera.get(4)
                if is_reading:
                    working_ports.append(dev_port)
            dev_port += 1
    return working_ports


def save_config(params: CalibrationParameters, path: str = os.getcwd()):
    """Save the calibration parameters to a yaml file

    Args:
        params (): calibration parameters
        path (str, optional): path to save the file. Defaults to os.getcwd().
    """
    parameters = yaml.safe_load(str(params))

    try:
        with open(f'{path}', 'w') as file:
            yaml.dump(parameters, file)
    except:
        raise RuntimeError()


def autocapture(fn_end: callable, kwargs):
    """autocapture routine

    Args:
        fn_end (callable): function to be called at the end of the autocapture
        kwargs (gui): gui object
    """
    for i in range(kwargs.ui.spinBox_img_no.value()):
        start_time = time.time()
        kwargs.ui.pushButton_capture.click()
        kwargs.ui.progressBar_img_cnt.setValue(
            kwargs.ui.progressBar_img_cnt.value()+1)
        
        while time.time() - start_time < kwargs.ui.spinBox_delay_seconds.value():
            if kwargs.stop_autocapture:
                return
    kwargs.gui_states['AutotimerStopped'].activate(reset_fn=None, gui=kwargs)


def load_imgs(img_paths: list) -> list:
    """load images from disk with opencv

    Args:
        img_paths (list): str list of image paths

    Returns:
        list: cv2 images list
    """
    imgs = list()
    for path in img_paths:
        imgs.append(cv2.imread(path))

    return imgs
