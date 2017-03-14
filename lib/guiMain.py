import sys
import ctypes
import os
import hashlib
from PyQt5 import QtCore, QtGui, QtWidgets
from lib.util import *
class EzGui:
    def __init__(self,path=""):
        self.loggedUser = "NULL"
        self.ftp=connectToServer()
        self.app = QtWidgets.QApplication(sys.argv)
        self.Login = QtWidgets.QWidget()
        self.ui = Ui_Login()
        self.ui.setupUi(self.Login)

        self.ezAppuntiId = u'ppll.ez.appunti.1'
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(self.ezAppuntiId)
        self.app.setStyleSheet(open(path+"gui/ez.qss", "r").read())
        self.app_icon = QtGui.QIcon()
        self.app_icon.addFile(path+'gui/logo24.png', QtCore.QSize(24, 24))
        self.app_icon.addFile(path+'gui/logo32.png', QtCore.QSize(32, 32))
        self.app_icon.addFile(path+'gui/logo48.png', QtCore.QSize(48, 48))
        self.app_icon.addFile(path+'gui/logo256.png', QtCore.QSize(256, 256))
        self.app.setWindowIcon(self.app_icon)
        self.ui = Ui_Login()
        self.ui.setupUi(self.Login)
        self.ui.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Login.setFont(QtGui.QFont("Roboto"))
        self.ui.ezLogo.setPixmap(QtGui.QPixmap(path+'gui/logoBig.png'))
        self.ui.wrongLogin.setPixmap(QtGui.QPixmap(path+'gui/wrongLogin.png'))
        self.ui.wrongLogin.setVisible(False)
        self.Login.setFixedSize(self.Login.size())
        if "users.txt" in self.ftp.nlst():
            self.ftp.retrbinary("RETR users.txt", open("users.txt", "wb").write)  # TODO Hide file
        self.ui.registerButton.clicked.connect(self.registerClicked)
        self.ui.loginButton.clicked.connect(self.loginClicked)
        self.Login.keyPressEvent=self.keyPressEvent
    def keyPressEvent(self,e):
        if e.key() == QtCore.Qt.Key_Return:
            self.loginClicked()
    def show(self):
        self.Login.show()
        self.Login.activateWindow()
        sys.exit(self.app.exec_())
    def registerClicked(self):
        self.Register = QtWidgets.QWidget()
        self.uiRegister= Ui_Register()
        self.uiRegister.setupUi(self.Register)
        self.Register.show()
        self.Login.close()
    def loginClicked(self):
        with open("users.txt") as f:
            for line_terminated in f:
                self.userData = line_terminated.split(";")
                if (self.userData[1] == self.ui.usernameEdit.text()):
                    if (hashlib.sha256(self.ui.passwordEdit.text().encode('utf-8')).hexdigest() == self.userData[2]):
                        print("\nLogged successfully to " + self.ui.usernameEdit.text())
                        self.loggedUser=self.ui.usernameEdit.text()
                        self.credentials = line_terminated.split(";")
                        self.credentials[-1]=self.credentials[-1].rstrip()
                        "USER-OK"
                        break
                    else:
                        print("Wrong password")
                        self.loggedUser = "WRONG_PASSWORD"
                        "NOT-PASSWORD"
                        self.ui.wrongLogin.setVisible(True)
                        self.Login.setFixedSize(461,406)
                        return
            if (self.loggedUser == "NULL"):
                print("No users found for entry " + self.ui.usernameEdit.text())
                "NOT-FOUND"
                self.ui.wrongLogin.setVisible(True)
                self.Login.setFixedSize(461, 406)
                return
        "USER-OK"
        self.ui.wrongLogin.setVisible(False)
        self.Login.setFixedSize(461, 321)

if __name__ == '__main__':
    # noinspection PyUnresolvedReferences
    from gui.login import *
    # noinspection PyUnresolvedReferences
    from gui.register import *
    app=EzGui()
    app.show()
else:
    from lib.gui.login import *
    from lib.gui.register import *
