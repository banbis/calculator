import sys
import json
from GUI.mainwindow import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Digcalculator(QMainWindow, Ui_MainWindow):
    # 类常量
    num1 = 0
    num2 = 0
    result = 0
    bin_ = ""
    dec_ = ""
    hex_ = ""
    sign = ""
    filePath = "D:/Development/calculator/table.json"
    mark = 1

    Dic = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }

    def __init__(self, parent=None):
        super(Digcalculator, self).__init__()
        self.setupUi(self)
        self.tableWidgetInit()
        self.action()  # 存放所有的槽函数
    # 槽函数

    def action(self):
        # 数字
        self.button_0.clicked.connect(self.buttonClicked)
        self.button_1.clicked.connect(self.buttonClicked)
        self.button_2.clicked.connect(self.buttonClicked)
        self.button_3.clicked.connect(self.buttonClicked)
        self.button_4.clicked.connect(self.buttonClicked)
        self.button_5.clicked.connect(self.buttonClicked)
        self.button_6.clicked.connect(self.buttonClicked)
        self.button_7.clicked.connect(self.buttonClicked)
        self.button_8.clicked.connect(self.buttonClicked)
        self.button_9.clicked.connect(self.buttonClicked)

        # 十六进制字母
        self.button_A.clicked.connect(self.letterClicked)
        self.button_B.clicked.connect(self.letterClicked)
        self.button_C.clicked.connect(self.letterClicked)
        self.button_D.clicked.connect(self.letterClicked)
        self.button_E.clicked.connect(self.letterClicked)
        self.button_F.clicked.connect(self.letterClicked)

        # 操作符号
        self.button_plus.clicked.connect(self.opClicked)
        self.button_minus.clicked.connect(self.opClicked)
        self.button_multiply.clicked.connect(self.opClicked)
        self.button_devide.clicked.connect(self.opClicked)

        # 应用符号
        self.button_equal.clicked.connect(self.equalClicked)
        self.button_clearAll.clicked.connect(self.clearAllClicked)

        # 表格操作
        self.button_addRow.clicked.connect(self.addClicked)
        self.button_removeRow.clicked.connect(self.removeClicked)

        # 进制操作
        self.button_bin_to_dec.clicked.connect(self.toDecClicked)
        self.button_hex_to_dec.clicked.connect(self.toDecClicked)

    def toDecClicked(self):
        byte_ = 1
        if self.sender().text() == "HEX":
            byte_ = 4
            self.button_A.setEnabled(True)
            self.button_B.setEnabled(True)
            self.button_C.setEnabled(True)
            self.button_D.setEnabled(True)
            self.button_E.setEnabled(True)
            self.button_F.setEnabled(True)

        # print(byte_)
        str_ = self.dec.text()
        # print(str_)
        num = self.toDec(str_, byte_)
        self.result = num
        self.dec_ = str(num)
        self.printf()

    def toDec(self, str_, byte_) -> int:
        num = 0
        for i in range(0, len(str_)-1):
            num = num + self.Dic[str_[i]] << byte_
        if str_ != "":
            num = num + self.Dic[str_[-1]]
        return num

    def buttonClicked(self):
        temp = self.sender().text()
        self.dec_ += temp
        self.dec.setText(self.dec_)
        if(self.mark == 1):
            self.num1 = self.num1 * 10 + int(temp)
        else:
            self.num2 = self.num2 * 10 + int(temp)

    def letterClicked(self):
        temp = self.sender().text()
        self.dec_ += temp
        self.dec.setText(self.dec_)

    def opClicked(self):
        self.mark = 2
        temp = self.sender().text()
        self.dec_ += temp
        self.sign = temp
        self.dec.setText(self.dec_)

    def equalClicked(self):

        print("{},{}".format(self.num1, self.num2))
        if self.sign == '+':
            self.result = self.num1 + self.num2
        if self.sign == '-':
            self.result = self.num1 - self.num2
        if self.sign == '*':
            self.result = self.num1 * self.num2
        if self.sign == '/':
            self.result = self.num1 / self.num2
        self.printf()
        self.dec_ = str(self.result)
        self.tableWidgetFlash()
        self.num1 = self.result
        self.num2 = 0.0
        self.mark = 1

    def clearAllClicked(self):
        self.dec_ = ""
        self.bin_ = ""
        self.hex_ = ""
        self.mark = 1
        self.num1 = self.num2 = self.result = 0
        self.dec.setText(self.dec_)
        self.bin.setText(self.bin_)
        self.hex.setText(self.hex_)

    def printf(self):
        self.dec.setText(str(self.result))
        self.bin.setText(str(bin(int(self.result))))
        self.hex.setText(str(hex(int(self.result))))

    def addClicked(self):
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)
        self.createItemsARow(rowCount, "")

    def removeClicked(self):
        self.tableWidget.removeRow(self.tableWidget.rowCount()-1)

    def tableWidgetInit(self):
        json_data = self.readJson()
        for i in range(0, len(json_data)):
            key_ = "row"+str(i+1)
            start = json_data[key_]["start"]
            end = json_data[key_]["end"]
            # 获取行号
            rowCount = self.tableWidget.rowCount()
            # 添加一行
            self.tableWidget.insertRow(rowCount)
            self.createItemsARow(rowCount, "{},{}".format(start, end))

    def tableWidgetFlash(self):
        interval = ""
        rowCount = self.tableWidget.rowCount()
        if(rowCount > 32):
            self.exception.setText("行数细分过多！")
            return
        start = [0 for i in range(32)]
        end = [0 for i in range(32)]
        _bin_ = str(bin(int(self.result)))[2:]
        length = len(_bin_)
        print(_bin_)
        cut = "0"
        # 设置操作权限
        for i in range(0, rowCount):
            interval = self.tableWidget.item(i, 0).text()
            num = interval.split(',')
            if len(num) == 1:
                self.exception.setText("请输入<num,num>的格式！")
                return
            start[i] = int(num[0])
            end[i] = int(num[1])
            if start[i] > end[i]:
                self.exception.setText("请输入正确的位区间！")
                self.tableWidget.removeRow(i)
                continue
            if end[i] >= length and start[i] <= length:
                cut = _bin_[0:length-start[i]]
                print("{}:{}~{},{}".format(i,start[i],end[i],cut))
            elif end[i] < length:
                cut = _bin_[length-end[i]-1:length-start[i]]
                print("{}:{}~{},{}".format(i,start[i],end[i],cut))
            value = self.toDec(cut, 1)
            self.tableWidget.item(i, 1).setText(str(value))
            cut = "0"
        json_data = self.creatJsonObject(start,end,rowCount)
        self.saveJson(json_data)

    def createItemsARow(self, curRow: int, string_: str):
        string = ""
        item = QTableWidgetItem(string_, 0)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(curRow, 0, item)
        item = QTableWidgetItem(string, 1)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(curRow, 1, item)
        item = QTableWidgetItem(string, 2)
        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.tableWidget.setItem(curRow, 2, item)

    def creatJsonObject(self,start,end,rowCount)->dict:
        start = start.copy()
        end = end.copy()
        json_data = {}
        for i in range(rowCount):
            temp = {}
            temp.setdefault("start",start[i])
            temp.setdefault("end",end[i])
            json_data.setdefault("row"+str(i+1),temp)
        print(json_data)
        return json_data
    def readJson(self) -> dict:
        with open(self.filePath, 'r', encoding='utf8')as fp:
            json_data = json.load(fp)
        return json_data

    def saveJson(self, json_date: dict):
        with open(self.filePath, 'w', encoding='utf8')as fp:
            json.dump(json_date, fp, ensure_ascii=False)

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(
            self, u'警告', u'确认退出?', QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Digcalculator()
    window.show()
    sys.exit(app.exec_())
