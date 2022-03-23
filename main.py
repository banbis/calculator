import sys
from GUI.mainwindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow
class Digcalculator(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(Digcalculator,self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())