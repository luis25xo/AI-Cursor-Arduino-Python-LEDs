# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interfaz_Arduino.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(449, 316)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 20, 204, 35))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 180, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox_SeleccionadorPuertos = QtWidgets.QComboBox(Dialog)
        self.comboBox_SeleccionadorPuertos.setGeometry(QtCore.QRect(240, 80, 191, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_SeleccionadorPuertos.setFont(font)
        self.comboBox_SeleccionadorPuertos.setObjectName("comboBox_SeleccionadorPuertos")
        self.pushButton_ConectarPuerto = QtWidgets.QPushButton(Dialog)
        self.pushButton_ConectarPuerto.setGeometry(QtCore.QRect(140, 120, 161, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_ConectarPuerto.setFont(font)
        self.pushButton_ConectarPuerto.setObjectName("pushButton_ConectarPuerto")
        self.label_EstadoDeConexion = QtWidgets.QLabel(Dialog)
        self.label_EstadoDeConexion.setGeometry(QtCore.QRect(140, 170, 154, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_EstadoDeConexion.setFont(font)
        self.label_EstadoDeConexion.setObjectName("label_EstadoDeConexion")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 210, 48, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_Encender_LED1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_Encender_LED1.setGeometry(QtCore.QRect(140, 210, 88, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Encender_LED1.setFont(font)
        self.pushButton_Encender_LED1.setObjectName("pushButton_Encender_LED1")
        self.pushButton_Apagar_LED1 = QtWidgets.QPushButton(Dialog)
        self.pushButton_Apagar_LED1.setGeometry(QtCore.QRect(250, 210, 88, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Apagar_LED1.setFont(font)
        self.pushButton_Apagar_LED1.setObjectName("pushButton_Apagar_LED1")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(80, 250, 48, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton_Encender_LED2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_Encender_LED2.setGeometry(QtCore.QRect(140, 250, 88, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Encender_LED2.setFont(font)
        self.pushButton_Encender_LED2.setObjectName("pushButton_Encender_LED2")
        self.pushButton_Apagar_LED2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_Apagar_LED2.setGeometry(QtCore.QRect(250, 250, 88, 27))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Apagar_LED2.setFont(font)
        self.pushButton_Apagar_LED2.setObjectName("pushButton_Apagar_LED2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Control de LEDs"))
        self.label_2.setText(_translate("Dialog", "Selecciona el puerto COM"))
        self.pushButton_ConectarPuerto.setText(_translate("Dialog", "Conectar"))
        self.label_EstadoDeConexion.setText(_translate("Dialog", "Estado: No conectado"))
        self.label_4.setText(_translate("Dialog", "LED 1:"))
        self.pushButton_Encender_LED1.setText(_translate("Dialog", "ON"))
        self.pushButton_Apagar_LED1.setText(_translate("Dialog", "OFF"))
        self.label_5.setText(_translate("Dialog", "LED 2:"))
        self.pushButton_Encender_LED2.setText(_translate("Dialog", "ON"))
        self.pushButton_Apagar_LED2.setText(_translate("Dialog", "OFF"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
