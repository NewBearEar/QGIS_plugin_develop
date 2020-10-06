# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'polygon_to_line_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Polygon2LineDialogBase(object):
    def setupUi(self, Polygon2LineDialogBase):
        Polygon2LineDialogBase.setObjectName("Polygon2LineDialogBase")
        Polygon2LineDialogBase.resize(505, 360)
        self.button_box = QtWidgets.QDialogButtonBox(Polygon2LineDialogBase)
        self.button_box.setGeometry(QtCore.QRect(110, 290, 341, 51))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.mMapLayerComboBox = QgsMapLayerComboBox(Polygon2LineDialogBase)
        self.mMapLayerComboBox.setGeometry(QtCore.QRect(60, 70, 331, 31))
        self.mMapLayerComboBox.setObjectName("mMapLayerComboBox")
        self.label = QtWidgets.QLabel(Polygon2LineDialogBase)
        self.label.setGeometry(QtCore.QRect(60, 40, 141, 20))
        self.label.setObjectName("label")
        self.pushButton_1 = QtWidgets.QPushButton(Polygon2LineDialogBase)
        self.pushButton_1.setGeometry(QtCore.QRect(410, 70, 41, 31))
        self.pushButton_1.setObjectName("pushButton_1")
        self.lineEdit = QtWidgets.QLineEdit(Polygon2LineDialogBase)
        self.lineEdit.setGeometry(QtCore.QRect(60, 140, 331, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Polygon2LineDialogBase)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 140, 41, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Polygon2LineDialogBase)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 141, 20))
        self.label_2.setObjectName("label_2")
        self.checkBox = QtWidgets.QCheckBox(Polygon2LineDialogBase)
        self.checkBox.setGeometry(QtCore.QRect(60, 190, 181, 26))
        self.checkBox.setObjectName("checkBox")
        self.startButton = QtWidgets.QPushButton(Polygon2LineDialogBase)
        self.startButton.setGeometry(QtCore.QRect(370, 190, 81, 31))
        self.startButton.setObjectName("startButton")
        self.progressBar = QtWidgets.QProgressBar(Polygon2LineDialogBase)
        self.progressBar.setGeometry(QtCore.QRect(60, 250, 391, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Polygon2LineDialogBase)
        self.button_box.accepted.connect(Polygon2LineDialogBase.accept)
        self.button_box.rejected.connect(Polygon2LineDialogBase.reject)
        QtCore.QMetaObject.connectSlotsByName(Polygon2LineDialogBase)

    def retranslateUi(self, Polygon2LineDialogBase):
        _translate = QtCore.QCoreApplication.translate
        Polygon2LineDialogBase.setWindowTitle(_translate("Polygon2LineDialogBase", "Polygon to Line"))
        self.label.setText(_translate("Polygon2LineDialogBase", "输入面状要素图层"))
        self.pushButton_1.setText(_translate("Polygon2LineDialogBase", "..."))
        self.pushButton_2.setText(_translate("Polygon2LineDialogBase", "..."))
        self.label_2.setText(_translate("Polygon2LineDialogBase", "输入线状要素图层"))
        self.checkBox.setText(_translate("Polygon2LineDialogBase", "完成后添加到项目"))
        self.startButton.setText(_translate("Polygon2LineDialogBase", "运行"))

from qgsmaplayercombobox import QgsMapLayerComboBox
