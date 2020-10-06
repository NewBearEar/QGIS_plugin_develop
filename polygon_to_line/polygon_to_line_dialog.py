# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Polygon2LineDialog
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

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
from qgis._core import QgsMapLayerProxyModel

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'polygon_to_line_dialog_base.ui'))


class Polygon2LineDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(Polygon2LineDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        # 对控件进行一些初始配置
        self.mMapLayerComboBox.setShowCrs(True)
        self.mMapLayerComboBox.setFilters(QgsMapLayerProxyModel.PolygonLayer)
        self.checkBox.setChecked(True)
        self.progressBar.setValue(0)