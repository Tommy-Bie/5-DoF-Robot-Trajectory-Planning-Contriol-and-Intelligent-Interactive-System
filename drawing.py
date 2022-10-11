import pybullet as p
from time import sleep
import pybullet_data as pd
import  numpy as np
def draw_cirlce(r,center_vector,limit_size,theta,table_high): #需要注意是单位是米
    ######
    center_vector=np.array(center_vector)
    x=np.zeros((limit_size,1))
    y=np.zeros((limit_size,1))
    ########

    for i in range(limit_size):
        x[i,0]=center_vector[0]+r*(np.cos(i/180*np.pi))
        y[i,0]=center_vector[1]+r*(np.sin(i/180*np.pi))

    ###现在是圆的高度，和倾斜角
    z1=(np.zeros((180,1)))
    z2=np.zeros((180,1))
    for i in range(180):
        z1[i,0]=(2*r*i/180)*np.sin(theta/180*np.pi)+table_high  #这款是180个数，
        z2[i,0]=(2*r*(180-i)/180)*np.sin(theta/180*np.pi)+table_high
    z=np.vstack((z1,z2))

    ###合并起来变成圆的三维位置输出,输出一个360*3的矩阵，是圆轨迹的坐标
    all=np.hstack((x,y,z))

    #fig = plt.figure()
    #ax = Axes3D(fig)
    #ax.scatter(x, y, z)
    # 添加坐标轴(顺序是Z, Y, X)  ####
    #ax.set_zlabel('Z', fontdict={'size': 10, 'color': 'red'})
    #ax.set_ylabel('Y', fontdict={'size': 10, 'color': 'red'})
    #ax.set_xlabel('X', fontdict={'size': 10, 'color': 'red'})
    #plt.show()
    return all  #输出是一个矩阵

def draw_cirlce2(r,center_vector,limit_size,theta,table_high): #需要注意是单位是米
    ######
    center_vector=np.array(center_vector)
    x=np.zeros((limit_size,1))
    y=np.zeros((limit_size,1))
    ########

    for i in range(limit_size):
        x[i,0]=center_vector[0]+r*(np.sin((i/180)*np.pi))
        y[i,0]=center_vector[1]+r*(np.cos((i/180)*np.pi))

    ###现在是圆的高度，和倾斜角
    z1=(np.zeros((180,1)))
    z2=np.zeros((180,1))
    for i in range(180):
        z1[i,0]=(2*r*i/180)*np.sin(theta/180*np.pi)+table_high  #这款是180个数，
        z2[i,0]=(2*r*(180-i)/180)*np.sin(theta/180*np.pi)+table_high
    z=np.vstack((z1,z2))

    ###合并起来变成圆的三维位置输出,输出一个360*3的矩阵，是圆轨迹的坐标
    all=np.hstack((x,y,z))

    #fig = plt.figure()
    #ax = Axes3D(fig)
    #ax.scatter(x, y, z)
    # 添加坐标轴(顺序是Z, Y, X)  ####
    #ax.set_zlabel('Z', fontdict={'size': 10, 'color': 'red'})
    #ax.set_ylabel('Y', fontdict={'size': 10, 'color': 'red'})
    #ax.set_xlabel('X', fontdict={'size': 10, 'color': 'red'})
    #plt.show()
    return all  #输出是一个矩阵

def draw_down2(r, center_vector, limit_size, theta, table_high):  # 需要注意是单位是米
    ######
    center_vector = np.array(center_vector)
    x = np.zeros((limit_size, 1))
    y = np.zeros((limit_size, 1))
    ########

    for i in range(180):
        x[i, 0] = center_vector[0]
        y[i, 0] = 0.2 - i * 0.4 / 180

    ###现在是圆的高度，和倾斜角
    z1 = (np.zeros((180, 1)))
    z2 = np.zeros((180, 1))
    for i in range(180):
        z1[i, 0] = (2 * r * i / 180) * np.sin(theta / 180 * np.pi) + table_high  # 这款是180个数，
        z2[i, 0] = (2 * r * (180 - i) / 180) * np.sin(theta / 180 * np.pi) + table_high
    z = np.vstack((z1, z2))

    ###合并起来变成圆的三维位置输出,输出一个360*3的矩阵，是圆轨迹的坐标
    all = np.hstack((x, y, z))

    return all  # 输出是一个矩阵

