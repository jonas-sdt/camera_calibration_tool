import cv2
import os
import yaml
        
class CharucoCalibrationSettings():
    """ Class to hold the calibration settings for charuco calibration
    """
    
    def __init__(self, marker_size:float, marker_no:tuple, marker_dict:cv2.aruco.Dictionary):
        """ Constructor

        Args:
            marker_size (float): size of a charuco marker in mm
            marker_no (tuple): number of markers in the charuco board (h, v)
            marker_dict (cv2.aruco.Dictionary): opencv charuco marker dictionary
        """

        if marker_no[0] < 1 or marker_no[1] < 1:
            raise ValueError("Marker number must be greater than 0")
        if marker_size < 1:
            raise ValueError("Marker size must be greater than 1 mm")
        if marker_dict is None:
            raise ValueError("Marker dictionary must not be None")
        
        self.marker_size = marker_size  # in mm
        self.marker_no = marker_no      # tuple (h, v)
        self.marker_dict = marker_dict  # cv2.aruco.Dictionary_get(cv2.aruco.DICT_...)

class ChessboardCalibrationSettings():
    """ Class to hold the calibration settings for chessboard calibration
    """
    
    def __init__(self, square_size:float, board_size:tuple):
        """ Constructor

        Args:
            square_size (float): size of a chessboard square in mm
            board_size (tuple): number of squares in the chessboard (h, v)
        """
        
        if board_size[0] < 1 or board_size[1] < 1:
            raise ValueError("Board size must be greater than 0")
        if square_size < 1:
            raise ValueError("Square size must be greater than 1 mm")
        
        self.square_size = square_size  # in mm
        self.board_size = board_size    # tuple (h, v)
        
class CalibrationParameters:
    """Class to hold the calibration parameters"""
    def __init__(self):
        """ Constructor
        """
         
        # initialize everything to 0
        self.f  =0
        self.s_x=0
        self.s_y=0
        self.c_x=0
        self.c_y=0
        self.k_1=0
        self.k_2=0
        self.R  =0
        self.t  =0

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
        string_build = lambda x: f"{x}: {str(self.__dict__[x])}\n"
        return "".join(list(map(string_build,self.to_dict())))
     
class FrameGrabber():
    """FrameGrabber class for opencv camera
    """
    
    def __init__(self, cam_index:int) -> None:
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
    
    def _open_camera(self, cam_index:int):
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
        """grabs frames from the camera continously"""
        
        while(1):
            ret, frame = self.cap.read()
            self.frame = frame
            fn_end()
            
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

def _calibrate_chessboard(settings:ChessboardCalibrationSettings, frames:list) -> CalibrationParameters:
    """calibrate the camera using chessboard
    
    Args:
        settings (ChessboardCalibrationSettings): chessboard calibration settings
        frames (list): list of frames to be used for calibration
    
    Returns:
        CalibrationParameters: calibration parameters
    """

    if settings is None:
        raise ValueError("Settings must not be None")
    if frames is None:
        raise ValueError("Frames must not be None")
    
    # todo
    
    return CalibrationParameters()

def _calibrate_charuco(settings:CharucoCalibrationSettings, frames:list) -> CalibrationParameters:
    """calibrate the camera using charuco
    
    Args:
        settings (CharucoCalibrationSettings): charuco calibration settings
        frames (list): list of frames to be used for calibration
    
    Returns:
        CalibrationParameters: calibration parameters
    """
    
    if settings is None:
        raise ValueError("Settings must not be None")
    if frames is None:
        raise ValueError("Frames must not be None")
    
    # todo
    
    return CalibrationParameters()

def _print_chessboard_corners(settings:ChessboardCalibrationSettings, frame):
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
    
    ret, corners = cv2.findChessboardCorners(gray, settings.board_size, None)
    
    if ret:
        cv2.drawChessboardCorners(frame, settings.board_size, corners, ret)
        return frame
    else:
        raise RuntimeError("Chessboard corners not found")

def _print_charuco_corners(settings:CharucoCalibrationSettings, frame):
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
    
    ret, corners = cv2.findChessboardCorners(gray, settings.board_size, None)
    
    if ret:
        cv2.drawChessboardCorners(frame, settings.board_size, corners, ret)
        return frame
    else:
        raise RuntimeError("Charuco corners not found")

class CameraCalibrator():
    """opencv camera calibration class for chessboard and charuco calibration
    """
    
    print_chessboard_corners = staticmethod(_print_chessboard_corners)
    
    print_charuco_corners = staticmethod(_print_charuco_corners)
    
    calibrate_chessboard = staticmethod(_calibrate_chessboard)
    
    calibrate_charuco = staticmethod(_calibrate_charuco)   

def list_available_cameras(exception:list) -> list:
        """lists all available cameras
        
        Args:
            exception (list): list of camera indexes to be excluded from getting tested
        
        Returns:
            list: list of available cameras
        """
        
        non_working_ports = []
        dev_port = 0
        working_ports = []
        while len(non_working_ports) < 6: # if there are more than 5 non working ports stop the testing. 
            if not dev_port in exception:
                camera = cv2.VideoCapture(dev_port)
                if not camera.isOpened():
                    non_working_ports.append(dev_port)
                else:
                    is_reading, img = camera.read()
                    w = camera.get(3)
                    h = camera.get(4)
                    if is_reading:
                        working_ports.append(dev_port)
                dev_port +=1
        return working_ports
    
def save_config(params:CalibrationParameters, path:str=os.getcwd()):
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