# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'camera_calibration_tool.ui'
##
## Created by: Qt User Interface Compiler version 5.15.6
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1488, 919)
        icon = QIcon()
        icon.addFile(u"src/data/app_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_central = QHBoxLayout()
        self.horizontalLayout_central.setObjectName(u"horizontalLayout_central")
        self.horizontalLayout_central.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_left = QVBoxLayout()
        self.verticalLayout_left.setObjectName(u"verticalLayout_left")
        self.tabWidget_source = QTabWidget(self.centralwidget)
        self.tabWidget_source.setObjectName(u"tabWidget_source")
        self.tabWidget_source.setMaximumSize(QSize(350, 16777215))
        self.FromCameraTab = QWidget()
        self.FromCameraTab.setObjectName(u"FromCameraTab")
        self.gridLayout_9 = QGridLayout(self.FromCameraTab)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalLayout_capture = QVBoxLayout()
        self.verticalLayout_capture.setObjectName(u"verticalLayout_capture")
        self.groupBox_2 = QGroupBox(self.FromCameraTab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.comboBox_camera = QComboBox(self.groupBox_2)
        self.comboBox_camera.setObjectName(u"comboBox_camera")

        self.gridLayout_2.addWidget(self.comboBox_camera, 0, 0, 1, 1)

        self.pushButton_camera_search = QPushButton(self.groupBox_2)
        self.pushButton_camera_search.setObjectName(u"pushButton_camera_search")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_camera_search.sizePolicy().hasHeightForWidth())
        self.pushButton_camera_search.setSizePolicy(sizePolicy)
        self.pushButton_camera_search.setMinimumSize(QSize(25, 25))
        self.pushButton_camera_search.setMaximumSize(QSize(25, 25))
        icon1 = QIcon()
        icon1.addFile(u"src/data/refresh_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_camera_search.setIcon(icon1)

        self.gridLayout_2.addWidget(self.pushButton_camera_search, 0, 1, 1, 1)


        self.verticalLayout_capture.addWidget(self.groupBox_2)

        self.groupBox_4 = QGroupBox(self.FromCameraTab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_10 = QGridLayout(self.groupBox_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setHorizontalSpacing(6)
        self.gridLayout_10.setVerticalSpacing(0)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.checkBox_save_images = QCheckBox(self.groupBox_4)
        self.checkBox_save_images.setObjectName(u"checkBox_save_images")
        self.checkBox_save_images.setMaximumSize(QSize(23, 23))

        self.gridLayout_10.addWidget(self.checkBox_save_images, 0, 0, 1, 1, Qt.AlignHCenter)

        self.lineEdit_path = QLineEdit(self.groupBox_4)
        self.lineEdit_path.setObjectName(u"lineEdit_path")
        self.lineEdit_path.setEnabled(False)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_path.sizePolicy().hasHeightForWidth())
        self.lineEdit_path.setSizePolicy(sizePolicy1)
        self.lineEdit_path.setMinimumSize(QSize(200, 0))

        self.gridLayout_10.addWidget(self.lineEdit_path, 0, 2, 1, 1)

        self.pushButton_path_window = QPushButton(self.groupBox_4)
        self.pushButton_path_window.setObjectName(u"pushButton_path_window")
        sizePolicy.setHeightForWidth(self.pushButton_path_window.sizePolicy().hasHeightForWidth())
        self.pushButton_path_window.setSizePolicy(sizePolicy)
        self.pushButton_path_window.setMaximumSize(QSize(100, 50))
        self.pushButton_path_window.setIconSize(QSize(0, 0))

        self.gridLayout_10.addWidget(self.pushButton_path_window, 0, 3, 1, 1)


        self.verticalLayout_capture.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.FromCameraTab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_11 = QGridLayout(self.groupBox_5)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.pushButton_start_autotimer = QPushButton(self.groupBox_5)
        self.pushButton_start_autotimer.setObjectName(u"pushButton_start_autotimer")

        self.gridLayout_11.addWidget(self.pushButton_start_autotimer, 2, 0, 1, 1)

        self.label_delay_seconds = QLabel(self.groupBox_5)
        self.label_delay_seconds.setObjectName(u"label_delay_seconds")

        self.gridLayout_11.addWidget(self.label_delay_seconds, 1, 0, 1, 1)

        self.label_img_no = QLabel(self.groupBox_5)
        self.label_img_no.setObjectName(u"label_img_no")

        self.gridLayout_11.addWidget(self.label_img_no, 0, 0, 1, 1)

        self.progressBar_img_cnt = QProgressBar(self.groupBox_5)
        self.progressBar_img_cnt.setObjectName(u"progressBar_img_cnt")
        self.progressBar_img_cnt.setMaximumSize(QSize(100, 16777215))
        self.progressBar_img_cnt.setMaximum(20)
        self.progressBar_img_cnt.setValue(0)

        self.gridLayout_11.addWidget(self.progressBar_img_cnt, 2, 1, 1, 1)

        self.spinBox_delay_seconds = QSpinBox(self.groupBox_5)
        self.spinBox_delay_seconds.setObjectName(u"spinBox_delay_seconds")
        self.spinBox_delay_seconds.setMaximumSize(QSize(100, 16777215))
        self.spinBox_delay_seconds.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_delay_seconds.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.spinBox_delay_seconds.setMinimum(5)
        self.spinBox_delay_seconds.setMaximum(60)
        self.spinBox_delay_seconds.setSingleStep(5)

        self.gridLayout_11.addWidget(self.spinBox_delay_seconds, 1, 1, 1, 1)

        self.spinBox_img_no = QSpinBox(self.groupBox_5)
        self.spinBox_img_no.setObjectName(u"spinBox_img_no")
        self.spinBox_img_no.setMinimumSize(QSize(50, 0))
        self.spinBox_img_no.setMaximumSize(QSize(100, 16777215))
        self.spinBox_img_no.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_img_no.setMinimum(5)
        self.spinBox_img_no.setValue(10)

        self.gridLayout_11.addWidget(self.spinBox_img_no, 0, 1, 1, 1)


        self.verticalLayout_capture.addWidget(self.groupBox_5)

        self.groupBox_6 = QGroupBox(self.FromCameraTab)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self._2 = QHBoxLayout(self.groupBox_6)
        self._2.setObjectName(u"_2")
        self.pushButton_capture = QPushButton(self.groupBox_6)
        self.pushButton_capture.setObjectName(u"pushButton_capture")
        icon2 = QIcon()
        icon2.addFile(u"src/data/save_icon.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_capture.setIcon(icon2)

        self._2.addWidget(self.pushButton_capture)


        self.verticalLayout_capture.addWidget(self.groupBox_6)


        self.gridLayout_9.addLayout(self.verticalLayout_capture, 0, 0, 1, 1)

        self.tabWidget_source.addTab(self.FromCameraTab, "")
        self.FromFileTab = QWidget()
        self.FromFileTab.setObjectName(u"FromFileTab")
        self.gridLayout_8 = QGridLayout(self.FromFileTab)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.checkBox_use_saved_images = QCheckBox(self.FromFileTab)
        self.checkBox_use_saved_images.setObjectName(u"checkBox_use_saved_images")

        self.horizontalLayout.addWidget(self.checkBox_use_saved_images)

        self.pushButton_select_images = QPushButton(self.FromFileTab)
        self.pushButton_select_images.setObjectName(u"pushButton_select_images")
        self.pushButton_select_images.setEnabled(False)

        self.horizontalLayout.addWidget(self.pushButton_select_images)


        self.gridLayout_8.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_2, 1, 0, 1, 1)

        self.tabWidget_source.addTab(self.FromFileTab, "")

        self.verticalLayout_left.addWidget(self.tabWidget_source)

        self.groupBox_images = QGroupBox(self.centralwidget)
        self.groupBox_images.setObjectName(u"groupBox_images")
        self.groupBox_images.setMaximumSize(QSize(350, 16777215))
        self.gridLayout_5 = QGridLayout(self.groupBox_images)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.listWidget_imgs = QListWidget(self.groupBox_images)
        self.listWidget_imgs.setObjectName(u"listWidget_imgs")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.listWidget_imgs.sizePolicy().hasHeightForWidth())
        self.listWidget_imgs.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.listWidget_imgs, 3, 0, 1, 1)

        self.horizontalLayout_delete_buttons = QHBoxLayout()
        self.horizontalLayout_delete_buttons.setObjectName(u"horizontalLayout_delete_buttons")
        self.pushButton_delete_last = QPushButton(self.groupBox_images)
        self.pushButton_delete_last.setObjectName(u"pushButton_delete_last")

        self.horizontalLayout_delete_buttons.addWidget(self.pushButton_delete_last)

        self.pushButton_delete_all = QPushButton(self.groupBox_images)
        self.pushButton_delete_all.setObjectName(u"pushButton_delete_all")

        self.horizontalLayout_delete_buttons.addWidget(self.pushButton_delete_all)


        self.gridLayout_5.addLayout(self.horizontalLayout_delete_buttons, 4, 0, 1, 1)


        self.verticalLayout_left.addWidget(self.groupBox_images)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_left.addItem(self.verticalSpacer)


        self.horizontalLayout_central.addLayout(self.verticalLayout_left)

        self.groupBox_Video = QGroupBox(self.centralwidget)
        self.groupBox_Video.setObjectName(u"groupBox_Video")
        self.groupBox_Video.setAlignment(Qt.AlignCenter)
        self.gridLayout_4 = QGridLayout(self.groupBox_Video)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.cameraView = QLabel(self.groupBox_Video)
        self.cameraView.setObjectName(u"cameraView")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cameraView.sizePolicy().hasHeightForWidth())
        self.cameraView.setSizePolicy(sizePolicy3)
        self.cameraView.setMaximumSize(QSize(1280, 1280))
        self.cameraView.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.cameraView, 0, 1, 1, 1)


        self.horizontalLayout_central.addWidget(self.groupBox_Video)

        self.verticalLayout_right = QVBoxLayout()
        self.verticalLayout_right.setObjectName(u"verticalLayout_right")
        self.groupBox_chessboard = QGroupBox(self.centralwidget)
        self.groupBox_chessboard.setObjectName(u"groupBox_chessboard")
        sizePolicy1.setHeightForWidth(self.groupBox_chessboard.sizePolicy().hasHeightForWidth())
        self.groupBox_chessboard.setSizePolicy(sizePolicy1)
        self.groupBox_chessboard.setMaximumSize(QSize(350, 16777215))
        self.gridLayout_3 = QGridLayout(self.groupBox_chessboard)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_chessboard = QVBoxLayout()
        self.verticalLayout_chessboard.setObjectName(u"verticalLayout_chessboard")

        self.gridLayout_3.addLayout(self.verticalLayout_chessboard, 1, 0, 1, 1)

        self.tabWidget_calibration = QTabWidget(self.groupBox_chessboard)
        self.tabWidget_calibration.setObjectName(u"tabWidget_calibration")
        self.tab_chessboard = QWidget()
        self.tab_chessboard.setObjectName(u"tab_chessboard")
        self.gridLayout_12 = QGridLayout(self.tab_chessboard)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_chessboard = QGridLayout()
        self.gridLayout_chessboard.setObjectName(u"gridLayout_chessboard")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.doubleSpinBox_sqare_size = QDoubleSpinBox(self.tab_chessboard)
        self.doubleSpinBox_sqare_size.setObjectName(u"doubleSpinBox_sqare_size")
        self.doubleSpinBox_sqare_size.setMinimum(5.000000000000000)

        self.horizontalLayout_7.addWidget(self.doubleSpinBox_sqare_size)


        self.gridLayout_chessboard.addLayout(self.horizontalLayout_7, 1, 3, 1, 1)

        self.label_square_size = QLabel(self.tab_chessboard)
        self.label_square_size.setObjectName(u"label_square_size")

        self.gridLayout_chessboard.addWidget(self.label_square_size, 1, 0, 1, 1)

        self.label_square_no = QLabel(self.tab_chessboard)
        self.label_square_no.setObjectName(u"label_square_no")

        self.gridLayout_chessboard.addWidget(self.label_square_no, 2, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.spinBox_chessboard_no_squares_h = QSpinBox(self.tab_chessboard)
        self.spinBox_chessboard_no_squares_h.setObjectName(u"spinBox_chessboard_no_squares_h")
        self.spinBox_chessboard_no_squares_h.setMinimum(5)

        self.horizontalLayout_8.addWidget(self.spinBox_chessboard_no_squares_h)

        self.label_x = QLabel(self.tab_chessboard)
        self.label_x.setObjectName(u"label_x")
        sizePolicy.setHeightForWidth(self.label_x.sizePolicy().hasHeightForWidth())
        self.label_x.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.label_x)

        self.spinBox_chessboard_no_squares_v = QSpinBox(self.tab_chessboard)
        self.spinBox_chessboard_no_squares_v.setObjectName(u"spinBox_chessboard_no_squares_v")
        self.spinBox_chessboard_no_squares_v.setMinimum(5)

        self.horizontalLayout_8.addWidget(self.spinBox_chessboard_no_squares_v)


        self.gridLayout_chessboard.addLayout(self.horizontalLayout_8, 2, 3, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_chessboard, 0, 0, 1, 1)

        self.tabWidget_calibration.addTab(self.tab_chessboard, "")
        self.tab_charuco = QWidget()
        self.tab_charuco.setObjectName(u"tab_charuco")
        self.gridLayout_13 = QGridLayout(self.tab_charuco)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label = QLabel(self.tab_charuco)
        self.label.setObjectName(u"label")

        self.gridLayout_13.addWidget(self.label, 0, 0, 1, 1)

        self.label_3 = QLabel(self.tab_charuco)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_13.addWidget(self.label_3, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.spinBox_charuco_no_markers_h = QSpinBox(self.tab_charuco)
        self.spinBox_charuco_no_markers_h.setObjectName(u"spinBox_charuco_no_markers_h")
        self.spinBox_charuco_no_markers_h.setMinimum(5)

        self.horizontalLayout_2.addWidget(self.spinBox_charuco_no_markers_h)

        self.label_2 = QLabel(self.tab_charuco)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.spinBox_charuco_no_markers_v = QSpinBox(self.tab_charuco)
        self.spinBox_charuco_no_markers_v.setObjectName(u"spinBox_charuco_no_markers_v")
        self.spinBox_charuco_no_markers_v.setMinimum(5)

        self.horizontalLayout_2.addWidget(self.spinBox_charuco_no_markers_v)


        self.gridLayout_13.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)

        self.comboBox_marker_dict = QComboBox(self.tab_charuco)
        self.comboBox_marker_dict.addItem("")
        self.comboBox_marker_dict.addItem("")
        self.comboBox_marker_dict.addItem("")
        self.comboBox_marker_dict.addItem("")
        self.comboBox_marker_dict.addItem("")
        self.comboBox_marker_dict.addItem("")
        self.comboBox_marker_dict.addItem("")
        self.comboBox_marker_dict.addItem("")
        self.comboBox_marker_dict.addItem("")
        self.comboBox_marker_dict.addItem("")
        self.comboBox_marker_dict.addItem("")
        self.comboBox_marker_dict.addItem("")
        self.comboBox_marker_dict.addItem("")
        self.comboBox_marker_dict.addItem("")
        self.comboBox_marker_dict.addItem("")
        self.comboBox_marker_dict.addItem("")
        self.comboBox_marker_dict.addItem("")
        self.comboBox_marker_dict.setObjectName(u"comboBox_marker_dict")

        self.gridLayout_13.addWidget(self.comboBox_marker_dict, 3, 1, 1, 1)

        self.label_4 = QLabel(self.tab_charuco)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_13.addWidget(self.label_4, 3, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.doubleSpinBox_marker_size = QDoubleSpinBox(self.tab_charuco)
        self.doubleSpinBox_marker_size.setObjectName(u"doubleSpinBox_marker_size")
        self.doubleSpinBox_marker_size.setMinimum(5.000000000000000)

        self.horizontalLayout_3.addWidget(self.doubleSpinBox_marker_size)


        self.gridLayout_13.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)

        self.tabWidget_calibration.addTab(self.tab_charuco, "")

        self.gridLayout_3.addWidget(self.tabWidget_calibration, 0, 0, 1, 1)


        self.verticalLayout_right.addWidget(self.groupBox_chessboard)

        self.groupBox_calibration = QGroupBox(self.centralwidget)
        self.groupBox_calibration.setObjectName(u"groupBox_calibration")
        self.groupBox_calibration.setMaximumSize(QSize(350, 16777215))
        self.gridLayout_7 = QGridLayout(self.groupBox_calibration)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_calibration = QVBoxLayout()
        self.verticalLayout_calibration.setObjectName(u"verticalLayout_calibration")
        self.pushButton_determ_param = QPushButton(self.groupBox_calibration)
        self.pushButton_determ_param.setObjectName(u"pushButton_determ_param")

        self.verticalLayout_calibration.addWidget(self.pushButton_determ_param)

        self.tableWidget_parameters = QTableWidget(self.groupBox_calibration)
        if (self.tableWidget_parameters.columnCount() < 1):
            self.tableWidget_parameters.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_parameters.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.tableWidget_parameters.rowCount() < 8):
            self.tableWidget_parameters.setRowCount(8)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_parameters.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_parameters.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_parameters.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_parameters.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_parameters.setVerticalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_parameters.setVerticalHeaderItem(5, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_parameters.setVerticalHeaderItem(6, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_parameters.setVerticalHeaderItem(7, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_parameters.setItem(0, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_parameters.setItem(1, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_parameters.setItem(2, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_parameters.setItem(3, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_parameters.setItem(4, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFlags(Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        self.tableWidget_parameters.setItem(5, 0, __qtablewidgetitem14)
        self.tableWidget_parameters.setObjectName(u"tableWidget_parameters")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.tableWidget_parameters.sizePolicy().hasHeightForWidth())
        self.tableWidget_parameters.setSizePolicy(sizePolicy4)
        self.tableWidget_parameters.setMinimumSize(QSize(0, 280))
        self.tableWidget_parameters.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget_parameters.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget_parameters.setGridStyle(Qt.SolidLine)
        self.tableWidget_parameters.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_parameters.horizontalHeader().setDefaultSectionSize(280)
        self.tableWidget_parameters.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout_calibration.addWidget(self.tableWidget_parameters)

        self.pushButton_save_param = QPushButton(self.groupBox_calibration)
        self.pushButton_save_param.setObjectName(u"pushButton_save_param")
        icon3 = QIcon()
        icon3.addFile(u"src/data/save_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u"src/data/save_icon.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pushButton_save_param.setIcon(icon3)

        self.verticalLayout_calibration.addWidget(self.pushButton_save_param)


        self.gridLayout_7.addLayout(self.verticalLayout_calibration, 0, 0, 1, 1)


        self.verticalLayout_right.addWidget(self.groupBox_calibration)

        self.verticalSpacer_bottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_right.addItem(self.verticalSpacer_bottom)


        self.horizontalLayout_central.addLayout(self.verticalLayout_right)


        self.gridLayout.addLayout(self.horizontalLayout_central, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget_source.setCurrentIndex(0)
        self.tabWidget_calibration.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Camera Calibration Tool", None))
#if QT_CONFIG(accessibility)
        MainWindow.setAccessibleName(QCoreApplication.translate("MainWindow", u"Camera Calibration Tool", None))
#endif // QT_CONFIG(accessibility)
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Camera", None))
#if QT_CONFIG(statustip)
        self.comboBox_camera.setStatusTip(QCoreApplication.translate("MainWindow", u"Choose a camera", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.comboBox_camera.setWhatsThis(QCoreApplication.translate("MainWindow", u"hello", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(statustip)
        self.pushButton_camera_search.setStatusTip(QCoreApplication.translate("MainWindow", u"Refresh cameras", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_camera_search.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Save Images", None))
#if QT_CONFIG(statustip)
        self.checkBox_save_images.setStatusTip(QCoreApplication.translate("MainWindow", u"Activate image saving", None))
#endif // QT_CONFIG(statustip)
        self.checkBox_save_images.setText("")
#if QT_CONFIG(statustip)
        self.lineEdit_path.setStatusTip(QCoreApplication.translate("MainWindow", u"Path to folder images will be saved to", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.lineEdit_path.setWhatsThis(QCoreApplication.translate("MainWindow", u"hello", None))
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(statustip)
        self.pushButton_path_window.setStatusTip(QCoreApplication.translate("MainWindow", u"Open folder selection dialog", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_path_window.setText(QCoreApplication.translate("MainWindow", u"Select path", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Self Timer", None))
#if QT_CONFIG(statustip)
        self.pushButton_start_autotimer.setStatusTip(QCoreApplication.translate("MainWindow", u"Start / Stop the self timer", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_start_autotimer.setText(QCoreApplication.translate("MainWindow", u"Start Self Timer", None))
        self.label_delay_seconds.setText(QCoreApplication.translate("MainWindow", u"Delay:", None))
        self.label_img_no.setText(QCoreApplication.translate("MainWindow", u"Number of Images:", None))
        self.progressBar_img_cnt.setFormat(QCoreApplication.translate("MainWindow", u"%v", None))
#if QT_CONFIG(statustip)
        self.spinBox_delay_seconds.setStatusTip(QCoreApplication.translate("MainWindow", u"Sleep time between images", None))
#endif // QT_CONFIG(statustip)
        self.spinBox_delay_seconds.setSuffix(QCoreApplication.translate("MainWindow", u"s", None))
#if QT_CONFIG(statustip)
        self.spinBox_img_no.setStatusTip(QCoreApplication.translate("MainWindow", u"Select number of images to take", None))
#endif // QT_CONFIG(statustip)
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Manual Capture", None))
#if QT_CONFIG(statustip)
        self.pushButton_capture.setStatusTip(QCoreApplication.translate("MainWindow", u"Capture image (if >Save Images< is activated this will automatically save the image to the specified path)", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_capture.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.tabWidget_source.setTabText(self.tabWidget_source.indexOf(self.FromCameraTab), QCoreApplication.translate("MainWindow", u"From Camera", None))
#if QT_CONFIG(statustip)
        self.checkBox_use_saved_images.setStatusTip(QCoreApplication.translate("MainWindow", u"Open already taken images for the calibration", None))
#endif // QT_CONFIG(statustip)
        self.checkBox_use_saved_images.setText(QCoreApplication.translate("MainWindow", u"Open from files", None))
#if QT_CONFIG(statustip)
        self.pushButton_select_images.setStatusTip(QCoreApplication.translate("MainWindow", u"Select image files for the calibration", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_select_images.setText(QCoreApplication.translate("MainWindow", u"Select files", None))
        self.tabWidget_source.setTabText(self.tabWidget_source.indexOf(self.FromFileTab), QCoreApplication.translate("MainWindow", u"From Files", None))
        self.groupBox_images.setTitle(QCoreApplication.translate("MainWindow", u"Images", None))
#if QT_CONFIG(statustip)
        self.pushButton_delete_last.setStatusTip(QCoreApplication.translate("MainWindow", u"Delete last image from the image list", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_delete_last.setText(QCoreApplication.translate("MainWindow", u"Delete Last", None))
#if QT_CONFIG(statustip)
        self.pushButton_delete_all.setStatusTip(QCoreApplication.translate("MainWindow", u"Delete all images from the image list", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_delete_all.setText(QCoreApplication.translate("MainWindow", u"Delete All", None))
#if QT_CONFIG(statustip)
        self.groupBox_Video.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.groupBox_Video.setTitle(QCoreApplication.translate("MainWindow", u"Video", None))
        self.cameraView.setText("")
        self.groupBox_chessboard.setTitle(QCoreApplication.translate("MainWindow", u"Calibration Body Specification", None))
#if QT_CONFIG(statustip)
        self.tabWidget_calibration.setStatusTip(QCoreApplication.translate("MainWindow", u"Horizontal number of sqares (white and black) on the calibration body", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(statustip)
        self.doubleSpinBox_sqare_size.setStatusTip(QCoreApplication.translate("MainWindow", u"Side length a chessboard sqare in cm", None))
#endif // QT_CONFIG(statustip)
        self.doubleSpinBox_sqare_size.setSuffix(QCoreApplication.translate("MainWindow", u" cm", None))
        self.label_square_size.setText(QCoreApplication.translate("MainWindow", u"Square Size:", None))
        self.label_square_no.setText(QCoreApplication.translate("MainWindow", u"Number of Squares (h x v):", None))
#if QT_CONFIG(statustip)
        self.spinBox_chessboard_no_squares_h.setStatusTip(QCoreApplication.translate("MainWindow", u"Horizontal number of sqares (white and black) on the calibration body", None))
#endif // QT_CONFIG(statustip)
        self.label_x.setText(QCoreApplication.translate("MainWindow", u"x", None))
#if QT_CONFIG(statustip)
        self.spinBox_chessboard_no_squares_v.setStatusTip(QCoreApplication.translate("MainWindow", u"Vertical number of sqares (white and black) on the calibration body", None))
#endif // QT_CONFIG(statustip)
        self.tabWidget_calibration.setTabText(self.tabWidget_calibration.indexOf(self.tab_chessboard), QCoreApplication.translate("MainWindow", u"Chessboard", None))
#if QT_CONFIG(statustip)
        self.label.setStatusTip(QCoreApplication.translate("MainWindow", u"Size of a aruco marker in cm", None))
#endif // QT_CONFIG(statustip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Marker size", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Number of Markers (h x v)", None))
#if QT_CONFIG(statustip)
        self.spinBox_charuco_no_markers_h.setStatusTip(QCoreApplication.translate("MainWindow", u"Horizontal number of markers on the calibration body", None))
#endif // QT_CONFIG(statustip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"x", None))
#if QT_CONFIG(statustip)
        self.spinBox_charuco_no_markers_v.setStatusTip(QCoreApplication.translate("MainWindow", u"Vertical number of markers on the calibration body", None))
#endif // QT_CONFIG(statustip)
        self.comboBox_marker_dict.setItemText(0, "")
        self.comboBox_marker_dict.setItemText(1, QCoreApplication.translate("MainWindow", u"DICT_4X4_50", None))
        self.comboBox_marker_dict.setItemText(2, QCoreApplication.translate("MainWindow", u"DICT_4X4_100", None))
        self.comboBox_marker_dict.setItemText(3, QCoreApplication.translate("MainWindow", u"DICT_4X4_250", None))
        self.comboBox_marker_dict.setItemText(4, QCoreApplication.translate("MainWindow", u"DICT_4X4_1000", None))
        self.comboBox_marker_dict.setItemText(5, QCoreApplication.translate("MainWindow", u"DICT_5X5_50", None))
        self.comboBox_marker_dict.setItemText(6, QCoreApplication.translate("MainWindow", u"DICT_5X5_100", None))
        self.comboBox_marker_dict.setItemText(7, QCoreApplication.translate("MainWindow", u"DICT_5X5_250", None))
        self.comboBox_marker_dict.setItemText(8, QCoreApplication.translate("MainWindow", u"DICT_5X5_1000", None))
        self.comboBox_marker_dict.setItemText(9, QCoreApplication.translate("MainWindow", u"DICT_6X6_50", None))
        self.comboBox_marker_dict.setItemText(10, QCoreApplication.translate("MainWindow", u"DICT_6X6_100", None))
        self.comboBox_marker_dict.setItemText(11, QCoreApplication.translate("MainWindow", u"DICT_6X6_250", None))
        self.comboBox_marker_dict.setItemText(12, QCoreApplication.translate("MainWindow", u"DICT_6X6_1000", None))
        self.comboBox_marker_dict.setItemText(13, QCoreApplication.translate("MainWindow", u"DICT_7X7_50", None))
        self.comboBox_marker_dict.setItemText(14, QCoreApplication.translate("MainWindow", u"DICT_7X7_100", None))
        self.comboBox_marker_dict.setItemText(15, QCoreApplication.translate("MainWindow", u"DICT_7X7_250", None))
        self.comboBox_marker_dict.setItemText(16, QCoreApplication.translate("MainWindow", u"DICT_7X7_1000", None))

#if QT_CONFIG(statustip)
        self.comboBox_marker_dict.setStatusTip(QCoreApplication.translate("MainWindow", u"CV Aruco Dictionary (4x4 represents the number of pixels)", None))
#endif // QT_CONFIG(statustip)
        self.comboBox_marker_dict.setCurrentText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Marker Dictionary", None))
#if QT_CONFIG(statustip)
        self.doubleSpinBox_marker_size.setStatusTip(QCoreApplication.translate("MainWindow", u"Side length of an aruco marker in cm", None))
#endif // QT_CONFIG(statustip)
        self.doubleSpinBox_marker_size.setSuffix(QCoreApplication.translate("MainWindow", u" cm", None))
        self.tabWidget_calibration.setTabText(self.tabWidget_calibration.indexOf(self.tab_charuco), QCoreApplication.translate("MainWindow", u"Charuco", None))
        self.groupBox_calibration.setTitle(QCoreApplication.translate("MainWindow", u"Calibration", None))
#if QT_CONFIG(statustip)
        self.pushButton_determ_param.setStatusTip(QCoreApplication.translate("MainWindow", u"Calculate camera paramters from calibration images", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_determ_param.setText(QCoreApplication.translate("MainWindow", u"Calculate Parameters", None))
        ___qtablewidgetitem = self.tableWidget_parameters.verticalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Parameter", None));
        ___qtablewidgetitem1 = self.tableWidget_parameters.verticalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"(f_x, f_y)", None));
        ___qtablewidgetitem2 = self.tableWidget_parameters.verticalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"(c_x,c_y)", None));
        ___qtablewidgetitem3 = self.tableWidget_parameters.verticalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"k_1", None));
        ___qtablewidgetitem4 = self.tableWidget_parameters.verticalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"k_2", None));
        ___qtablewidgetitem5 = self.tableWidget_parameters.verticalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"p_1", None));
        ___qtablewidgetitem6 = self.tableWidget_parameters.verticalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"p_2", None));
        ___qtablewidgetitem7 = self.tableWidget_parameters.verticalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"k_3", None));

        __sortingEnabled = self.tableWidget_parameters.isSortingEnabled()
        self.tableWidget_parameters.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.tableWidget_parameters.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.tableWidget_parameters.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(accessibility)
        self.tableWidget_parameters.setAccessibleDescription(QCoreApplication.translate("MainWindow", u"hello", None))
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(statustip)
        self.pushButton_save_param.setStatusTip(QCoreApplication.translate("MainWindow", u"Save camera parameters as a .yaml file.", None))
#endif // QT_CONFIG(statustip)
        self.pushButton_save_param.setText(QCoreApplication.translate("MainWindow", u"Save Parameters", None))
    # retranslateUi