def draw_heart(r,center_vector,limit_size,theta,table_high): #需要注意是单位是米
    ######
    center_vector=np.array(center_vector)
    x=np.zeros((limit_size,1))
    y=np.zeros((limit_size,1))
    ########

    for i in range(limit_size):
        x[i,0] = 0.16* (np.sin(i/180*np.pi))**3;
        y[i,0] = 0.13* np.cos(i/180*np.pi) - 0.05*np.cos(2*i/180*np.pi)- 0.02*np.cos(3*i/180*np.pi)-0.01*np.cos(4*i/180*np.pi)

    ###现在是圆的高度，和倾斜角
    z1=(np.zeros((180,1)))
    z2=np.zeros((180,1))
    for i in range(180):
        z1[i,0]=(2*r*i/180)*np.sin(theta/180*np.pi)+table_high  #这款是180个数，
        z2[i,0]=(2*r*(180-i)/180)*np.sin(theta/180*np.pi)+table_high
    z=np.vstack((z1,z2))

    ###合并起来变成圆的三维位置输出,输出一个360*3的矩阵，是圆轨迹的坐标
    all=np.hstack((x,y,z))

    return all  #输出是一个矩阵

def draw_cirlce(r,center_vector,limit_size,theta,table_high): #需要注意是单位是米
    ######
    center_vector=np.array(center_vector)
    x=np.zeros((limit_size,1))
    y=np.zeros((limit_size,1))
    ########

    for i in range(limit_size):
        x[i,0]=center_vector[0]+r*(np.cos(i/180*np.pi))
        y[i,0]=center_vector[1]+r*(np.sin(i/180*np.pi))

    ###现在是圆的高度，和倾斜角
    z1=(np.zeros((180,1)))
    z2=np.zeros((180,1))
    for i in range(180):
        z1[i,0]=(2*r*i/180)*np.sin(theta/180*np.pi)+table_high  #这款是180个数，
        z2[i,0]=(2*r*(180-i)/180)*np.sin(theta/180*np.pi)+table_high
    z=np.vstack((z1,z2))

    ###合并起来变成圆的三维位置输出,输出一个360*3的矩阵，是圆轨迹的坐标
    all=np.hstack((x,y,z))

    #fig = plt.figure()
    #ax = Axes3D(fig)
    #ax.scatter(x, y, z)
    # 添加坐标轴(顺序是Z, Y, X)  ####
    #ax.set_zlabel('Z', fontdict={'size': 10, 'color': 'red'})
    #ax.set_ylabel('Y', fontdict={'size': 10, 'color': 'red'})
    #ax.set_xlabel('X', fontdict={'size': 10, 'color': 'red'})
    #plt.show()
    return all  #输出是一个矩阵

def draw_cirlce2(r,center_vector,limit_size,theta,table_high): #需要注意是单位是米
    ######
    center_vector=np.array(center_vector)
    x=np.zeros((limit_size,1))
    y=np.zeros((limit_size,1))
    ########

    for i in range(limit_size):
        x[i,0]=center_vector[0]+r*(np.sin((i/180)*np.pi))
        y[i,0]=center_vector[1]+r*(np.cos((i/180)*np.pi))

    ###现在是圆的高度，和倾斜角
    z1=(np.zeros((180,1)))
    z2=np.zeros((180,1))
    for i in range(180):
        z1[i,0]=(2*r*i/180)*np.sin(theta/180*np.pi)+table_high  #这款是180个数，
        z2[i,0]=(2*r*(180-i)/180)*np.sin(theta/180*np.pi)+table_high
    z=np.vstack((z1,z2))

    ###合并起来变成圆的三维位置输出,输出一个360*3的矩阵，是圆轨迹的坐标
    all=np.hstack((x,y,z))

    return all  #输出是一个矩阵

