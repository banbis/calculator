# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(633, 576)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 621, 501))
        self.tabWidget.setObjectName("tabWidget")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.widget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 601, 471))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.hex = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.hex.setEnabled(False)
        self.hex.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(20)
        self.hex.setFont(font)
        self.hex.setObjectName("hex")
        self.gridLayout.addWidget(self.hex, 0, 2, 1, 3)
        self.button_1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_1.setMinimumSize(QtCore.QSize(94, 64))
        self.button_1.setMaximumSize(QtCore.QSize(94, 64))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.button_1.setFont(font)
        self.button_1.setObjectName("button_1")
        self.gridLayout.addWidget(self.button_1, 3, 2, 1, 1)
        self.button_D = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_D.setEnabled(False)
        self.button_D.setMinimumSize(QtCore.QSize(94, 64))
        self.button_D.setMaximumSize(QtCore.QSize(94, 64))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.button_D.setFont(font)
        self.button_D.setObjectName("button_D")
        self.gridLayout.addWidget(self.button_D, 5, 1, 1, 1)
        self.button_B = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_B.setEnabled(False)
        self.button_B.setMinimumSize(QtCore.QSize(94, 64))
        self.button_B.setMaximumSize(QtCore.QSize(94, 64))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.button_B.setFont(font)
        self.button_B.setObjectName("button_B")
        self.gridLayout.addWidget(self.button_B, 4, 1, 1, 1)
        self.button_hex_to_dec = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_hex_to_dec.setMinimumSize(QtCore.QSize(94, 64))
        self.button_hex_to_dec.setMaximumSize(QtCore.QSize(94, 64))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_hex_to_dec.setFont(font)
        self.button_hex_to_dec.setObjectName("button_hex_to_dec")
        self.gridLayout.addWidget(self.button_hex_to_dec, 3, 0, 1, 1)
        self.button_A = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_A.setEnabled(False)
        self.button_A.setMinimumSize(QtCore.QSize(94, 64))
        self.button_A.setMaximumSize(QtCore.QSize(94, 64))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.button_A.setFont(font)
        self.button_A.setObjectName("button_A")
        self.gridLayout.addWidget(self.button_A, 4, 0, 1, 1)
        self.button_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_4.setMinimumSize(QtCore.QSize(94, 64))
        self.button_4.setMaximumSize(QtCore.QSize(94, 64))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.button_4.setFont(font)
        self.button_4.setObjectName("button_4")
        self.gridLayout.addWidget(self.button_4, 4, 2, 1, 1)
        self.button_bin_to_dec = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_bin_to_dec.setMinimumSize(QtCore.QSize(94, 64))
        self.button_bin_to_dec.setMaximumSize(QtCore.QSize(94, 64))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_bin_to_dec.setFont(font)
        self.button_bin_to_dec.setObjectName("button_bin_to_dec")
        self.gridLayout.addWidget(self.button_bin_to_dec, 3, 1, 1, 1)
        self.button_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_7.setMinimumSize(QtCore.QSize(94, 64))
        self.button_7.setMaximumSize(QtCore.QSize(94, 64))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.button_7.setFont(font)
        self.button_7.setObjectName("button_7")
        self.gridLayout.addWidget(self.button_7, 5, 2, 1, 1)
        self.button_F = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_F.setEnabled(False)
        self.button_F.setMinimumSize(QtCore.QSize(94, 64))
        self.button_F.setMaximumSize(QtCore.QSize(94, 64))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.button_F.setFont(font)
        self.button_F.setObjectName("button_F")
        self.gridLayout.addWidget(self.button_F, 6, 1, 1, 1)
        self.button_E = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_E.setEnabled(False)
        self.button_E.setMinimumSize(QtCore.QSize(94, 64))
        self.button_E.setMaximumSize(QtCore.QSize(94, 64))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.button_E.setFont(font)
        self.button_E.setObjectName("button_E")
        self.gridLayout.addWidget(self.button_E, 6, 0, 1, 1)
        self.button_clearAll = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_clearAll.setMinimumSize(QtCore.QSize(94, 64))
        self.button_clearAll.setMaximumSize(QtCore.QSize(94, 64))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.button_clearAll.setFont(font)
        self.button_clearAll.setObjectName("button_clearAll")
        self.gridLayout.addWidget(self.button_clearAll, 6, 2, 1, 1)
        self.bin = QtWidgets.QTextEdit(self.gridLayoutWidget)
        self.bin.setEnabled(False)
        self.bin.setMinimumSize(QtCore.QSize(0, 41))
        self.bin.setMaximumSize(QtCore.QSize(16777215, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(20)
        self.bin.setFont(font)
        self.bin.setObjectName("bin")
        self.gridLayout.addWidget(self.bin, 2, 2, 1, 3)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(94, 41))
        self.label.setMaximumSize(QtCore.QSize(94, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 5, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setMinimumSize(QtCore.QSize(94, 41))
        self.label_3.setMaximumSize(QtCore.QSize(94, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(24)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 5, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setMinimumSize(QtCore.QSize(94, 41))
        self.label_2.setMaximumSize(QtCore.QSize(94, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 5, 1, 1)
        self.dec = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.dec.setEnabled(False)
        self.dec.setMinimumSize(QtCore.QSize(0, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(20)
        self.dec.setFont(font)
        self.dec.setObjectName("dec")
        self.gridLayout.addWidget(self.dec, 1, 2, 1, 3)
        self.button_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_3.setMinimumSize(QtCore.QSize(94, 64))
        self.button_3.setMaximumSize(QtCore.QSize(94, 64))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.button_3.setFont(font)
        self.button_3.setObjectName("button_3")
        self.gridLayout.addWidget(self.button_3, 3, 4, 1, 1)
        self.button_multiply = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_multiply.setMinimumSize(QtCore.QSize(94, 64))
        self.button_multiply.setMaximumSize(QtCore.QSize(94, 64))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.button_multiply.setFont(font)
        self.button_multiply.setObjectName("button_multiply")
        self.gridLayout.addWidget(self.button_multiply, 4, 5, 1, 1)
        self.button_devide = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_devide.setMinimumSize(QtCore.QSize(94, 64))
        self.button_devide.setMaximumSize(QtCore.QSize(94, 64))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.button_devide.setFont(font)
        self.button_devide.setObjectName("button_devide")
        self.gridLayout.addWidget(self.button_devide, 3, 5, 1, 1)
        self.button_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_5.setMinimumSize(QtCore.QSize(94, 64))
        self.button_5.setMaximumSize(QtCore.QSize(94, 64))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.button_5.setFont(font)
        self.button_5.setObjectName("button_5")
        self.gridLayout.addWidget(self.button_5, 4, 3, 1, 1)
        self.button_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_6.setMinimumSize(QtCore.QSize(94, 64))
        self.button_6.setMaximumSize(QtCore.QSize(94, 64))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.button_6.setFont(font)
        self.button_6.setObjectName("button_6")
        self.gridLayout.addWidget(self.button_6, 4, 4, 1, 1)
        self.button_9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_9.setMinimumSize(QtCore.QSize(94, 64))
        self.button_9.setMaximumSize(QtCore.QSize(94, 64))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.button_9.setFont(font)
        self.button_9.setObjectName("button_9")
        self.gridLayout.addWidget(self.button_9, 5, 4, 1, 1)
        self.button_8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_8.setMinimumSize(QtCore.QSize(94, 64))
        self.button_8.setMaximumSize(QtCore.QSize(94, 64))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.button_8.setFont(font)
        self.button_8.setObjectName("button_8")
        self.gridLayout.addWidget(self.button_8, 5, 3, 1, 1)
        self.button_0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_0.setMinimumSize(QtCore.QSize(94, 64))
        self.button_0.setMaximumSize(QtCore.QSize(94, 64))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.button_0.setFont(font)
        self.button_0.setObjectName("button_0")
        self.gridLayout.addWidget(self.button_0, 6, 3, 1, 1)
        self.button_plus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_plus.setMinimumSize(QtCore.QSize(94, 64))
        self.button_plus.setMaximumSize(QtCore.QSize(94, 64))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.button_plus.setFont(font)
        self.button_plus.setObjectName("button_plus")
        self.gridLayout.addWidget(self.button_plus, 5, 5, 1, 1)
        self.button_minus = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_minus.setMinimumSize(QtCore.QSize(94, 64))
        self.button_minus.setMaximumSize(QtCore.QSize(94, 64))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.button_minus.setFont(font)
        self.button_minus.setObjectName("button_minus")
        self.gridLayout.addWidget(self.button_minus, 6, 5, 1, 1)
        self.button_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_2.setEnabled(True)
        self.button_2.setMinimumSize(QtCore.QSize(94, 64))
        self.button_2.setMaximumSize(QtCore.QSize(94, 64))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.button_2.setFont(font)
        self.button_2.setObjectName("button_2")
        self.gridLayout.addWidget(self.button_2, 3, 3, 1, 1)
        self.button_equal = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_equal.setMinimumSize(QtCore.QSize(94, 64))
        self.button_equal.setMaximumSize(QtCore.QSize(94, 64))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.button_equal.setFont(font)
        self.button_equal.setObjectName("button_equal")
        self.gridLayout.addWidget(self.button_equal, 6, 4, 1, 1)
        self.button_C = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.button_C.setEnabled(False)
        self.button_C.setMinimumSize(QtCore.QSize(94, 64))
        self.button_C.setMaximumSize(QtCore.QSize(94, 64))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.button_C.setFont(font)
        self.button_C.setObjectName("button_C")
        self.gridLayout.addWidget(self.button_C, 5, 0, 1, 1)
        self.tabWidget.addTab(self.widget, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 611, 471))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.tableWidget.setFont(font)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(202)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(202)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exception = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.exception.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setBold(True)
        font.setWeight(75)
        self.exception.setFont(font)
        self.exception.setAlignment(QtCore.Qt.AlignCenter)
        self.exception.setObjectName("exception")
        self.horizontalLayout.addWidget(self.exception)
        self.button_addRow = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_addRow.setMinimumSize(QtCore.QSize(51, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_addRow.setFont(font)
        self.button_addRow.setObjectName("button_addRow")
        self.horizontalLayout.addWidget(self.button_addRow)
        self.button_removeRow = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_removeRow.setMinimumSize(QtCore.QSize(51, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.button_removeRow.setFont(font)
        self.button_removeRow.setObjectName("button_removeRow")
        self.horizontalLayout.addWidget(self.button_removeRow)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 633, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_1.setText(_translate("MainWindow", "1"))
        self.button_D.setText(_translate("MainWindow", "D"))
        self.button_B.setText(_translate("MainWindow", "B"))
        self.button_hex_to_dec.setText(_translate("MainWindow", "HEX"))
        self.button_A.setText(_translate("MainWindow", "A"))
        self.button_4.setText(_translate("MainWindow", "4"))
        self.button_bin_to_dec.setText(_translate("MainWindow", "BIN"))
        self.button_7.setText(_translate("MainWindow", "7"))
        self.button_F.setText(_translate("MainWindow", "F"))
        self.button_E.setText(_translate("MainWindow", "E"))
        self.button_clearAll.setText(_translate("MainWindow", "Clear"))
        self.label.setText(_translate("MainWindow", "HEX"))
        self.label_3.setText(_translate("MainWindow", "BIN"))
        self.label_2.setText(_translate("MainWindow", "DEC"))
        self.button_3.setText(_translate("MainWindow", "3"))
        self.button_multiply.setText(_translate("MainWindow", "*"))
        self.button_devide.setText(_translate("MainWindow", "/"))
        self.button_5.setText(_translate("MainWindow", "5"))
        self.button_6.setText(_translate("MainWindow", "6"))
        self.button_9.setText(_translate("MainWindow", "9"))
        self.button_8.setText(_translate("MainWindow", "8"))
        self.button_0.setText(_translate("MainWindow", "0"))
        self.button_plus.setText(_translate("MainWindow", "+"))
        self.button_minus.setText(_translate("MainWindow", "-"))
        self.button_2.setText(_translate("MainWindow", "2"))
        self.button_equal.setText(_translate("MainWindow", "="))
        self.button_C.setText(_translate("MainWindow", "C"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("MainWindow", "计算器"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "位区间"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "值"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "备注"))
        self.exception.setText(_translate("MainWindow", "Calulator"))
        self.button_addRow.setText(_translate("MainWindow", "AdRow"))
        self.button_removeRow.setText(_translate("MainWindow", "ReRow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "位表格"))
        self.menu.setTitle(_translate("MainWindow", "计算器"))
