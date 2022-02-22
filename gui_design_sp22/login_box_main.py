# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 15:43:18 2022

@author: tuo27112
"""

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

from login_box import Ui_Form


#subclass your widget (QWidget). add functionality to this class
class LoginWindow(qtw.QWidget):
    
    def __init__(self, *args, **kwargs):
        #super gives reference to parent object (init method)
        #Passing any arguments that were passed in so this still behaves like a QWidget
        super(). __init__(*args, **kwargs)
        #your code will go here
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
         
        # self.ui.submit_button.clicked.connect(self.authenticate)
        
    # def authenticate(self):

    #     username = self.ui.username_edit.text()
    #     password = self.ui.password_edit.text()
        
    #     if username == 'user' and password == 'pass':
    #         qtw.QMessageBox.information(self, 'Success', "You logged in m8")
    #     else:
    #         qtw.QMessageBox.critical(self, 'Fail', 'No login for you')




if __name__ == '__main__':
    
  
    app = qtw.QApplication([])

    widget = LoginWindow()
    widget.show()
    
    app.exec_()


# -x just opens the widget, not necessary
#THIS GOES IN TERMINAL
#pyuic5 -x -o login_box.py login_box.ui

# self.submit_button



        
        
    