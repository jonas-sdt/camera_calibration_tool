from gui_class import Ui_MainWindow
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import QRunnable, Slot, QThreadPool
import sys
import os
from calibration import *
from qt_worker import Worker
import time

def print_red(string):
    print(f"\033[91m{string}\033[0m")
def print_blue(string):
    print(f"\033[44m{string}\033[0m")

class GUI_State():
    
    def __init__(self, fn:callable):
        """Constructor for GUI_State

        Args:
            fn (callable): run this function when this state is activated
            active_gui_elements (list): list of gui elements to be activated
            inactive_gui_elements (list, optional): list of gui elements to be deactivated. Defaults to None.
        """
        self.fn = fn
    
    def activate(self, reset_fn, gui):
        """Function to activate this state

        Args:
            reset_fn (callable): function to reset the gui if neccessary.
            gui (GUI): GUI object to be changed
        """
        if reset_fn is not None:
            reset_fn()
            
        # run the function of this state
        self.fn()
        
        gui.previous_state  = gui.current_state
        gui.current_state   = self
        
class GUI(QtWidgets.QMainWindow):
    def __init__(self, calibration_settings, calibration_parameters:CalibrationParameters, image_dir):
        
        self.calibration_settings = calibration_settings
        self.save_frame = False
        self.frame = None
        self.stop_capture = True
        self.calibration_images = CalibrationImages()
        
        # * init Qt
        self.app = QtWidgets.QApplication(sys.argv)
        super().__init__(None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # * set gui states
        self.gui_states = None
        self.current_state = None
        self._setGUIStates()
        if self.gui_states is None:
            raise ValueError("gui_states must not be None")
        self._resetGUI()
        self.gui_states["Init"].activate(self._resetGUI, self)
        
        # * set signal slots
        self._set_signal_slots()
        
        # * fill with given parameters
        if type(calibration_settings) is ChessboardCalibrationSettings:
            self.ui.tabWidget_calibration.setCurrentIndex(0)
            self.ui.spinBox_chessboard_no_squares_h.setValue(calibration_settings.board_size[0])
            self.ui.spinBox_chessboard_no_squares_v.setValue(calibration_settings.board_size[1])
        elif type(calibration_settings) is CharucoCalibrationSettings:
            self.ui.tabWidget_calibration.setCurrentIndex(1)
            self.ui.spinBox_charuco_no_markers_h.setValue(calibration_settings.marker_no[0])
            self.ui.spinBox_charuco_no_markers_v.setValue(calibration_settings.marker_no[1])
            self.ui.comboBox_marker_dict.setCurrentText(calibration_settings.marker_dict)

        # * set image dir
        self.ui.lineEdit_path.setText(image_dir)
        
        # * set calibration parameters
        self.calibration_parameters = calibration_parameters
        
        # * search for cameras and fill combobox
        self.ui.pushButton_camera_search.click()
        
        # * start gui
        self._start_gui()
    
    def _start_gui(self):
        """Starts the Qt GUI - this function runs until the GUI is closed"""
        self.show()
        exit_code = self.app.exec_()
        sys.exit(exit_code)
    
    def update_frame(self, frame, kwargs):
        """Updates the frame in the GUI"""
        
        if self.save_frame is True:
            self.frame = frame
            
        try:
            if type(self.calibration_settings) is ChessboardCalibrationSettings:
                frame = CameraCalibrator.print_chessboard_corners(self.calibration_settings, frame)
            elif type(self.calibration_settings) is CharucoCalibrationSettings:
                frame = CameraCalibrator.print_charuco_corners(self.calibration_settings, frame)
            else:
                raise ValueError("Unknown calibration settings type")
        except:
            pass
        height, width, channel = frame.shape
        bytesPerLine = 3 * width
        cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)
        qImg = QtGui.QImage(frame.data, width, height, bytesPerLine, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qImg)
        self.ui.cameraView.setPixmap(pixmap)

    ##################
    ### GUI states ###        
    ##################

    def _setGUIStates(self):
        
        self.gui_states = {
            "Reset":                    GUI_State(self._resetGUI),
            "Init":                     GUI_State(self._initGUI),
            "CameraNotSelected":        GUI_State(self._stateCameraNotSelected),
            "CameraSelected":           GUI_State(self._stateCameraSelected),
            "SaveImagesChecked":        GUI_State(self._stateSaveImagesChecked),
            "UseSavedImagesChecked":    GUI_State(self._stateUseSavedImagesChecked),
            "AutotimerStarted":         GUI_State(self._stateAutotimerStarted),
            "AutotimerStopped":         GUI_State(self._stateAutotimerStopped),
            "ParametersDetermined":     GUI_State(self._stateParametersDetermined),
        }
    
    def _resetGUI(self):
        self.stop_autocapture = True
        self.stop_capture = True
        """resets the gui to the default state
        """
        deactivate = [self.ui.checkBox_save_images,
                      self.ui.lineEdit_path,
                      self.ui.pushButton_path_window,
                      self.ui.pushButton_path_window,
                      self.ui.pushButton_capture,
                      self.ui.pushButton_select_images,
                      self.ui.listWidget_imgs,
                      self.ui.pushButton_delete_last,
                      self.ui.pushButton_delete_all,
                      self.ui.pushButton_determ_param,
                      self.ui.pushButton_save_param,
                      self.ui.checkBox_save_images,
                      self.ui.pushButton_start_autotimer]
        
        for element in deactivate:
            element.setEnabled(False)
        
        self.ui.listWidget_imgs.clear()
        self.ui.cameraView.clear()
        self.ui.cameraView.setText("No camera / image selected")
        
        self.ui.spinBox_img_no.setValue(0)
        self.ui.lineEdit_path.setText(str(os.getcwd()))
        if not self.calibration_settings is None:
            if type(self.calibration_settings) is CharucoCalibrationSettings:
                self.ui.spinBox_charuco_no_markers_v.setValue(self.calibration_settings.marker_no[1])
                self.ui.spinBox_charuco_no_markers_h.setValue(self.calibration_settings.marker_no[0])
                self.ui.comboBox_marker_dict.setCurrentText(self.calibration_settings.marker_dict)
            elif type(self.calibration_settings) is ChessboardCalibrationSettings:
                self.ui.doubleSpinBox_sqare_size.setValue(self.calibration_settings.square_size/10)
                self.ui.spinBox_chessboard_no_squares_v.setValue(self.calibration_settings.board_size[1])
                self.ui.spinBox_chessboard_no_squares_h.setValue(self.calibration_settings.board_size[0])
            else:
                raise Exception("Unknown calibration settings type")
            
        else:
            self.ui.doubleSpinBox_sqare_size.setValue(0.00)
            self.ui.spinBox_chessboard_no_squares_v.setValue(0)
            self.ui.spinBox_chessboard_no_squares_h.setValue(0)
            self.ui.doubleSpinBox_marker_size.setValue(0.00)
            self.ui.spinBox_charuco_no_markers_v.setValue(0)
            self.ui.spinBox_charuco_no_markers_h.setValue(0)
            self.ui.comboBox_marker_dict.setCurrentIndex(0)
            
            self.ui.tabWidget_calibration

    def _initGUI(self):
        self.ui.comboBox_camera.setEnabled(True)
        # ! Deactivate the camera selection for now
        # available_cameras = list_available_cameras([])
        # self.ui.comboBox_camera.addItems(available_cameras)
    
    def _stateCameraNotSelected(self):
        self.stop_capture = True
        self.ui.comboBox_camera.setEnabled(True)
        
    def _stateCameraSelected(self):
        self.stop_capture = False
        self.ui.checkBox_save_images.setEnabled(True)
        self.ui.pushButton_capture.setEnabled(True)
        self.ui.pushButton_start_autotimer.setEnabled(True)
        self.ui.spinBox_delay_seconds.setEnabled(True)

    def _stateSaveImagesChecked(self):
        self.ui.checkBox_save_images.setEnabled(True)
        self.ui.lineEdit_path.setEnabled(True)
        self.ui.pushButton_capture.setEnabled(True)
        self.ui.pushButton_path_window.setEnabled(True)

    def _stateUseSavedImagesChecked(self):
        self.ui.comboBox_camera.setEnabled(False)
        self.ui.pushButton_capture.setEnabled(False)
        self.ui.pushButton_select_images.setEnabled(True)
    
    def _stateAutotimerStarted(self):
        self.ui.checkBox_save_images.setEnabled(False)
        self.ui.comboBox_camera.setEnabled(False)
        self.ui.lineEdit_path.setEnabled(False)
        self.ui.listWidget_imgs.setEnabled(True)
        self.ui.progressBar_img_cnt.setEnabled(True)
        self.ui.progressBar_img_cnt.setMaximum(self.ui.spinBox_img_no.value())
        self.ui.pushButton_camera_search.setEnabled(False)
        self.ui.pushButton_capture.setEnabled(False)
        self.ui.pushButton_delete_all.setEnabled(False)
        self.ui.pushButton_delete_last.setEnabled(False)
        self.ui.pushButton_start_autotimer.setEnabled(True)
        self.ui.pushButton_start_autotimer.setText("Stop Self Timer")
        self.ui.spinBox_delay_seconds.setEnabled(False)
        self.ui.spinBox_img_no.setEnabled(False)
        self.ui.tabWidget_calibration.setEnabled(False)
        self.ui.tabWidget_source.setTabEnabled(1, False)
    
    def _stateAutotimerStopped(self):
        self.ui.checkBox_save_images.setEnabled(True)
        self.ui.comboBox_camera.setEnabled(True)
        self.ui.lineEdit_path.setEnabled(True)
        self.ui.listWidget_imgs.setEnabled(True)
        self.ui.progressBar_img_cnt.setEnabled(True)
        self.ui.pushButton_camera_search.setEnabled(True)
        self.ui.pushButton_capture.setEnabled(True)
        self.ui.pushButton_delete_all.setEnabled(True)
        self.ui.pushButton_delete_last.setEnabled(True)
        self.ui.pushButton_start_autotimer.setEnabled(True)
        self.ui.pushButton_start_autotimer.setText("Start Self Timer")
        self.ui.spinBox_delay_seconds.setEnabled(True)
        self.ui.spinBox_img_no.setEnabled(True)
        self.ui.tabWidget_calibration.setEnabled(True)
        self.ui.tabWidget_source.setTabEnabled(1, True)
    
    def _stateParametersDetermined(self):
        # fill tableWidget with parameters
        self.ui.tableWidget_parameters.setItem(0,1,QtWidgets.QTableWidgetItem(str(f"({self.calibration_parameters.f_x}, {self.calibration_parameters.f_y})")))
        self.ui.tableWidget_parameters.setItem(1,1,QtWidgets.QTableWidgetItem(str(f"({self.calibration_parameters.c_x}, {self.calibration_parameters.c_y})")))
        self.ui.tableWidget_parameters.setItem(2,1,QtWidgets.QTableWidgetItem(str(self.calibration_parameters.k_1)))
        self.ui.tableWidget_parameters.setItem(3,1,QtWidgets.QTableWidgetItem(str(self.calibration_parameters.k_2)))
        self.ui.tableWidget_parameters.setItem(4,1,QtWidgets.QTableWidgetItem(str(self.calibration_parameters.p_1)))
        self.ui.tableWidget_parameters.setItem(5,1,QtWidgets.QTableWidgetItem(str(self.calibration_parameters.p_2)))
        self.ui.tableWidget_parameters.setItem(6,1,QtWidgets.QTableWidgetItem(str(self.calibration_parameters.k_3)))
        self.ui.pushButton_save_param.setEnabled(True)


    #####################
    ####### slots #######
    #####################

    def _set_signal_slots(self):
        """Set the signal slots for the GUI elements
        """
        self.ui.comboBox_camera.currentIndexChanged.connect(self._slot_comboBox_camera_changed)
        self.ui.pushButton_camera_search.clicked.connect(self._slot_pushButton_camera_search_pushed)
        self.ui.checkBox_use_saved_images.stateChanged.connect(self._slot_checkBox_use_saved_images_checked)
        self.ui.pushButton_select_images.clicked.connect(self._slot_pushButton_select_images_pushed)
        self.ui.checkBox_save_images.stateChanged.connect(self._slot_checkBox_save_images_checked)
        self.ui.pushButton_path_window.clicked.connect(self._slot_pushButton_path_window_pushed)
        self.ui.pushButton_start_autotimer.clicked.connect(self._slot_pushButton_start_autotimer_pushed)
        self.ui.pushButton_capture.clicked.connect(self._slot_pushButton_capture_pushed)
        self.ui.listWidget_imgs.itemClicked.connect(self._slot_listWidget_imgs_itemClicked)
        self.ui.pushButton_delete_last.clicked.connect(self._slot_pushButton_delete_last_pushed)
        self.ui.pushButton_delete_all.clicked.connect(self._slot_pushButton_delete_all_pushed)
        self.ui.pushButton_determ_param.clicked.connect(self._slot_pushButton_determ_param_pushed)
        self.ui.pushButton_save_param.clicked.connect(self._slot_pushButton_save_param_pushed)
        self.ui.tabWidget_calibration.currentChanged.connect(self._slot_tabWidget_calibration_changed)
        self.ui.spinBox_chessboard_no_squares_h.valueChanged.connect(self._slot_spinBox_chessboard_no_squares_h_changed)
        self.ui.spinBox_chessboard_no_squares_v.valueChanged.connect(self._slot_spinBox_chessboard_no_squares_v_changed)
        self.ui.doubleSpinBox_sqare_size.valueChanged.connect(self._slot_doubleSpinBox_sqare_size_changed)
        self.ui.spinBox_charuco_no_markers_h.valueChanged.connect(self._slot_spinBox_charuco_no_markers_h_changed)
        self.ui.spinBox_charuco_no_markers_v.valueChanged.connect(self._slot_spinBox_charuco_no_markers_v_changed)
        self.ui.doubleSpinBox_marker_size.valueChanged.connect(self._slot_doubleSpinBox_marker_size_changed)
        self.ui.comboBox_marker_dict.currentIndexChanged.connect(self._slot_comboBox_marker_dict_changed)
    
    def _slot_comboBox_camera_changed(self):
        """Event handler for: comboBox_camera if the index changes
        """
        self.stop_capture = True
        #if index == 0:
        if self.ui.comboBox_camera.currentIndex() == 0:
            self.gui_states['CameraNotSelected'].activate(reset_fn=self._resetGUI,gui=self)
        else:
            self.gui_states['CameraSelected'].activate(reset_fn=self._resetGUI,gui=self)
            try:
                if self.ui.comboBox_camera.currentText() != "":
                    self.stop_capture = False
                    self.frame_grabber = FrameGrabber(int(self.ui.comboBox_camera.currentText()[-1:]))
                    self.video_stream_thread = Worker(self.frame_grabber.video_stream, self.update_frame, [self, self.calibration_settings])
                    self.threadpool = QThreadPool()
                    self.threadpool.start(self.video_stream_thread)
            except Exception as e:
                print(e)
                self.ui.comboBox_camera.setCurrentIndex(0)

    def _slot_pushButton_camera_search_pushed(self):
        """Event handler for: pushButton_camera_search if pushed
        """
        self.stop_capture = True
        available_cameras = list_available_cameras([])
        if len(available_cameras) == 0:
            self.ui.comboBox_camera.clear()
            self.ui.comboBox_camera.addItem("")
            self.ui.comboBox_camera.addItem("No cameras found")
            self.ui.comboBox_camera.setCurrentIndex(0)
            self.ui.comboBox_camera.model().item(1).setEnabled(False)
        else:
            self.ui.comboBox_camera.clear()
            self.ui.comboBox_camera.addItem("")
            for camera in available_cameras:
                self.ui.comboBox_camera.addItem("Camera: " + str(camera))
        
        self.gui_states['CameraNotSelected'].activate(reset_fn=self._resetGUI, gui=self)
        
    def _slot_checkBox_use_saved_images_checked(self):
        """Event handler for: checkBox_use_saved_images if checked/unchecked
        """
        
        self.ui.comboBox_camera.clear()
        self.ui.comboBox_camera.addItem("")
        
        self.stop_capture = True
        time.sleep(0.1)
        self.ui.cameraView.setText("No camera / image selected")
        if self.ui.checkBox_use_saved_images.isChecked():
            self.gui_states['UseSavedImagesChecked'].activate(reset_fn=self._resetGUI, gui=self)
        
        else:
            self.gui_states['CameraNotSelected'].activate(reset_fn=self._resetGUI, gui=self)
        
    def _slot_pushButton_select_images_pushed(self):
        """Event handler for: pushButton_select_images if pushed
        """
        imgs = QtWidgets.QFileDialog.getOpenFileNames(self, "Select Images", "", "Image Files (*.png *.jpg *.bmp)")[0]
        try:
            self.calibration_images.frames = load_imgs(imgs)
            self.ui.listWidget_imgs.setEnabled(True)
            self.ui.listWidget_imgs.addItems("Image " + str(i) for i in range(len(self.calibration_images.frames)))
            self.ui.pushButton_delete_all.setEnabled(True)
            self.ui.pushButton_delete_last.setEnabled(True)
            if self.ui.listWidget_imgs.count() > 5:
                self.ui.pushButton_determ_param.setEnabled(True)
        except:
            pass
        
    def _slot_checkBox_save_images_checked(self):
        """Event handler for: checkbox to save images
        if the checkbox is checked, the state is changed to SaveImagesChecked
        else the previous state is activated
        """
        if self.ui.checkBox_save_images.isChecked():
            self.gui_states['SaveImagesChecked'].activate(reset_fn=None, gui=self)
        else:
            self.previous_state.activate(reset_fn=self._resetGUI, gui=self)
        
    def _slot_pushButton_path_window_pushed(self):
        """Event handler for: pushButton_path_window if pushed
        """
        self.ui.lineEdit_path.setText(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))
    
    def _slot_pushButton_start_autotimer_pushed(self):
        """Event handler for: pushButton_start_autotimer if pushed
        """
        if self.ui.pushButton_start_autotimer.text() == "Start Self Timer":
            self.stop_capture = False
            self.gui_states['AutotimerStarted'].activate(reset_fn=None, gui=self)
            self.capture_thread = Worker(autocapture, self.update_frame, self)
            self.threadpool_autotimer = QThreadPool()
            self.threadpool_autotimer.start(self.capture_thread)
        else:
            self.stop_autocapture = True
            self.previous_state.activate(reset_fn=self._resetGUI, gui=self)
    
    def _slot_pushButton_capture_pushed(self):
        """Event handler for: pushButton_capture if pushed
        """
        self.ui.listWidget_imgs.setEnabled(True)
        self.ui.pushButton_delete_last.setEnabled(True)
        self.ui.pushButton_delete_all.setEnabled(True)
        self.stop_capture = False
        self.calibration_images.frames.append(self.frame)
        
        self.ui.listWidget_imgs.addItem("Image " + str(len(self.calibration_images.frames)))
        
        # check if chessboard corners can be found in image
        if type(self.calibration_settings)==ChessboardCalibrationSettings:
            ret, corners = cv2.findChessboardCorners(self.frame, list((i-1 for i in self.calibration_settings.board_size)))
        
            if not ret:
                # change label to red
                self.ui.listWidget_imgs.item(len(self.calibration_images.frames)-1).setForeground(QtGui.QColor(255, 0, 0))
        
        if self.ui.checkBox_save_images.isChecked():
            self.calibration_images.save_image(len(self.calibration_images.frames)-1, self.ui.lineEdit_path.text())
            
        if len(self.calibration_images.frames) > 10 and self.stop_autocapture is not False:
            self.ui.pushButton_determ_param.setEnabled(True)
    
    def _slot_listWidget_imgs_itemClicked(self):
        """Event handler for: listWidget_imgs if item is clicked
        """
        if self.ui.checkBox_use_saved_images.isChecked():
            self.update_frame(self.calibration_images.frames[self.ui.listWidget_imgs.currentRow()], None)
    
    def _slot_pushButton_delete_all_pushed(self):
        """Event handler for: pushButton_delete_all if pushed
        """
        self.calibration_images.frames.clear()
        self.ui.listWidget_imgs.clear()
        
        # check if list is empty and disable buttons
        if self.ui.listWidget_imgs.count() == 0:
            self.ui.pushButton_delete_all.setEnabled(False)
            self.ui.pushButton_delete_last.setEnabled(False)
            self.ui.pushButton_determ_param.setEnabled(False)
            
        elif self.ui.listWidgecalibration_framest_imgs.count() < 5:
            self.ui.pushButton_determ_param.setEnabled(False)
        elif self.ui.listWidget_imgs.count() > 5:
            self.ui.pushButton_determ_param.setEnabled(True)
    
    def _slot_pushButton_delete_last_pushed(self):
        """Event handler for: pushButton_delete_last if pushed
        """
        self.calibration_images.frames.pop()
        self.ui.listWidget_imgs.takeItem(self.ui.listWidget_imgs.count()-1)
        # check if list is empty and disable buttons
        if self.ui.listWidget_imgs.count() == 0:
            self.ui.pushButton_delete_all.setEnabled(False)
            self.ui.pushButton_delete_last.setEnabled(False)
            self.ui.pushButton_determ_param.setEnabled(False)
            
        elif self.ui.listWidget_imgs.count() < 5:
            self.ui.pushButton_determ_param.setEnabled(False)
        elif self.ui.listWidget_imgs.count() > 5:
            self.ui.pushButton_determ_param.setEnabled(True)
    
    def _slot_tabWidget_calibration_changed(self):
        """Event handler for: tabWidget_calibration if entry is changed
        """
        if self.ui.tabWidget_calibration.currentIndex() == 0:
            self.calibration_settings = ChessboardCalibrationSettings(self.ui.doubleSpinBox_sqare_size.value()*10, (self.ui.spinBox_chessboard_no_squares_h.value(), self.ui.spinBox_chessboard_no_squares_v.value()))
        elif self.ui.tabWidget_calibration.currentIndex() == 1:
            self.calibration_settings = CharucoCalibrationSettings(self.ui.doubleSpinBox_marker_size.value(), (self.ui.spinBox_charuco_no_markers_h.value(),self.ui.spinBox_charuco_no_markers_v.value()), self.ui.comboBox_marker_dict.currentIndex())
        else:
            raise ValueError("Unknown calibration type")
    
    def _slot_spinBox_chessboard_no_squares_h_changed(self):
        """Event handler for: spinBox_chessboard_no_squares_h if value changed
        """
        self.calibration_settings = ChessboardCalibrationSettings(self.ui.doubleSpinBox_sqare_size.value()*10, (self.ui.spinBox_chessboard_no_squares_h.value(), self.ui.spinBox_chessboard_no_squares_v.value()))
    
    def _slot_spinBox_chessboard_no_squares_v_changed(self):
        """Event handler for: spinBox_chessboard_no_squares_v if value changed
        """
        self.calibration_settings = ChessboardCalibrationSettings(self.ui.doubleSpinBox_sqare_size.value()*10, (self.ui.spinBox_chessboard_no_squares_h.value(), self.ui.spinBox_chessboard_no_squares_v.value()))
    
    def _slot_doubleSpinBox_sqare_size_changed(self):
        """Event handler for: doubleSpinBox_sqare_size if value changed
        """
        self.calibration_settings = ChessboardCalibrationSettings(self.ui.doubleSpinBox_sqare_size.value()*10, (self.ui.spinBox_chessboard_no_squares_h.value(), self.ui.spinBox_chessboard_no_squares_v.value()))
    
    def _slot_spinBox_charuco_no_markers_h_changed(self):
        """Event handler for: spinBox_charuco_no_markers_h if value changed
        """
        self.calibration_settings = CharucoCalibrationSettings(self.ui.doubleSpinBox_marker_size.value(), (self.ui.spinBox_charuco_no_markers_h.value(), self.ui.spinBox_charuco_no_markers_v.value()), self.ui.comboBox_marker_dict.currentIndex())
        
    def _slot_spinBox_charuco_no_markers_v_changed(self):
        """Event handler for: spinBox_charuco_no_markers_v if value changed
        """
        self.calibration_settings = CharucoCalibrationSettings(self.ui.doubleSpinBox_marker_size.value(), (self.ui.spinBox_charuco_no_markers_h.value(), self.ui.spinBox_charuco_no_markers_v.value()), self.ui.comboBox_marker_dict.currentIndex())
    
    def _slot_doubleSpinBox_marker_size_changed(self):
        """Event handler for: doubleSpinBox_marker_size if value changed
        """
        self.calibration_settings = CharucoCalibrationSettings(self.ui.doubleSpinBox_marker_size.value(), (self.ui.spinBox_charuco_no_markers_h.value(), self.ui.spinBox_charuco_no_markers_v.value()), self.ui.comboBox_marker_dict.currentIndex())
        
    def _slot_comboBox_marker_dict_changed(self):
        """Event handler for: comboBox_marker_dict if value changed
        """
        self.calibration_settings = CharucoCalibrationSettings(self.ui.doubleSpinBox_marker_size.value(), (self.ui.spinBox_charuco_no_markers_h.value(), self.ui.spinBox_charuco_no_markers_v.value()), self.ui.comboBox_marker_dict.currentIndex())
    
    def _slot_pushButton_determ_param_pushed(self):
        """Event handler for: pushButton_determ_param if pushed
        """
        if self.calibration_settings is None:
            raise ValueError("No calibration settings defined")
        elif type(self.calibration_settings) is ChessboardCalibrationSettings:
            self.calibration_parameters = CameraCalibrator.calibrate_chessboard(self.calibration_settings, self.calibration_images.frames)
            self.gui_states["ParametersDetermined"].activate(reset_fn=None,gui=self)
        elif type(self.calibration_settings) is CharucoCalibrationSettings:
            self.calibration_parameters = CameraCalibrator.calibrate_charuco(self.calibration_settings, self.calibration_images.frames)
            self.gui_states["ParametersDetermined"].activate(reset_fn=None,gui=self)
        else:
            raise ValueError("Unknown calibration type")
    
    def _slot_pushButton_save_param_pushed(self):
        """Event handler for: pushButton_save_param if pushed
        """
        path = QtWidgets.QFileDialog.getSaveFileName(self, "Save Parameters", "", "Parameter Files (*.json)")[0]
        # if path doesn't end with .yaml, add it
        path = path if path.endswith(".json") else path + ".json"
        save_config(self.calibration_parameters, path)
    