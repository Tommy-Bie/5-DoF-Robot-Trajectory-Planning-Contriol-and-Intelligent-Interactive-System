# Author: Eric Tan
# Creation Date: 2021/12/12
# ---------------------------
import numpy as np
from math import *
from messagebox import *
import matplotlib.pyplot as plt

# 连杆的长度
l_2 = 10.4    # 10.4  # 6.2
l_3 = 9.6     # 10
l_4 = 20.3    # 2.7

# 错误捕捉
class Error1(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

class Error2(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

# 逆运动学
def my_rkdl(point):
    Px, Py, Pz, theta, theta5 = point[0], point[1], point[2], point[3], point[4]
    t1, t2, t3, t4 = [], [], [], []
    t5 = [theta5] * 4
    # 求关节角1;
    # 由于arctan的局限性，需要分类讨论
    if Px == 0:
        t1.append(0)
        t1 = t1 * 4
    elif Px < 0 and Py < 0:
        t1.append(atan(Py / Px) - pi)
        t1 = t1 * 2
        t1.extend([atan(Py / Px)] * 2)
    elif Px < 0:
        t1.append(-pi - atan(Py / Px))
        t1 = t1 * 2
        t1.extend([atan(Py / Px)] * 2)
    else:
        t1.append(atan(Py / Px))  # 弧度
        t1 = t1 * 2
        t1.extend([atan(Py / Px) + pi] * 2)
    # TODO：第一组解
    # 求连杆3末端坐标
    Pxx = abs(Px) - abs(l_4 * cos(theta) * cos(t1[0]))
    Pyy = abs(Py) - abs(l_4 * cos(theta) * sin(t1[0]))
    Pzz = Pz - l_4 * sin(theta)

    # 几何法求关节角2、3、4
    u = sqrt(Pxx ** 2 + Pyy ** 2)
    r = sqrt(u ** 2 + Pzz ** 2)

    is_error = False
    try:
        if (l_2 + l_3) < r or (l_2 - l_3) > r:  # 判断能否构成三角形
            raise Error1("不可达！无法组成三角形")
        tmp = (r ** 2 + l_2 ** 2 - l_3 ** 2) / (2 * r * l_2)
        alpha = acos(tmp)
        beta = atan(Pzz / u)
        # if beta < alpha:
        #     # print("Unreachable! Please increase the z value")
        #     raise Error2("不可达！请增大z值")
        t2.append(beta - alpha)
        tmp2 = (l_2 ** 2 + l_3 ** 2 - r ** 2) / (2 * l_2 * l_3)
        gamma = acos(tmp2)
        t3.append(pi - gamma)
        t4.append(theta - t2[0] - t3[0])

        # TODO：第二组解
        # t1.append(atan(Py / Px))
        t2.append(beta + alpha)
        t3.append(gamma - pi)
        t4.append(theta - t2[1] - t3[1])

        # TODO：第三组解
        # t1.append(atan(Py / Px) + pi)
        t2.append(pi - beta + alpha)
        t3.append(gamma - pi)
        t4.append(pi - theta - t2[2] - t3[2])

        # TODO：第四组解
        # t1.append(atan(Py / Px) + pi)
        t2.append(pi - beta - alpha)
        t3.append(pi - gamma)
        t4.append(pi - theta - t2[3] - t3[3])
    except Error1:
            is_error = True
            messagebox1()
    except Error2:
            is_error = True
            messagebox2()

    t1_agl = [i * 180 / pi for i in t1]
    t2_agl = [i * 180 / pi for i in t2]
    t3_agl = [i * 180 / pi for i in t3]
    t4_agl = [i * 180 / pi for i in t4]
    return [t1, t2, t3, t4, t5], is_error


# 正运动学
def my_kdl(theta1, theta2, theta3, theta4, theta5):
    T1_0 = np.array([[cos(theta1), -sin(theta1), 0, 0],
                     [sin(theta1), cos(theta1), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])
    T2_1 = np.array([[cos(theta2), -sin(theta2), 0, 0],
                     [0, 0, 1, 0],
                     [sin(theta2), cos(theta2), 0, 0],
                     [0, 0, 0, 1]])
    T3_2 = np.array([[cos(theta3), -sin(theta3), 0, 10.4],
                     [sin(theta3), cos(theta3), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])
    T4_3 = np.array([[-sin(theta4), -cos(theta4), 0, 9.6],
                     [cos(theta4), -sin(theta4), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])
    T5_4 = np.array([[cos(theta5), -sin(theta5), 0, 0],
                     [0, 0, -1, -15.3],
                     [sin(theta5), cos(theta5), 0, 0],
                     [0, 0, 0, 1]])

    T5_0 = T1_0.dot(T2_1).dot(T3_2).dot(T4_3).dot(T5_4)
    T3_0 = T1_0.dot(T2_1).dot(T3_2)
    T4_0 = T1_0.dot(T2_1).dot(T3_2).dot(T4_3)
    return T5_0


# 关节角转化为舵机控制信号
def angle2pwm(t):
    return 1500 + t * 2000 / 270

# 5次多项式插值求取求取一段时间的离散数值点,多变量
def trajectory_5poly(q0, qv0, qa0, qf, qvf, qaf, tf, dt):
    '''
        本函数用5项插值将离散数据连续化，多变量
        input:q0,qv0,qa0起点位置速度加速度
              qf,qvf,qaf终点位置速度加速度
              tf终点时间，dt时间间隔
        output:[q,qv,qa] 对应时刻位置速度加速度
    '''
    n = len(q0)     # 起点数目 = 需要规划的段数
    k = []      # 每个元素为该段的时间节点数
    k.append(np.floor(tf[0] / dt).astype(int) + 1)
    if n > 1:
        k.append(np.floor(tf[1] / dt).astype(int) + 1)
    if n > 2:
        k.append(np.floor(tf[2] / dt).astype(int) + 1)
    if n > 3:
        k.append(np.floor(tf[3] / dt).astype(int) + 1)

    # 求取5次多项式插值系数
    a0 = np.zeros(n)
    a1 = np.zeros(n)
    a2 = np.zeros(n)
    a3 = np.zeros(n)
    a4 = np.zeros(n)
    a5 = np.zeros(n)
    for i in range(n):
        a0[i] = q0[i]
        a1[i] = qv0[i]
        a2[i] = qa0[i] / 2.0
        a3[i] = (20 * (qf[i] - q0[i]) - (8 * qvf[i] + 12 * qv0[i]) * tf[i] + (qaf[i] - 3 * qa0[i]) * tf[i] * tf[i]) / (
                2 * pow(tf[i], 3))
        a4[i] = (-30 * (qf[i] - q0[i]) + (14 * qvf[i] + 16 * qv0[i]) * tf[i] - (2 * qaf[i] - 3 * qa0[i]) * tf[i] * tf[i]) / (
                2 * pow(tf[i], 4))
        a5[i] = (12 * (qf[i] - q0[i]) - (6 * qvf[i] + 6 * qv0[i]) * tf[i] + (qaf[i] - qa0[i]) * tf[i] * tf[i]) / (
                2 * pow(tf[i], 5))

    # 数据点求取
    qq, qv, qa = [], [], []
    qq.append(np.zeros(k[0]))
    qv.append(np.zeros(k[0]))
    qa.append(np.zeros(k[0]))
    if n > 1:
        qq.append(np.zeros(k[1]-1))     # TODO：由于第二段开始，均从dt开始规划，故长度-1
        qv.append(np.zeros(k[1]-1))
        qa.append(np.zeros(k[1]-1))
    if n > 2:
        qq.append(np.zeros(k[2]-1))
        qv.append(np.zeros(k[2]-1))
        qa.append(np.zeros(k[2]-1))
    if n > 3:
        qq.append(np.zeros(k[3]-1))
        qv.append(np.zeros(k[3]-1))
        qa.append(np.zeros(k[3]-1))

    t_seq = []
    t_seq0 = np.linspace(0, tf[0], k[0])
    t_seq.append(t_seq0)
    if n > 1:
        t_seq1 = np.linspace(dt, tf[1], k[1]-1)  # TODO:从第二段开始，把第一个值去掉,即直接从dt开始
        t_seq.append(t_seq1)
    if n > 2:
        t_seq2 = np.linspace(dt, tf[2], k[2]-1)
        t_seq.append(t_seq2)
    if n > 3:
        t_seq3 = np.linspace(dt, tf[3], k[3]-1)
        t_seq.append(t_seq3)

    for j in range(n):
        if j == 0:      # 第一列
            for i in range(k[0]):
                t = t_seq0[i]
                qq[j][i] = a0[j] + a1[j] * t + a2[j] * pow(t, 2) + a3[j] * pow(t, 3) + a4[j] * pow(t, 4) + a5[j] * pow(
                    t, 5)
                qv[j][i] = a1[j] + 2 * a2[j] * t + 3 * a3[j] * pow(t, 2) + 4 * a4[j] * pow(t, 3) + 5 * a5[j] * pow(t, 4)
                qa[j][i] = 2 * a2[j] + 6 * a3[j] * t + 12 * a4[j] * pow(t, 2) + 20 * a5[j] * pow(t, 3)
        elif j == 1 and n-j > 0:
            for i in range(k[1]-1):
                t = t_seq1[i]
                qq[j][i] = a0[j] + a1[j] * t + a2[j] * pow(t, 2) + a3[j] * pow(t, 3) + a4[j] * pow(t, 4) + a5[j] * pow(
                    t, 5)
                qv[j][i] = a1[j] + 2 * a2[j] * t + 3 * a3[j] * pow(t, 2) + 4 * a4[j] * pow(t, 3) + 5 * a5[j] * pow(t, 4)
                qa[j][i] = 2 * a2[j] + 6 * a3[j] * t + 12 * a4[j] * pow(t, 2) + 20 * a5[j] * pow(t, 3)
        elif j == 2 and n-j>0:
            for i in range(k[2]-1):
                t = t_seq2[i]
                qq[j][i] = a0[j] + a1[j] * t + a2[j] * pow(t, 2) + a3[j] * pow(t, 3) + a4[j] * pow(t, 4) + a5[j] * pow(
                    t, 5)
                qv[j][i] = a1[j] + 2 * a2[j] * t + 3 * a3[j] * pow(t, 2) + 4 * a4[j] * pow(t, 3) + 5 * a5[j] * pow(t, 4)
                qa[j][i] = 2 * a2[j] + 6 * a3[j] * t + 12 * a4[j] * pow(t, 2) + 20 * a5[j] * pow(t, 3)
        elif j == 3 and n-j>0:
            for i in range(k[3]-1):
                t = t_seq3[i]
                qq[j][i] = a0[j] + a1[j] * t + a2[j] * pow(t, 2) + a3[j] * pow(t, 3) + a4[j] * pow(t, 4) + a5[j] * pow(
                    t, 5)
                qv[j][i] = a1[j] + 2 * a2[j] * t + 3 * a3[j] * pow(t, 2) + 4 * a4[j] * pow(t, 3) + 5 * a5[j] * pow(t, 4)
                qa[j][i] = 2 * a2[j] + 6 * a3[j] * t + 12 * a4[j] * pow(t, 2) + 20 * a5[j] * pow(t, 3)
    return [qq, qv, qa, t_seq]


# 关节空间规划
def joint_plan(num_joints, dt, tf, qv, *points):
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
            q0_tmp.append(point_joint[j][i][1])
            qf_tmp.append(point_joint[j + 1][i][1])
            tf_tmp.append(tf[j])
        q0.append(q0_tmp)
        qf.append(qf_tmp)
        tf_list.append(tf_tmp)
    # qv0 = [0] * (len(point_joint) - 1)  # 中间点停止
    qv0 = [0]
    qv0.extend(qv)  # 中间点有速度
    qvf = qv
    qvf.append(0)
    # qvf = [0] * (len(point_joint) - 1)
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
    t_seq = trajectory_jnt[0][-1]   # 去第一个关节的最后一个返回值：时间t
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

    for i in range(num_joints):
        plt.plot(t_plt, qq_plt[i], label=f'joint{i + 1}')
    plt.legend()
    plt.show()
    return trajectory_jnt, qq_plt, qv_plt, t_plt

# 笛卡尔空间规划
def cartesian_plan(num_joints, dt, tf, qv, *points):
    points_cart = [point for point in points]
    point_joint = []

    # 逆运动学：笛卡尔空间转为关节空间
    for point in points_cart:
        point_joint.append(my_rkdl(point)[0])

    # 数据准备：轨迹规划需要的数据格式
    q0 = []  # 一个列表元素就是一个关节
    qf = []
    tf_list = []
    for i in range(num_joints):
        q0_tmp = []
        qf_tmp = []
        tf_tmp = []
        for j in range(len(point_joint) - 1):
            q0_tmp.append(point_joint[j][i][1])
            qf_tmp.append(point_joint[j + 1][i][1])
            tf_tmp.append(tf[j])
        q0.append(q0_tmp)
        qf.append(qf_tmp)
        tf_list.append(tf_tmp)
    # qv0 = [0] * (len(point_joint) - 1)  # 中间点停止
    # qvf = [0] * (len(point_joint) - 1)
    qv0 = [0]
    qv0.extend(qv)  # 中间点有速度
    qvf = qv
    qvf.append(0)
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
    # plt.grid()
    # plt.xlabel("time(s)")
    # plt.ylabel("pos(rad)")
    # plt.show()
    #
    # for i in range(num_joints):
    #     plt.plot(t_plt, qv_plt[i], label=f'joint{i + 1}')
    # plt.legend()
    # plt.grid()
    # plt.xlabel("time(s)")
    # plt.ylabel("vel(rad/s)")
    # plt.show()
    #
    # for i in range(num_joints):
    #     plt.plot(t_plt, qa_plt[i], label=f'joint{i + 1}')
    # plt.legend()
    # plt.grid()
    # plt.xlabel("time(s)")
    # plt.ylabel("acc(rad/s^2)")
    # plt.show()
    return trajectory_jnt, qq_plt, qv_plt, t_plt