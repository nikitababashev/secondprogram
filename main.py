import sys
import random

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(756, 723)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(160, 20, 441, 41))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "random ellipse"))


class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.flag)
        self.fl = False

    def paintEvent(self, event):
        if self.fl:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def flag(self):
        self.fl = True
        self.repaint()
        self.fl = False

    def draw(self, qp):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        x = random.randint(100, 500)
        y = random.randint(100, 500)
        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(100, 200, x, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = MyWidget()
    db.show()
    sys.exit(app.exec())