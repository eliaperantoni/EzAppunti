# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.setEnabled(True)
        Login.resize(461,321)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        self.registerButton = QtWidgets.QPushButton(Login)
        self.registerButton.setGeometry(QtCore.QRect(40, 250, 131, 31))
        self.registerButton.setObjectName("registerButton")
        self.loginButton = QtWidgets.QPushButton(Login)
        self.loginButton.setGeometry(QtCore.QRect(180, 250, 241, 31))
        self.loginButton.setObjectName("loginButton")
        self.usernameEdit = QtWidgets.QLineEdit(Login)
        self.usernameEdit.setGeometry(QtCore.QRect(40, 170, 381, 31))
        self.usernameEdit.setObjectName("usernameEdit")
        self.passwordEdit = QtWidgets.QLineEdit(Login)
        self.passwordEdit.setGeometry(QtCore.QRect(40, 210, 381, 31))
        self.passwordEdit.setObjectName("passwordEdit")
        self.ezLogo = QtWidgets.QLabel(Login)
        self.ezLogo.setGeometry(QtCore.QRect(0, 40, 461, 121))
        self.ezLogo.setText("")
        self.ezLogo.setPixmap(QtGui.QPixmap("../../../../logoBig2.png"))
        self.ezLogo.setAlignment(QtCore.Qt.AlignCenter)
        self.ezLogo.setObjectName("ezLogo")
        self.wrongLogin = QtWidgets.QLabel(Login)
        self.wrongLogin.setEnabled(True)
        self.wrongLogin.setGeometry(QtCore.QRect(0, 280, 461, 111))
        self.wrongLogin.setText("")
        self.wrongLogin.setPixmap(QtGui.QPixmap("wrongLogin.png"))
        self.wrongLogin.setAlignment(QtCore.Qt.AlignCenter)
        self.wrongLogin.setObjectName("wrongLogin")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "EzAppunti"))
        self.registerButton.setText(_translate("Login", "Registrazione"))
        self.loginButton.setText(_translate("Login", "Login"))
        self.usernameEdit.setPlaceholderText(_translate("Login", "Username"))
        self.passwordEdit.setPlaceholderText(_translate("Login", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())

