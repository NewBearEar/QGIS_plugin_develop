# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MyPluginTest1
                                 A QGIS plugin
 test my env
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2020-09-22
        git sha              : $Format:%H$
        copyright            : (C) 2020 by xjs147
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
#import pydevd_pycharm
import qgis._core
import qgis.core
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.core import QgsWkbTypes,QgsMapLayer
from qgis.core import QgsFeature, QgsProject, QgsMapLayerType
from qgis.PyQt.QtGui import QIcon
from qgis.gui import QgisInterface,QgsMapLayerComboBox
from qgis.PyQt.QtWidgets import QAction
from qgis.PyQt.QtWidgets import QFileDialog
from qgis.core import QgsGeometry

# Initialize Qt resources from file resources.py
from .resources import *
# Import the code for the dialog
from .xjsplugin_dialog import MyPluginTest1Dialog
import os.path
import networkx as nx
from collections import OrderedDict
import matplotlib.pyplot as plt


class MyPluginTest1:
    """QGIS Plugin Implementation."""

    def __init__(self, iface:QgisInterface):
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
            'MyPluginTest1_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&MyPluginTest1')

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None

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
        return QCoreApplication.translate('MyPluginTest1', message)

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

        icon_path = ':/plugins/xjsplugin/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'MyPluginTest1'),
            callback=self.run,
            parent=self.iface.mainWindow())

        # will be set False in run()
        self.first_start = True

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&MyPluginTest1'),
                action)
            self.iface.removeToolBarIcon(action)

    def run(self):
        """Run method that performs all the real work"""

        # Create the dialog with elements (after translation) and keep reference
        # Only create GUI ONCE in callback, so that it will only load when the plugin is started
        if self.first_start == True:
            self.first_start = False
            self.dlg = MyPluginTest1Dialog()  # type:MyPluginTest1Dialog


        # show the dialog
        self.dlg.show()
        # 图层选择框
        mlCombobox = self.dlg.mMapLayerComboBox  # type:QgsMapLayerComboBox

        # define my signal
        self.dlg.pushButton.clicked.connect(self.tj)
        
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code. 此处是窗口确定之后执行的代码
            # pydevd_pycharm.settrace('localhost', port=53100, stdoutToServer=True, stderrToServer=True)
            curLy = mlCombobox.currentLayer()
            #print(self.startConvert(curLy))
            self.startConvert(curLy)
            pass

    def tj(self):
        from qgis.core import QgsProject
        '''
        project = QgsProject.instance()  #type:QgsProject
        # project.read('/media/bear/NEW/学习2/2020年GIS实习/GIS实习插件开发/develop_test.qgz')
        # project.clear()
        #file_name = QFileDialog.getOpenFileName(None,caption=self.tr("open file dialog"), directory='/home/bear',
        #                                        filter=self.tr('shapefile(*.shp)'))
        layers = QgsProject.instance().mapLayers()
        for la in layers:   # type:QgsMapLayer
            pass

        l = [layer.name() for layer in layers.values()]

        activeLayer = self.iface.activeLayer()
        features = activeLayer.getFeatures()
        '''
        #pydevd_pycharm.settrace('localhost', port=53100, stdoutToServer=True, stderrToServer=True)


        project = QgsProject.instance()  # type:QgsProject
        maplayers = project.mapLayers()

        '''
        vecMapLayerDict = {}
        for layerObj in maplayers.values():  # type:QgsMapLayer
            if layerObj.type() == QgsMapLayerType.VectorLayer:
                layerName = layerObj.name()
                vecMapLayerDict[layerName] = layerObj
                if layerName == 'DLTB':
                    features = layerObj.getFeatures()
                    count = 0
                    for feature in features:
                        if count > 10:
                            break
                        geom = feature.geometry()
                        geomSingleType = QgsWkbTypes.isSingleType(geom.wkbType())
                        if geom.type() == QgsWkbTypes.PolygonGeometry:
                            if geomSingleType:
                                p = geom.asPolygon()

                            else:
                                multiPolygon = geom.asMultiPolygon()
                                for polygon in multiPolygon:
                                    self.parsePolygon(polygon)
                        count = count + 1

        print(vecMapLayerDict)
        '''

        '''
        for feature in features:  # type:QgsFeature
            # 检索每一个要素的几何形状和属性
            
            print("Feature ID: ", feature.id())
            # 获取几何
            geom = feature.geometry()
            geomSingleType = QgsWkbTypes.isSingleType(geom.wkbType())
            if geom.type() == QgsWkbTypes.PointGeometry:
                # 几何类型可以是单个或多个类型，
                if geomSingleType:
                    x = geom.asPoint()
                    print("Point: ", x)
                else:
                    x = geom.asMultiPoint()
                    print("MultiPoint: ", x)
            elif geom.type() == QgsWkbTypes.LineGeometry:
                if geomSingleType:
                    x = geom.asPolyline()
                    print("Line: ", x, "length: ", geom.length())
                else:
                    x = geom.asMultiPolyline()
                    print("MultiLine: ", x, "length: ", geom.length())
            elif geom.type() == QgsWkbTypes.PolygonGeometry:
                if geomSingleType:
                    x = geom.asPolygon()
                    print("Polygon: ", x, "Area: ", geom.area())
                else:
                    x = geom.asMultiPolygon()
                    print("MultiPolygon: ", x, "Area: ", geom.area())
            else:
                print("Unknown or invalid geometry")
            # 获取属性
            attrs = feature.attributes()
            # attrs是一个列表。它包含要素的所有属性值
            print(attrs)
        '''


        # 获取矢量图层字典
    def getProjectVecMapLayerDict(self):
        project = QgsProject.instance()  # type:QgsProject
        maplayers = project.mapLayers()
        vecMapLayerDict = {}
        for layerObj in maplayers.values():  # type:QgsMapLayer
            if layerObj.type() == QgsMapLayerType.VectorLayer:
                layerName = layerObj.name()
                vecMapLayerDict[layerName] = layerObj
        return vecMapLayerDict


    def parsePolygon2Network(self,polygon,nodeCoorDict,graph):
        #nodeCoorDict = {}
        nodeCount = len(nodeCoorDict)   # count充当添加时的id号
        for conponent in polygon:
            #print(conponent)
            for point in conponent:
                #print(point.x(), point.y())
                ptCoor = (point.x(),point.y())
                if ptCoor not in nodeCoorDict.values():
                    nodeCoorDict[nodeCount] = ptCoor
                    graph.add_node(nodeCount)
                    nodeCount = nodeCount+1
                else:
                    nodeId = self.get_key(nodeCoorDict,ptCoor)
                    print(nodeId,ptCoor)
        return nodeCoorDict


    def startConvert(self,layer:QgsMapLayer):

        layerName = layer.name()
        nodeCoorDict = OrderedDict()
        graph = nx.Graph()
        if layerName:
            features = layer.getFeatures()
            count = 0
            for feature in features:
                if count > 10:
                    break
                geom = feature.geometry()
                geomSingleType = QgsWkbTypes.isSingleType(geom.wkbType())
                if geom.type() == QgsWkbTypes.PolygonGeometry:
                    if geomSingleType:
                        polygon = geom.asPolygon()
                    else:
                        multiPolygon = geom.asMultiPolygon()
                        for polygon in multiPolygon:
                            nodeCoorDict = self.parsePolygon2Network(polygon,nodeCoorDict,graph)
                count = count + 1
        '''
        plt.subplot(121)
        nx.draw(graph, with_labels=True, font_weight='bold')
        plt.show()
        '''
        return nodeCoorDict

    def get_key(self,dict, value):
        return [k for k, v in dict.items() if v == value]
