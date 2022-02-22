# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 19:51:02 2022

@author: tuo27112
"""

import sys

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


# subclass your widget (QWidget). add functionality to this class
class MainWindow(qtw.QWidget):
    

    
    def __init__(self, *args, **kwargs):
        # super gives reference to parent object (init method)
        # Passing any arguments that were passed in so this still behaves like a QWidget
        super(). __init__(*args, **kwargs)
        #your code will go here
        #self. is used when we want to access these methods outside of the init method
        self.username_input = qtw.QLineEdit()
        self.password_input = qtw.QLineEdit()
        self.password_input.setEchoMode(qtw.QLineEdit.Password)
        
        self.cancel_button = qtw.QPushButton('Cancel')
        self.submit_button = qtw.QPushButton('Login')
        
        layout = qtw.QFormLayout()
        layout.addRow('Username', self.username_input)
        layout.addRow('Password', self.password_input)
        
        button_widget = qtw.QWidget()
        button_widget.setLayout(qtw.QHBoxLayout())
        button_widget.layout().addWidget(self.cancel_button)
        button_widget.layout().addWidget(self.submit_button)
        layout.addRow("", button_widget)
        self.setLayout(layout) 

        self.cancel_button.clicked.connect(self.close)
        
        
        self.username_input.textChanged.connect(self.set_button_text)



        # your code ends here
        self.show()
        
    # decorator adds small speed boost and type safety (making sure the right data 
    #types are being sent to the function)
    # this method sends the text from the line edit (in this case, username_input)
    #to the submit button
    @qtc.pyqtSlot(str)    
    def set_button_text(self, text):
        
        if text:
            self.submit_button.setText(f'Log In {text}')
        else:
            self.submit_button.setText('Log In')




if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())