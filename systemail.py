# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tela_email.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from string import Template
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import gmail.midia_email_rc



class MailWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 530)
        MainWindow.setMinimumSize(QtCore.QSize(800, 530))
        MainWindow.setMaximumSize(QtCore.QSize(800, 530))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/window_icon/logo_window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(86, 86, 86);")

        self.styleRed = ("background-color: rgb(255, 114, 116);\n"
                         "border-radius: 10px;")
        self.styleGreen = ("background-color: rgb(81, 226, 76);\n"
                           "border-radius: 10px;")


        self.email = 'vyniciusmartorano26@gmail.com'
        self.password = 'Felipebia123'



        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(600, 500))
        self.frame.setStyleSheet("background-color: rgb(10, 10, 10);")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(125, 138, 550, 350))
        self.frame_3.setMinimumSize(QtCore.QSize(550, 350))
        self.frame_3.setMaximumSize(QtCore.QSize(550, 350))
        self.frame_3.setStyleSheet("\n"
"border-radius: 8px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.input_email_destinatario = QtWidgets.QLineEdit(self.frame_3)
        self.input_email_destinatario.setGeometry(QtCore.QRect(12, 201, 220, 40))
        self.input_email_destinatario.setMinimumSize(QtCore.QSize(220, 40))
        self.input_email_destinatario.setMaximumSize(QtCore.QSize(220, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.input_email_destinatario.setFont(font)
        self.input_email_destinatario.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(30,30,30);\n"
"    padding: 7px;\n"
"    border-radius: 5px;\n"
"    color: rgb(105,105,105);\n"
"    border: 2px; solid rgb(45,45,45);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55,55,55)\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(255, 207, 0);\n"
"    color: rgb(200,200,200)\n"
"}")
        self.input_email_destinatario.setObjectName("input_email_destinatario")
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setGeometry(QtCore.QRect(250, 30, 280, 300))
        self.frame_4.setMinimumSize(QtCore.QSize(280, 300))
        self.frame_4.setMaximumSize(QtCore.QSize(270, 450))
        self.frame_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.text_box_conteudo = QtWidgets.QTextEdit(self.frame_4)
        self.text_box_conteudo.setGeometry(QtCore.QRect(12, 62, 256, 191))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.text_box_conteudo.setFont(font)
        self.text_box_conteudo.setStyleSheet("QTextEdit {\n"
"    background-color: rgb(50,50,50);\n"
"    color: rgb(200,200,200);\n"
"    padding: 10px;\n"
"}\n"
"QTextEdit:hover {\n"
"    border: 4px solid rgb(60,60,60);\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"border: 2px solid rgb(255, 207, 0);\n"
"}")
        self.text_box_conteudo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.text_box_conteudo.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.text_box_conteudo.setObjectName("text_box_conteudo")
        self.button_send_email = QtWidgets.QPushButton(self.frame_4)
        self.button_send_email.setEnabled(True)
        self.button_send_email.setGeometry(QtCore.QRect(208, 265, 60, 25))
        self.button_send_email.setMinimumSize(QtCore.QSize(60, 25))
        self.button_send_email.setMaximumSize(QtCore.QSize(50, 15))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.button_send_email.setFont(font)
        self.button_send_email.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.button_send_email.setStyleSheet("QPushButton {\n"
"    background-color: rgb(50, 50, 50);\n"
"    border: 2px solid rgb(60, 60, 60);\n"
"    border-radius: 5px;\n"
"    color: rgb(200,200,200)\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(60, 60, 60);\n"
"    border: 2px solid rgb(70, 70, 70);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(250, 230, 0);\n"
"    border: 2px solid rgb(255, 165, 24);\n"
"    color: rgb(35,35,35);\n"
"}")
        self.button_send_email.setIconSize(QtCore.QSize(25, 25))
        self.button_send_email.setObjectName("button_send_email")
        self.input_cabecalho = QtWidgets.QLineEdit(self.frame_4)
        self.input_cabecalho.setEnabled(True)
        self.input_cabecalho.setGeometry(QtCore.QRect(12, 10, 256, 40))
        self.input_cabecalho.setMinimumSize(QtCore.QSize(256, 40))
        self.input_cabecalho.setMaximumSize(QtCore.QSize(256, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.input_cabecalho.setFont(font)
        self.input_cabecalho.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(50,50,50);\n"
"    color: rgb(200,200,200);\n"
"    padding: 7px;\n"
"    border-radius: 5px;\n"
"    border: 2px; solid rgb(45,45,45);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55,55,55)\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(255, 207, 0);\n"
"    color: rgb(200,200,200)\n"
"}")
        self.input_cabecalho.setMaxLength(25)
        self.input_cabecalho.setObjectName("input_cabecalho")
        self.input_nome_destinatario = QtWidgets.QLineEdit(self.frame_3)
        self.input_nome_destinatario.setEnabled(True)
        self.input_nome_destinatario.setGeometry(QtCore.QRect(12, 153, 220, 40))
        self.input_nome_destinatario.setMinimumSize(QtCore.QSize(220, 40))
        self.input_nome_destinatario.setMaximumSize(QtCore.QSize(220, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.input_nome_destinatario.setFont(font)
        self.input_nome_destinatario.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(30,30,30);\n"
"    padding: 7px;\n"
"    border-radius: 5px;\n"
"    color: rgb(105,105,105);\n"
"    border: 2px; solid rgb(45,45,45);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55,55,55)\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(255, 207, 0);\n"
"    color: rgb(200,200,200)\n"
"}")
        self.input_nome_destinatario.setMaxLength(25)
        self.input_nome_destinatario.setObjectName("input_nome_destinatario")
        self.input_nome_remetente = QtWidgets.QLineEdit(self.frame_3)
        self.input_nome_remetente.setEnabled(True)
        self.input_nome_remetente.setGeometry(QtCore.QRect(12, 43, 220, 40))
        self.input_nome_remetente.setMinimumSize(QtCore.QSize(220, 40))
        self.input_nome_remetente.setMaximumSize(QtCore.QSize(220, 40))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.input_nome_remetente.setFont(font)
        self.input_nome_remetente.setStyleSheet("QLineEdit {\n"
"    background-color: rgb(30,30,30);\n"
"    padding: 7px;\n"
"    border-radius: 5px;\n"
"    color: rgb(105,105,105);\n"
"    border: 2px; solid rgb(45,45,45);\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(55,55,55)\n"
"}\n"
"\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(255, 207, 0);\n"
"    color: rgb(200,200,200)\n"
"}")
        self.input_nome_remetente.setMaxLength(25)
        self.input_nome_remetente.setObjectName("input_nome_remetente")
        self.label_1 = QtWidgets.QLabel(self.frame_3)
        self.label_1.setGeometry(QtCore.QRect(65, 0, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("QLabel{\n"
"background-color: rgb(254,211,0);\n"
"border-radius: 15px;\n"
"}\n"
"QLabel:hover {\n"
"    border: 3px solid rgb(255, 249, 75);\n"
"}")
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setGeometry(QtCore.QRect(65, 113, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel{\n"
"background-color: rgb(254,211,0);\n"
"border-radius: 15px;\n"
"}\n"
"QLabel:hover {\n"
"    border: 3px solid rgb(255, 249, 75);\n"
"}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(299, 0, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel{\n"
"background-color: rgb(254,211,0);\n"
"border-radius: 15px;\n"
"}\n"
"QLabel:hover {\n"
"    border: 3px solid rgb(255, 249, 75);\n"
"}\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.frame_error_email = QtWidgets.QFrame(self.frame)
        self.frame_error_email.setEnabled(True)
        self.frame_error_email.setGeometry(QtCore.QRect(200, 7, 450, 34))
        self.frame_error_email.setStyleSheet(self.styleRed)
        self.frame_error_email.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_error_email.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_error_email.setObjectName("frame_error_email")
        self.label_error_email = QtWidgets.QLabel(self.frame_error_email)
        self.label_error_email.setGeometry(QtCore.QRect(14, 5, 401, 25))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.label_error_email.setFont(font)
        self.label_error_email.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_error_email.setAlignment(QtCore.Qt.AlignCenter)
        self.label_error_email.setObjectName("label_error_email")
        self.button_close_error = QtWidgets.QPushButton(self.frame_error_email)
        self.button_close_error.setGeometry(QtCore.QRect(420, 7, 20, 20))
        self.button_close_error.setMinimumSize(QtCore.QSize(20, 20))
        self.button_close_error.setMaximumSize(QtCore.QSize(20, 20))
        self.button_close_error.setStyleSheet("QPushButton {\n"
"    border-radius: 3px;\n"
"    \n"
"    background-image: url(:/icon/cil-x.png);\n"
"    background-position: center;\n"
"    \n"
"    background-color: rgb(60,60,60);\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    background-color: rgb(255, 85, 255);\n"
"    color: rgba(200, 200, 200, 200);\n"
"}\n"
"QPushbotton:pressed {\n"
"    \n"
"    background-color: rgb(35, 35, 35);\n"
"    \n"
"    \n"
"    color: rgb(200, 200, 200);\n"
"}")
        self.button_close_error.setText("")
        self.button_close_error.setObjectName("button_close_error")
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setGeometry(QtCore.QRect(20, 20, 61, 61))
        self.frame_6.setStyleSheet("background-image: url(:/icon/IconGmail.png);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_2.setStyleSheet("background-color: rgb(15,15,15);\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(-1, 10, -1, 10)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(75, 75, 75);")
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.verticalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "E-gmail"))
        self.input_email_destinatario.setPlaceholderText(_translate("MainWindow", "E-gmail"))
        self.text_box_conteudo.setPlaceholderText(_translate("MainWindow", "Texto"))
        self.button_send_email.setText(_translate("MainWindow", "Enviar"))
        self.input_cabecalho.setPlaceholderText(_translate("MainWindow", "Cabe??alho"))
        self.input_nome_destinatario.setPlaceholderText(_translate("MainWindow", "Nome"))
        self.input_nome_remetente.setPlaceholderText(_translate("MainWindow", "Nome "))
        self.label_1.setText(_translate("MainWindow", "Remetente"))
        self.label_2.setText(_translate("MainWindow", "Destinatario"))
        self.label_3.setText(_translate("MainWindow", "Conte??do do E-mail"))
        self.label_error_email.setText(_translate("MainWindow", "ERRO"))
        self.label_5.setText(_translate("MainWindow", "Designed By: Vynicius Martorano"))


        #comandos
        self.frame_error_email.hide()
        self.button_close_error.clicked.connect(self.frame_error_email.hide)

        if self.button_send_email.clicked.connect(self.verifica):
            self.button_send_email.clicked.connect(self.enviar)


    def verifica(self):
        self.text = ''
        self.libera = False
        if self.input_nome_remetente.text() == '' and self.input_nome_destinatario.text() == '' and self.input_email_destinatario.text() == '' and self.input_cabecalho.text() == '' and self.getText() == '':
            text = 'Todos os elementos est??o vazios'
            self.label_error_email.setText(text)
            self.frame_error_email.show()
            self.libera = False
        else:
            if self.input_nome_remetente.text() == '':
                self.text += 'Nome do remetente vazio '
                self.frame_error_email.setStyleSheet(self.styleRed)
                self.label_error_email.setText(self.text)
                self.frame_error_email.show()
                self.libera = False

            elif self.input_nome_destinatario.text() == '':
                self.text += 'Nome do destinat??rio vazio'
                self.frame_error_email.setStyleSheet(self.styleRed)
                self.label_error_email.setText(self.text)
                self.frame_error_email.show()
                self.libera = False

            elif self.input_email_destinatario.text() == '':
                self.text += 'Email vazio '
                self.frame_error_email.setStyleSheet(self.styleRed)
                self.label_error_email.setText(self.text)
                self.frame_error_email.show()
                self.libera = False

            elif self.input_cabecalho.text() == '':
                self.text += 'Cabe??alho vazio '
                self.frame_error_email.setStyleSheet(self.styleRed)
                self.label_error_email.setText(self.text)
                self.frame_error_email.show()
                self.libera = False

            elif self.getText() == '':
                self.text += 'Conte??do vazio'
                self.frame_error_email.setStyleSheet(self.styleRed)
                self.label_error_email.setText(self.text)
                self.frame_error_email.show()
                self.libera = False

            else:
                self.libera = True
        return self.libera


    def enviar(self):
        if self.libera:
            html = open('gmail/template.html', 'r')
            template = Template(html.read())
            data_atual = datetime.now().strftime('%d/%m/%Y')
            corpo_msg = template.safe_substitute(nome=f'Ol?? {self.input_nome_destinatario}, Este ?? um email de testes!',
                                                nome_destinatario=self.input_nome_destinatario.text(),
                                                 data=data_atual,texto=self.getText(),
                                                 nomeremetente=self.input_nome_remetente.text())
            msg = MIMEMultipart()
            msg['from'] = self.input_nome_remetente.text()
            msg['to'] = self.input_email_destinatario.text()
            msg['subject'] = self.input_cabecalho.text()

            corpo = MIMEText(corpo_msg, 'html')
            msg.attach(corpo)

            with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
                try:
                    smtp.ehlo()
                    smtp.starttls()
                    smtp.login(self.email, self.password)
                    smtp.send_message(msg)
                    self.frame_error_email.setStyleSheet(self.styleGreen)
                    self.frame_error_email.show()
                    self.label_error_email.setText('E-mail enviado com sucesso!')
                except Exception as e:
                    self.frame_error_email.setStyleSheet(self.styleRed)
                    self.label_error_email.setText('Houve um erro ao enviar seu E-gmail.')
                    self.frame_error_email.show()
                    print(f'Erro: {e}')


    def getText(self):
        #transformar o texto da box em string
        text = self.text_box_conteudo.toPlainText()
        txtstring = str(text)
        return txtstring







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MailWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
