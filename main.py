import sys
import numpy as np
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QPixmap, QRegExpValidator
from PyQt5.QtWidgets import *
from math import sin, cos, log, log2, tan as tg, atan as arctg
import matplotlib.pyplot as plt

crashed = 0


def ctg(x):
    return 1 / tg(x)


def getPlot(func, xmin=-30.0, xmax=30.0, ymin=-30.0, ymax=30.0):
    global crashed
    crashed = 0
    plt.clf()
    func = func.replace("^", '**')

    step = (xmax - xmin) / 50000
    # x = np.linspace(-10, 10, 101)
    # y = f(x, func)
    x = []
    y = []
    i = xmin

    while i < xmax:
        try:
            val = eval(func.replace("x", '(' + str(i) + ')'))
            if ymin <= val <= ymax:
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
inputXMax = QLineEdit(w)
inputXMax.setText("30")
inputXMax.setGeometry(10, 110, 150, 20)
inputYMin = QLineEdit(w)
inputYMin.setText("-30")
inputYMin.setGeometry(10, 140, 150, 20)
inputYMax = QLineEdit(w)
inputYMax.setText("30")
inputYMax.setGeometry(10, 170, 150, 20)
button = QPushButton(w)
button.setText('Показать')
button.setGeometry(10, 200, 150, 50)
label.setGeometry(200, 0, pixmap.width(), pixmap.height())


def onClick():
    getPlot(inputLE.text(), xmin=float(inputXMin.text()), xmax=float(inputXMax.text()), ymin=float(inputYMin.text()),
            ymax=float(inputYMax.text()))
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