def draw_down(r, center_vector, limit_size, theta, table_high):  # 需要注意是单位是米
        ######
        center_vector = np.array(center_vector)
        x = np.zeros((limit_size, 1))
        y = np.zeros((limit_size, 1))
        ########

        for i in range(90):
            x[i, 0] = center_vector[0]
            y[i, 0] = 0.2 - i * 0.2 / 90

        ###现在是圆的高度，和倾斜角
        z1 = (np.zeros((180, 1)))
        z2 = np.zeros((180, 1))
        for i in range(180):
            z1[i, 0] = (2 * r * i / 180) * np.sin(theta / 180 * np.pi) + table_high  # 这款是180个数，
            z2[i, 0] = (2 * r * (180 - i) / 180) * np.sin(theta / 180 * np.pi) + table_high
        z = np.vstack((z1, z2))

        ###合并起来变成圆的三维位置输出,输出一个360*3的矩阵，是圆轨迹的坐标
        all = np.hstack((x, y, z))

        return all  # 输出是一个矩阵


def draw_up(r, center_vector, limit_size, theta, table_high):  # 需要注意是单位是米
    ######
    center_vector = np.array(center_vector)
    x = np.zeros((limit_size, 1))
    y = np.zeros((limit_size, 1))
    ########

    for i in range(90):
        x[i, 0] = center_vector[0]
        y[i, 0] = 0 + i * 0.2 / 90

    ###现在是圆的高度，和倾斜角
    z1 = (np.zeros((180, 1)))
    z2 = np.zeros((180, 1))
    for i in range(180):
        z1[i, 0] = (2 * r * i / 180) * np.sin(theta / 180 * np.pi) + table_high  # 这款是180个数，
        z2[i, 0] = (2 * r * (180 - i) / 180) * np.sin(theta / 180 * np.pi) + table_high
    z = np.vstack((z1, z2))

    ###合并起来变成圆的三维位置输出,输出一个360*3的矩阵，是圆轨迹的坐标
    all = np.hstack((x, y, z))

    return all  # 输出是一个矩阵




def draw_up(r, center_vector, limit_size, theta, table_high):  # 需要注意是单位是米
    ######
    center_vector = np.array(center_vector)
    x = np.zeros((limit_size, 1))
    y = np.zeros((limit_size, 1))
    ########

    for i in range(90):
        x[i, 0] = center_vector[0]
        y[i, 0] = 0 + i * 0.2 / 90

    ###现在是圆的高度，和倾斜角
    z1 = (np.zeros((180, 1)))
    z2 = np.zeros((180, 1))
    for i in range(180):
        z1[i, 0] = (2 * r * i / 180) * np.sin(theta / 180 * np.pi) + table_high  # 这款是180个数，
        z2[i, 0] = (2 * r * (180 - i) / 180) * np.sin(theta / 180 * np.pi) + table_high
    z = np.vstack((z1, z2))

    ###合并起来变成圆的三维位置输出,输出一个360*3的矩阵，是圆轨迹的坐标
    all = np.hstack((x, y, z))

    return all  # 输出是一个矩阵

def draw_right(r, center_vector, limit_size, theta, table_high):  # 需要注意是单位是米
    ######
    center_vector = np.array(center_vector)
    x = np.zeros((limit_size, 1))
    y = np.zeros((limit_size, 1))
    ########

    for i in range(180):
        x[i, 0] = center_vector[0]-0.2+i*0.4/180
        y[i, 0] = center_vector[1]

    ###现在是圆的高度，和倾斜角
    z1 = (np.zeros((180, 1)))
    z2 = np.zeros((180, 1))
    for i in range(180):
        z1[i, 0] = (2 * r * i / 180) * np.sin(theta / 180 * np.pi) + table_high  # 这款是180个数，
        z2[i, 0] = (2 * r * (180 - i) / 180) * np.sin(theta / 180 * np.pi) + table_high
    z = np.vstack((z1, z2))

    ###合并起来变成圆的三维位置输出,输出一个360*3的矩阵，是圆轨迹的坐标
    all = np.hstack((x, y, z))

    return all  # 输出是一个矩阵

