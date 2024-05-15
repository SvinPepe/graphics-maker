import sys
import numpy as np
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QPixmap, QRegExpValidator
from PyQt5.QtWidgets import *
from math import sin, cos, log, log2, tan as tg, atan as arctg
import matplotlib.pyplot as plt

crashed = 0


def f(x, func):
    return eval(func)


def getPlot(func, xmin=-30.0, xmax=30.0):
    global crashed
    crashed = 0
    plt.clf()
    func = func.replace("^", '**')

    step = (xmax - xmin) / 1000
    # x = np.linspace(-10, 10, 101)
    # y = f(x, func)
    x = []
    y = []
    i = xmin

    while i < xmax:

        try:

            val = eval(func.replace("x", '(' + str(i) + ')'))
            if abs(val) < 1e9:
                x.append(i)
                y.append(val)
            else:
                x.append(None)
                y.append(None)

        except:
            crashed = 1
        i += step
    if not crashed:
        plt.plot(x, y, color='green', marker='')
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.savefig('foo.png')


app = QApplication(sys.argv)
w = QWidget()
pixmap = QPixmap("foo.png")
label = QLabel(w)
inputLE = QLineEdit(w)
inputLE.setGeometry(10, 50, 150, 20)
inputXMin = QLineEdit(w)
inputXMin.setText("-30")
inputXMin.setGeometry(10, 80, 150, 20)
# regex = QRegExp(r"[0-9]*")
# validator = QRegExpValidator(regex)
# inputXMin.setValidator(validator)
inputXMax = QLineEdit(w)
inputXMax.setText("30")
inputXMax.setGeometry(10, 110, 150, 20)
button = QPushButton(w)
button.setText('Показать')
button.setGeometry(10, 150, 150, 50)
label.setGeometry(200, 0, pixmap.width(), pixmap.height())


def onClick():
    getPlot(inputLE.text(), xmin=float(inputXMin.text()), xmax=float(inputXMax.text()))
    if not crashed:
        pixmap = QPixmap("foo.png")
        label.setPixmap(pixmap)
    else:
        pixmap = QPixmap("error.jpg")
        label.setPixmap(pixmap)


button.clicked.connect(onClick)

w.setGeometry(200, 200, 1000, 500)
w.setWindowTitle('BURGER')
w.show()
sys.exit(app.exec_())
