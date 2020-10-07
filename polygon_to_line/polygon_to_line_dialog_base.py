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
        Polygon2LineDialogBase.resize(711, 358)
        self.button_box = QtWidgets.QDialogButtonBox(Polygon2LineDialogBase)
        self.button_box.setGeometry(QtCore.QRect(20, 300, 401, 51))
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Help|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.mMapLayerComboBox = QgsMapLayerComboBox(Polygon2LineDialogBase)
        self.mMapLayerComboBox.setGeometry(QtCore.QRect(30, 60, 331, 31))
        self.mMapLayerComboBox.setObjectName("mMapLayerComboBox")
        self.label = QtWidgets.QLabel(Polygon2LineDialogBase)
        self.label.setGeometry(QtCore.QRect(30, 30, 141, 20))
        self.label.setObjectName("label")
        self.pushButton_1 = QtWidgets.QPushButton(Polygon2LineDialogBase)
        self.pushButton_1.setGeometry(QtCore.QRect(370, 60, 51, 31))
        self.pushButton_1.setObjectName("pushButton_1")
        self.lineEdit = QtWidgets.QLineEdit(Polygon2LineDialogBase)
        self.lineEdit.setGeometry(QtCore.QRect(30, 130, 331, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Polygon2LineDialogBase)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 130, 51, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Polygon2LineDialogBase)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 141, 20))
        self.label_2.setObjectName("label_2")
        self.checkBox = QtWidgets.QCheckBox(Polygon2LineDialogBase)
        self.checkBox.setGeometry(QtCore.QRect(30, 180, 181, 26))
        self.checkBox.setObjectName("checkBox")
        self.startButton = QtWidgets.QPushButton(Polygon2LineDialogBase)
        self.startButton.setGeometry(QtCore.QRect(340, 180, 81, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.progressBar = QtWidgets.QProgressBar(Polygon2LineDialogBase)
        self.progressBar.setGeometry(QtCore.QRect(30, 240, 391, 31))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.textBrowser = QtWidgets.QTextBrowser(Polygon2LineDialogBase)
        self.textBrowser.setGeometry(QtCore.QRect(440, 20, 251, 321))
        self.textBrowser.setObjectName("textBrowser")
        self.line = QtWidgets.QFrame(Polygon2LineDialogBase)
        self.line.setGeometry(QtCore.QRect(20, 10, 411, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Polygon2LineDialogBase)
        self.line_2.setGeometry(QtCore.QRect(10, 20, 20, 271))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Polygon2LineDialogBase)
        self.line_3.setGeometry(QtCore.QRect(20, 280, 411, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Polygon2LineDialogBase)
        self.line_4.setGeometry(QtCore.QRect(420, 20, 20, 271))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

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
        self.textBrowser.setHtml(_translate("Polygon2LineDialogBase", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Polygon to Line</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">面转线算法</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">通过构建无向图网络的方式，将面状要素转换为带属性的线状要素，并记录每条边的拓扑关系（左右面要素的ID号）。运行算法前请保证源数据不存在空洞、压盖等拓扑错误</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">By constructing undirected graph , the polygon features are transformed into polyline features with attributes, and the topological relationship of each edge (ID number of left and right face features) is recorded.Before running the algorithm, please ensure that the source data does not have topology errors such as holes and covers</p></body></html>"))

from qgsmaplayercombobox import QgsMapLayerComboBox
