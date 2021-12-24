from login import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import QTimer,QDateTime, QEventLoop
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from systemail import *


class WindowLogin(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        self.liberado = False

        #
        #FUNCTIONS
        #

        #BT CLOSE POPUP
        self.botton_erro_close.clicked.connect(lambda: self.frame_error.hide())

        #iniciar app com o frame de erro fechado
        self.frame_error.hide()

        #exibir o frame novamente
        #self.frame_error.show()

        self.conect_button.clicked.connect(self.checkFields)
        self.dados = [{'user':'vyniciussalusto@gmail.com','password':'Felipebia123'},{'user': 'vitor', 'password':'123'},
                      {'user':'italo','password':'cuequinha123'},{'user':'cm2designer@gmail.com','password':'12345678'}]




    def checkFields(self):
        textUser = ''
        textPassword = ''


        def showMensage(mensage):
            self.frame_error.show()
            self.label_error.setText(mensage)


        #check user
        if not self.input_user.text():
            textUser = ' User Empyt'
        else:
            textUser = ''
            self.input_user.setStyleSheet(self.styleOK)

        #check password
        if not self.input_password.text():
            textPassword = 'Password Empyt'
        else:
            textPassword = ''

        #check fields
        if textUser + textPassword != '':
            text = f'{textUser}, {textPassword}'
            showMensage(text)
        else:
            for cadastro in self.dados:
                if self.input_user.text() == cadastro['user'] and self.input_password.text() == cadastro['password']:
                    text = 'Login OK'
                    self.frame_error.setStyleSheet(self.frame_green_style)
                    showMensage(text)
                    self.checkopen(True)
                    if self.check_user.isChecked():
                        text = text + '  | Save user: OK'
                    showMensage(text)

                    #timer de 2 segundos
                    loop = QEventLoop()
                    QTimer.singleShot(2000, loop.quit)
                    loop.exec_()

                    # fechar a janela de login
                    self.close()
                    break

                else:
                    self.valido = False
                    text = 'Incorrect User or Password'
                    self.frame_error.setStyleSheet(self.frame_ERRO_style)
                    showMensage(text)
                    self.checkopen(False)


    def checkopen(self,key):
        self.liberado = key
        return self.liberado




if __name__ == "__main__":
    qt = QApplication(sys.argv)
    janela = WindowLogin()
    janela.show()

    qt.exec_()