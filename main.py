import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from systemail import *
from principal import *


app = QApplication(sys.argv)
login = WindowLogin()


MainWindow = QtWidgets.QMainWindow()
ui = MailWindow()
ui.setupUi(MainWindow)



def checar():
    if login.liberado:
        MainWindow.show()


login.show()
login.conect_button.clicked.connect(checar)
app.exec_()



