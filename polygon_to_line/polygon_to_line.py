# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Polygon2Line
                                 A QGIS plugin
 面转线工具，记录拓扑关系
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2020-09-28
        git sha              : $Format:%H$
        copyright            : (C) 2020 by Beamatch
        email                : 2017301110147@whu.edu.cn
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction, QPushButton, QFileDialog, QMessageBox, QLineEdit, QCheckBox, QProgressBar

# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .polygon_to_line_dialog import Polygon2LineDialog
import os.path
# import some useful module frome qgis.core
from qgis.core import (QgsProject,
                       QgsWkbTypes,
                       QgsMapLayer,
                       QgsFeature,
                       QgsMapLayerType, QgsPointXY, QgsVectorLayer, QgsGeometry, QgsVectorFileWriter,
                       QgsFeatureIterator)
import pydevd_pycharm
import networkx as nx
from collections import OrderedDict
import matplotlib.pyplot as plt


class Polygon2Line:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'Polygon2Line_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Polygon to Line')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

        # output file name
        self.outputFileName = None


    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('Polygon2Line', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/polygon_to_line/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'Polygon to Line Tool'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Polygon to Line'),
                action)
            self.iface.removeToolBarIcon(action)


    def run(self):
        """Run method that performs all the real work"""
        # 打开窗口算一次run
        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started
        if self.first_start == True:
            self.first_start = False
            self.dlg = Polygon2LineDialog()
            # 添加控件
            outputFileBtn = self.dlg.pushButton_2  # type:QPushButton
            startBtn = self.dlg.startButton  # type:QPushButton
            # 连接槽函数,只连接一次
            outputFileBtn.clicked.connect(self.openSaveFile)
            startBtn.clicked.connect(self.start)
        # 每次打开窗口初始化控件值
        self.dlg.lineEdit.setText('')
        self.outputFileName = None
        self.dlg.progressBar.setValue(0)
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.
            pass

    def startConvert(self,layer:QgsMapLayer):

        layerName = layer.name()
        nodeCoorDict = OrderedDict()
        graph = nx.Graph()

        if layerName:
            features_forCounts = layer.getFeatures()  # type:QgsFeatureIterator
            # 记录当前处理的polygon id编号
            plyId = 0
            count = 0
            feaNums = sum(1 for _ in features_forCounts)  #此时已经迭代过了

            features = layer.getFeatures()  # type:QgsFeatureIterator
            pbar = self.dlg.progressBar  # type:QProgressBar
            pbar.setRange(0, feaNums)
            print(feaNums)
            for feature in features:
                #if count >= 10:
                #    break
                geom = feature.geometry()
                geomSingleType = QgsWkbTypes.isSingleType(geom.wkbType())
                if geom.type() == QgsWkbTypes.PolygonGeometry:
                    if geomSingleType:
                        polygon = geom.asPolygon()
                        nodeCoorDict, graph = self.parsePolygon2Network(polygon, nodeCoorDict, graph, plyId=plyId)
                        plyId = plyId + 1
                    else:
                        multiPolygon = geom.asMultiPolygon()
                        for polygon in multiPolygon:
                            nodeCoorDict,graph = self.parsePolygon2Network(polygon,nodeCoorDict,graph,plyId=plyId)
                            plyId = plyId + 1
                pbar.setValue(count)
                count = count + 1
                #print("complete!")
        #plt.subplot(121)
        #print(nodeCoorDict)
        '''
        # 每个节点坐标，绘制带坐标的图
        pos = list(nodeCoorDict.values())
        #nx.draw(graph,pos, with_labels=True)
        nx.draw(graph, pos,node_size=20)
        nx.fruchterman_reingold_layout(graph)
        plt.show()
        '''
        print('all complete')
        pbar.setValue(feaNums)
        return nodeCoorDict,graph,True

    def parsePolygon2Network(self,polygon,nodeCoorDict,graph,plyId):
        #nodeCoorDict = {}
        # 记录图层是否刚被处理
        ply_first_parse = True
        nodeCount = len(nodeCoorDict)   # count充当添加时的id号
        lastNode = 0
        currNode = 0
        for conponent in polygon:
            # 记录某个组件是否刚被处理
            conponent_first_parse = True
            #print(conponent)
            # 判断多边形是否clockwise
            isPlyConClockWised = self.isPlyConClockWise(conponent)
            conponent_ptlist = []
            if not isPlyConClockWised:
                # 反转列表
                conponent_ptlist = conponent[::-1]

            else:
                conponent_ptlist = conponent
            #print(isPlyConClockWised)
            # 用于测试限制点数
            #ptCounts = 0
            # 暂时不考虑空洞和重叠多边形
            for point in conponent_ptlist:
                #print(point.x(), point.y())
                ptCoor = (point.x(),point.y())
                #if ptCounts > 80:
                #    break
                if ptCoor not in nodeCoorDict.values():
                    nodeCoorDict[nodeCount] = ptCoor
                    #test
                    graph.add_node(nodeCount)
                    nodeId = nodeCount
                    nodeCount = nodeCount+1
                else:
                    nodeIdList = self.get_key(nodeCoorDict,ptCoor)
                    # 简化操作默认取第一个
                    nodeId = nodeIdList[0]
                    #print(plyId,nodeId,ptCoor)
                # 当前节点
                currNode = nodeId

                # 只有第一个节点时不记录边,避免边错误连接
                # polygon第一次的时候，conponent必定为第一次
                #if ply_first_parse:
                #    ply_first_parse = False
                #    pass
                if conponent_first_parse:
                    conponent_first_parse = False
                    pass

                else:
                    now_edge = (lastNode,currNode,{'left':-1,'right':plyId})
                    if graph.has_edge(lastNode,currNode):
                        #print('重复边')
                        #print(graph.edges)
                        graph[lastNode][currNode]['left'] = plyId
                    else:
                        graph.add_edge(lastNode,currNode,left=-1,right=plyId)
                    #print("edge "+str(lastNode)+" to "+str(currNode))
                # 处理完毕，记录该节点为上一个节点
                lastNode = nodeId

                #ptCounts = ptCounts+1

        return nodeCoorDict,graph

    def get_key(self,dict, value):
        return [k for k, v in dict.items() if v == value]

    def isPlyConClockWise(self,plyConponent):
        # 寻找多边形必定为凸的位置（最大、最小横纵坐标位置）
        maxX = 0
        maxX_pos = 0
        count = 0
        for pt in plyConponent:
            if pt.x() > maxX:
                maxX = pt.x()
                maxX_pos = count
            count = count + 1
        pt2_pos = maxX_pos
        if 0==maxX_pos:
            # 如果在开始位置
            pt1_pos = len(plyConponent)-1-1
            pt3_pos = maxX_pos+1
        elif maxX_pos == len(plyConponent)-1:
            # 如果在结束位置
            pt1_pos = maxX_pos - 1
            pt3_pos = 0+1
        else:
            # 如果在中间
            pt1_pos = maxX_pos - 1
            pt3_pos = maxX_pos + 1
        # 判断多边形是否为顺时针
        pt1 = plyConponent[pt1_pos]  # type:QgsPointXY
        pt2 = plyConponent[pt2_pos]  # type:QgsPointXY
        pt3 = plyConponent[pt3_pos]  # type:QgsPointXY
        # 计算向量
        edgeVec1 = [pt2.x()-pt1.x(),pt2.y()-pt1.y()]
        edgeVec2 = [pt3.x()-pt2.x(),pt3.y()-pt2.y()]
        # 计算叉积
        crossProd = edgeVec1[0]*edgeVec2[1] - edgeVec1[1]*edgeVec2[0]
        if 0==crossProd:
            print('多边形可能有重合的两个点')
            return True
        elif crossProd > 0:
            return False
        else:
            return True

    def createNewLineLayerByGraph(self,graph:nx.Graph,nodeCoorDict,layerCRS):
        edgeList = graph.edges
        layerCRS_str = layerCRS.authid()
        uri = "LineString?crs="+layerCRS_str+"&field=id:integer&field=left:integer&field=right:integer"
        lineLayer = QgsVectorLayer(uri,"Polygon to Line layer",  "memory")
        lineDataProvider = lineLayer.dataProvider()
        count = 0
        for edge in edgeList:
            feature = QgsFeature()
            pt1_coor = nodeCoorDict[edge[0]]
            pt2_coor = nodeCoorDict[edge[1]]
            #print(graph[edge[0]][edge[1]])
            leftPly = graph[edge[0]][edge[1]]['left']
            rightPly = graph[edge[0]][edge[1]]['right']
            qgsPt1 = QgsPointXY(pt1_coor[0],pt1_coor[1])
            qgsPt2 = QgsPointXY(pt2_coor[0], pt2_coor[1])
            #print(qgsPt1,qgsPt2,leftPly,rightPly)
            feature.setGeometry(QgsGeometry.fromPolylineXY([qgsPt1,qgsPt2]))
            feature.setAttributes([count,leftPly,rightPly])
            # 向provider添加Features
            lineDataProvider.addFeatures([feature])
            count = count+1
        # 根据provider更改范围
        lineLayer.updateExtents()
        #print(lineLayer)
        testfeas = lineLayer.getFeatures()
        mLineEdit = self.dlg.lineEdit  # type:QLineEdit
        outputPath = mLineEdit.text()
        if not self.outputFileName:
            QMessageBox.warning(None, "can not save file", "保存路径不能为空")
            return None,False
        error = QgsVectorFileWriter.writeAsVectorFormat(lineLayer, outputPath, "UTF-8",
                                                        driverName="ESRI Shapefile")
        if error[0] == QgsVectorFileWriter.NoError:
            print("success again!")
        else:
            print(error)
        return lineLayer,True
        #for fet in testfeas:
        #    print("id:",fet.id(),fet.attributes(),fet.geometry().asPolyline())

    def openSaveFile(self):
        filename,_ = QFileDialog.getSaveFileName(caption='output file',directory='.',filter='shapefile(*.shp)')
        #print(filename)
        self.outputFileName = filename
        mLineEdit = self.dlg.lineEdit   # type:QLineEdit
        mLineEdit.setText(filename)
        #if not self.outputFileName:
        #    QMessageBox.warning(None,"can not save file","不能保存到选定文件")

    def start(self):
        mlCombobox = self.dlg.mMapLayerComboBox  # type:QgsMapLayerComboBox
        # pydevd_pycharm.settrace('localhost', port=53100, stdoutToServer=True, stderrToServer=True)
        curLy = mlCombobox.currentLayer()  # type:QgsMapLayer
        # print(self.startConvert(curLy))
        nodeCoorDict, graph, isConvertSuccessed = self.startConvert(curLy)
        # 图层坐标系
        layerCRS = curLy.crs()
        # print(layerCRS.authid())
        ply2lineLayer, isLayerCreateSuccessed = self.createNewLineLayerByGraph(graph, nodeCoorDict, layerCRS)
        # 将转换的图层添加到工程
        if isConvertSuccessed and isLayerCreateSuccessed:
            QMessageBox.information(None, 'Convert Successfully!', '面转线成功!')
        checkBox1 = self.dlg.checkBox  # type:QCheckBox
        if checkBox1.isChecked():
            QgsProject.instance().addMapLayer(ply2lineLayer)
        # print(graph.edges)