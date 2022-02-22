# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_box.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.username_input = QtWidgets.QLineEdit(Form)
        self.username_input.setObjectName("username_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.username_input)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.password_input = QtWidgets.QLineEdit(Form)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.password_input)
        self.cancel_button = QtWidgets.QPushButton(Form)
        self.cancel_button.setObjectName("cancel_button")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cancel_button)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pushButton_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Log In!"))
        self.label_2.setText(_translate("Form", "Username"))
        self.label_3.setText(_translate("Form", "Password"))
        self.cancel_button.setText(_translate("Form", "Login"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))
