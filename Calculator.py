
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import math

import re


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")

        self.setFixedSize(375, 400)

        self.setStyleSheet("QPushButton {"
                           "border: 1px solid #282928;"
                           "background-color: #666666;"
                           "color: white;"
                           "font-size: 18px;"
                           "}")

        self.UiComponents()

        self.show()

    def UiComponents(self):

        self.label = QLabel(self)

        self.label.setGeometry(0, 0, 375, 80)

        self.label.setWordWrap(True)

        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "background : #282928;"
                                 "color: white;"
                                 "padding: 10px 5px;"
                                 "}")

        self.label.setAlignment(Qt.AlignRight)

        self.label.setFont(QFont('Arial', 15))

        push7 = QPushButton("7", self)

        push7.setGeometry(0, 144, 75, 64)

        push8 = QPushButton("8", self)

        push8.setGeometry(75, 144, 75, 64)

        push9 = QPushButton("9", self)

        push9.setGeometry(150, 144, 75, 64)

        push_mul = QPushButton("\u00D7", self)

        push_mul.setGeometry(225, 144, 75, 64)

        push_mul.setStyleSheet("QPushButton {"
                               "background-color: #ffa703;"
                               "}")

        push_cos = QPushButton("cos", self)

        push_cos.setGeometry(300, 144, 75, 64)

        push_cos.setStyleSheet("QPushButton {"
                               "background-color: #ffa703;"
                               "}")

        push4 = QPushButton("4", self)

        push4.setGeometry(0, 208, 75, 64)

        push5 = QPushButton("5", self)

        push5.setGeometry(75, 208, 75, 64)

        push6 = QPushButton("6", self)

        push6.setGeometry(150, 208, 75, 64)

        push_minus = QPushButton("\u2212", self)

        push_minus.setGeometry(225, 208, 75, 64)

        push_minus.setStyleSheet("QPushButton {"
                                 "background-color: #ffa703;"
                                 "}")

        push_tan = QPushButton("tan", self)

        push_tan.setGeometry(300, 208, 75, 64)

        push_tan.setStyleSheet("QPushButton {"
                               "background-color: #ffa703;"
                               "}")

        push1 = QPushButton("1", self)

        push1.setGeometry(0, 272, 75, 64)

        push2 = QPushButton("2", self)

        push2.setGeometry(75, 272, 75, 64)

        push3 = QPushButton("3", self)

        push3.setGeometry(150, 272, 75, 64)

        push_plus = QPushButton("\u002b", self)

        push_plus.setGeometry(225, 272, 75, 64)

        push_plus.setStyleSheet("QPushButton {"
                                "background-color: #ffa703;"
                                "}")

        push_cot = QPushButton("cot", self)

        push_cot.setGeometry(300, 272, 75, 64)

        push_cot.setStyleSheet("QPushButton {"
                               "background-color: #ffa703;"
                               "}")

        push0 = QPushButton("0", self)

        push0.setGeometry(0, 336, 150, 64)

        push_point = QPushButton(".", self)

        push_point.setGeometry(150, 336, 75, 64)

        push_equal = QPushButton("\u003D", self)

        push_equal.setGeometry(225, 336, 75, 64)

        push_equal.setStyleSheet("QPushButton {"
                                 "background-color: #ffa703;"
                                 "}")

        push_log = QPushButton("log", self)

        push_log.setGeometry(300, 336, 75, 64)

        push_log.setStyleSheet("QPushButton {"
                               "background-color: #ffa703;"
                               "}")

        push_clear = QPushButton("AC", self)
        push_clear.setGeometry(0, 80, 75, 64)

        push_clear.setStyleSheet("QPushButton {"
                                 "background-color: #3b3b3b;"
                                 "}")

        push_mod = QPushButton("%", self)
        push_mod.setGeometry(75, 80, 75, 64)

        push_mod.setStyleSheet("QPushButton {"
                               "background-color: #3b3b3b;"
                               "}")

        push_sqrt = QPushButton("\u221A", self)
        push_sqrt.setGeometry(150, 80, 75, 64)

        push_sqrt.setStyleSheet("QPushButton {"
                                "background-color: #3b3b3b;"
                                "}")

        push_div = QPushButton("\u00F7", self)
        push_div.setGeometry(225, 80, 75, 64)

        push_div.setStyleSheet("QPushButton {"
                               "background-color: #ffa703;"
                               "}")

        push_sin = QPushButton("sin", self)
        push_sin.setGeometry(300, 80, 75, 64)

        push_sin.setStyleSheet("QPushButton {"
                               "background-color: #ffa703;"
                               "}")

        push_minus.clicked.connect(self.action_minus)
        push_equal.clicked.connect(self.action_equal)
        push0.clicked.connect(self.action0)
        push1.clicked.connect(self.action1)
        push2.clicked.connect(self.action2)
        push3.clicked.connect(self.action3)
        push4.clicked.connect(self.action4)
        push5.clicked.connect(self.action5)
        push6.clicked.connect(self.action6)
        push7.clicked.connect(self.action7)
        push8.clicked.connect(self.action8)
        push9.clicked.connect(self.action9)
        push_div.clicked.connect(self.action_div)
        push_mul.clicked.connect(self.action_mul)
        push_plus.clicked.connect(self.action_plus)
        push_point.clicked.connect(self.action_point)
        push_clear.clicked.connect(self.action_clear)
        push_mod.clicked.connect(self.action_mod)
        push_sin.clicked.connect(self.action_sin)
        push_cos.clicked.connect(self.action_cos)
        push_tan.clicked.connect(self.action_tan)
        push_cot.clicked.connect(self.action_cot)
        push_sqrt.clicked.connect(self.action_sqrt)
        push_log.clicked.connect(self.action_log)

    def action_equal(self):

        equation = self.label.text()

        try:
            ans = eval(equation)

            self.label.setText(str(ans))
        except:
            self.label.setText("Wrong Input")

    def action_plus(self):
        text = self.label.text()
        self.label.setText(text + " + ")

    def action_minus(self):
        text = self.label.text()
        self.label.setText(text + " - ")

    def action_div(self):
        text = self.label.text()
        self.label.setText(text + " / ")

    def action_mul(self):
        text = self.label.text()
        self.label.setText(text + " * ")

    def action_point(self):
        text = self.label.text()
        self.label.setText(text + ".")

    def action_mod(self):
        text = self.label.text()
        text_split = re.split('[ ]', text)
        if len(text_split) == 1:
            self.label.setText("0")
        else:
            perc = text_split[-1]
            sign = text_split[-2]
            rem_expression = ''.join(text_split[:-2])
            rem = eval(rem_expression)
            percentage = (float(rem) * float(perc)) / 100
            result = "%s %s %s" % (str(rem), str(sign), str(percentage))
            self.label.setText(str(result))

    def action_log(self):
        text = self.label.text()
        self.label.setText(str(math.log10(float(text))))

    def action_sqrt(self):
        text = self.label.text()
        self.label.setText(str(math.sqrt(float(text))))

    def action_sin(self):
        text = self.label.text()
        self.label.setText(str(math.sin(math.radians(float(text)))))

    def action_cos(self):
        text = self.label.text()
        self.label.setText(str(math.cos(math.radians(float(text)))))

    def action_tan(self):
        text = self.label.text()
        self.label.setText(str(math.tan(math.radians(float(text)))))

    def action_cot(self):
        text = self.label.text()
        rad = math.radians(float(text))
        cot = math.cos(rad) / math.sin(rad)
        self.label.setText(str(cot))

    def action0(self):
        text = self.label.text()
        self.label.setText(text + "0")

    def action1(self):
        text = self.label.text()
        self.label.setText(text + "1")

    def action2(self):
        text = self.label.text()
        self.label.setText(text + "2")

    def action3(self):
        text = self.label.text()
        self.label.setText(text + "3")

    def action4(self):
        text = self.label.text()
        self.label.setText(text + "4")

    def action5(self):
        text = self.label.text()
        self.label.setText(text + "5")

    def action6(self):
        text = self.label.text()
        self.label.setText(text + "6")

    def action7(self):
        text = self.label.text()
        self.label.setText(text + "7")

    def action8(self):
        text = self.label.text()
        self.label.setText(text + "8")

    def action9(self):
        text = self.label.text()
        self.label.setText(text + "9")

    def action_clear(self):
        self.label.setText("")

    def action_del(self):
        text = self.label.text()
        print(text[:len(text) - 1])
        self.label.setText(text[:len(text) - 1])


App = QApplication(sys.argv)

window = Window()

sys.exit(App.exec())
