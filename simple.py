# -*- coding: utf-8 -*-
import numpy as np
import time


def sgn(x):
    """激活函数"""
    y = 1 if x >= 0 else -1
    return y


class DHNN:
    def __init__(self, v0, tra):
        """初始化"""
        self.n = np.size(v0)  # 神经元个数
        self.W = np.diag(np.zeros(self.n))  # 权矩阵 对角线元素为零的对称矩阵
        self.V = v0  # 神经元状态 取值:{-1,1}
        self.Ip = np.zeros(self.n)  # 偏置矢量
        self.T = np.zeros(self.n)  # 阈值矢量
        self.train(tra)

    def update(self, i):
        """网络更新"""
        net = np.dot(self.V, self.W[:, i]) + self.Ip[i] - self.T[i]
        self.V[i] = sgn(net)
        E = -1 / 2 * np.dot(np.dot(self.V.T, self.W), self.V) - np.dot(self.Ip.T, self.V) + np.dot(self.T.T, self.V)
        # print('能量', E)
        # print('状态', self.V)
        return E, sgn(net)

    def train(self, sample):
        """网络权重计算（记忆存储）"""
        S = sample
        for i in range(self.n):
            for j in range(self.n):
                delta = 1 if i == j else 0
                a = []
                for m in S:
                    a_ = m[i] * m[j]
                    a.append(a_)
                self.W[i, j] = (1 - delta) * np.sum(a)
        print('权重\n', self.W)


if __name__ == '__main__':
    St = np.array([[-1, -1, 1, 1],
                   [-1, 1, 1, -1]])
    test = DHNN(np.array([1, 1, -1, 1]), St)
    while True:
        time.sleep(1)
        test.update(3)
