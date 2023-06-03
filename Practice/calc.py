# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# python -m PyQt5.uic.pyuic -x [FILENAME].ui -o [FILENAME].py


from PyQt5 import QtCore, QtGui, QtWidgets


# Функция интерфейса
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(244, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -1, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(175, 168, 212);")
        self.label.setObjectName("label")
        self.btn_podelit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_podelit.setGeometry(QtCore.QRect(0, 290, 83, 60))
        self.btn_podelit.setObjectName("btn_podelit")
        self.btn_umnozit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_umnozit.setGeometry(QtCore.QRect(80, 290, 83, 60))
        self.btn_umnozit.setObjectName("btn_umnozit")
        self.btn_resalt = QtWidgets.QPushButton(self.centralwidget)
        self.btn_resalt.setGeometry(QtCore.QRect(160, 290, 83, 60))
        self.btn_resalt.setObjectName("btn_resalt")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(160, 230, 83, 60))
        self.btn_minus.setObjectName("btn_minus")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(80, 230, 83, 60))
        self.btn_plus.setObjectName("btn_plus")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(0, 230, 41, 60))
        self.btn_0.setObjectName("btn_0")
        self.btn_dut = QtWidgets.QPushButton(self.centralwidget)
        self.btn_dut.setGeometry(QtCore.QRect(41, 230, 41, 60))
        self.btn_dut.setObjectName("btn_dut")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 170, 83, 60))
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(80, 170, 83, 60))
        self.btn_8.setObjectName("btn_8")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(160, 170, 83, 60))
        self.btn_9.setObjectName("btn_9")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 110, 83, 60))
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(80, 110, 83, 60))
        self.btn_5.setObjectName("btn_5")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(160, 110, 83, 60))
        self.btn_6.setObjectName("btn_6")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(160, 50, 83, 60))
        self.btn_3.setObjectName("btn_3")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(80, 50, 83, 60))
        self.btn_2.setObjectName("btn_2")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 50, 83, 60))
        self.btn_1.setObjectName("btn_1")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_functions()

    # Присвоение текстовых значений кнопок
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Мой первый Калькулятор"))
        self.label.setText(_translate("MainWindow", "0"))
        self.btn_podelit.setText(_translate("MainWindow", "/"))
        self.btn_umnozit.setText(_translate("MainWindow", "*"))
        self.btn_resalt.setText(_translate("MainWindow", "="))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_dut.setText(_translate("MainWindow", "."))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_1.setText(_translate("MainWindow", "1"))

    # Функционал кнопок
    def add_functions(self):
        self.btn_0.clicked.connect(lambda: self.write_number(self.btn_0.text()))
        self.btn_1.clicked.connect(lambda: self.write_number(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.write_number(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.write_number(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.write_number(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.write_number(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.write_number(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.write_number(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.write_number(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.write_number(self.btn_9.text()))
        self.btn_plus.clicked.connect(lambda: self.write_number(self.btn_plus.text()))
        self.btn_minus.clicked.connect(lambda: self.write_number(self.btn_minus.text()))
        self.btn_podelit.clicked.connect(lambda: self.write_number(self.btn_podelit.text()))
        self.btn_umnozit.clicked.connect(lambda: self.write_number(self.btn_umnozit.text()))
        self.btn_resalt.clicked.connect(lambda: self.write_number(self.btn_resalt.text()))
        self.btn_dut.clicked.connect(lambda: self.write_number(self.btn_dut.text()))

    def write_number(self, number):
        if self.label_result.text() == '0':
            self.label_result.setText(self.label_result.text() + number)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())