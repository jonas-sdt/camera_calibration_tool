from gui_class import Ui_MainWindow
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtCore import QRunnable, Slot, QThreadPool
import sys
import os
from calibration import *
from qt_worker import Worker

class GUI_State():
    def __init__(self, fn:callable, active_gui_elements:list, inactive_gui_elements:list=None):
        self.fn = fn
        self.inactive_gui_elements = inactive_gui_elements if inactive_gui_elements is not None else []
        self.active_gui_elements = []
    
    def activate(self, reset_fn, gui):
        
        reset_fn()    
        
        # deactivate the elements of this state
        for element in self.inactive_gui_elements:
            element.setEnabled(False)
        
        # only activate the elements of this state
        for element in self.active_gui_elements:
            element.setEnabled(True)
            
        # run the function of this state
        self.fn()
        
        gui.previous_state  = gui.current_state
        gui.current_state   = self
        
class GUI(QtWidgets.QMainWindow):
    def __init__(self):
        
        # * init variables
        self.calibration_settings = None
        
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
        
        # * start gui
        self._start_gui()
    
    def _start_gui(self):
        """Starts the Qt GUI - this function runs until the GUI is closed"""
        self.show()
        exit_code = self.app.exec_()
        self._stop()
        sys.exit(exit_code)
        
    def _stop(self):
        """Deletes the video stream and stops the GUI - when implemented... TODO"""
        pass

    ##################
    ### GUI states ###        
    ##################

    def _setGUIStates(self):
        
        self.gui_states = {
            "Reset":                    GUI_State(self._resetGUI, []),
            "Init":                     GUI_State(self._initGUI, []),
            "CameraNotSelected":        GUI_State(self._stateCameraNotSelected, []),
            "CameraSelected":           GUI_State(self._stateCameraSelected, []),
            "SaveImagesChecked":               GUI_State(self._stateSaveImagesChecked, []),
            "UseSavedImagesChecked":    GUI_State(self._stateUseSavedImagesChecked, []),
            "AutotimerChecked":         GUI_State(self._stateAutotimerChecked, []),
            "AutotimerStarted":         GUI_State(self._stateAutotimerStarted, []),
            "AutotimerStopped":         GUI_State(self._stateAutotimerStopped, []),
            "ParametersEntered":        GUI_State(self._stateParametersEntered, []),
            "ParametersDetermined":     GUI_State(self._stateParametersDetermined, []),
            "PreviewCalibrationChecked":GUI_State(self._statePreviewCalibrationChecked, [])
        }
    
    def _resetGUI(self):
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
                      self.ui.checkBox_preview_calibration,
                      self.ui.checkBox_save_images,
                      self.ui.checkBox_preview_calibration,
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
                self.ui.spinBox_charuco_no_markers_v.setText(self.calibration_settings.no_markers_v)
                self.ui.spinBox_charuco_no_markers_h.setText(self.calibration_settings.no_markers_h)
                self.ui.comboBox_marker_dict.setCurrentIndex(self.calibration_settings.marker_dict)
            elif type(self.calibration_settings) is ChessboardCalibrationSettings:
                self.ui.doubleSpinBox_sqare_size.setValue(self.calibration_settings.size)
                self.ui.spinBox_chessboard_no_squares_v.setText(self.calibration_settings.no_squares_v)
                self.ui.spinBox_chessboard_no_squares_h.setText(self.calibration_settings.no_squares_h)
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
        available_cameras = list_available_cameras([])
        self.ui.comboBox_camera.addItems(available_cameras)
    
    def _stateCameraNotSelected(self):
        self.ui.comboBox_camera.setEnabled(True)
        
    def _stateCameraSelected(self):
        self.ui.comboBox_camera.setIndex(0)
        self.ui.checkBox_save_images.setEnabled(True)
        self.ui.spinBox_delay_seconds.setEnabled(True)
        self.ui.pushButton_capture.setEnabled(True)
        self.ui.pushButton_start_autotimer.setEnabled(True)

    def _stateSaveImagesChecked(self):
        self.ui.checkBox_save_images.setEnabled(True)
        self.ui.lineEdit_path.setEnabled(True)
        self.ui.pushButton_path_window.setEnabled(True)

    def _stateUseSavedImagesChecked(self):
        self.ui.pushButton_select_images.setEnabled(True)
        self.ui.pushButton_capture.setEnabled(False)
        self.ui.comboBox_camera.setEnabled(False)
    
    def _stateAutotimerChecked(self):
        pass
    
    def _stateAutotimerStarted(self):
        pass
    
    def _stateAutotimerStopped(self):
        pass

    def _stateParametersEntered(self):
        pass
    
    def _stateParametersDetermined(self):
        pass
    
    def _statePreviewCalibrationChecked(self):
        pass

    #####################
    ####### slots #######
    #####################

    def _set_signal_slots(self):
        self.ui.comboBox_camera.currentIndexChanged.connect(self._slot_comboBox_camera_changed)
        self.ui.pushButton_camera_search.clicked.connect(self._slot_pushButton_camera_search_pushed)
        self.ui.checkBox_use_saved_images.stateChanged.connect(self._slot_checkBox_use_saved_images_checked)
        self.ui.checkBox_save_images.stateChanged.connect(self._slot_checkBox_save_images_checked)
        self.ui.pushButton_path_window.clicked.connect(self._slot_pushButton_path_window_pushed)
        self.ui.pushButton_start_autotimer.clicked.connect(self._slot_pushButton_start_autotimer_pushed)
        self.ui.pushButton_capture.clicked.connect(self._slot_pushButton_capture_pushed)
        self.ui.listWidget_imgs.itemClicked.connect(self._slot_listWidget_imgs_itemClicked)
        self.ui.pushButton_delete_last.clicked.connect(self._slot_pushButton_delete_last_pushed)
        self.ui.pushButton_delete_all.clicked.connect(self._slot_pushButton_delete_all_pushed)
        self.ui.pushButton_determ_param.clicked.connect(self._slot_pushButton_determ_param_pushed)
        self.ui.pushButton_save_param.clicked.connect(self._slot_pushButton_save_param_pushed)
        self.ui.checkBox_preview_calibration.clicked.connect(self._slot_checkBox_preview_calibration_checked)
    
    def _slot_comboBox_camera_changed(self):
        """Event handler for TODO
        """
        
        #if index == 0:
        if self.ui.comboBox_camera.currentIndex() == 0:
            self.gui_states['CameraNotSelected'].activate(reset_fn=self._resetGUI,gui=self)
        else:
            self.gui_states['CameraSelected'].activate(reset_fn=self._resetGUI,gui=self)
            try:
                self.frame_grabber = FrameGrabber(self.ui.comboBox_camera.currentText())
            except Exception as e:
                print(e)
                self.ui.comboBox_camera.setCurrentIndex(0)

    def _slot_pushButton_camera_search_pushed(self):
        """Event handler for TODO
        """
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
        """Event handler for TODO
        """
        if self.ui.checkBox_use_saved_images.isChecked():
            self.gui_states['UseSavedImagesChecked'].activate(reset_fn=self._resetGUI, gui=self)
        
        else:
            self.gui_states['CameraNotSelected'].activate(reset_fn=self._resetGUI, gui=self)
        
    def _slot_checkBox_save_images_checked(self):
        """Event handler for the checkbox to save images
        if the checkbox is checked, the state is changed to SaveImagesChecked
        else the previous state is activated
        """
        if self.ui.checkBox_save_images.isChecked():
            self.gui_states['SaveImagesChecked'].activate(reset_fn=self._resetGUI, gui=self)
        else:
            self.previous_state.activate(reset_fn=self._resetGUI, gui=self)
        
    def _slot_pushButton_path_window_pushed(self):
        """Event handler for TODO
        """
        pass
    
    def _slot_pushButton_start_autotimer_pushed(self):
        """Event handler for TODO
        """
        pass
    
    def _slot_pushButton_capture_pushed(self):
        """Event handler for TODO
        """
        pass
    
    def _slot_listWidget_imgs_itemClicked(self):
        """Event handler for TODO
        """
        pass
    
    def _slot_pushButton_delete_all_pushed(self):
        """Event handler for TODO
        """
        pass
    
    def _slot_pushButton_delete_last_pushed(self):
        """Event handler for TODO
        """
        pass
    
    def _slot_tabWidget_calibration_changed(self):
        """Event handler for TODO
        """
        pass
    
    def _slot_pushButton_determ_param_pushed(self):
        """Event handler for TODO
        """
        pass
    
    def _slot_pushButton_save_param_pushed(self):
        """Event handler for TODO
        """
        pass
    
    def _slot_checkBox_preview_calibration_checked(self):
        """Event handler for TODO
        """
        pass
    

if __name__ == "__main__":
    gui= GUI()
    gui.start_gui()
    