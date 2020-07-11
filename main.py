# -*- coding: utf-8 -*-
import numpy as np
import cv2 as cv
from data import train_num as dt_num

size = 16


def sgn(x):
    """激活函数"""
    y = 1 if x >= 0 else -1
    return y


# save_img = []

def loadimg(path):
    img = cv.imread(path, 0)
    img = cv.resize(img, (size, size), interpolation=cv.INTER_AREA)
    img = cv.threshold(img, 127, 1, cv.THRESH_BINARY)
    img = img[1]
    img.dtype = np.int8
    # print('数字\n', img)
    # a_ = str(img)
    # save_img.append(a_)
    img[img == 0] = -1
    img = img.ravel()
    return img


def noisenum():
    small = np.random.randint(1, 6, 256)
    small[small == 2] = -1
    # img = np.array([])
    # for i in small:
    #     img = np.append(img, [i, i, i, i])
    return small


class DHNN:
    def __init__(self, v0, tra):
        """初始化"""
        self.n = np.size(v0)  # 神经元个数
        self.W = np.diag(np.zeros(self.n))  # 权矩阵 对角线元素为零的对称矩阵
        self.V = v0  # 神经元状态 {-1,1}
        self.Ip = np.zeros(self.n)  # 偏置矢量
        self.T = np.zeros(self.n)  # 阈值矢量
        self.show()
        self.train(tra)

    def update(self):
        for i in range(self.n):
            # i = np.random.randint(0, self.n)
            net = np.dot(self.V, self.W[:, i]) + self.Ip[i] - self.T[i]
            self.V[i] = sgn(net)
            E = -1 / 2 * np.dot(np.dot(self.V.T, self.W), self.V) - np.dot(self.Ip.T, self.V) + np.dot(self.T.T, self.V)
            print('能量函数', E)
            self.show()

    def train(self, num):
        """网络权重计算（记忆存储）"""
        S = num
        for i in range(self.n):
            for j in range(self.n):
                delta = 1 if i == j else 0
                a = []
                for m in S:
                    a_ = m[i] * m[j]
                    a.append(a_)
                self.W[i, j] = (1 - delta) * np.sum(a)
                # self.W[j, i] = self.W[i, j]

        print('权重', self.W)

    def show(self):
        img = self.V.copy()

        img = img.reshape((size, size))
        # print(img)
        img[img == -1] = 0
        img.dtype = np.uint8
        img[img == 1] = 255
        img = cv.resize(img, (256, 256), interpolation=cv.INTER_CUBIC)
        cv.imshow('What is this', img)
        cv.waitKey(30)


# train_num = []
# for i in range(10):
#     img = loadimg(f'pix/{i}.jpg')
#     train_num.append(img)

# print('样本', train_num)

# imgg = []
# for i in save_img:
#     a_ = i.replace(' ', ',')
#     a_ = a_.replace('\n', '')
#     imgg.append(a_)
#
# print(imgg)

if __name__ == '__main__':
    pass
    tr_num = np.array([
        dt_num[0],
        dt_num[1],
        dt_num[2],
        dt_num[3]
        # dt_num[4]
        # dt_num[5],
        # dt_num[6],
        # dt_num[7],
        # dt_num[8],
        # dt_num[9]
    ])
    test_img = loadimg('pix/3.jpg')

    test = DHNN(test_img, tr_num)
    while True:
        test.update()
