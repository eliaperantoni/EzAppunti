# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(670, 442)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        ####################################
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Title", "Author", "Date", "Tags","","","","",""])
        self.rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(self.rowPosition)
        self.tableWidget.setItem(self.rowPosition, 0, QtWidgets.QTableWidgetItem("a"))
        self.tableWidget.setItem(self.rowPosition, 1, QtWidgets.QTableWidgetItem("12"))
        self.tableWidget.setItem(self.rowPosition, 2, QtWidgets.QTableWidgetItem("text3"))
        self.tableWidget.setItem(self.rowPosition, 3, QtWidgets.QTableWidgetItem("text3"))
        self.tableWidget.setItem(self.rowPosition, 4, QtWidgets.QTableWidgetItem("text3"))
        self.rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(self.rowPosition)
        self.tableWidget.setItem(self.rowPosition, 0, QtWidgets.QTableWidgetItem("b"))
        self.tableWidget.setItem(self.rowPosition, 1, QtWidgets.QTableWidgetItem("13"))
        self.tableWidget.setItem(self.rowPosition, 2, QtWidgets.QTableWidgetItem("56"))
        self.tableWidget.setItem(self.rowPosition, 3, QtWidgets.QTableWidgetItem("text3"))
        self.tableWidget.setItem(self.rowPosition, 4, QtWidgets.QTableWidgetItem("text3"))
        self.rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(self.rowPosition)
        self.tableWidget.setItem(self.rowPosition, 0, QtWidgets.QTableWidgetItem("c"))
        self.tableWidget.setItem(self.rowPosition, 1, QtWidgets.QTableWidgetItem("8"))
        self.tableWidget.setItem(self.rowPosition, 2, QtWidgets.QTableWidgetItem("text3"))
        self.tableWidget.setItem(self.rowPosition, 3, QtWidgets.QTableWidgetItem("text3"))
        self.tableWidget.setItem(self.rowPosition, 4, QtWidgets.QTableWidgetItem("text3"))
        ####################################
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tableWidget.setSortingEnabled(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

