from PyQt5 import QtCore, QtGui, QtWidgets

from kdl_utils import my_rkdl, angle2pwm, joint_plan, cartesian_plan, trajectory_5poly
from messagebox import *


def joint_plan_simu(num_joints, dt, tf, *points):
    # 角度
    point_joint = [point for point in points]

    # 数据准备：轨迹规划需要的数据格式
    q0 = []  # 一个列表元素就是一个关节
    qf = []
    tf_list = []
    for i in range(num_joints):
        q0_tmp = []
        qf_tmp = []
        tf_tmp = []
        for j in range(len(point_joint) - 1):
            q0_tmp.append(point_joint[j][i])
            qf_tmp.append(point_joint[j + 1][i])
            tf_tmp.append(tf[j])
        q0.append(q0_tmp)
        qf.append(qf_tmp)
        tf_list.append(tf_tmp)
    qv0 = [0] * (len(point_joint) - 1)  # 中间点停止
    qvf = [0] * (len(point_joint) - 1)
    qa0 = [0] * (len(point_joint) - 1)
    qaf = [0] * (len(point_joint) - 1)
    # tf = 6
    # dt = 0.2

    # 5个关节分别轨迹规划：
    trajectory_jnt = []  # 每个元素为一个关节
    for i in range(num_joints):
        trajectory = trajectory_5poly(q0[i], qv0, qa0, qf[i], qvf, qaf, tf_list[i], dt)  # 输出位置、速度、角速度的离散值
        trajectory_jnt.append(trajectory)

    # 准备绘图时间表
    t_plt = []
    t_seq = trajectory_jnt[0][-1]
    t_plt.extend(t_seq[0])
    if len(q0[0]) > 1:
        tmp = t_seq[1] + t_seq[0][-1]
        t_plt.extend(tmp)
    if len(q0[0]) > 2:
        tmp = t_seq[2] + t_seq[0][-1] + t_seq[1][-1]
        t_plt.extend(tmp)
    if len(q0[0]) > 3:
        tmp = t_seq[3] + t_seq[0][-1] + t_seq[1][-1] + t_seq[2][-1]
        t_plt.extend(tmp)

    # 准备绘图数据
    qq_plt, qv_plt, qa_plt = [], [], []
    for i in range(num_joints):
        tmp1, tmp2, tmp3 = [], [], []
        for j in range(len(trajectory_jnt[i][0])):
            tmp1.extend(trajectory_jnt[i][0][j])
            tmp2.extend(trajectory_jnt[i][1][j])
            tmp3.extend(trajectory_jnt[i][2][j])
        qq_plt.append(tmp1)
        qv_plt.append(tmp2)
        qa_plt.append(tmp3)

    # for i in range(num_joints):
    #     plt.plot(t_plt, qq_plt[i], label=f'joint{i + 1}')
    # plt.legend()
    # plt.show()
    return trajectory_jnt, qq_plt, qv_plt, t_plt