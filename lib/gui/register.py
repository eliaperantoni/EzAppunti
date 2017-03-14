# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.setEnabled(True)
        Register.resize(461, 223)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Register.sizePolicy().hasHeightForWidth())
        Register.setSizePolicy(sizePolicy)
        self.registerButton = QtWidgets.QPushButton(Register)
        self.registerButton.setGeometry(QtCore.QRect(40, 160, 381, 31))
        self.registerButton.setObjectName("registerButton")
        self.usernameEdit = QtWidgets.QLineEdit(Register)
        self.usernameEdit.setGeometry(QtCore.QRect(40, 40, 381, 31))
        self.usernameEdit.setObjectName("usernameEdit")
        self.passwordEdit = QtWidgets.QLineEdit(Register)
        self.passwordEdit.setGeometry(QtCore.QRect(40, 80, 381, 31))
        self.passwordEdit.setObjectName("passwordEdit")
        self.confirmEdit = QtWidgets.QLineEdit(Register)
        self.confirmEdit.setGeometry(QtCore.QRect(40, 120, 381, 31))
        self.confirmEdit.setObjectName("confirmEdit")

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "EzAppunti"))
        self.registerButton.setText(_translate("Register", "Registrazione"))
        self.usernameEdit.setPlaceholderText(_translate("Register", "Username"))
        self.passwordEdit.setPlaceholderText(_translate("Register", "Password"))
        self.confirmEdit.setPlaceholderText(_translate("Register", "Confirm password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QWidget()
    ui = Ui_Register()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec_())

