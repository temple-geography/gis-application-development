# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 19:51:02 2022

@author: tuo27112
"""

import sys

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

# input into terminal after creating ui file in qt designer:
# pyuic5 login_box.ui -o login_box.py

#subclass your widget (QWidget). add functionality to this class
class MainWindow(qtw.QWidget):
    
    def __init__(self, *args, **kwargs):
        # super gives reference to parent object (init method)
        # Passing any arguments that were passed in so this still behaves like a QWidget
        super(). __init__(*args, **kwargs)
        #your code will go here
        
        # your code ends here
        self.show()


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    w = MainWindow()
    app.exec_()