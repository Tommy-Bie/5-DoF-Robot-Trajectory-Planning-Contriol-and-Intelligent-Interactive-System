# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1419, 842)
        MainWindow.setStyleSheet("#MainWindow{\n"
"    border-image: url(:/png/bg11.png);\n"
"    \n"
"    \n"
"\n"
"    \n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(520, 10, 571, 431))
        self.tabWidget.setStyleSheet("QTabBar::tab{\n"
"border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"height:25;\n"
"font: 75 10pt \"微软雅黑\";\n"
"font: bold;\n"
"}\n"
"\n"
"QTabBar::tab:selected{background-color:rgb(249, 161, 126);}\n"
"QTabBar::tab:!selected{background-color:rgb(255, 255, 255);}\n"
"QTabWidget::pane{     \n"
"    border: none;\n"
"}\n"
"\n"
"QTabWidget:pane{   \n"
"    background: transparent;    \n"
"}\n"
"")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.interval_button = QtWidgets.QPushButton(self.tab_2)
        self.interval_button.setGeometry(QtCore.QRect(251, 361, 81, 24))
        self.interval_button.setStyleSheet("\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"font: 75 9pt \"微软雅黑\";\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(86,112,149, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.interval_button.setObjectName("interval_button")
        self.interval = QtWidgets.QLineEdit(self.tab_2)
        self.interval.setGeometry(QtCore.QRect(161, 361, 83, 24))
        self.interval.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.interval.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.interval.setObjectName("interval")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 10, 561, 321))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_21 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 0, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout_2.addWidget(self.label_22, 0, 2, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout_2.addWidget(self.label_23, 0, 3, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 0, 4, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout_2.addWidget(self.label_25, 0, 5, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.theta1o = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta1o.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta1o.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta1o.setObjectName("theta1o")
        self.gridLayout_2.addWidget(self.theta1o, 1, 1, 1, 1)
        self.theta11 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta11.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta11.setObjectName("theta11")
        self.gridLayout_2.addWidget(self.theta11, 1, 2, 1, 1)
        self.theta12 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta12.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta12.setObjectName("theta12")
        self.gridLayout_2.addWidget(self.theta12, 1, 3, 1, 1)
        self.theta13 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta13.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta13.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta13.setObjectName("theta13")
        self.gridLayout_2.addWidget(self.theta13, 1, 4, 1, 1)
        self.theta1t = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta1t.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta1t.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta1t.setObjectName("theta1t")
        self.gridLayout_2.addWidget(self.theta1t, 1, 5, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.theta2o = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta2o.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta2o.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta2o.setObjectName("theta2o")
        self.gridLayout_2.addWidget(self.theta2o, 2, 1, 1, 1)
        self.theta21 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta21.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta21.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta21.setObjectName("theta21")
        self.gridLayout_2.addWidget(self.theta21, 2, 2, 1, 1)
        self.theta22 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta22.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta22.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta22.setObjectName("theta22")
        self.gridLayout_2.addWidget(self.theta22, 2, 3, 1, 1)
        self.theta23 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta23.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta23.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta23.setObjectName("theta23")
        self.gridLayout_2.addWidget(self.theta23, 2, 4, 1, 1)
        self.theta2t = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta2t.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta2t.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta2t.setObjectName("theta2t")
        self.gridLayout_2.addWidget(self.theta2t, 2, 5, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)
        self.theta3o = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta3o.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta3o.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta3o.setObjectName("theta3o")
        self.gridLayout_2.addWidget(self.theta3o, 3, 1, 1, 1)
        self.theta31 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta31.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta31.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta31.setObjectName("theta31")
        self.gridLayout_2.addWidget(self.theta31, 3, 2, 1, 1)
        self.theta32 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta32.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta32.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta32.setObjectName("theta32")
        self.gridLayout_2.addWidget(self.theta32, 3, 3, 1, 1)
        self.theta33 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta33.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta33.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta33.setObjectName("theta33")
        self.gridLayout_2.addWidget(self.theta33, 3, 4, 1, 1)
        self.theta3t = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta3t.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta3t.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta3t.setObjectName("theta3t")
        self.gridLayout_2.addWidget(self.theta3t, 3, 5, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 4, 0, 1, 1)
        self.theta4o = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta4o.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta4o.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta4o.setObjectName("theta4o")
        self.gridLayout_2.addWidget(self.theta4o, 4, 1, 1, 1)
        self.theta41 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta41.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta41.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta41.setObjectName("theta41")
        self.gridLayout_2.addWidget(self.theta41, 4, 2, 1, 1)
        self.theta42 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta42.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta42.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta42.setObjectName("theta42")
        self.gridLayout_2.addWidget(self.theta42, 4, 3, 1, 1)
        self.theta43 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta43.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta43.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta43.setObjectName("theta43")
        self.gridLayout_2.addWidget(self.theta43, 4, 4, 1, 1)
        self.theta4t = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta4t.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta4t.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta4t.setObjectName("theta4t")
        self.gridLayout_2.addWidget(self.theta4t, 4, 5, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 5, 0, 1, 1)
        self.theta5o = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta5o.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta5o.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta5o.setObjectName("theta5o")
        self.gridLayout_2.addWidget(self.theta5o, 5, 1, 1, 1)
        self.theta51 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta51.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta51.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta51.setObjectName("theta51")
        self.gridLayout_2.addWidget(self.theta51, 5, 2, 1, 1)
        self.theta52 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta52.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta52.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta52.setObjectName("theta52")
        self.gridLayout_2.addWidget(self.theta52, 5, 3, 1, 1)
        self.theta53 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta53.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta53.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta53.setObjectName("theta53")
        self.gridLayout_2.addWidget(self.theta53, 5, 4, 1, 1)
        self.theta5t = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta5t.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta5t.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta5t.setObjectName("theta5t")
        self.gridLayout_2.addWidget(self.theta5t, 5, 5, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.gridLayout_2.addWidget(self.label_37, 6, 0, 1, 1)
        self.theta5t_d_3 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta5t_d_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta5t_d_3.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta5t_d_3.setReadOnly(True)
        self.theta5t_d_3.setObjectName("theta5t_d_3")
        self.gridLayout_2.addWidget(self.theta5t_d_3, 6, 1, 1, 1)
        self.time1 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.time1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.time1.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.time1.setObjectName("time1")
        self.gridLayout_2.addWidget(self.time1, 6, 2, 1, 1)
        self.time2 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.time2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.time2.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.time2.setObjectName("time2")
        self.gridLayout_2.addWidget(self.time2, 6, 3, 1, 1)
        self.time3 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.time3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.time3.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.time3.setObjectName("time3")
        self.gridLayout_2.addWidget(self.time3, 6, 4, 1, 1)
        self.timet = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.timet.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.timet.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.timet.setObjectName("timet")
        self.gridLayout_2.addWidget(self.timet, 6, 5, 1, 1)
        self.label_57 = QtWidgets.QLabel(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_57.setFont(font)
        self.label_57.setObjectName("label_57")
        self.gridLayout_2.addWidget(self.label_57, 7, 0, 1, 1)
        self.theta5o_d_4 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta5o_d_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta5o_d_4.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta5o_d_4.setReadOnly(True)
        self.theta5o_d_4.setObjectName("theta5o_d_4")
        self.gridLayout_2.addWidget(self.theta5o_d_4, 7, 1, 1, 1)
        self.mid1v = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.mid1v.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mid1v.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.mid1v.setObjectName("mid1v")
        self.gridLayout_2.addWidget(self.mid1v, 7, 2, 1, 1)
        self.mid2v = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.mid2v.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mid2v.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.mid2v.setObjectName("mid2v")
        self.gridLayout_2.addWidget(self.mid2v, 7, 3, 1, 1)
        self.mid3v = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.mid3v.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mid3v.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.mid3v.setObjectName("mid3v")
        self.gridLayout_2.addWidget(self.mid3v, 7, 4, 1, 1)
        self.theta5o_d_5 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.theta5o_d_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta5o_d_5.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta5o_d_5.setReadOnly(True)
        self.theta5o_d_5.setObjectName("theta5o_d_5")
        self.gridLayout_2.addWidget(self.theta5o_d_5, 7, 5, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 8, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 8, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 8, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 8, 4, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 8, 5, 1, 1)
        self.Button0 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.Button0.setStyleSheet("\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"font: 75 9pt \"微软雅黑\";\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(86,112,149, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.Button0.setObjectName("Button0")
        self.gridLayout_2.addWidget(self.Button0, 9, 1, 1, 1)
        self.Button1 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.Button1.setStyleSheet("\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"font: 75 9pt \"微软雅黑\";\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(86,112,149, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.Button1.setObjectName("Button1")
        self.gridLayout_2.addWidget(self.Button1, 9, 2, 1, 1)
        self.Button2 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.Button2.setStyleSheet("\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"font: 75 9pt \"微软雅黑\";\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(86,112,149, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.Button2.setObjectName("Button2")
        self.gridLayout_2.addWidget(self.Button2, 9, 3, 1, 1)
        self.Button3 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.Button3.setStyleSheet("\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"font: 75 9pt \"微软雅黑\";\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(86,112,149, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.Button3.setObjectName("Button3")
        self.gridLayout_2.addWidget(self.Button3, 9, 4, 1, 1)
        self.Buttont = QtWidgets.QPushButton(self.layoutWidget_2)
        self.Buttont.setStyleSheet("\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"font: 75 9pt \"微软雅黑\";\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(86,112,149, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.Buttont.setObjectName("Buttont")
        self.gridLayout_2.addWidget(self.Buttont, 9, 5, 1, 1)
        self.label_58 = QtWidgets.QLabel(self.tab_2)
        self.label_58.setGeometry(QtCore.QRect(361, 360, 92, 27))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_58.setFont(font)
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self.tab_2)
        self.label_59.setGeometry(QtCore.QRect(21, 361, 120, 27))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_59.setFont(font)
        self.label_59.setObjectName("label_59")
        self.planmode_joint = QtWidgets.QComboBox(self.tab_2)
        self.planmode_joint.setGeometry(QtCore.QRect(460, 360, 91, 26))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.planmode_joint.setFont(font)
        self.planmode_joint.setObjectName("planmode_joint")
        self.planmode_joint.addItem("")
        self.planmode_joint.addItem("")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.interval_d_button = QtWidgets.QPushButton(self.tab)
        self.interval_d_button.setGeometry(QtCore.QRect(252, 362, 71, 24))
        self.interval_d_button.setStyleSheet("\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"font: 75 9pt \"微软雅黑\";\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(86,112,149, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.interval_d_button.setObjectName("interval_d_button")
        self.interval_d = QtWidgets.QLineEdit(self.tab)
        self.interval_d.setGeometry(QtCore.QRect(138, 362, 101, 24))
        self.interval_d.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.interval_d.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.interval_d.setObjectName("interval_d")
        self.label_39 = QtWidgets.QLabel(self.tab)
        self.label_39.setGeometry(QtCore.QRect(11, 361, 120, 27))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_3.setGeometry(QtCore.QRect(0, 10, 561, 320))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_20 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 0, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 0, 2, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 0, 3, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 0, 4, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 0, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.Xo = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.Xo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Xo.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.Xo.setObjectName("Xo")
        self.gridLayout.addWidget(self.Xo, 1, 1, 1, 1)
        self.X1 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.X1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.X1.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.X1.setObjectName("X1")
        self.gridLayout.addWidget(self.X1, 1, 2, 1, 1)
        self.X2 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.X2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.X2.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.X2.setObjectName("X2")
        self.gridLayout.addWidget(self.X2, 1, 3, 1, 1)
        self.X3 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.X3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.X3.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.X3.setObjectName("X3")
        self.gridLayout.addWidget(self.X3, 1, 4, 1, 1)
        self.Xt = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.Xt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Xt.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.Xt.setObjectName("Xt")
        self.gridLayout.addWidget(self.Xt, 1, 5, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.Yo = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.Yo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Yo.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.Yo.setObjectName("Yo")
        self.gridLayout.addWidget(self.Yo, 2, 1, 1, 1)
        self.Y1 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.Y1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Y1.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.Y1.setObjectName("Y1")
        self.gridLayout.addWidget(self.Y1, 2, 2, 1, 1)
        self.Y2 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.Y2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Y2.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.Y2.setObjectName("Y2")
        self.gridLayout.addWidget(self.Y2, 2, 3, 1, 1)
        self.Y3 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.Y3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Y3.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.Y3.setObjectName("Y3")
        self.gridLayout.addWidget(self.Y3, 2, 4, 1, 1)
        self.Yt = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.Yt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Yt.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.Yt.setObjectName("Yt")
        self.gridLayout.addWidget(self.Yt, 2, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.Zo = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.Zo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Zo.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.Zo.setObjectName("Zo")
        self.gridLayout.addWidget(self.Zo, 3, 1, 1, 1)
        self.Z1 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.Z1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Z1.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.Z1.setObjectName("Z1")
        self.gridLayout.addWidget(self.Z1, 3, 2, 1, 1)
        self.Z2 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.Z2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Z2.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.Z2.setObjectName("Z2")
        self.gridLayout.addWidget(self.Z2, 3, 3, 1, 1)
        self.Z3 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.Z3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Z3.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.Z3.setObjectName("Z3")
        self.gridLayout.addWidget(self.Z3, 3, 4, 1, 1)
        self.Zt = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.Zt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Zt.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.Zt.setObjectName("Zt")
        self.gridLayout.addWidget(self.Zt, 3, 5, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.theta4o_d = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.theta4o_d.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta4o_d.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta4o_d.setObjectName("theta4o_d")
        self.gridLayout.addWidget(self.theta4o_d, 4, 1, 1, 1)
        self.theta41_d = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.theta41_d.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta41_d.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta41_d.setObjectName("theta41_d")
        self.gridLayout.addWidget(self.theta41_d, 4, 2, 1, 1)
        self.theta42_d = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.theta42_d.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta42_d.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta42_d.setObjectName("theta42_d")
        self.gridLayout.addWidget(self.theta42_d, 4, 3, 1, 1)
        self.theta43_d = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.theta43_d.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta43_d.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta43_d.setObjectName("theta43_d")
        self.gridLayout.addWidget(self.theta43_d, 4, 4, 1, 1)
        self.theta4t_d = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.theta4t_d.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta4t_d.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta4t_d.setObjectName("theta4t_d")
        self.gridLayout.addWidget(self.theta4t_d, 4, 5, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.theta5o_d = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.theta5o_d.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta5o_d.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta5o_d.setObjectName("theta5o_d")
        self.gridLayout.addWidget(self.theta5o_d, 5, 1, 1, 1)
        self.theta51_d = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.theta51_d.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta51_d.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta51_d.setObjectName("theta51_d")
        self.gridLayout.addWidget(self.theta51_d, 5, 2, 1, 1)
        self.theta52_d = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.theta52_d.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta52_d.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta52_d.setObjectName("theta52_d")
        self.gridLayout.addWidget(self.theta52_d, 5, 3, 1, 1)
        self.theta53_d = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.theta53_d.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta53_d.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta53_d.setObjectName("theta53_d")
        self.gridLayout.addWidget(self.theta53_d, 5, 4, 1, 1)
        self.theta5t_d = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.theta5t_d.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta5t_d.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta5t_d.setObjectName("theta5t_d")
        self.gridLayout.addWidget(self.theta5t_d, 5, 5, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.gridLayout.addWidget(self.label_36, 6, 0, 1, 1)
        self.theta5o_d_3 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.theta5o_d_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta5o_d_3.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta5o_d_3.setReadOnly(True)
        self.theta5o_d_3.setObjectName("theta5o_d_3")
        self.gridLayout.addWidget(self.theta5o_d_3, 6, 1, 1, 1)
        self.time1_d = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.time1_d.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.time1_d.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.time1_d.setObjectName("time1_d")
        self.gridLayout.addWidget(self.time1_d, 6, 2, 1, 1)
        self.time2_d = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.time2_d.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.time2_d.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.time2_d.setObjectName("time2_d")
        self.gridLayout.addWidget(self.time2_d, 6, 3, 1, 1)
        self.time3_d = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.time3_d.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.time3_d.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.time3_d.setObjectName("time3_d")
        self.gridLayout.addWidget(self.time3_d, 6, 4, 1, 1)
        self.timet_d = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.timet_d.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.timet_d.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.timet_d.setObjectName("timet_d")
        self.gridLayout.addWidget(self.timet_d, 6, 5, 1, 1)
        self.label_55 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_55.setFont(font)
        self.label_55.setObjectName("label_55")
        self.gridLayout.addWidget(self.label_55, 7, 0, 1, 1)
        self.theta5o_d_2 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.theta5o_d_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta5o_d_2.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta5o_d_2.setReadOnly(True)
        self.theta5o_d_2.setObjectName("theta5o_d_2")
        self.gridLayout.addWidget(self.theta5o_d_2, 7, 1, 1, 1)
        self.mid1v_d = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.mid1v_d.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mid1v_d.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.mid1v_d.setObjectName("mid1v_d")
        self.gridLayout.addWidget(self.mid1v_d, 7, 2, 1, 1)
        self.mid2v_d = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.mid2v_d.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mid2v_d.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.mid2v_d.setObjectName("mid2v_d")
        self.gridLayout.addWidget(self.mid2v_d, 7, 3, 1, 1)
        self.mid3v_d = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.mid3v_d.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mid3v_d.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.mid3v_d.setObjectName("mid3v_d")
        self.gridLayout.addWidget(self.mid3v_d, 7, 4, 1, 1)
        self.theta5t_d_2 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.theta5t_d_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.theta5t_d_2.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.theta5t_d_2.setReadOnly(True)
        self.theta5t_d_2.setObjectName("theta5t_d_2")
        self.gridLayout.addWidget(self.theta5t_d_2, 7, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(81, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 8, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(81, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 8, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(82, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 8, 3, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(81, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 8, 4, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(81, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 8, 5, 1, 1)
        self.Button0_d = QtWidgets.QPushButton(self.layoutWidget_3)
        self.Button0_d.setStyleSheet("\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"font: 75 9pt \"微软雅黑\";\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(86,112,149, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.Button0_d.setObjectName("Button0_d")
        self.gridLayout.addWidget(self.Button0_d, 9, 1, 1, 1)
        self.Button1_d = QtWidgets.QPushButton(self.layoutWidget_3)
        self.Button1_d.setStyleSheet("\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"font: 75 9pt \"微软雅黑\";\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(86,112,149, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.Button1_d.setObjectName("Button1_d")
        self.gridLayout.addWidget(self.Button1_d, 9, 2, 1, 1)
        self.Button2_d = QtWidgets.QPushButton(self.layoutWidget_3)
        self.Button2_d.setStyleSheet("\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"font: 75 9pt \"微软雅黑\";\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(86,112,149, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.Button2_d.setObjectName("Button2_d")
        self.gridLayout.addWidget(self.Button2_d, 9, 3, 1, 1)
        self.Button3_d = QtWidgets.QPushButton(self.layoutWidget_3)
        self.Button3_d.setStyleSheet("\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"font: 75 9pt \"微软雅黑\";\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(86,112,149, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.Button3_d.setObjectName("Button3_d")
        self.gridLayout.addWidget(self.Button3_d, 9, 4, 1, 1)
        self.Buttont_d = QtWidgets.QPushButton(self.layoutWidget_3)
        self.Buttont_d.setStyleSheet("\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"font: 75 9pt \"微软雅黑\";\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(86,112,149, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.Buttont_d.setObjectName("Buttont_d")
        self.gridLayout.addWidget(self.Buttont_d, 9, 5, 1, 1)
        self.planmode_cart = QtWidgets.QComboBox(self.tab)
        self.planmode_cart.setGeometry(QtCore.QRect(450, 360, 91, 26))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.planmode_cart.setFont(font)
        self.planmode_cart.setObjectName("planmode_cart")
        self.planmode_cart.addItem("")
        self.planmode_cart.addItem("")
        self.label_56 = QtWidgets.QLabel(self.tab)
        self.label_56.setGeometry(QtCore.QRect(351, 360, 92, 27))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget_4 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget_4.setGeometry(QtCore.QRect(0, 10, 551, 211))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget_4)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem10 = QtWidgets.QSpacerItem(81, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem10, 4, 1, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.gridLayout_3.addWidget(self.label_44, 0, 2, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(81, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem11, 4, 4, 1, 1)
        self.Zt_2 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.Zt_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Zt_2.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.Zt_2.setObjectName("Zt_2")
        self.gridLayout_3.addWidget(self.Zt_2, 3, 5, 1, 1)
        self.Y2_2 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.Y2_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Y2_2.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.Y2_2.setObjectName("Y2_2")
        self.gridLayout_3.addWidget(self.Y2_2, 2, 3, 1, 1)
        self.X3_2 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.X3_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.X3_2.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.X3_2.setObjectName("X3_2")
        self.gridLayout_3.addWidget(self.X3_2, 1, 4, 1, 1)
        self.Y3_2 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.Y3_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Y3_2.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.Y3_2.setObjectName("Y3_2")
        self.gridLayout_3.addWidget(self.Y3_2, 2, 4, 1, 1)
        self.X2_2 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.X2_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.X2_2.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.X2_2.setObjectName("X2_2")
        self.gridLayout_3.addWidget(self.X2_2, 1, 3, 1, 1)
        self.Button1_d_2 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.Button1_d_2.setStyleSheet("\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"font: 75 9pt \"微软雅黑\";\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(86,112,149, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.Button1_d_2.setObjectName("Button1_d_2")
        self.gridLayout_3.addWidget(self.Button1_d_2, 5, 2, 1, 1)
        self.Yt_2 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.Yt_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Yt_2.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.Yt_2.setObjectName("Yt_2")
        self.gridLayout_3.addWidget(self.Yt_2, 2, 5, 1, 1)
        self.Xt_2 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.Xt_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Xt_2.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.Xt_2.setObjectName("Xt_2")
        self.gridLayout_3.addWidget(self.Xt_2, 1, 5, 1, 1)
        self.Z3_2 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.Z3_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Z3_2.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.Z3_2.setObjectName("Z3_2")
        self.gridLayout_3.addWidget(self.Z3_2, 3, 4, 1, 1)
        self.X1_2 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.X1_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.X1_2.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.X1_2.setObjectName("X1_2")
        self.gridLayout_3.addWidget(self.X1_2, 1, 2, 1, 1)
        self.Y1_2 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.Y1_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Y1_2.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.Y1_2.setObjectName("Y1_2")
        self.gridLayout_3.addWidget(self.Y1_2, 2, 2, 1, 1)
        self.Z2_2 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.Z2_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Z2_2.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.Z2_2.setObjectName("Z2_2")
        self.gridLayout_3.addWidget(self.Z2_2, 3, 3, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.gridLayout_3.addWidget(self.label_43, 0, 1, 1, 1)
        self.Button3_d_2 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.Button3_d_2.setStyleSheet("\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"font: 75 9pt \"微软雅黑\";\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(86,112,149, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.Button3_d_2.setObjectName("Button3_d_2")
        self.gridLayout_3.addWidget(self.Button3_d_2, 5, 4, 1, 1)
        self.Button0_d_2 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.Button0_d_2.setStyleSheet("\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"font: 75 9pt \"微软雅黑\";\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(86,112,149, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.Button0_d_2.setObjectName("Button0_d_2")
        self.gridLayout_3.addWidget(self.Button0_d_2, 5, 1, 1, 1)
        self.Xo_2 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.Xo_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Xo_2.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.Xo_2.setObjectName("Xo_2")
        self.gridLayout_3.addWidget(self.Xo_2, 1, 1, 1, 1)
        self.label_48 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_48.setFont(font)
        self.label_48.setObjectName("label_48")
        self.gridLayout_3.addWidget(self.label_48, 1, 0, 1, 1)
        self.Yo_2 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.Yo_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Yo_2.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.Yo_2.setObjectName("Yo_2")
        self.gridLayout_3.addWidget(self.Yo_2, 2, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(82, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem12, 4, 3, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(81, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem13, 4, 5, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(81, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem14, 4, 2, 1, 1)
        self.label_47 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.gridLayout_3.addWidget(self.label_47, 0, 5, 1, 1)
        self.Button2_d_2 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.Button2_d_2.setStyleSheet("\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"font: 75 9pt \"微软雅黑\";\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(86,112,149, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.Button2_d_2.setObjectName("Button2_d_2")
        self.gridLayout_3.addWidget(self.Button2_d_2, 5, 3, 1, 1)
        self.Z1_2 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.Z1_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Z1_2.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.Z1_2.setObjectName("Z1_2")
        self.gridLayout_3.addWidget(self.Z1_2, 3, 2, 1, 1)
        self.Buttont_d_2 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.Buttont_d_2.setStyleSheet("\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"font: 75 9pt \"微软雅黑\";\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(86,112,149, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.Buttont_d_2.setObjectName("Buttont_d_2")
        self.gridLayout_3.addWidget(self.Buttont_d_2, 5, 5, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.gridLayout_3.addWidget(self.label_45, 0, 3, 1, 1)
        self.label_46 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.gridLayout_3.addWidget(self.label_46, 0, 4, 1, 1)
        self.Zo_2 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.Zo_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Zo_2.setStyleSheet("border-radius: 10px;  \n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"\n"
"")
        self.Zo_2.setObjectName("Zo_2")
        self.gridLayout_3.addWidget(self.Zo_2, 3, 1, 1, 1)
        self.label_49 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.gridLayout_3.addWidget(self.label_49, 2, 0, 1, 1)
        self.label_50 = QtWidgets.QLabel(self.layoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_50.setFont(font)
        self.label_50.setObjectName("label_50")
        self.gridLayout_3.addWidget(self.label_50, 3, 0, 1, 1)
        self.label_51 = QtWidgets.QLabel(self.tab_3)
        self.label_51.setGeometry(QtCore.QRect(400, 330, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_51.setFont(font)
        self.label_51.setObjectName("label_51")
        self.realtime_sim_button = QtWidgets.QPushButton(self.tab_3)
        self.realtime_sim_button.setGeometry(QtCore.QRect(420, 260, 61, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.realtime_sim_button.setFont(font)
        self.realtime_sim_button.setStyleSheet("\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(91, 118, 236, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"image: url(:/png/control.png);\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.realtime_sim_button.setText("")
        self.realtime_sim_button.setObjectName("realtime_sim_button")
        self.ik_sim_button = QtWidgets.QPushButton(self.tab_3)
        self.ik_sim_button.setGeometry(QtCore.QRect(90, 260, 61, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.ik_sim_button.setFont(font)
        self.ik_sim_button.setStyleSheet("\n"
"\n"
"\n"
"\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"\n"
"image: url(:/png/arrowtip.png);\n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(19, 134, 209, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.ik_sim_button.setText("")
        self.ik_sim_button.setObjectName("ik_sim_button")
        self.label_52 = QtWidgets.QLabel(self.tab_3)
        self.label_52.setGeometry(QtCore.QRect(70, 330, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_52.setFont(font)
        self.label_52.setObjectName("label_52")
        self.caidanbutton = QtWidgets.QPushButton(self.tab_3)
        self.caidanbutton.setGeometry(QtCore.QRect(260, 260, 61, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.caidanbutton.setFont(font)
        self.caidanbutton.setStyleSheet("\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"image: url(:/png/heart.png);\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 37, 205, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.caidanbutton.setText("")
        self.caidanbutton.setObjectName("caidanbutton")
        self.tabWidget.addTab(self.tab_3, "")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(530, 490, 561, 311))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(720, 449, 161, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.start_Button = QtWidgets.QPushButton(self.centralwidget)
        self.start_Button.setGeometry(QtCore.QRect(1230, 640, 61, 61))
        self.start_Button.setStyleSheet("\n"
"\n"
" \n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"image: url(:/png/start.png);\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.start_Button.setText("")
        self.start_Button.setObjectName("start_Button")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(1220, 710, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(1330, 130, 61, 28))
        font = QtGui.QFont()
        font.setFamily("LCD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(1141, 123, 24, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(1141, 178, 24, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(1141, 233, 24, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(1141, 288, 24, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(1141, 343, 24, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(1330, 185, 61, 28))
        font = QtGui.QFont()
        font.setFamily("LCD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(1330, 240, 61, 28))
        font = QtGui.QFont()
        font.setFamily("LCD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(1330, 295, 61, 28))
        font = QtGui.QFont()
        font.setFamily("LCD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(1330, 350, 61, 28))
        font = QtGui.QFont()
        font.setFamily("LCD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(1160, 80, 171, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(1190, 105, 111, 291))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.theta1slider = QtWidgets.QSlider(self.layoutWidget)
        self.theta1slider.setStyleSheet("QSlider::groove{\n"
"    background-color: qlineargradient(spread:pad, x1:0.085, y1:0.715636, x2:0.990299, y2:0.227, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"    \n"
"    \n"
"\n"
"height: 8px; /* 整体高度 */\n"
"\n"
"\n"
"\n"
"margin: 0px 0; /* 0px 设置已划过的地方高度, \"0\" 距离父控件的距离*/\n"
"\n"
"}\n"
"\n"
"/* 顶部拖动设计 */\n"
"\n"
"QSlider::handle{\n"
"\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(189, 190, 192, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"\n"
"width: 18px;\n"
"\n"
"margin: -2px 0; /*滑块大小设置*/\n"
"\n"
"border-radius: 3px; /* 圆角设置 */\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"/* 未滑动的区域 */\n"
"\n"
"QSlider::add-page:horizontal\n"
"\n"
"{undefined\n"
"\n"
"border-radius: 3px;\n"
"qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 193, 255), stop:1 rgba(255, 255, 255, 255))\n"
"\n"
"height: 8px; /* 整体高度 */\n"
"\n"
"}\n"
"\n"
"\n"
"/* 已划过的设置*/\n"
"\n"
"QSlider::sub-page:horizontal\n"
"\n"
"{undefined\n"
"\n"
"border: 1px solid #00ffFF; /* 边框颜色 */\n"
"\n"
"background:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #000000, stop:1 #0000FF); /* 颜色渐变*/\n"
"\n"
"border-radius: 3px;\n"
"\n"
"height: 8px; /* 整体高度 */\n"
"\n"
"}\n"
"")
        self.theta1slider.setMinimum(-135)
        self.theta1slider.setMaximum(135)
        self.theta1slider.setProperty("value", 0)
        self.theta1slider.setSliderPosition(0)
        self.theta1slider.setOrientation(QtCore.Qt.Horizontal)
        self.theta1slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.theta1slider.setTickInterval(0)
        self.theta1slider.setObjectName("theta1slider")
        self.verticalLayout_2.addWidget(self.theta1slider)
        self.theta2slider = QtWidgets.QSlider(self.layoutWidget)
        self.theta2slider.setStyleSheet("QSlider::groove{\n"
"    background-color: qlineargradient(spread:pad, x1:0.085, y1:0.715636, x2:0.990299, y2:0.227, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"    \n"
"    \n"
"\n"
"height: 8px; /* 整体高度 */\n"
"\n"
"\n"
"\n"
"margin: 0px 0; /* 0px 设置已划过的地方高度, \"0\" 距离父控件的距离*/\n"
"\n"
"}\n"
"\n"
"/* 顶部拖动设计 */\n"
"\n"
"QSlider::handle{\n"
"\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(189, 190, 192, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"\n"
"width: 18px;\n"
"\n"
"margin: -2px 0; /*滑块大小设置*/\n"
"\n"
"border-radius: 3px; /* 圆角设置 */\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"/* 未滑动的区域 */\n"
"\n"
"QSlider::add-page:horizontal\n"
"\n"
"{undefined\n"
"\n"
"border-radius: 3px;\n"
"qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 193, 255), stop:1 rgba(255, 255, 255, 255))\n"
"\n"
"height: 8px; /* 整体高度 */\n"
"\n"
"}\n"
"\n"
"\n"
"/* 已划过的设置*/\n"
"\n"
"QSlider::sub-page:horizontal\n"
"\n"
"{undefined\n"
"\n"
"border: 1px solid #00ffFF; /* 边框颜色 */\n"
"\n"
"background:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #000000, stop:1 #0000FF); /* 颜色渐变*/\n"
"\n"
"border-radius: 3px;\n"
"\n"
"height: 8px; /* 整体高度 */\n"
"\n"
"}\n"
"")
        self.theta2slider.setMinimum(-90)
        self.theta2slider.setMaximum(90)
        self.theta2slider.setProperty("value", 0)
        self.theta2slider.setSliderPosition(0)
        self.theta2slider.setOrientation(QtCore.Qt.Horizontal)
        self.theta2slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.theta2slider.setTickInterval(0)
        self.theta2slider.setObjectName("theta2slider")
        self.verticalLayout_2.addWidget(self.theta2slider)
        self.theta3slider = QtWidgets.QSlider(self.layoutWidget)
        self.theta3slider.setStyleSheet("QSlider::groove{\n"
"    background-color: qlineargradient(spread:pad, x1:0.085, y1:0.715636, x2:0.990299, y2:0.227, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"    \n"
"    \n"
"\n"
"height: 8px; /* 整体高度 */\n"
"\n"
"\n"
"\n"
"margin: 0px 0; /* 0px 设置已划过的地方高度, \"0\" 距离父控件的距离*/\n"
"\n"
"}\n"
"\n"
"/* 顶部拖动设计 */\n"
"\n"
"QSlider::handle{\n"
"\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(189, 190, 192, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"\n"
"width: 18px;\n"
"\n"
"margin: -2px 0; /*滑块大小设置*/\n"
"\n"
"border-radius: 3px; /* 圆角设置 */\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"/* 未滑动的区域 */\n"
"\n"
"QSlider::add-page:horizontal\n"
"\n"
"{undefined\n"
"\n"
"border-radius: 3px;\n"
"qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 193, 255), stop:1 rgba(255, 255, 255, 255))\n"
"\n"
"height: 8px; /* 整体高度 */\n"
"\n"
"}\n"
"\n"
"\n"
"/* 已划过的设置*/\n"
"\n"
"QSlider::sub-page:horizontal\n"
"\n"
"{undefined\n"
"\n"
"border: 1px solid #00ffFF; /* 边框颜色 */\n"
"\n"
"background:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #000000, stop:1 #0000FF); /* 颜色渐变*/\n"
"\n"
"border-radius: 3px;\n"
"\n"
"height: 8px; /* 整体高度 */\n"
"\n"
"}\n"
"")
        self.theta3slider.setMinimum(-135)
        self.theta3slider.setMaximum(135)
        self.theta3slider.setProperty("value", 0)
        self.theta3slider.setSliderPosition(0)
        self.theta3slider.setOrientation(QtCore.Qt.Horizontal)
        self.theta3slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.theta3slider.setTickInterval(0)
        self.theta3slider.setObjectName("theta3slider")
        self.verticalLayout_2.addWidget(self.theta3slider)
        self.theta4slider = QtWidgets.QSlider(self.layoutWidget)
        self.theta4slider.setStyleSheet("QSlider::groove{\n"
"    background-color: qlineargradient(spread:pad, x1:0.085, y1:0.715636, x2:0.990299, y2:0.227, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"    \n"
"    \n"
"\n"
"height: 8px; /* 整体高度 */\n"
"\n"
"\n"
"\n"
"margin: 0px 0; /* 0px 设置已划过的地方高度, \"0\" 距离父控件的距离*/\n"
"\n"
"}\n"
"\n"
"/* 顶部拖动设计 */\n"
"\n"
"QSlider::handle{\n"
"\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(189, 190, 192, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"\n"
"width: 18px;\n"
"\n"
"margin: -2px 0; /*滑块大小设置*/\n"
"\n"
"border-radius: 3px; /* 圆角设置 */\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"/* 未滑动的区域 */\n"
"\n"
"QSlider::add-page:horizontal\n"
"\n"
"{undefined\n"
"\n"
"border-radius: 3px;\n"
"qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 193, 255), stop:1 rgba(255, 255, 255, 255))\n"
"\n"
"height: 8px; /* 整体高度 */\n"
"\n"
"}\n"
"\n"
"\n"
"/* 已划过的设置*/\n"
"\n"
"QSlider::sub-page:horizontal\n"
"\n"
"{undefined\n"
"\n"
"border: 1px solid #00ffFF; /* 边框颜色 */\n"
"\n"
"background:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #000000, stop:1 #0000FF); /* 颜色渐变*/\n"
"\n"
"border-radius: 3px;\n"
"\n"
"height: 8px; /* 整体高度 */\n"
"\n"
"}\n"
"")
        self.theta4slider.setMinimum(-135)
        self.theta4slider.setMaximum(135)
        self.theta4slider.setProperty("value", 0)
        self.theta4slider.setSliderPosition(0)
        self.theta4slider.setOrientation(QtCore.Qt.Horizontal)
        self.theta4slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.theta4slider.setTickInterval(0)
        self.theta4slider.setObjectName("theta4slider")
        self.verticalLayout_2.addWidget(self.theta4slider)
        self.theta5slider = QtWidgets.QSlider(self.layoutWidget)
        self.theta5slider.setStyleSheet("QSlider::groove{\n"
"    background-color: qlineargradient(spread:pad, x1:0.085, y1:0.715636, x2:0.990299, y2:0.227, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"    \n"
"    \n"
"\n"
"height: 8px; /* 整体高度 */\n"
"\n"
"\n"
"\n"
"margin: 0px 0; /* 0px 设置已划过的地方高度, \"0\" 距离父控件的距离*/\n"
"\n"
"}\n"
"\n"
"/* 顶部拖动设计 */\n"
"\n"
"QSlider::handle{\n"
"\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(189, 190, 192, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"\n"
"width: 18px;\n"
"\n"
"margin: -2px 0; /*滑块大小设置*/\n"
"\n"
"border-radius: 3px; /* 圆角设置 */\n"
"\n"
"\n"
"}\n"
"\n"
"\n"
"/* 未滑动的区域 */\n"
"\n"
"QSlider::add-page:horizontal\n"
"\n"
"{undefined\n"
"\n"
"border-radius: 3px;\n"
"qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 193, 255), stop:1 rgba(255, 255, 255, 255))\n"
"\n"
"height: 8px; /* 整体高度 */\n"
"\n"
"}\n"
"\n"
"\n"
"/* 已划过的设置*/\n"
"\n"
"QSlider::sub-page:horizontal\n"
"\n"
"{undefined\n"
"\n"
"border: 1px solid #00ffFF; /* 边框颜色 */\n"
"\n"
"background:qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #000000, stop:1 #0000FF); /* 颜色渐变*/\n"
"\n"
"border-radius: 3px;\n"
"\n"
"height: 8px; /* 整体高度 */\n"
"\n"
"}\n"
"")
        self.theta5slider.setMinimum(-135)
        self.theta5slider.setMaximum(135)
        self.theta5slider.setProperty("value", 0)
        self.theta5slider.setSliderPosition(0)
        self.theta5slider.setOrientation(QtCore.Qt.Horizontal)
        self.theta5slider.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.theta5slider.setTickInterval(0)
        self.theta5slider.setObjectName("theta5slider")
        self.verticalLayout_2.addWidget(self.theta5slider)
        self.reset_button = QtWidgets.QPushButton(self.centralwidget)
        self.reset_button.setGeometry(QtCore.QRect(1130, 390, 61, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.reset_button.setFont(font)
        self.reset_button.setStyleSheet("\n"
"\n"
"\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(199,237,233, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.reset_button.setObjectName("reset_button")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 481, 781))
        self.widget.setObjectName("widget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 481, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 50, 481, 341))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(0, 390, 481, 51))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_4.addWidget(self.label_14)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.widget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(0, 440, 481, 341))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        pg.setConfigOptions(antialias=True)  # 开启曲线抗锯齿
        self.win1 = pg.GraphicsLayoutWidget()  # 创建pg layout，可实现数据界面布局自动管理
        self.win2 = pg.GraphicsLayoutWidget()  # 创建pg layout，可实现数据界面布局自动管理
        # pg绘图窗口可以作为一个widget添加到GUI中的graph_layout，当然也可以添加到Qt其他所有的容器中
        self.verticalLayout_3.addWidget(self.win1)
        self.verticalLayout_5.addWidget(self.win2)
        self.p1 = self.win1.addPlot(title="Joint Pos")  # 添加第一个绘图窗口
        self.p1.setLabel('left', text='pos', units='rad/s', color='#ffffff')  # y轴设置函数
        self.p1.showGrid(x=True, y=True)  # 栅格设置函数
        self.p1.setLogMode(x=False, y=False)  # False代表线性坐标轴，True代表对数坐标轴
        self.p1.setLabel('bottom', text='time', units='s')  # x轴设置函数
        self.p1.addLegend(size=(50, 30))  # 可选择是否添加legend
        self.p2 = self.win2.addPlot(title="Joint Vel")  # 添加第一个绘图窗口
        self.p2.setLabel('left', text='vel', units='rad/s', color='#ffffff')  # y轴设置函数
        self.p2.showGrid(x=True, y=True)  # 栅格设置函数
        self.p2.setLogMode(x=False, y=False)  # False代表线性坐标轴，True代表对数坐标轴
        self.p2.setLabel('bottom', text='time', units='s')  # x轴设置函数
        self.p2.addLegend(size=(50, 30))  # 可选择是否添加legend

        self.gripper_release = QtWidgets.QPushButton(self.centralwidget)
        self.gripper_release.setGeometry(QtCore.QRect(1290, 390, 61, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.gripper_release.setFont(font)
        self.gripper_release.setStyleSheet("\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0.085, y1:0.715636, x2:1, y2:0.579273, stop:0 rgba(147,179,218, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.gripper_release.setObjectName("gripper_release")
        self.gripper_close = QtWidgets.QPushButton(self.centralwidget)
        self.gripper_close.setGeometry(QtCore.QRect(1210, 390, 61, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.gripper_close.setFont(font)
        self.gripper_close.setStyleSheet("\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(175, 215, 237, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.gripper_close.setObjectName("gripper_close")
        self.visual_button = QtWidgets.QPushButton(self.centralwidget)
        self.visual_button.setGeometry(QtCore.QRect(1130, 570, 61, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.visual_button.setFont(font)
        self.visual_button.setStyleSheet("\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"image: url(:/png/camera.png);\n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(215,215,215, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.visual_button.setText("")
        self.visual_button.setObjectName("visual_button")
        self.interact_button = QtWidgets.QPushButton(self.centralwidget)
        self.interact_button.setGeometry(QtCore.QRect(1130, 710, 61, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.interact_button.setFont(font)
        self.interact_button.setStyleSheet(" \n"
"\n"
" \n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(116,116,116, 255), stop:1 rgba(255, 255, 255, 255));\n"
"image: url(:/png/hand.png);\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.interact_button.setText("")
        self.interact_button.setObjectName("interact_button")
        self.label_41 = QtWidgets.QLabel(self.centralwidget)
        self.label_41.setGeometry(QtCore.QRect(1120, 640, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.label_42 = QtWidgets.QLabel(self.centralwidget)
        self.label_42.setGeometry(QtCore.QRect(1120, 780, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.bionics_button = QtWidgets.QPushButton(self.centralwidget)
        self.bionics_button.setGeometry(QtCore.QRect(1330, 710, 61, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.bionics_button.setFont(font)
        self.bionics_button.setStyleSheet(" \n"
"\n"
" \n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(95,95,95, 255), stop:1 rgba(255, 255, 255, 255));\n"
"image: url(:/png/arm.png);\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.bionics_button.setText("")
        self.bionics_button.setObjectName("bionics_button")
        self.label_53 = QtWidgets.QLabel(self.centralwidget)
        self.label_53.setGeometry(QtCore.QRect(1320, 780, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_53.setFont(font)
        self.label_53.setObjectName("label_53")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(1090, 440, 81, 131))
        self.widget_2.setStyleSheet("image: url(:/png/robot.png);")
        self.widget_2.setObjectName("widget_2")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(1160, 460, 231, 51))
        self.widget_3.setStyleSheet("image: url(:/png/tech.png);")
        self.widget_3.setObjectName("widget_3")
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setGeometry(QtCore.QRect(1200, 510, 131, 41))
        self.widget_5.setStyleSheet("image: url(:/png/scut2.png);")
        self.widget_5.setObjectName("widget_5")
        self.label_54 = QtWidgets.QLabel(self.centralwidget)
        self.label_54.setGeometry(QtCore.QRect(1320, 640, 81, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_54.setFont(font)
        self.label_54.setObjectName("label_54")
        self.speech_control_button = QtWidgets.QPushButton(self.centralwidget)
        self.speech_control_button.setGeometry(QtCore.QRect(1330, 570, 61, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.speech_control_button.setFont(font)
        self.speech_control_button.setStyleSheet(" \n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"image: url(:/png/speech.png);\n"
"\n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(143,143,143, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.speech_control_button.setText("")
        self.speech_control_button.setObjectName("speech_control_button")
        self.label_40 = QtWidgets.QLabel(self.centralwidget)
        self.label_40.setGeometry(QtCore.QRect(1110, 10, 80, 27))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.serial_num = QtWidgets.QComboBox(self.centralwidget)
        self.serial_num.setGeometry(QtCore.QRect(1200, 10, 101, 26))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.serial_num.setFont(font)
        self.serial_num.setObjectName("serial_num")
        self.serial_num.addItem("")
        self.serial_num.addItem("")
        self.serial_num.addItem("")
        self.serialconnect_buttton = QtWidgets.QPushButton(self.centralwidget)
        self.serialconnect_buttton.setGeometry(QtCore.QRect(1320, 30, 81, 24))
        self.serialconnect_buttton.setStyleSheet("\n"
"\n"
"/*按钮普通态*/\n"
"QPushButton\n"
"{\n"
"font: 75 9pt \"微软雅黑\";\n"
"border: 2px groove gray;\n"
"border-style: outset;\n"
"border-radius: 10px;  \n"
"background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(86,112,149, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮停留态*/\n"
"QPushButton:hover\n"
"{\n"
"  background-color: qlineargradient(spread:pad, x1:0.115, y1:0.897454, x2:1, y2:0.579273, stop:0 rgba(216, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
" \n"
"/*按钮按下态*/\n"
"QPushButton:pressed\n"
"{\n"
"    /*背景颜色*/  \n"
"    background-color:rgb(14 , 135 , 228);\n"
"    /*左内边距为3像素，让按下时字向右移动3像素*/  \n"
"    padding-left:3px;\n"
"    /*上内边距为3像素，让按下时字向下移动3像素*/  \n"
"    padding-top:3px;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.serialconnect_buttton.setObjectName("serialconnect_buttton")
        self.label_60 = QtWidgets.QLabel(self.centralwidget)
        self.label_60.setGeometry(QtCore.QRect(1120, 50, 60, 27))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_60.setFont(font)
        self.label_60.setObjectName("label_60")
        self.baudrate_num = QtWidgets.QComboBox(self.centralwidget)
        self.baudrate_num.setGeometry(QtCore.QRect(1200, 50, 101, 26))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.baudrate_num.setFont(font)
        self.baudrate_num.setObjectName("baudrate_num")
        self.baudrate_num.addItem("")
        self.baudrate_num.addItem("")
        self.baudrate_num.addItem("")
        self.baudrate_num.addItem("")
        self.baudrate_num.addItem("")
        self.baudrate_num.addItem("")
        self.baudrate_num.addItem("")
        self.baudrate_num.addItem("")
        self.baudrate_num.addItem("")
        self.baudrate_num.addItem("")
        self.baudrate_num.addItem("")
        self.baudrate_num.addItem("")
        self.baudrate_num.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1419, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.baudrate_num.setCurrentIndex(10)
        self.theta1slider.valueChanged['int'].connect(self.label_15.setNum)
        self.theta2slider.valueChanged['int'].connect(self.label_26.setNum)
        self.theta3slider.valueChanged['int'].connect(self.label_27.setNum)
        self.theta4slider.valueChanged['int'].connect(self.label_28.setNum)
        self.theta5slider.valueChanged['int'].connect(self.label_29.setNum)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.interval_button.setText(_translate("MainWindow", "导入"))
        self.label_21.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">起始点</p></body></html>"))
        self.label_22.setText(_translate("MainWindow", "中间点1"))
        self.label_23.setText(_translate("MainWindow", "中间点2"))
        self.label_24.setText(_translate("MainWindow", "中间点3"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">目标点</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">θ<span style=\" vertical-align:sub;\">1</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">θ<span style=\" vertical-align:sub;\">2</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">θ<span style=\" vertical-align:sub;\">3</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">θ<span style=\" vertical-align:sub;\">4</span></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">θ<span style=\" vertical-align:sub;\">5</span></p></body></html>"))
        self.label_37.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">区间运行时间</span></p></body></html>"))
        self.theta5t_d_3.setText(_translate("MainWindow", "0"))
        self.label_57.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">中间点速度</span></p></body></html>"))
        self.theta5o_d_4.setText(_translate("MainWindow", "0"))
        self.theta5o_d_5.setText(_translate("MainWindow", "0"))
        self.Button0.setText(_translate("MainWindow", "导入"))
        self.Button1.setText(_translate("MainWindow", "导入"))
        self.Button2.setText(_translate("MainWindow", "导入"))
        self.Button3.setText(_translate("MainWindow", "导入"))
        self.Buttont.setText(_translate("MainWindow", "导入"))
        self.label_58.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">规划模式</span></p></body></html>"))
        self.label_59.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">修改插值间隔</span></p></body></html>"))
        self.planmode_joint.setItemText(0, _translate("MainWindow", "步进"))
        self.planmode_joint.setItemText(1, _translate("MainWindow", "连续"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "   关节空间   "))
        self.interval_d_button.setText(_translate("MainWindow", "导入"))
        self.label_39.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">修改插值间隔</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">起始点</p></body></html>"))
        self.label_17.setText(_translate("MainWindow", "中间点1"))
        self.label_18.setText(_translate("MainWindow", "中间点2"))
        self.label_19.setText(_translate("MainWindow", "中间点3"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">目标点</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">x坐标</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">y坐标</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">z坐标</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p>自定义θ<span style=\" vertical-align:sub;\">4</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p>自定义θ<span style=\" vertical-align:sub;\">5</span></p></body></html>"))
        self.label_36.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">区间运行时间</span></p></body></html>"))
        self.theta5o_d_3.setText(_translate("MainWindow", "0"))
        self.label_55.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">中间点速度</span></p></body></html>"))
        self.theta5o_d_2.setText(_translate("MainWindow", "0"))
        self.theta5t_d_2.setText(_translate("MainWindow", "0"))
        self.Button0_d.setText(_translate("MainWindow", "导入"))
        self.Button1_d.setText(_translate("MainWindow", "导入"))
        self.Button2_d.setText(_translate("MainWindow", "导入"))
        self.Button3_d.setText(_translate("MainWindow", "导入"))
        self.Buttont_d.setText(_translate("MainWindow", "导入"))
        self.planmode_cart.setItemText(0, _translate("MainWindow", "步进"))
        self.planmode_cart.setItemText(1, _translate("MainWindow", "连续"))
        self.label_56.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">规划模式</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "   笛卡尔空间    "))
        self.label_44.setText(_translate("MainWindow", "中间点1"))
        self.Button1_d_2.setText(_translate("MainWindow", "导入"))
        self.label_43.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">起始点</p></body></html>"))
        self.Button3_d_2.setText(_translate("MainWindow", "导入"))
        self.Button0_d_2.setText(_translate("MainWindow", "导入"))
        self.label_48.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">x坐标</p></body></html>"))
        self.label_47.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">目标点</p></body></html>"))
        self.Button2_d_2.setText(_translate("MainWindow", "导入"))
        self.Buttont_d_2.setText(_translate("MainWindow", "导入"))
        self.label_45.setText(_translate("MainWindow", "中间点2"))
        self.label_46.setText(_translate("MainWindow", "中间点3"))
        self.label_49.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">y坐标</p></body></html>"))
        self.label_50.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">z坐标</p></body></html>"))
        self.label_51.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">实时控制仿真</p></body></html>"))
        self.label_52.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">轨迹规划仿真</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "   离线仿真模块   "))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">实时状态提示栏</span></p></body></html>"))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">启动机械臂</p></body></html>"))
        self.label_15.setText(_translate("MainWindow", "0"))
        self.label_30.setText(_translate("MainWindow", "<html><head/><body><p>θ<span style=\" vertical-align:sub;\">1</span></p></body></html>"))
        self.label_31.setText(_translate("MainWindow", "<html><head/><body><p>θ<span style=\" vertical-align:sub;\">2</span></p></body></html>"))
        self.label_32.setText(_translate("MainWindow", "<html><head/><body><p>θ<span style=\" vertical-align:sub;\">3</span></p></body></html>"))
        self.label_33.setText(_translate("MainWindow", "<html><head/><body><p>θ<span style=\" vertical-align:sub;\">4</span></p></body></html>"))
        self.label_34.setText(_translate("MainWindow", "<html><head/><body><p>θ<span style=\" vertical-align:sub;\">5</span></p></body></html>"))
        self.label_26.setText(_translate("MainWindow", "0"))
        self.label_27.setText(_translate("MainWindow", "0"))
        self.label_28.setText(_translate("MainWindow", "0"))
        self.label_29.setText(_translate("MainWindow", "0"))
        self.label_35.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">实时控制区</span></p></body></html>"))
        self.reset_button.setText(_translate("MainWindow", "复位"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">关节角度</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">关节速度</span></p></body></html>"))
        self.gripper_release.setText(_translate("MainWindow", "释放"))
        self.gripper_close.setText(_translate("MainWindow", "闭合"))
        self.label_41.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">视觉标定</p></body></html>"))
        self.label_42.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">手势交互</p></body></html>"))
        self.label_53.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">机器人仿生</p></body></html>"))
        self.label_54.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">语音控制</p></body></html>"))
        self.label_40.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">选择串口</span></p></body></html>"))
        self.serial_num.setItemText(0, _translate("MainWindow", "COM7"))
        self.serial_num.setItemText(1, _translate("MainWindow", "COM8"))
        self.serial_num.setItemText(2, _translate("MainWindow", "COM9"))
        self.serialconnect_buttton.setText(_translate("MainWindow", "连接"))
        self.label_60.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">波特率</span></p></body></html>"))
        self.baudrate_num.setItemText(0, _translate("MainWindow", "600"))
        self.baudrate_num.setItemText(1, _translate("MainWindow", "1200"))
        self.baudrate_num.setItemText(2, _translate("MainWindow", "2400"))
        self.baudrate_num.setItemText(3, _translate("MainWindow", "4800"))
        self.baudrate_num.setItemText(4, _translate("MainWindow", "9600"))
        self.baudrate_num.setItemText(5, _translate("MainWindow", "14400"))
        self.baudrate_num.setItemText(6, _translate("MainWindow", "19200"))
        self.baudrate_num.setItemText(7, _translate("MainWindow", "28800"))
        self.baudrate_num.setItemText(8, _translate("MainWindow", "38400"))
        self.baudrate_num.setItemText(9, _translate("MainWindow", "57600"))
        self.baudrate_num.setItemText(10, _translate("MainWindow", "115200"))
        self.baudrate_num.setItemText(11, _translate("MainWindow", "230400"))
        self.baudrate_num.setItemText(12, _translate("MainWindow", "460800"))

import start_rc
