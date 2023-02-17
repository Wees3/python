from PySide6 import QtWidgets
import sys
from datetime import date
from datetime import datetime
import webbrowser
import socket

import os
import platform
myOs = platform.system()
print(myOs)


today = date.today()


now = datetime.now()

current_time = now.strftime("%H:%M:%S")



class FormConnexion(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.resize(300,100)
        self.setWindowTitle("Quentin App")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        self.setup_connections()
        # self.main_widget()


    def create_layouts(self):
        self.layoutV = QtWidgets.QVBoxLayout()
        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()
        self.layoutH3 = QtWidgets.QHBoxLayout()
        self.layoutH4 = QtWidgets.QHBoxLayout()

    def create_widgets(self):
        self.lbl_Login = QtWidgets.QLabel("Login")
        self.LEdit_Login = QtWidgets.QLineEdit("quentin")
        self.LEdit_Login.setPlaceholderText("Saisir votre login")

        self.lbl_Password = QtWidgets.QLabel("Password")
        self.LEdit_Password = QtWidgets.QLineEdit("123")
        self.LEdit_Password.setPlaceholderText("Saisir votre mot de passe")
        self.LEdit_Password.setEchoMode(QtWidgets.QLineEdit.Password)

        self.btn_Valider = QtWidgets.QPushButton("Valider")
        self.btn_Quitter = QtWidgets.QPushButton("Quitter")

        self.lbl_Status = QtWidgets.QLabel("Status: Non connecté")

    def addWigets_to_layouts(self):
        self.layoutH1.addWidget(self.lbl_Login)
        self.layoutH1.addWidget(self.LEdit_Login)

        self.layoutH2.addWidget(self.lbl_Password)
        self.layoutH2.addWidget(self.LEdit_Password)

        self.layoutH3.addWidget(self.btn_Valider)
        self.layoutH3.addWidget(self.btn_Quitter)

        self.layoutH4.addWidget(self.lbl_Status)


        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.layoutH2)
        self.layoutV.addLayout(self.layoutH3)
        self.layoutV.addLayout(self.layoutH4)
        self.setLayout(self.layoutV)

    # def main_widget(self):
    #     self.widget = QtWidgets.QWidget(self)  
    #     self.widget.setLayout(self.layoutV)
    #     self.setCentralWidget(self.widget)
       
    def setup_connections(self):
        self.btn_Quitter.clicked.connect(quit)
        # self.btn_Effacer.clicked.connect(self.clear_Ledit)
        self.btn_Valider.clicked.connect(self.seConnceter)
         
    def clear_Ledit(self):
        self.LEdit_Login.setText("")
        self.LEdit_Password.setText("")

    def seConnceter(self):
        if self.LEdit_Login.text() =="quentin" and self.LEdit_Password.text() =="123":
            print("connecté")
            self.lbl_Status.setText('Status: Connecté')
            formConnect.hide()
            mainForm.show()

        else:
            print("Erreur de connexion")
            self.lbl_Status.setText('Status: Erreur de saisie')
            self.clear_Ledit()



class MyForm(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.resize(300,100)
        self.setWindowTitle("Quentin App")
        self.create_layouts()
        self.create_widgets()
        self.addWigets_to_layouts()
        self.setup_connections()
        # self.main_widget()


    def create_layouts(self):
        self.layoutV = QtWidgets.QVBoxLayout()
        self.layoutH1 = QtWidgets.QHBoxLayout()
        self.layoutH2 = QtWidgets.QHBoxLayout()
        self.layoutH3 = QtWidgets.QHBoxLayout()
        self.layoutH4 = QtWidgets.QHBoxLayout()

    def create_widgets(self):
        self.lbl_Login = QtWidgets.QLabel("Bonjour Quentin")
      

        self.lbl_Password = QtWidgets.QLabel(f"Today's date: {today} --- {current_time}" )
   

        self.btn_Valider = QtWidgets.QPushButton("Valider")
        self.btn_Quitter = QtWidgets.QPushButton("Quitter")

        self.lbl_Status = QtWidgets.QLabel(f"Connecté sur {myOs}")

    def addWigets_to_layouts(self):
        self.layoutH1.addWidget(self.lbl_Login)
     

        self.layoutH2.addWidget(self.lbl_Password)


        self.layoutH3.addWidget(self.btn_Valider)
        self.layoutH3.addWidget(self.btn_Quitter)

        self.layoutH4.addWidget(self.lbl_Status)


        self.layoutV.addLayout(self.layoutH1)
        self.layoutV.addLayout(self.layoutH2)
        self.layoutV.addLayout(self.layoutH3)
        self.layoutV.addLayout(self.layoutH4)
        self.setLayout(self.layoutV)

    # def main_widget(self):
    #     self.widget = QtWidgets.QWidget(self)  
    #     self.widget.setLayout(self.layoutV)
    #     self.setCentralWidget(self.widget)
       
    def setup_connections(self):
        self.btn_Quitter.clicked.connect(quit)
        self.btn_Valider.clicked.connect(self.lancerBrowser)
        # self.btn_Effacer.clicked.connect(self.clear_Ledit)
       
         
    # def clear_Ledit(self):
    #     self.LEdit_Login.setText("")
    #     self.LEdit_Password.setText("")
    def lancerBrowser(self):
        webbrowser.open("https://worldofwarcraft.blizzard.com/fr-fr/")

  
    

if __name__ == '__main__':
    # Create the Qt Application
    app = QtWidgets.QApplication([])
    # Create and show the form
    formConnect = FormConnexion()
    mainForm = MyForm()

    formConnect.show()
    mainForm.hide()
    
    # Run the main Qt loop
    sys.exit(app.exec())
    # app.exec()
