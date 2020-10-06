# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xjsplugin_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MyPluginTest1DialogBase(object):
    def setupUi(self, MyPluginTest1DialogBase):
        MyPluginTest1DialogBase.setObjectName("MyPluginTest1DialogBase")
        MyPluginTest1DialogBase.resize(400, 300)
        self.button_box = QtWidgets.QDialogButtonBox(MyPluginTest1DialogBase)
        self.button_box.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.pushButton = QtWidgets.QPushButton(MyPluginTest1DialogBase)
        self.pushButton.setGeometry(QtCore.QRect(280, 80, 100, 28))
        self.pushButton.setObjectName("pushButton")
        self.mMapLayerComboBox = QgsMapLayerComboBox(MyPluginTest1DialogBase)
        self.mMapLayerComboBox.setGeometry(QtCore.QRect(30, 80, 221, 31))
        self.mMapLayerComboBox.setObjectName("mMapLayerComboBox")

        self.retranslateUi(MyPluginTest1DialogBase)
        self.button_box.accepted.connect(MyPluginTest1DialogBase.accept)
        self.button_box.rejected.connect(MyPluginTest1DialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(MyPluginTest1DialogBase)

    def retranslateUi(self, MyPluginTest1DialogBase):
        _translate = QtCore.QCoreApplication.translate
        MyPluginTest1DialogBase.setWindowTitle(_translate("MyPluginTest1DialogBase", "MyPluginTest1"))
        self.pushButton.setText(_translate("MyPluginTest1DialogBase", "TestButton"))

from qgsmaplayercombobox import QgsMapLayerComboBox
