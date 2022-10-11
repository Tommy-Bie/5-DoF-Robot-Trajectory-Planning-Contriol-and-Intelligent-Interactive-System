from PyQt5 import QtCore, QtGui, QtWidgets
from uidoc import Ui_MainWindow
from PyQt5.QtGui import QIcon
import numpy as np
import math
from math import *
import time
import serial
import pyqtgraph as pg
import mediapipe as mp
from kdl_utils import my_rkdl, angle2pwm, joint_plan, cartesian_plan
from messagebox import *
import cv2
import glob
from threading import Thread
import pybullet as p
import pybullet_data as pd
from aip import AipSpeech
import pyaudio
import wave
from joint_plan_sim import joint_plan_simu
from drawing import *
import ctypes

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid") #为设置任务栏图标做准备

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()
    # 按钮功能设计
    def initUI(self):
        self.setWindowTitle('TPB-TECH DOF-5 Robot Upper Computer')  # 设置窗体标题
        self.setWindowIcon(QIcon('robot.png'))  # 设置窗体标题图标及任务栏图标
        #坐标导入按钮，连接至各个读取输入坐标的函数
        self.Button0.clicked.connect(self.read_o_joint)
        self.Button1.clicked.connect(self.read_1_joint)
        self.Button2.clicked.connect(self.read_2_joint)
        self.Button3.clicked.connect(self.read_3_joint)
        self.Buttont.clicked.connect(self.read_t_joint)
        self.Button0_d.clicked.connect(self.read_o_cart)
        self.Button1_d.clicked.connect(self.read_1_cart)
        self.Button2_d.clicked.connect(self.read_2_cart)
        self.Button3_d.clicked.connect(self.read_3_cart)
        self.Buttont_d.clicked.connect(self.read_t_cart)
        self.Button0_d_2.clicked.connect(self.read_o_sim)
        self.Button1_d_2.clicked.connect(self.read_1_sim)
        self.Button2_d_2.clicked.connect(self.read_2_sim)
        self.Button3_d_2.clicked.connect(self.read_3_sim)
        self.Buttont_d_2.clicked.connect(self.read_t_sim)

        self.start_Button.clicked.connect(self.tra_plan)       # 连接机器人运行函数
        self.reset_button.clicked.connect(self.RST)
        self.theta1slider.sliderReleased.connect(self.read_theta1)
        self.theta2slider.sliderReleased.connect(self.read_theta2)
        self.theta3slider.sliderReleased.connect(self.read_theta3)
        self.theta4slider.sliderReleased.connect(self.read_theta4)
        self.theta5slider.sliderReleased.connect(self.read_theta5)
        self.serialconnect_buttton.clicked.connect(self.read_serialnum)  # 串口连接

        self.interval_d_button.clicked.connect(self.read_interval_d)  # 读取插值间隔按钮
        self.interval_button.clicked.connect(self.read_interval)

        self.planmode_joint.currentIndexChanged.connect(self.read_plan_mode_joint)  # 规划模式
        self.planmode_cart.currentIndexChanged.connect(self.read_plan_mode_cart)

        self.gripper_close.clicked.connect(self.grip_close)  # 闭合按钮
        self.gripper_release.clicked.connect(self.grip_open)  # 释放按钮

        # 5个附加功能
        self.visual_button.clicked.connect(self.vision_eye_to_hand)         # 视觉标定按钮
        self.interact_button.clicked.connect(self.gesture_interact)       # 手势交互按钮
        self.speech_control_button.clicked.connect(self.speech_control)  # 语音控制按钮
        self.bionics_button.clicked.connect(self.arm_pose)  # 机器人仿生按钮
        self.realtime_sim_button.clicked.connect(self.build_thread1)    # 离线仿真
        self.ik_sim_button.clicked.connect(self.build_thread2)
        self.caidanbutton.clicked.connect(self.build_thread3)



        self.modify_interval = False    # 是否修改了插值间隔
        self.calibrate_flag = True
        self.ser = 0    # 检测串口是否连接

    # 读取规划模式
    def read_plan_mode_joint(self):
        self.plan_mode = self.planmode_joint.currentText()

    def read_plan_mode_cart(self):
        self.plan_mode = self.planmode_cart.currentText()

    # 获取坐标
    def read_o_joint(self):
        try:
            self.is_cart = 0
            self.mid = 0
            self.j0 = [0, 0, 0, 0, 0]
            self.j0[0] = self.theta1o.text()
            self.j0[1] = self.theta2o.text()
            self.j0[2] = self.theta3o.text()
            self.j0[3] = self.theta4o.text()
            self.j0[4] = self.theta5o.text()

            msg_pos = "导入起始点成功  " + "θ1:" + self.j0[0] + "度 \t" + "θ2:" + self.j0[1] + "度 \t" + "θ3:" + \
                      self.j0[2] + "度 \t" + "θ4:" + self.j0[3] + "度 \t" + "θ5:" + self.j0[4] + "度 \t"
            self.textBrowser.append(msg_pos)
            self.j0 = list(map(float, self.j0))
            self.j0 = [i / 180 * pi for i in self.j0]
        except:
            messagebox6()

    def read_1_joint(self):
        try:
            self.mid = 1
            self.j1 = [0, 0, 0, 0, 0]
            self.j1[0] = self.theta11.text()
            self.j1[1] = self.theta21.text()
            self.j1[2] = self.theta31.text()
            self.j1[3] = self.theta41.text()
            self.j1[4] = self.theta51.text()
            self.vel1 = float(self.mid1v.text())

            msg_pos = "导入中间点1成功  " + "θ1:" + self.j1[0] + "度 \t" + "θ2:" + self.j1[1] + "度 \t" + "θ3:" + \
                      self.j1[2] + "度 \t" + "θ4:" + self.j1[3] + "度 \t" + "θ5:" + self.j1[4] + "度 \t"
            self.textBrowser.append(msg_pos)
            self.j1 = list(map(float, self.j1))
            self.j1 = [i / 180 * pi for i in self.j1]
            self.t1 = float(self.time1.text())
        except:
            messagebox6()

    def read_2_joint(self):
        try:
            self.mid = 2
            self.j2 = [0, 0, 0, 0, 0]
            self.j2[0] = self.theta12.text()
            self.j2[1] = self.theta22.text()
            self.j2[2] = self.theta32.text()
            self.j2[3] = self.theta42.text()
            self.j2[4] = self.theta52.text()
            self.vel2 = float(self.mid2v.text())

            msg_pos = "导入中间点2成功  " + "θ1:" + self.j2[0] + "度 \t" + "θ2:" + self.j2[1] + "度 \t" + "θ3:" + \
                      self.j2[2] + "度 \t" + "θ4:" + self.j2[3] + "度 \t" + "θ5:" + self.j2[4] + "度 \t"
            self.textBrowser.append(msg_pos)
            self.j2 = list(map(float, self.j2))
            self.j2 = [i / 180 * pi for i in self.j2]
            self.t2 = float(self.time2.text())
        except:
            messagebox6()

    def read_3_joint(self):
        try:
            self.mid = 3
            self.j3 = [0, 0, 0, 0, 0]
            self.j3[0] = self.theta13.text()
            self.j3[1] = self.theta23.text()
            self.j3[2] = self.theta33.text()
            self.j3[3] = self.theta43.text()
            self.j3[4] = self.theta53.text()
            self.vel3 = float(self.mid3v.text())

            msg_pos = "导入中间点3成功  " + "θ1:" + self.j3[0] + "度 \t" + "θ2:" + self.j3[1] + "度 \t" + "θ3:" + \
                      self.j3[2] + "度 \t" + "θ4:" + self.j3[3] + "度 \t" + "θ5:" + self.j3[4] + "度 \t"
            self.textBrowser.append(msg_pos)
            self.j3 = list(map(float, self.j3))
            self.j3 = [i / 180 * pi for i in self.j3]
            self.t3 = float(self.time3.text())
        except:
            messagebox6()

    def read_t_joint(self):
        try:
            self.jt = [0, 0, 0, 0, 0]
            self.jt[0] = self.theta1t.text()
            self.jt[1] = self.theta2t.text()
            self.jt[2] = self.theta3t.text()
            self.jt[3] = self.theta4t.text()
            self.jt[4] = self.theta5t.text()

            msg_pos = "导入目标点成功  " + "θ1:" + self.jt[0] + "度\t" + "θ2:" + self.jt[1] + "度\t" + "θ3:" + \
                      self.jt[2] + "度\t" + "θ4:" + self.jt[3] + "度\t" + "θ5:" + self.jt[4] + "度\t"
            self.textBrowser.append(msg_pos)
            self.jt = list(map(float, self.jt))
            self.jt = [i / 180 * pi for i in self.jt]
            self.tt = float(self.timet.text())
        except:
            messagebox6()

    def read_o_cart(self):
        try:
            self.is_cart = 1
            self.mid = 0
            self.d0 = [0, 0, 0, 0, 0]
            self.d0[0] = self.Xo.text()
            self.d0[1] = self.Yo.text()
            self.d0[2] = self.Zo.text()
            self.d0[3] = self.theta4o_d.text()
            self.d0[4] = self.theta5o_d.text()
            self.d0_prt = self.d0

            self.d0 = list(map(float, self.d0))
            self.d0[3] = self.d0[3] * pi / 180  # 角度转弧度
            self.d0[4] = self.d0[4] * pi / 180
            t, is_error = my_rkdl(self.d0)  # 检验可达性
            if not is_error:
                msg_pos = "导入起始点成功  " + "X:" + self.d0_prt[0] + "\tY:" + self.d0_prt[1] + "\tZ:" + \
                          self.d0_prt[2] + "\tθ4:" + self.d0_prt[3] + "度\t" + "\tθ5:" + self.d0_prt[4] + "度\t"
                self.textBrowser.append(msg_pos)
        except:
            messagebox6()

    def read_1_cart(self):
        try:
            self.mid = 1
            self.d1 = [0, 0, 0, 0, 0]
            self.d1[0] = self.X1.text()
            self.d1[1] = self.Y1.text()
            self.d1[2] = self.Z1.text()
            self.d1[3] = self.theta41_d.text()
            self.d1[4] = self.theta51_d.text()
            self.t1_d = float(self.time1_d.text())
            self.d1_prt = self.d1
            self.vel1 = float(self.mid1v_d.text())

            self.d1 = list(map(float, self.d1))
            self.d1[3] = self.d1[3] * pi / 180
            self.d1[4] = self.d1[4] * pi / 180
            t, is_error = my_rkdl(self.d1)
            if not is_error:
                msg_pos = "导入中间点1成功  " + "X:" + self.d1_prt[0] + "\tY:" + self.d1_prt[1] + "\tZ:" + \
                          self.d1_prt[2] + "\tθ4:" + self.d1_prt[3] + "度\t" + "\tθ5:" + self.d1_prt[4] + "度\t"
                self.textBrowser.append(msg_pos)
        except:
            messagebox6()

    def read_2_cart(self):
        try:
            self.mid = 2
            self.d2 = [0, 0, 0, 0, 0]
            self.d2[0] = self.X2.text()
            self.d2[1] = self.Y2.text()
            self.d2[2] = self.Z2.text()
            self.d2[3] = self.theta42_d.text()
            self.d2[4] = self.theta52_d.text()
            self.t2_d = float(self.time2_d.text())
            self.d2_prt = self.d2
            self.vel2 = float(self.mid2v_d.text())

            self.d2 = list(map(float, self.d2))
            self.d2[3] = self.d2[3] * pi / 180
            self.d2[4] = self.d2[4] * pi / 180
            t, is_error = my_rkdl(self.d2)
            if not is_error:
                msg_pos = "导入中间点2成功  " + "X:" + self.d2_prt[0] + "\tY:" + self.d2_prt[1] + "\tZ:" + \
                          self.d2_prt[2] + "\tθ4:" + self.d2_prt[3] + "度\t" + "\tθ5:" + self.d2_prt[4] + "度\t"
                self.textBrowser.append(msg_pos)
        except:
            messagebox6()

    def read_3_cart(self):
        try:
            self.mid = 3
            self.d3 = [0, 0, 0, 0, 0]
            self.d3[0] = self.X3.text()
            self.d3[1] = self.Y3.text()
            self.d3[2] = self.Z3.text()
            self.d3[3] = self.theta43_d.text()
            self.d3[4] = self.theta53_d.text()
            self.t3_d = float(self.time3_d.text())
            self.d3_prt = self.d3
            self.vel3 = float(self.mid3v_d.text())

            self.d3 = list(map(float, self.d3))
            self.d3[3] = self.d3[3] * pi / 180
            self.d3[4] = self.d3[4] * pi / 180
            t, is_error = my_rkdl(self.d3)
            if not is_error:
                msg_pos = "导入中间点3成功  " + "X:" + self.d3_prt[0] + "\tY:" + self.d3_prt[1] + "\tZ:" + \
                          self.d3_prt[2] + "\tθ4:" + self.d3_prt[3] + "度\t" + "\tθ5:" + self.d3_prt[4] + "度\t"
                self.textBrowser.append(msg_pos)
        except:
            messagebox6()

    def read_t_cart(self):
        try:
            self.dt = [0, 0, 0, 0, 0]
            self.dt[0] = self.Xt.text()
            self.dt[1] = self.Yt.text()
            self.dt[2] = self.Zt.text()
            self.dt[3] = self.theta4t_d.text()
            self.dt[4] = self.theta5t_d.text()
            self.tt_d = float(self.timet_d.text())
            self.dt_prt = self.dt

            self.dt = list(map(float, self.dt))
            self.dt[3] = self.dt[3] * pi / 180  # 角度转弧度
            self.dt[4] = self.dt[4] * pi / 180
            t, is_error = my_rkdl(self.dt)
            if not is_error:
                msg_pos = "导入目标点成功  " + "X:" + self.dt_prt[0] + "\tY:" + self.dt_prt[1] + "\tZ:" + \
                          self.dt_prt[2] + "\tθ4:" + self.dt_prt[3] + "度\t" + "\tθ5:" + self.dt_prt[4] + "度\t"
                self.textBrowser.append(msg_pos)
        except:
            messagebox6()

    # 读取插值间隔
    def read_interval_d(self):
        try:
            self.modify_interval =True
            self.interval_cart = float(self.interval_d.text())
            msg_pos = "修改插值间隔成功\t" + str(self.interval_cart)+"秒"
            self.textBrowser.append(msg_pos)
        except:
            messagebox6()

    def read_interval(self):
        try:
            self.modify_interval = True
            self.interval_joint = float(self.interval.text())
            msg_pos = "修改插值间隔成功\t" + str(self.interval_joint)+"秒"
            self.textBrowser.append(msg_pos)
        except:
            messagebox6()

    # 读取角度值
    def read_theta1(self):
        self.theta1 = self.theta1slider.value()           # 读取上位机输入角度值
        try:
            pwm = angle2pwm(self.theta1)                # 将关节角转为舵机pwm值
            str1 = '#000P' + str(int(pwm)) + 'T200!'    # 编写一次性多舵机指令
            self.ser.write(str1.encode())               # 发送指令
            time.sleep(0.2)                             # 程序休眠
        except:
            self.theta1slider.setValue(0)               # 异常捕获，鲁棒性提示
            messagebox3()

    def read_theta2(self):
        self.theta2=self.theta2slider.value()
        try:
            pwm = angle2pwm(self.theta2 * (-1))
            str1 = '#001P' + str(int(pwm)) + 'T200!'
            self.ser.write(str1.encode())
            time.sleep(0.2)
        except:
            self.theta2slider.setValue(0)
            messagebox3()

    def read_theta3(self):
        self.theta3=self.theta3slider.value()
        try:
            pwm = angle2pwm(self.theta3)
            str1 = '#002P' + str(int(pwm)) + 'T200!'
            self.ser.write(str1.encode())
            time.sleep(0.2)
        except:
            self.theta3slider.setValue(0)
            messagebox3()

    def read_theta4(self):
        self.theta4=self.theta4slider.value()
        try:
            pwm = angle2pwm(self.theta4)
            str1 = '#003P' + str(int(pwm)) + 'T200!'
            self.ser.write(str1.encode())
            time.sleep(0.2)
        except:
            self.theta4slider.setValue(0)
            messagebox3()

    def read_theta5(self):
        self.theta5=self.theta5slider.value()
        try:
            pwm = angle2pwm(self.theta5)
            str1 = '#004P' + str(int(pwm)) + 'T200!'
            self.ser.write(str1.encode())
            time.sleep(0.2)
        except:
            self.theta5slider.setValue(0)
            messagebox3()

    # 读取串口选项
    def read_serialnum(self):
        try:
            if self.ser:
                messagebox7()
            else:
                self.serialnum = self.serial_num.currentText()
                self.baudrate_number=int(self.baudrate_num.currentText())
                self.ser = serial.Serial(port=self.serialnum, baudrate=self.baudrate_number)
                messagebox4()
        except:
            messagebox5()

    # 状态栏提示语
    def show_reach_1(self):
        msg_pos = "到达中间点1"
        self.textBrowser.append(msg_pos)

    def show_reach_2(self):
        msg_pos = "到达中间点2"
        self.textBrowser.append(msg_pos)

    def show_reach_3(self):
        msg_pos = "到达中间点3"
        self.textBrowser.append(msg_pos)

    def show_reach_t(self):
        msg_pos = "到达目标点"
        self.textBrowser.append(msg_pos)

    def show_begin(self):
        msg_pos = "机械臂启动"
        self.textBrowser.append(msg_pos)

    def show_start_plan(self):
        msg_pos = "\n轨迹规划开始："
        self.textBrowser.append(msg_pos)

    def show_finish_plan(self):
        msg_pos = "路径规划完成!"
        self.textBrowser.append(msg_pos)

    def show_legend(self):  # 图例提示
        msg_pos = "蓝色：关节1，绿色：关节2，红色：关节3，藏青色：关节4，品红色：关节5\n..."
        self.textBrowser.append(msg_pos)

    def show_sending(self, i):
        msg_pos = f"动作组{i}写入"
        self.textBrowser.append(msg_pos)

    def show_finish_send(self):
        msg_pos = "指令写入完成，开始运动..."
        self.textBrowser.append(msg_pos)

    # 更新graph显示内容
    def update_data(self):
        k = int(self.ptr / 0.2 + 2)
        self.data_x = np.squeeze(np.array(self.t_plt[:k]))
        self.data0 = np.squeeze(np.array(self.qq[0][:k]))
        self.data1 = np.squeeze(np.array(self.qq[1][:k]))
        self.data2 = np.squeeze(np.array(self.qq[2][:k]))
        self.data3 = np.squeeze(np.array(self.qq[3][:k]))
        self.data4 = np.squeeze(np.array(self.qq[4][:k]))
        self.data0_v = np.squeeze(np.array(self.qv[0][:k]))
        self.data1_v = np.squeeze(np.array(self.qv[1][:k]))
        self.data2_v = np.squeeze(np.array(self.qv[2][:k]))
        self.data3_v = np.squeeze(np.array(self.qv[3][:k]))
        self.data4_v = np.squeeze(np.array(self.qv[4][:k]))
        self.p1.addLegend(loc='best')  # 可选择是否添加legend
        # 数据填充到绘制曲线中
        # 颜色：b，g，r，c，m，y，k，w
        self.p1.plot().setData(self.data_x, self.data0, pen='b', name='qq1')
        self.p1.plot().setData(self.data_x, self.data1, pen='g', name='qq2')
        self.p1.plot().setData(self.data_x, self.data2, pen='r', name='qq3')
        self.p1.plot().setData(self.data_x, self.data3, pen='c', name='qq4')
        self.p1.plot().setData(self.data_x, self.data4, pen='m', name='qq5')
        self.p2.plot().setData(self.data_x, self.data0_v, pen='b', name='qv1')
        self.p2.plot().setData(self.data_x, self.data1_v, pen='g', name='qv2')
        self.p2.plot().setData(self.data_x, self.data2_v, pen='r', name='qv3')
        self.p2.plot().setData(self.data_x, self.data3_v, pen='c', name='qv4')
        self.p2.plot().setData(self.data_x, self.data4_v, pen='m', name='qv5')
        # x 轴记录点
        self.ptr += 0.2
        # 重新设定 x 相关的坐标原点
        self.p1.plot().setPos(self.ptr, 0)
        self.p2.plot().setPos(self.ptr, 0)
        if k == len(self.qq[0]):  # 显示完毕
            self.timer.stop()  # 杀死定时器
            self.timer.deleteLater()
            self.show_finish_plan()
            self.message_send()  # 控制机器人运动

    # 轨迹规划与动态显示
    def tra_plan(self):
        try:
            # 读取一次当前的规划模式，避免初始时没选择导致问题
            if self.is_cart == 1:
                self.plan_mode = self.planmode_cart.currentText()
            else:
                self.plan_mode = self.planmode_joint.currentText()
            if self.plan_mode == '步进':
                self.plan_mode = 0
            else:
                self.plan_mode = 1
            # 清空上一幅图
            self.verticalLayout_3.removeWidget(self.win1)  # F1为定义的图
            self.win1.deleteLater()  # 此处为加入的代码
            self.verticalLayout_5.removeWidget(self.win2)  # F1为定义的图
            self.win2.deleteLater()  # 此处为加入的代码
            # 新建一幅图
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

            if self.plan_mode == 0:   # 步进模式：中间点速度均为0
                if self.is_cart == 1:  # 笛卡尔空间
                    if self.modify_interval:
                        if self.mid == 0:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = cartesian_plan(5, self.interval_cart, [self.tt_d], [0], self.d0, self.dt)
                        elif self.mid == 1:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = cartesian_plan(5, self.interval_cart, [self.t1_d, self.tt_d], [0], self.d0, self.d1, self.dt)
                        elif self.mid == 2:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = cartesian_plan(5, self.interval_cart, [self.t1_d, self.t2_d, self.tt_d], [0, 0], self.d0, self.d1, self.d2, self.dt)
                        else:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = cartesian_plan(5, self.interval_cart, [self.t1_d, self.t2_d, self.t3_d, self.tt_d], [0, 0, 0], self.d0, self.d1, self.d2, self.d3, self.dt)
                    else:
                        if self.mid == 0:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = cartesian_plan(5, 0.2, [self.tt_d], [0], self.d0, self.dt)
                        elif self.mid == 1:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = cartesian_plan(5, 0.2, [self.t1_d, self.tt_d], [0], self.d0, self.d1, self.dt)
                        elif self.mid == 2:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = cartesian_plan(5, 0.2, [self.t1_d, self.t2_d, self.tt_d], [0, 0], self.d0, self.d1, self.d2, self.dt)
                        else:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = cartesian_plan(5, 0.2, [self.t1_d, self.t2_d, self.t3_d, self.tt_d], [0, 0, 0], self.d0, self.d1, self.d2, self.d3, self.dt)
                else:  # 关节空间
                    if self.modify_interval:
                        if self.mid == 0:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = joint_plan(5, self.interval_joint, [self.tt], [0], self.j0, self.jt)
                        elif self.mid == 1:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = joint_plan(5, self.interval_joint, [self.t1, self.tt], [0], self.j0, self.j1, self.jt)
                        elif self.mid == 2:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = joint_plan(5, self.interval_joint, [self.t1, self.t2, self.tt], [0, 0], self.j0, self.j1, self.j2, self.jt)
                        else:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = joint_plan(5, self.interval_joint, [self.t1, self.t2, self.t3, self.tt], [0, 0, 0], self.j0, self.j1, self.j2, self.j3, self.jt)
                    else:
                        if self.mid == 0:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = joint_plan(5, 0.2, [self.tt], [0], self.j0, self.jt)
                        elif self.mid == 1:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = joint_plan(5, 0.2, [self.t1, self.tt], [0], self.j0, self.j1, self.jt)
                        elif self.mid == 2:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = joint_plan(5, 0.2, [self.t1, self.t2, self.tt], [0, 0], self.j0, self.j1, self.j2, self.jt)
                        else:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = joint_plan(5, 0.2, [self.t1, self.t2, self.t3, self.tt], [0, 0, 0], self.j0, self.j1, self.j2, self.j3, self.jt)

            if self.plan_mode == 1:   # 连续模式：中间点速度用户给定
                if self.is_cart == 1:  # 笛卡尔空间
                    if self.modify_interval:    # 修改了差值间隔
                        if self.mid == 0:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = cartesian_plan(5, self.interval_cart, [self.tt_d], [0], self.d0, self.dt)
                        elif self.mid == 1:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = cartesian_plan(5, self.interval_cart, [self.t1_d, self.tt_d], [self.vel1], self.d0, self.d1, self.dt)
                        elif self.mid == 2:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = cartesian_plan(5, self.interval_cart, [self.t1_d, self.t2_d, self.tt_d], [self.vel1,self.vel2], self.d0, self.d1, self.d2, self.dt)
                        else:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = cartesian_plan(5, self.interval_cart, [self.t1_d, self.t2_d, self.t3_d, self.tt_d], [self.vel1, self.vel2, self.vel3], self.d0, self.d1, self.d2, self.d3, self.dt)
                    else:
                        if self.mid == 0:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = cartesian_plan(5, 0.2, [self.tt_d], self.d0, self.dt)
                        elif self.mid == 1:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = cartesian_plan(5, 0.2, [self.t1_d, self.tt_d], [self.vel1], self.d0, self.d1, self.dt)
                        elif self.mid == 2:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = cartesian_plan(5, 0.2, [self.t1_d, self.t2_d, self.tt_d], [self.vel1, self.vel2], self.d0, self.d1, self.d2, self.dt)
                        else:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = cartesian_plan(5, 0.2, [self.t1_d, self.t2_d, self.t3_d, self.tt_d], [self.vel1, self.vel2, self.vel3], self.d0, self.d1, self.d2, self.d3, self.dt)
                else:  # 关节空间
                    if self.modify_interval:
                        if self.mid == 0:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = joint_plan(5, self.interval_joint, [self.tt], [0], self.j0, self.jt)
                        elif self.mid == 1:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = joint_plan(5, self.interval_joint, [self.t1, self.tt], [self.vel1], self.j0, self.j1, self.jt)
                        elif self.mid == 2:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = joint_plan(5, self.interval_joint, [self.t1, self.t2, self.tt], [self.vel1, self.vel2], self.j0, self.j1, self.j2, self.jt)
                        else:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = joint_plan(5, self.interval_joint, [self.t1, self.t2, self.t3, self.tt], [self.vel1, self.vel2, self.vel3], self.j0, self.j1, self.j2, self.j3, self.jt)
                    else:
                        if self.mid == 0:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = joint_plan(5, 0.2, [self.tt], [0], self.j0, self.jt)
                        elif self.mid == 1:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = joint_plan(5, 0.2, [self.t1, self.tt], [self.vel1], self.j0, self.j1, self.jt)
                        elif self.mid == 2:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = joint_plan(5, 0.2, [self.t1, self.t2, self.tt], [self.vel1, self.vel2], self.j0, self.j1, self.j2, self.jt)
                        else:
                            trajectory_jnt, self.qq, self.qv, self.t_plt = joint_plan(5, 0.2, [self.t1, self.t2, self.t3, self.tt], [self.vel1, self.vel2, self.vel3], self.j0, self.j1, self.j2, self.j3, self.jt)

            self.show_start_plan()  # 开始路径规划
            self.show_legend()  # 提示图例
            # 实时更新pyqtpragh
            self.ptr = 0
            # 设定定时器
            self.timer = pg.QtCore.QTimer()
            # 定时器信号绑定 update_data 函数
            self.timer.timeout.connect(self.update_data)
            # 定时器间隔50ms，可以理解为 50ms 刷新一次数据
            self.timer.start(50)
        except:
            messagebox3()

    # 开始运动
    def message_send_multi(self):
        num_total = 0   # 记录动作组总数
        for k in range(len(self.qq)):
            for i in range(len(self.qq[k][0])):  # 26个插值点
                pwm = []
                for idx, data in enumerate(self.qq[k]):  # 5个关节角
                    if idx == 0:
                        pwm.append(angle2pwm(data[i] * 180 / pi))
                        if pwm[0] > 1500:
                            pwm[0] += 50
                    elif idx == 1:
                        pwm.append(angle2pwm(data[i] * 180 / pi - 90))
                    else:
                        pwm.append(angle2pwm((-1) * data[i] * 180 / pi))

                # 保存动作组
                if max(pwm) < 2500 and min(pwm) > 500:
                    if i + num_total + 1 < 10:
                        str1 = '<G000' + str(int(i)+num_total) + '#000P' + str(int(pwm[0])) + 'T200!#001P' + str(int(pwm[1])) + \
                               'T200!#002P' + str(int(pwm[2])) + 'T200!#003P' + str(int(pwm[3])) + \
                               'T200!#004P' + str(int(pwm[4])) + 'T200!>'
                    elif i + num_total + 1 < 100:
                        str1 = '<G00' + str(int(i)+num_total) + '#000P' + str(int(pwm[0])) + 'T200!#001P' + str(int(pwm[1])) + \
                               'T200!#002P' + str(int(pwm[2])) + 'T200!#003P' + str(int(pwm[3])) + \
                               'T200!#004P' + str(int(pwm[4])) + 'T200!>'
                    else:
                        str1 = '<G0' + str(int(i) + num_total) + '#000P' + str(int(pwm[0])) + 'T200!#001P' + str(int(pwm[1])) + \
                               'T200!#002P' + str(int(pwm[2])) + 'T200!#003P' + str(int(pwm[3])) + \
                               'T200!#004P' + str(int(pwm[4])) + 'T200!>'
                    self.ser.write(str1.encode())
                    time.sleep(0.2)
                    msg_pos = f"动作组{i}写入"
                    self.textBrowser.append(msg_pos)
            num_move = len(self.qq[k][0])
            num_total += (num_move + 3)
            str2 = '<G00' + str(int(num_total-3)) + '#005P2100T1000!>'
            self.ser.write(str2.encode())
            time.sleep(1)
            str3 = '<G00' + str(
                int(num_total-2)) + '#000P1500T2000!#001P1500T2000!#002P1500T2000!#003P1500T2000!#004P1500T2000!>'
            self.ser.write(str3.encode())
            time.sleep(1)
            str4 = '<G00' + str(int(num_total-1)) + '#005P1300T2000!>'
            self.ser.write(str4.encode())
            time.sleep(1)

        self.show_finish_send()
        str5 = "$DGT:0-" + str(int(num_total)) + ',1!'
        self.ser.write(str5.encode())
        time.sleep(4)

    # 开始运动
    def message_send(self):
        for i in range(len(self.qq[0])):  # 26个插值点
            pwm = []
            for idx, data in enumerate(self.qq):  # 5个关节角
                if idx == 0:
                    pwm.append(angle2pwm(data[i] * 180 / pi))
                elif idx == 1:
                    pwm.append(angle2pwm(data[i] * 180 / pi - 90))
                else:
                    pwm.append(angle2pwm((-1) * data[i] * 180 / pi))

            # 保存动作组
            if max(pwm) < 2500 and min(pwm) > 500:
                if i < 10:      # 动作组数量小于10
                    str1 = '<G000' + str(int(i)) + '#000P' + str(int(pwm[0])) + 'T80!#001P' + str(int(pwm[1])) + \
                           'T80!#002P' + str(int(pwm[2])) + 'T80!#003P' + str(int(pwm[3])) + \
                           'T80!#004P' + str(int(pwm[4])) + 'T80!>'
                elif i < 100:   # 动作组数量小于100
                    str1 = '<G00' + str(int(i)) + '#000P' + str(int(pwm[0])) + 'T80!#001P' + str(int(pwm[1])) + \
                           'T80!#002P' + str(int(pwm[2])) + 'T80!#003P' + str(int(pwm[3])) + \
                           'T80!#004P' + str(int(pwm[4])) + 'T80!>'
                else:
                    str1 = '<G0' + str(int(i)) + '#000P' + str(int(pwm[0])) + 'T80!#001P' + str(int(pwm[1])) + \
                           'T80!#002P' + str(int(pwm[2])) + 'T80!#003P' + str(int(pwm[3])) + \
                           'T80!#004P' + str(int(pwm[4])) + 'T80!>'
                self.ser.write(str1.encode())   # 保存动作组
                time.sleep(0.1)
                msg_pos = f"动作组{i + 1}写入"
                self.textBrowser.append(msg_pos)
        if len(self.qq[0]) < 100:
            num_move = len(self.qq[0])
            str2 = '<G00' + str(int(num_move)) + '#005P2100T1000!>'
            self.ser.write(str2.encode())
            time.sleep(0.5)
            str3 = '<G00' + str(
                int(num_move + 1)) + '#000P1500T2000!#001P1500T2000!#002P1500T2000!#003P1500T2000!#004P1500T2000!>'
            self.ser.write(str3.encode())
            time.sleep(0.5)
            str4 = '<G00' + str(int(num_move + 2)) + '#005P1500T1000!>'
            self.ser.write(str4.encode())
            time.sleep(0.5)
            self.show_finish_send()
            str5 = "$DGT:0-" + str(int(num_move + 2)) + ',1!'
            self.ser.write(str5.encode())
            time.sleep(2)
        else:
            num_move = len(self.qq[0])
            str2 = '<G0' + str(int(num_move)) + '#005P2100T1000!>'
            self.ser.write(str2.encode())
            time.sleep(0.5)
            str3 = '<G0' + str(
                int(num_move + 1)) + '#000P1500T2000!#001P1500T2000!#002P1500T2000!#003P1500T2000!#004P1500T2000!>'
            self.ser.write(str3.encode())
            time.sleep(0.5)
            str4 = '<G0' + str(int(num_move + 2)) + '#005P1500T1000!>'
            self.ser.write(str4.encode())
            time.sleep(0.5)
            self.show_finish_send()
            str5 = "$DGT:0-" + str(int(num_move + 2)) + ',1!'
            self.ser.write(str5.encode())
            time.sleep(2)

    # 复位按钮
    def RST(self):
        try:
            self.theta1slider.setValue(0)
            self.theta2slider.setValue(0)
            self.theta3slider.setValue(0)
            self.theta4slider.setValue(0)
            self.theta5slider.setValue(0)
            self.ser.write(
                '{#000P1500T1000!#001P1500T1000!#002P1500T1000!#003P1500T1000!#004P1500T1000!#005P1500T1000!}'.encode())
            time.sleep(2)
        except:
            messagebox3()

    def grip_close(self):
        try:
            self.ser.write('#005P1800T1000!'.encode())
            time.sleep(2)
        except:
            messagebox3()

    def grip_open(self):
        try:
            self.ser.write('#005P1200T1000!'.encode())
            time.sleep(2)
        except:
            messagebox3()

    # 手势交互    
    def gesture_interact(self):
        try:
            if not self.ser:
                raise Exception("未连接串口")
            # 初始化
            mpHands = mp.solutions.hands
            hands = mpHands.Hands(False, 2, 1, 0.8, 0.8)  # 用于检测手
            mpDraw = mp.solutions.drawing_utils  # 绘制关键点
            results = 0

            pTime = 0
            count_list = [0, 0]  # 记录结果的列表

            cap = cv2.VideoCapture(0)
            cap.set(3, 700)  # 设置窗口的宽高
            cap.set(4, 600)
            # 检查是否正确打开视频
            if cap.isOpened():
                open, frame = cap.read()
            else:
                open = False

            while open:
                success, img = cap.read()  # 读取数据帧
                img, result_f = self.findHands(img, mpHands, hands, mpDraw)  # 检测手
                lmList = self.findPosition(img, result_f, draw=False)  # 获取手部20个关键点坐标

                if len(lmList) != 0:
                    max_list = [lmList[4][2], lmList[8][2], lmList[12][2], lmList[16][2], lmList[20][2]]  # 每个手指的尖端部位
                    count = 0  # 手势数字结果
                    # 手势为4
                    if max_list[1] < lmList[9][2] and max_list[2] < lmList[9][2] and max_list[3] < lmList[9][2] and \
                            max_list[4] < lmList[9][2] and max_list[0] > lmList[9][2] and max_list[0] > lmList[17][2]:
                        count = 4
                    # 手势为3
                    elif max_list[1] < lmList[9][2] and max_list[2] < lmList[9][2] and max_list[3] < lmList[9][2] and \
                            lmList[20][2] > lmList[9][2]:
                        count = 3
                    # 手势为2
                    elif max_list[1] < lmList[9][2] < lmList[16][2] and max_list[2] < lmList[9][2] < lmList[20][2]:
                        count = 2
                    # 手势为1
                    elif max_list[1] < lmList[9][2] < lmList[16][2] and lmList[20][2] > lmList[9][2] and lmList[12][2] > \
                            lmList[9][2]:
                        count = 1
                    # 手势为5
                    elif max_list[1] < lmList[9][2] and max_list[2] < lmList[9][2] and max_list[3] < lmList[9][2] and \
                            max_list[4] < lmList[9][2] and max_list[0] < lmList[17][2]:
                        count = 5
                    # 手势为6
                    elif max_list[0] < lmList[17][2] and max_list[4] < lmList[1][2] and max_list[1] > lmList[9][2] and \
                            max_list[2] > lmList[9][2] and max_list[3] > lmList[9][2]:
                        count = 6

                    cv2.putText(img, f'{int(count)}', (100, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)  # 显示手势图片
                    count_list.append(count)

                    # 根据手势发送指令
                    self.sendmessage(count, count_list)

                cTime = time.time()
                fps = 1 / (cTime - pTime)  # 每秒传输帧数
                pTime = cTime
                cv2.imshow("Image", cv2.resize(img, (700, 600)))
                cv2.waitKey(1)
                if cv2.getWindowProperty('Image', cv2.WND_PROP_VISIBLE) < 1:
                    break
        except:
            messagebox3()

    def findHands(self, img, mpHands, hands, mpDraw, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                if draw:
                    mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
        return img, results

    def findPosition(self, img, results, draw=True):
        lmLists = []

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmLists.append([id, cx, cy])
                    if draw:
                        cv2.circle(img, (cx, cy), 12, (255, 0, 255), cv2.FILLED)
        return lmLists

    def sendmessage(self, count, count_ls):
        if count == 1:
            if count_ls[-2] != 1:
                self.ser.write('#000P1800T1000!'.encode())
                time.sleep(1)
                self.ser.write('#000P1500T1000!'.encode())
                time.sleep(1)
        if count == 2:
            if count_ls[-2] != 2:
                self.ser.write('#001P1300T1000!'.encode())
                time.sleep(1)
                self.ser.write('#001P1500T1500!'.encode())
                time.sleep(1)
        if count == 3:
            if count_ls[-2] != 3:
                self.ser.write('#002P1800T1000!'.encode())
                time.sleep(1)
                self.ser.write('#002P1500T1000!'.encode())
                time.sleep(1)
        if count == 4:
            if count_ls[-2] != 4:
                self.ser.write('#003P1800T1000!'.encode())
                time.sleep(1)
                self.ser.write('#003P1500T1000!'.encode())
                time.sleep(1)
        if count == 5:
            if count_ls[-2] != 5:
                self.ser.write('#004P1800T1000!'.encode())
                time.sleep(1)
                self.ser.write('#004P1500T1000!'.encode())
                time.sleep(1)
        if count == 6:
            if count_ls[-2] != 6:
                self.ser.write('#005P1800T1000!'.encode())
                time.sleep(1)
                self.ser.write('#005P1500T1000!'.encode())
                time.sleep(1)


    def vision_eye_to_hand(self):
        try:
            if not self.ser:
                raise Exception("未连接串口")
            cbraw = 6  # chessboard raw 行
            cbcol = 4  # chessboard column 列
            if self.calibrate_flag == True:
                self.calibrate_flag = False
                self.mtx, self.dist = self.calibrate_zzy(cbraw, cbcol)
                self.centre, self.ratio_trans, image = self.calibrate()
                cor_pixel = self.edge_detect(image)
                for k in range(len(cor_pixel[0])):
                    msg_pos = f"目标点的像素坐标：{cor_pixel[0][k]}, {cor_pixel[1][k]}"
                    self.textBrowser.append(msg_pos)
                X_world, Y_world = self.CoordinateSystemTransformation(self.centre, self.ratio_trans, cor_pixel)
                start_point = [0, 0, 40.3, pi / 2, 0]
                self.qq = []
                for k in range(len(X_world)):
                    msg_pos = f"目标点的世界坐标：({X_world[k]},{Y_world[k]})"
                    self.textBrowser.append(msg_pos)
                    target_point = [X_world[k] / 10, Y_world[k] / 10, -10, -pi / 6, 0]
                    trajectory_jnt, qq_tmp, self.qv, self.t_plt = cartesian_plan(5, 0.2, [5], [0], start_point, target_point)
                    self.qq.append(qq_tmp)
                self.message_send_multi()
                time.sleep(3)
            else:
                image = self.img_cap()
                cor_pixel = self.edge_detect(image)
                for k in range(len(cor_pixel[0])):
                    msg_pos = f"目标点的像素坐标：{cor_pixel[0][k]}, {cor_pixel[1][k]}"
                    self.textBrowser.append(msg_pos)
                X_world, Y_world = self.CoordinateSystemTransformation(self.centre, self.ratio_trans, cor_pixel)
                start_point = [0, 0, 40.3, pi / 2, 0]
                self.qq, self.qv, self.t_plt = [], [], []
                for k in range(len(X_world)):
                    msg_pos = f"目标点的世界坐标：({X_world[k]},{Y_world[k]})"
                    self.textBrowser.append(msg_pos)
                    target_point = [X_world[k] / 10, Y_world[k] / 10, -10, -pi / 6, 0]
                    trajectory_jnt, qq_tmp, qv_tmp, plt_tmp = cartesian_plan(5, 0.2, [5], [0], start_point, target_point)
                    self.qq.append(qq_tmp)
                    self.qv.append(qv_tmp)
                    self.t_plt.append(plt_tmp)
                self.message_send_multi()
                time.sleep(5)
        except:
            messagebox3()


    def calibrate_zzy(self, cbraw, cbcol):

        # 目标点object points 初始化
        objp = np.zeros((cbraw * cbcol, 3), np.float32)  # 棋盘上每个点对应三个坐标值(x,y,z)
        '''
        暂时假设棋盘在x-y平面，即z=0
        所以只改objp中所有坐标点的前两个坐标值x和y，z不改仍然为0
        mgrid把列向量[0:cbraw]复制了cbcol列，把行向量[0:cbcol]复制了cbraw行
        转置并reshape之后，objp的每行都是cbcol*cbraw网格中的某个点的世界坐标
        '''
        objp[:, :2] = np.mgrid[0:cbraw, 0:cbcol].T.reshape(-1, 2)

        objpoints = []  # 世界坐标系中的三维点
        imgpoints = []  # 图像坐标系中的二维点

        images = glob.glob(r'chessboard/{}_{}/*.jpg'.format(cbraw, cbcol))  # 所有棋盘图片

        # 对每张棋盘图片识别出角点，并记录物体的世界坐标和图像坐标
        for fname in images:
            img = cv2.imread(fname)  # 每次读取一张棋盘图
            # img = cv2.resize(img,None,fx=0.8,fy=0.8,interpolation=cv2.INTER_CUBIC)  # 如果图片大小不合适考虑放缩
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转为灰度图像
            # 寻找角点，角点存入corners, ret为找到角点的flag
            ret, corners = cv2.findChessboardCorners(gray, (cbraw, cbcol), None)
            # 设置寻找角点迭代优化过程（亚像素级角点检测）的终止条件
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
            # 亚像素级角点检测 第三个参数为搜索窗口的一班 比如说(5,5)name搜索窗口就是(2*5+1)*(2*5+1)=11*11
            corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)

            objpoints.append(objp)  # 方格点放在objpoints中
            imgpoints.append(corners2)  # 角点放在imgpoints中

            # 在棋盘上绘制角点，使用drawChessboardCorners函数
            img = cv2.drawChessboardCorners(img, (cbraw, cbcol), corners2, ret)
            cv2.imshow('chessboard', img)
            cv2.waitKey(1000)

        '''
        每张棋盘图都分别对应一个旋转和平移矩阵（外参数），但相机内参和畸变系数是唯一的
        mtx：相机内参；dist：畸变系数；revcs：旋转矩阵；tvecs：平移矩阵
        传入所有图片各个角点的三维、二维坐标进行相机标定，使用calibrateCamera函数
        '''
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
        '''
           使用getOptimalNewCameraMatrix优化相机内参，此步可选
           第四个参数值为0-1，0表示尽可能裁剪不想要的像素，1表示保留所有像素点
           '''
        return mtx, dist

    def undistortion(self, mtx, dist, img):
        h, w = img.shape[:2]
        newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

        # 纠正畸变
        dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

        # 输出纠正畸变以后的图片并保存
        x, y, w, h = roi
        dst = dst[y:y + h, x:x + w]
        msg_pos = '畸变修正成功'
        self.textBrowser.append(msg_pos)
        return dst

    def img_cap(self):
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            ret, frame = cap.read()
            cv2.imshow('Preview', frame)
            if cv2.waitKey(1) == 27:
                cv2.destroyAllWindows()
                break
        return frame

    def calibrate(self):
        msg_pos = '请开始标定...'
        self.textBrowser.append(msg_pos)
        dis_real = 60
        point = []  # 存储标定点,只需要三个

        def Mouse(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDBLCLK:
                cv2.circle(final, (x, y), 5, (0, 0, 255), -1)
                point.append([x, y])
                msg_pos = f'标定点：{x},{y}'
                self.textBrowser.append(msg_pos)

        # 通过预览画面调整位置
        msg_pos = '进入预览界面，请按esc进入标定'
        self.textBrowser.append(msg_pos)
        cap = cv2.VideoCapture(0)

        while cap.isOpened():
            ret, frame = cap.read()
            cv2.imshow('Preview', frame)
            if cv2.waitKey(1) == 27:
                cv2.destroyAllWindows()
                break

        # 在标定图中标出世界坐标系原点(必须第一个)和参数l对应的两个点
        final = self.undistortion(self.mtx, self.dist, frame.copy())
        final_copy = final.copy()
        msg_pos = '请在图上选取三个点：分别是世界坐标系原点和两个标定点，选取完后按esc继续'
        self.textBrowser.append(msg_pos)
        cv2.namedWindow('Calibration')
        cv2.setMouseCallback('Calibration', Mouse)
        while True:
            cv2.imshow('Calibration', final)
            if cv2.waitKey(1) == 27:
                cv2.destroyAllWindows()
                break
        cap.release()

        if len(point) >= 3:
            distance = ((point[1][0] - point[2][0]) ** 2 + (point[1][1] - point[2][1]) ** 2) ** 0.5  # 两个标定点的像素距离
            p = distance / dis_real  # 实际距离 / 像素距离 = 转换比
            msg_pos = f'世界坐标系原点在图像坐标系中的位置为({point[0][0]},{point[0][1]})'
            self.textBrowser.append(msg_pos)
            msg_pos = f'世界坐标系1mm对应图像坐标系{p}个像素'
            self.textBrowser.append(msg_pos)
            return point[0], p, final_copy
        else:
            msg_pos = '未完成标定！'
            self.textBrowser.append(msg_pos)
            return [0, 0], 0, [0, 0]


    def edge_detect(self, image):
        msg_pos = '\nRoI选取：请在图中选取两个点作为RoI的左上和右下点，选取完后按esc继续'
        self.textBrowser.append(msg_pos)
        image_copy = image.copy()
        roi_2points = []  # roi是一个正放的矩形，包含矩形的左上和右下点坐标

        def Mouse2(event, x, y, flags, param, ):
            if event == cv2.EVENT_LBUTTONDBLCLK:
                msg_pos = 'RoI选取点'
                self.textBrowser.append(msg_pos)
                cv2.circle(image_copy, (x, y), 5, (0, 0, 255), -1)
                roi_2points.append([y, x])  # 大坑！ 反过来
                msg_pos = f'[{x},{y}]'
                self.textBrowser.append(msg_pos)

        break_flag = False
        while True:
            # 在图上标两个点
            cv2.namedWindow('choose_roi')
            cv2.setMouseCallback('choose_roi', Mouse2)
            while True:
                cv2.imshow('choose_roi', image_copy)
                if cv2.waitKey(1) == 27:
                    break_flag = True
                    cv2.destroyAllWindows()
                    break
            if break_flag == True:
                break

        thresh = cv2.Canny(image, 110, 256)  # 两个阈值越小检测的边缘信息越多
        edge_x, edge_y = np.nonzero(thresh)
        img_test = np.zeros_like(thresh)  # 全黑图
        img_test2 = np.zeros_like(thresh)
        img_test2[roi_2points[0][0], roi_2points[0][1]] = img_test2[roi_2points[1][0], roi_2points[1][1]] = 255
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        edge_xy = list(zip(edge_x, edge_y))  # x，y合在一起

        roi_thresh_point_x_multi = []   # 每个元素存储了一个物体的edge信息
        roi_thresh_point_y_multi = []
        roi_thresh_points_multi = []
        for k in range(0, len(roi_2points), 2):
            # 获取thresh图的边缘
            roi_thresh_point_x = []
            roi_thresh_point_y = []
            roi_thresh_points = []
            for i in range(len(edge_x)):
                if (roi_2points[k][0] < edge_x[i] < roi_2points[k+1][0]) and (
                        roi_2points[k][1] < edge_y[i] < roi_2points[k+1][1]):
                    roi_thresh_point_x.append(edge_x[i])
                    roi_thresh_point_y.append(edge_y[i])
            roi_thresh_point_x_multi.append(roi_thresh_point_x)
            roi_thresh_point_y_multi.append(roi_thresh_point_y)

            for i in range(len(edge_xy)):
                if (roi_2points[k][0] < edge_xy[i][0] < roi_2points[k+1][0]) and (
                        roi_2points[k][1] < edge_xy[i][1] < roi_2points[k+1][1]):
                    roi_thresh_points.append(edge_xy[i])
            roi_thresh_points_multi.append(roi_thresh_points)

        for k in range(len(roi_thresh_point_x_multi)):
            img_test[roi_thresh_point_x_multi[k], roi_thresh_point_y_multi[k]] = 255
            for i in range(len(roi_thresh_points_multi)):
                img_test2[roi_thresh_points_multi[k][i]] = 255

        edge_x_final_multi = []
        edge_y_final_multi = []
        for k in range(len(roi_thresh_point_x_multi)):
            edge_x_final = []
            edge_y_final = []
            for j in range(len(roi_thresh_point_x_multi[k])):
                edge_x_final.append(roi_thresh_points_multi[k][j][0])
                edge_y_final.append(roi_thresh_points_multi[k][j][1])
            edge_x_final_multi.append(edge_x_final)
            edge_y_final_multi.append(edge_y_final)

        edge_x_ave_multi = []
        edge_y_ave_multi = []
        for k in range(len(edge_x_final_multi)):
            edge_x_ave = (np.max(edge_x_final_multi[k]) + np.min(edge_x_final_multi[k])) / 2
            edge_y_ave = (np.max(edge_y_final_multi[k]) + np.min(edge_y_final_multi[k])) / 2
            edge_x_ave_multi.append(edge_y_ave)
            edge_y_ave_multi.append(edge_x_ave)

        thresh_copy = thresh.copy()
        for k in range(len(edge_x_ave_multi)):
            thresh_copy[int(edge_y_ave_multi[k])][int(edge_x_ave_multi[k])] = 255

        while True:
            cv2.imshow("contours", thresh)
            cv2.imshow("contours with object center", thresh_copy)
            cv2.imshow('contours in RoI', img_test)
            if cv2.waitKey(1) == 27:
                cv2.destroyAllWindows()
                break

        return edge_x_ave_multi, edge_y_ave_multi

    # 目标点像素坐标转世界坐标
    def CoordinateSystemTransformation(self, centre, p, cor_pixel):
        X_world, Y_world = [], []
        for k in range(len(cor_pixel[0])):
            X_world.append((cor_pixel[0][k] - centre[0]) / p)
            Y_world.append((centre[1] - cor_pixel[1][k]) / p)
        return [X_world, Y_world]

    # 机器人仿生
    def arm_pose(self):
        try:
            if not self.ser:
                raise Exception("未连接串口")
            mp_drawing = mp.solutions.drawing_utils
            mp_drawing_styles = mp.solutions.drawing_styles
            mp_pose = mp.solutions.pose
            mp_holistic = mp.solutions.holistic
            cap = cv2.VideoCapture(0)
            with mp_holistic.Holistic(
                    min_detection_confidence=0.5,
                    min_tracking_confidence=0.5) as holistic:
                count = 0
                while cap.isOpened():
                    success, image = cap.read()
                    if not success:
                        # If loading a video, use 'break' instead of 'continue'.
                        continue

                    # To improve performance, optionally mark the image as not writeable to
                    # pass by reference.
                    image.flags.writeable = False
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    results = holistic.process(image)

                    # Draw the pose annotation on the image.
                    image.flags.writeable = True
                    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                    lmList = []
                    if results.pose_landmarks and results.right_hand_landmarks:
                        mp_drawing.draw_landmarks(
                            image,
                            results.pose_landmarks,
                            mp_pose.POSE_CONNECTIONS,
                            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

                        mp_drawing.draw_landmarks(
                            image,
                            results.right_hand_landmarks,
                            mp_holistic.HAND_CONNECTIONS,
                            landmark_drawing_spec=mp_drawing_styles
                                .get_default_hand_landmarks_style())

                        '''
                        手臂部分
                        '''
                        # 计算角度 12、14、16
                        if count % 30 == 0:
                            for id, lm in enumerate(results.pose_landmarks.landmark):
                                h, w, c = image.shape
                                cx, cy = int(lm.x * w), int(lm.y * h)
                                lmList.append([id, cx, cy])
                            x1, y1 = lmList[12][1:]
                            x2, y2 = lmList[14][1:]
                            x3, y3 = lmList[16][1:]
                            # Calculate the Angle
                            angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                                                 math.atan2(y1 - y2, x1 - x2))

                            if angle < 0:
                                angle += 360
                            if angle > 180:
                                angle = 360 - angle
                            msg_pos = f'大小臂夹角：{angle}'
                            self.textBrowser.append(msg_pos)
                            if angle < 110:
                                msg_pos = '抬起'
                                self.textBrowser.append(msg_pos)
                            elif angle >= 110:
                                msg_pos = '放下'
                                self.textBrowser.append(msg_pos)
                            msg_pos = f'theta2:{180 - angle}'
                            self.textBrowser.append(msg_pos)
                            theta2 = 180 - angle

                            angle1 = math.degrees(math.atan2(x2 - x1, y2 - y1))
                            if angle1 < 0:
                                angle1 += 360
                            if angle1 > 180:
                                angle1 = 360 - angle1
                            msg_pos = f'theta1:{180 - angle1}'
                            self.textBrowser.append(msg_pos)
                            theta1 = 180 - angle1

                            # ******************************************************************************************************
                            '''
                            手部部分
                            '''
                            lmList2 = []  # 存放手部关键点
                            for id, lm in enumerate(results.right_hand_landmarks.landmark):
                                h, w, c = image.shape
                                cx, cy = int(lm.x * w), int(lm.y * h)
                                lmList2.append([id, cx, cy])
                            max_list = [lmList2[4][2], lmList2[8][2], lmList2[12][2], lmList2[16][2],
                                        lmList2[20][2]]  # 每个手指的尖端部位（指尖）
                            theta6 = 180
                            pwm6 = 1500
                            if abs(lmList2[12][2] - lmList2[8][2]) < 11 and abs(lmList2[12][2] - lmList2[16][2]) < 11:
                                theta5 = 0

                            elif abs(lmList2[12][2] - lmList2[8][2]) > 15 and abs(lmList2[12][2] - lmList2[16][2]) > 15:
                                theta5 = 90
                            else:
                                theta5 = 45

                            print(lmList2[12][1] - lmList2[9][1])
                            if lmList2[12][1] > lmList2[9][1]:
                                theta6 = 0
                                pwm6 = 1800
                                msg_pos = '末端夹具：闭合'
                                self.textBrowser.append(msg_pos)
                            else:
                                theta6 = 180
                                pwm6 = 1300
                                msg_pos = '末端夹具：释放'
                                self.textBrowser.append(msg_pos)

                            # 发送指令
                            pwm1 = angle2pwm((-1) * theta1)
                            pwm2 = angle2pwm(theta2)
                            pwm5 = angle2pwm(theta5)
                            str1 = "{#002P" + str(int(pwm1)) + 'T100!#003P' + str(int(pwm2)) + 'T100!#004P' + str(
                                int(pwm5)) + 'T100!#005P' + str(int(pwm6)) + 'T100!}'
                            self.ser.write(str1.encode())
                        count += 1

                    # Flip the image horizontally for a selfie-view display.
                    cv2.imshow('MediaPipe Pose', cv2.flip(image, 1))
                    if cv2.waitKey(5) & 0xFF == 27:
                        break
            cap.release()
        except:
            messagebox3()

    # 语音控制
    def speech_control(self):
        try:
            if not self.ser:
                raise Exception("未连接串口")
            APP_ID = '25369511'
            API_KEY = 'wMN5BDn1Gx6TH1Zzu6yznQhV'
            SECRET_KEY = 'ZIIHzhTQ3HTKGK9Oij9IKLZpEgVQV8Py'
            client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

            save_file = 'test.wav'
            record_time = 5

            while True:
                # msg_pos = '\n\n==================================================\n请说出指令：'
                # self.textBrowser.append(msg_pos)
                # time.sleep(2)
                print('\n\n==================================================\n请说出指令：')

                self.audio_record(save_file, record_time)  # 录制语音指令
                # print('111')
                # time.sleep(1)
                # msg_pos = '正在识别...'
                # self.textBrowser.append(msg_pos)
                print('正在识别...')

                # 默认1537（普通话 输入法模型）
                result = client.asr(self.get_file_content('test.wav'), 'wav', 16000, {'dev_pid': 1537, })  # 识别语音指令

                if len(result['result']) != 0:  # 语音识别结果不为空，识别结果为一个list
                    if result['result'][0].find('退出') == -1:
                        speech = result['result'][0]

                        joint_str = speech[2]  # '一'至'六'
                        angle_str = speech[4:6]

                        if joint_str == '一':
                            joint = 0
                        elif joint_str == '二':
                            joint = 1
                        elif joint_str == '三':
                            joint = 2
                        elif joint_str == '四':
                            joint = 3
                        elif joint_str == '五':
                            joint = 4
                        elif joint_str == '六':
                            joint = 5

                        angle = int(angle_str)

                        msg_pos = '关节：' + str(joint + 1) + '\t角度：' + str(angle)
                        self.textBrowser.append(msg_pos)
                        if joint == 1:
                            pwm = angle2pwm(angle * (-1))
                        else:
                            pwm = angle2pwm(angle)
                    if result['result'][0].find("出") != -1:  # 如果是"退出"指令则结束程序
                        msg_pos = '退出语音控制'
                        self.textBrowser.append(msg_pos)
                        break

                    str1 = '#00' + str(joint) + 'P' + str(int(pwm)) + 'T200!'
                    self.ser.write(str1.encode())
                    time.sleep(3)
                    self.ser.write(
                        '{#000P1500T1000!#001P1500T1000!#002P1500T1000!#003P1500T1000!#004P1500T1000!#005P1500T1000!}'.encode())
                    time.sleep(3)
        except:
            messagebox3()
    # def speech_control(self):
    #     try:
    #         if not self.ser:
    #             raise Exception("未连接串口")
    #         APP_ID = '25369511'
    #         API_KEY = 'wMN5BDn1Gx6TH1Zzu6yznQhV'
    #         SECRET_KEY = 'ZIIHzhTQ3HTKGK9Oij9IKLZpEgVQV8Py'
    #         client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
    #
    #         save_file = 'test.wav'
    #         record_time = 5
    #         msg_pos = '\n\n==================================================\n请说出指令：'
    #         self.textBrowser.append(msg_pos)
    #         self.audio_record(save_file, record_time)
    #         result = client.asr(self.get_file_content('test.wav'), 'wav', 16000, {
    #             'dev_pid': 1537,  # 默认1537（普通话 输入法模型），dev_pid参数见本节开头的表格
    #         })
    #
    #         msg_pos = '语音识别：' + result['result'][0]
    #         self.textBrowser.append(msg_pos)
    #         speech = result['result'][0]
    #
    #         # 提取语音中对应位置的元素
    #         joint_str = speech[2]  # '一'至'六'
    #         angle_str = speech[4:6]
    #
    #         # 转换为需要的数据
    #         if joint_str == '一':
    #             joint = 0
    #         elif joint_str == '二':
    #             joint = 1
    #         elif joint_str == '三':
    #             joint = 2
    #         elif joint_str == '四':
    #             joint = 3
    #         elif joint_str == '五':
    #             joint = 4
    #         elif joint_str == '六':
    #             joint = 5
    #         angle = int(angle_str)
    #
    #         # print('关节：', joint)
    #         # print('角度:', angle)
    #         msg_pos = '关节：' + str(joint + 1) + '\t角度：' + str(angle)
    #         self.textBrowser.append(msg_pos)
    #
    #         if joint == 1:
    #             pwm = angle2pwm(angle * (-1))
    #         else:
    #             pwm = angle2pwm(angle)
    #         str1 = '#00' + str(joint) + 'P' + str(int(pwm)) + 'T200!'
    #         self.ser.write(str1.encode())
    #         time.sleep(4)
    #         self.ser.write(
    #             '{#000P1500T1000!#001P1500T1000!#002P1500T1000!#003P1500T1000!#004P1500T1000!#005P1500T1000!}'.encode())
    #         time.sleep(2)
    #
    #     except:
    #         messagebox3()
    # 读取文件
    def get_file_content(self, file_path):
        with open(file_path, 'rb') as fp:
            return fp.read()

    # 用Pyaudio库录制音频
    #   out_file:输出音频文件名
    #   rec_time:音频录制时间(秒)
    def audio_record(self, out_file, rec_time):
        CHUNK = 1024
        FORMAT = pyaudio.paInt16  # 16bit编码格式
        CHANNELS = 1  # 单声道
        RATE = 16000  # 16000采样频率
        p = pyaudio.PyAudio()
        # 创建音频流
        stream = p.open(format=FORMAT,  # 音频流wav格式
                        channels=CHANNELS,  # 单声道
                        rate=RATE,  # 采样率16000
                        input=True,
                        frames_per_buffer=CHUNK)

        msg_pos = 'Start Recording...'
        self.textBrowser.append(msg_pos)
        print('Start Recording...')

        frames = []  # 录制的音频流
        # 录制音频数据
        for i in range(0, int(RATE / CHUNK * rec_time)):
            data = stream.read(CHUNK)
            frames.append(data)
        # 录制完成
        stream.stop_stream()
        stream.close()
        p.terminate()

        msg_pos = 'Recording Done...'
        self.textBrowser.append(msg_pos)
        print('Recording Done...')

        # 保存音频文件
        wf = wave.open(out_file, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

    # 读取离线仿真所需数据
    def read_o_sim(self):
        try:
            self.mid_sim = 0
            self.s0 = [0, 0, 0]
            self.s0[0] = float(self.Xo_2.text())
            self.s0[1] = float(self.Yo_2.text())
            msg_pos = "离线仿真模块：导入起始点成功\t" + "X:" + str(self.s0[0]) + "\tY:" + str(self.s0[1]) + "\tZ:" + str(
                self.s0[2])
            self.textBrowser.append(msg_pos)
        except:
            messagebox6()

    def read_1_sim(self):
        try:
            self.mid_sim = 1
            self.s1 = [0, 0, 0]
            self.s1[0] = float(self.X1_2.text())
            self.s1[1] = float(self.Y1_2.text())
            self.s1[2] = float(self.Z1_2.text())
            msg_pos = "离线仿真模块：导入中间点1成功\t" + "X:" + str(self.s1[0]) + "\tY:" + str(self.s1[1]) + "\tZ:" + str(
                self.s1[2])
            self.textBrowser.append(msg_pos)
        except:
            messagebox6()

    def read_2_sim(self):
        try:
            self.mid_sim = 2
            self.s2 = [0, 0, 0]
            self.s2[0] = float(self.X2_2.text())
            self.s2[1] = float(self.Y2_2.text())
            self.s2[2] = float(self.Z2_2.text())
            msg_pos = "离线仿真模块：导入中间点2成功\t" + "X:" + str(self.s2[0]) + "\tY:" + str(self.s2[1]) + "\tZ:" + str(
                self.s2[2])
            self.textBrowser.append(msg_pos)
        except:
            messagebox6()

    def read_3_sim(self):
        try:
            self.mid_sim = 3
            self.s3 = [0, 0, 0]
            self.s3[0] = float(self.X3_2.text())
            self.s3[1] = float(self.Y3_2.text())
            self.s3[2] = float(self.Z3_2.text())
            msg_pos = "离线仿真模块：导入中间点3成功\t" + "X:" + str(self.s3[0]) + "\tY:" + str(self.s3[1]) + "\tZ:" + str(
                self.s3[2])
            self.textBrowser.append(msg_pos)
        except:
            messagebox6()

    def read_t_sim(self):
        try:

            self.st = [0, 0, 0]
            self.st[0] = float(self.Xt_2.text())
            self.st[1] = float(self.Yt_2.text())
            self.st[2] = float(self.Zt_2.text())
            msg_pos = "离线仿真模块：导入目标点成功\t" + "X:" + str(self.st[0]) + "\tY:" + str(self.st[1]) + "\tZ:" + str(
                self.st[2])
            self.textBrowser.append(msg_pos)
        except:
            messagebox6()

        # 实时控制关节角离线仿真

    def realtime_sim(self):

        # connect to engine servers
        physicsClient = p.connect(p.GUI)
        # add search path for loadURDF
        p.setAdditionalSearchPath(pd.getDataPath())
        # define world
        p.setGravity(0, 0, -9.8)
        p.resetDebugVisualizerCamera(cameraDistance=1.5, cameraYaw=0, cameraPitch=-40,
                                     cameraTargetPosition=[0.2, -0.2, 0.5])

        #######################################
        ###    define and setup robot       ###
        #######################################
        robotUrdfPath = r"F:\Pycharm_Projects\robot_simu\urdf\RobotSimu.urdf"
        # load Object
        tableUid = p.loadURDF("table/table.urdf", basePosition=[0.5, 0, -0.65])
        objectUid = p.loadURDF("cube_small.urdf", basePosition=[0.7, 0, 0])

        robotStartPos = [0, 0, 0]
        robotStartOrn = p.getQuaternionFromEuler([0, 0, 0])
        robotID = p.loadURDF(robotUrdfPath, robotStartPos, robotStartOrn,
                             flags=p.URDF_USE_SELF_COLLISION_EXCLUDE_PARENT)


        # joint position control
        position_control_group = []

        position_control_group.append(p.addUserDebugParameter('joint1', -0.75 * math.pi, 0.75 * math.pi, 0))
        position_control_group.append(p.addUserDebugParameter('joint2', -0.5 * math.pi, 0.5 * math.pi, 0))
        position_control_group.append(p.addUserDebugParameter('joint3', -0.75 * math.pi, 0.75 * math.pi, 0))
        position_control_group.append(p.addUserDebugParameter('joint4', -0.75 * math.pi, 0.75 * math.pi, 0))
        position_control_group.append(p.addUserDebugParameter('joint5', -0.75 * math.pi, 0.75 * math.pi, 0))

        position_control_joint_name = ["joint1",
                                       "joint2",
                                       "joint3",
                                       "joint4",
                                       "joint5", ]

        Exitbtn = p.addUserDebugParameter(
            paramName="Exit Simulation",
            rangeMin=1,
            rangeMax=0,
            startValue=0
        )
        previous_Exitbtn_value = p.readUserDebugParameter(Exitbtn)

        Resetbtn = p.addUserDebugParameter(
            paramName="Reset",
            rangeMin=1,
            rangeMax=0,
            startValue=0
        )
        previous_Resetbtn_value = p.readUserDebugParameter(Resetbtn)

        while True:
            if p.readUserDebugParameter(Exitbtn) != previous_Exitbtn_value:
                p.disconnect()

            time.sleep(0.01)
            p.configureDebugVisualizer(p.COV_ENABLE_SINGLE_STEP_RENDERING)  # 允许机械臂慢慢渲染
            # control
            parameter = []
            for i in range(5):
                parameter.append(p.readUserDebugParameter(position_control_group[i]))
            num = 0
            for num in range(5):
                # joint = joints[jointName]
                p.setJointMotorControl2(robotID, num, p.POSITION_CONTROL,
                                        targetPosition=parameter[num],
                                        # force=0.1,
                                        # maxVelocity=10
                                        )
                # num += 1
            # 添加复位按钮
            if p.readUserDebugParameter(Resetbtn) != previous_Resetbtn_value:

                for num in range(5):
                    # joint = joints[jointName]
                    p.setJointMotorControl2(robotID, num, p.POSITION_CONTROL,
                                            targetPosition=0)

            p.stepSimulation()
        p.disconnect()
    #建立离线仿真模块运行线程，避免与上位机线程产生冲突
    def build_thread1(self):
        thread1 = Thread(target=self.realtime_sim)
        thread1.start()

        # 轨迹规划离线仿真

    def plan_simulation(self):
        physicsClient = p.connect(p.GUI)  # or p.DIRECT for non-graphical version
        p.setAdditionalSearchPath(pd.getDataPath())  # optionally
        p.setGravity(0, 0, -9.81)
        p.resetDebugVisualizerCamera(cameraDistance=0.8, cameraYaw=0, cameraPitch=-40,
                                     cameraTargetPosition=[0.2, -0.2, 0.5])
        planeId = p.loadURDF("plane.urdf")
        robotId = p.loadURDF(r"F:\Pycharm_Projects\robot_simu\urdf\RobotSimu.urdf")
         #根据中间点个数的不同情形，调用pybullet库逆运动学函数获取关节角
        if self.mid_sim == 0:
            self.j0_s = p.calculateInverseKinematics(robotId, 4, self.s0)
            self.jt_s = p.calculateInverseKinematics(robotId, 4, self.st)
            _, self.joint_sim, _, _ = joint_plan_simu(5, 0.2, [6], self.j0_s, self.jt_s)
        elif self.mid_sim == 1:
            self.j0_s = p.calculateInverseKinematics(robotId, 4, self.s0)
            self.j1_s = p.calculateInverseKinematics(robotId, 4, self.s1)
            self.jt_s = p.calculateInverseKinematics(robotId, 4, self.st)

            _, self.joint_sim, _, _ = joint_plan_simu(5, 0.2, [6, 6], self.j0_s, self.j1_s,
                                                 self.jt_s)
        elif self.mid_sim == 2:
            self.j0_s = p.calculateInverseKinematics(robotId, 4, self.s0)
            self.j1_s = p.calculateInverseKinematics(robotId, 4, self.s1)
            self.j2_s = p.calculateInverseKinematics(robotId, 4, self.s2)
            self.jt_s = p.calculateInverseKinematics(robotId, 4, self.st)
            _, self.joint_sim, _, _ = joint_plan_simu(5, 0.2, [6, 6, 6], self.j0_s,
                                                 self.j1_s, self.j2_s, self.jt_s)
        else:
            self.j0_s = p.calculateInverseKinematics(robotId, 4, self.s0)
            self.j1_s = p.calculateInverseKinematics(robotId, 4, self.s1)
            self.j2_s = p.calculateInverseKinematics(robotId, 4, self.s2)
            self.j3_s = p.calculateInverseKinematics(robotId, 4, self.s3)
            self.jt_s = p.calculateInverseKinematics(robotId, 4, self.st)

            _, self.joint_sim, _, _ = joint_plan_simu(5, 0.2, [6, 6, 6, 6], self.j0_s, self.j1_s, self.j2_s, self.j3_s,
                                                 self.jt_s)

        # while 1:
        target = []
        for j in range(len(self.joint_sim[2])):
            targetPositionsJoints = []
            for i in range(5):
                targetPositionsJoints.append(self.joint_sim[i][j])

            # targetPositionsJoints[0] = -1.57+targetPositionsJoints[0]
            #targetPositionsJoints[1] = 1.57 - targetPositionsJoints[1]
            target.append(targetPositionsJoints)

            p.setJointMotorControlArray(robotId, range(5), p.POSITION_CONTROL, targetPositions=target[j])
            p.stepSimulation()
        #loctemp=p.getLinkState(robotId, 4)
        #location=loctemp[4]

            time.sleep(0.1)
        p.disconnect()

    # 建立离线仿真模块运行线程，避免与上位机线程产生冲突
    def build_thread2(self):
        thread2 = Thread(target=self.plan_simulation)
        thread2.start()

    def draw(self):
        # p.disconnect()
        physicsClient = p.connect(p.GUI)  # or p.DIRECT for non-graphical version
        p.setAdditionalSearchPath(pd.getDataPath())  # optionally
        p.setGravity(0, 0, -9.81)
        p.resetDebugVisualizerCamera(cameraDistance=1.5, cameraYaw=0, cameraPitch=-89,
                                     cameraTargetPosition=[0.9, 0, 0.6])
        p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
        planeId = p.loadURDF("plane.urdf")
        path = r"F:\Pycharm_Projects\robot_simu\urdf\RobotSimu.urdf"
        robotId1 = p.loadURDF(path, [-0.4, 0, 0])
        robotId2 = p.loadURDF(path, [0, 0.1, 0])
        robotId3 = p.loadURDF(path, [0.5, 0, 0])
        robotId4 = p.loadURDF(path, [0.9, 0, 0])
        robotId5 = p.loadURDF(path, [1.4, 0, 0])
        robotId6 = p.loadURDF(path, [1.9, 0, 0])

        dd1 = draw_down2(-0.4, [-0.4, 0], 360, 0, table_high=0.3)  # 画I
        dh = draw_heart(0.1, [0, 0], 360, 0, table_high=0.3)  # 画心形
        circle_xyz1 = draw_cirlce(0.1, [0.5, 0.1], 360, 0, table_high=0.3)  # 画S
        circle_xyz2 = draw_cirlce2(0.1, [0.5, -0.1], 360, 0, table_high=0.3)
        circle_xyz3 = draw_cirlce(0.2, [0.9, 0], 360, 0, table_high=0.3)  # 画C
        circle_xyz4 = draw_cirlce(0.15, [1.4, 0], 360, 0, table_high=0.3)  # 画U
        dd2 = draw_down(0.2, [1.25, 0], 360, 0, table_high=0.3)
        du = draw_up(0.2, [1.55, 0], 360, 0, table_high=0.3)
        dd3 = draw_down2(0.2, [1.9, 0], 360, 0, table_high=0.3)  # 画T
        dr = draw_right(0.2, [1.9, 0.2], 360, 0, table_high=0.3)
        #展示焰火函数
        def fire():

            cube_small_Uid = p.loadURDF("cube_small.urdf", [-0.7, 0, 0])
            cube_small_Uid1 = p.loadURDF("cube_small.urdf", [2.2, 0, 0])
            cube_small_Uid2 = p.loadURDF("cube_small.urdf", [-0.7, 0, 0.01])
            cube_small_Uid3 = p.loadURDF("cube_small.urdf", [2.2, 0, 0.01])

            p.changeVisualShape(cube_small_Uid, -1,
                                rgbaColor=[np.random.uniform(0, 1), np.random.uniform(0, 1),
                                           np.random.uniform(0, 1), 1])

            p.changeVisualShape(cube_small_Uid1, -1,
                                rgbaColor=[np.random.uniform(0, 1), np.random.uniform(0, 1),
                                           np.random.uniform(0, 1), 1])

            p.changeVisualShape(cube_small_Uid2, -1,
                                rgbaColor=[np.random.uniform(0, 1), np.random.uniform(0, 1),
                                           np.random.uniform(0, 1), 1])

            p.changeVisualShape(cube_small_Uid3, -1,
                                rgbaColor=[np.random.uniform(0, 1), np.random.uniform(0, 1),
                                           np.random.uniform(0, 1), 1])

        ###
        while 1:

            for i in range(179):
                targetposition = p.calculateInverseKinematics(robotId1, 4, dd1[i, :])
                p.addUserDebugLine(dd1[i, :], dd1[i + 1, :], lineColorRGB=[1, 0, 0], lifeTime=3000, lineWidth=3)
                p.setJointMotorControlArray(robotId1, range(5), p.POSITION_CONTROL, targetPositions=targetposition)

                p.stepSimulation()  # 环境开始

            ###

            for i in range(360):
                targetposition = p.calculateInverseKinematics(robotId2, 4, dh[i, :])
                p.addUserDebugLine(dh[i - 1, :], dh[i, :], lineColorRGB=[1, 0, 0], lifeTime=3000, lineWidth=3)
                p.setJointMotorControlArray(robotId2, range(5), p.POSITION_CONTROL, targetPositions=targetposition)

                p.stepSimulation()  # 环境开始

            ###

            for i in range(0, 270):
                targetposition = p.calculateInverseKinematics(robotId3, 4, circle_xyz1[i, :])
                p.addUserDebugLine(circle_xyz1[i - 1, :], circle_xyz1[i, :], lineColorRGB=[1, 0, 0], lifeTime=3000,
                                   lineWidth=3)
                p.setJointMotorControlArray(robotId3, range(5), p.POSITION_CONTROL, targetPositions=targetposition)

                p.stepSimulation()  # 环境开始

            for i in range(270):
                targetposition = p.calculateInverseKinematics(robotId3, 4, circle_xyz2[i, :])
                p.addUserDebugLine(circle_xyz2[i - 1, :], circle_xyz2[i, :], lineColorRGB=[1, 0, 0], lifeTime=3000,
                                   lineWidth=3)
                p.setJointMotorControlArray(robotId3, range(5), p.POSITION_CONTROL, targetPositions=targetposition)

                p.stepSimulation()  # 环境开始

            # 360*3
            ###

            for i in range(45, 315):
                targetposition = p.calculateInverseKinematics(robotId4, 4, circle_xyz3[i, :])
                p.addUserDebugLine(circle_xyz3[i - 1, :], circle_xyz3[i, :], lineColorRGB=[1, 0, 0], lifeTime=3000,
                                   lineWidth=3)
                p.setJointMotorControlArray(robotId4, range(5), p.POSITION_CONTROL, targetPositions=targetposition)

                p.stepSimulation()  # 环境开始

            for i in range(89):
                targetposition = p.calculateInverseKinematics(robotId5, 4, dd2[i, :])
                p.addUserDebugLine(dd2[i, :], dd2[i + 1, :], lineColorRGB=[1, 0, 0], lifeTime=3000, lineWidth=3)
                p.setJointMotorControlArray(robotId5, range(5), p.POSITION_CONTROL, targetPositions=targetposition)

                p.stepSimulation()  # 环境开始

            for i in range(180, 360):
                targetposition = p.calculateInverseKinematics(robotId5, 4, circle_xyz4[i, :])
                p.addUserDebugLine(circle_xyz4[i - 1, :], circle_xyz4[i, :], lineColorRGB=[1, 0, 0], lifeTime=3000,
                                   lineWidth=3)
                p.setJointMotorControlArray(robotId5, range(5), p.POSITION_CONTROL, targetPositions=targetposition)

                p.stepSimulation()  # 环境开始

            for i in range(89):
                targetposition = p.calculateInverseKinematics(robotId5, 4, du[i, :])
                p.addUserDebugLine(du[i, :], du[i + 1, :], lineColorRGB=[1, 0, 0], lifeTime=3000, lineWidth=3)
                p.setJointMotorControlArray(robotId5, range(5), p.POSITION_CONTROL, targetPositions=targetposition)

                p.stepSimulation()  # 环境开始

            ###

            for i in range(179):
                targetposition = p.calculateInverseKinematics(robotId6, 4, dr[i, :])
                p.addUserDebugLine(dr[i, :], dr[i + 1, :], lineColorRGB=[1, 0, 0], lifeTime=3000, lineWidth=3)
                p.setJointMotorControlArray(robotId6, range(5), p.POSITION_CONTROL, targetPositions=targetposition)

                p.stepSimulation()  # 环境开始

            for i in range(179):
                targetposition = p.calculateInverseKinematics(robotId6, 4, dd3[i, :])
                p.addUserDebugLine(dd3[i, :], dd3[i + 1, :], lineColorRGB=[1, 0, 0], lifeTime=3000, lineWidth=3)
                p.setJointMotorControlArray(robotId6, range(5), p.POSITION_CONTROL, targetPositions=targetposition)

                p.stepSimulation()  # 环境开始

            p.resetDebugVisualizerCamera(cameraDistance=4.98, cameraYaw=0, cameraPitch=-29.8,
                                         cameraTargetPosition=[0.9, 0, 0.6])
             #焰火模拟展示
            for i in range(10000000000000000000):
                fire()
                p.stepSimulation()

    # 建立离线仿真模块运行线程，避免与上位机线程产生冲突
    def build_thread3(self):
        thread3 = Thread(target=self.draw)
        thread3.start()