# Author: Eric Tan
# Creation Date: 2021/12/12
# ---------------------------
from PyQt5.QtWidgets import *

def messagebox1():
    msgBox = QMessageBox()
    msgBox.setWindowTitle('提示')
    msgBox.setText("不可达！无法组成三角形")
    # 隐藏ok按钮
    msgBox.addButton(QMessageBox.Ok)
    msgBox.button(QMessageBox.Ok).hide()
    # 模态对话框
    msgBox.exec_()

def messagebox2():
    msgBox = QMessageBox()
    msgBox.setWindowTitle('提示')
    msgBox.setText("不可达！请增大z值")
    # 隐藏ok按钮
    msgBox.addButton(QMessageBox.Ok)
    msgBox.button(QMessageBox.Ok).hide()
    # 模态对话框
    msgBox.exec_()

def messagebox3():
    msgBox = QMessageBox()
    msgBox.setWindowTitle('提示')
    msgBox.setText("错误！请先打开串口")
    # 隐藏ok按钮
    msgBox.addButton(QMessageBox.Ok)
    msgBox.button(QMessageBox.Ok).hide()
    # 模态对话框
    msgBox.exec_()

def messagebox4():
    msgBox = QMessageBox()
    msgBox.setWindowTitle('提示')
    msgBox.setText("串口连接成功！")
    # 隐藏ok按钮
    msgBox.addButton(QMessageBox.Ok)
    msgBox.button(QMessageBox.Ok).hide()
    # 模态对话框
    msgBox.exec_()

def messagebox5():
    msgBox = QMessageBox()
    msgBox.setWindowTitle('提示')
    msgBox.setText("连接失败！请选择正确的串口")
    # 隐藏ok按钮
    msgBox.addButton(QMessageBox.Ok)
    msgBox.button(QMessageBox.Ok).hide()
    # 模态对话框
    msgBox.exec_()

def messagebox6():
    msgBox = QMessageBox()
    msgBox.setWindowTitle('提示')
    msgBox.setText("请输入正确的数值！")
    # 隐藏ok按钮
    msgBox.addButton(QMessageBox.Ok)
    msgBox.button(QMessageBox.Ok).hide()
    # 模态对话框
    msgBox.exec_()

def messagebox7():
    msgBox = QMessageBox()
    msgBox.setWindowTitle('提示')
    msgBox.setText("串口已连接！请勿重复连接")
    # 隐藏ok按钮
    msgBox.addButton(QMessageBox.Ok)
    msgBox.button(QMessageBox.Ok).hide()
    # 模态对话框
    msgBox.exec_()