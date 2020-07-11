# -*- coding: utf-8 -*-
import numpy as np
from PySide2.QtCore import QTimer
from PySide2.QtWidgets import *

from hopui import Ui_MainWindow
from simple import DHNN


class Window(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.start.clicked.connect(self.start)
        self.ui.play.clicked.connect(self.play)
        self.ui.next.clicked.connect(self.refresh)
        self.is_run = False
        self.time = QTimer(self)
        self.time.setInterval(400)
        self.time.timeout.connect(self.refresh)

        self.ui.lineEdit.setText('0101')
        self.ui.textEdit.setPlainText('0011\n0110')

    def get(self):
        line = self.ui.lineEdit.text()
        sample = self.ui.textEdit.toPlainText().split()
        self.input = np.array([int(i) for i in line])
        self.input[self.input == 0] = -1
        a = []
        for i in sample:
            a_ = [int(j) for j in i]
            a.append(a_)
        self.sample = np.array(a)
        self.sample[self.sample == 0] = -1
        # print(self.input, self.sample)
        self.ui.lcdNumber.display(line)

    def start(self):
        self.get()
        self.ui.print.clear()
        self.n = np.size(self.input)
        self.test = DHNN(self.input, self.sample)
        self.m = 0
        self.ui.print.appendPlainText(f'权重:\n{self.test.W}\n-------------------------')
        self.time.stop()
        self.ui.play.setText('自动')
        self.is_run = False

    def play(self):
        if not self.is_run:
            self.time.start()
            self.ui.play.setText('暂停')
            self.is_run = True
        else:
            self.time.stop()
            self.ui.play.setText('自动')
            self.is_run = False

    def refresh(self):
        e, sg = self.test.update(self.m)
        self.ui.print.appendPlainText(f'更新第{self.m + 1}个神经元：{sg}')
        self.m += 1
        self.m = self.m % self.n
        line = self.test.V.copy()
        line[line == -1] = 0
        line = [str(i) for i in line]
        line = "".join(line)
        self.ui.lcdNumber.display(line)
        self.ui.print.appendPlainText(f'能量函数值：{e}\n-------------------------')


if __name__ == "__main__":
    app = QApplication()
    window = Window()
    window.show()
    app.exec_()
