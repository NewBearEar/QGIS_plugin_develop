# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MyPluginTest1
                                 A QGIS plugin
 test my env
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-09-22
        copyright            : (C) 2020 by xjs147
        email                : 2017301110147@whu.edu.cn
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load MyPluginTest1 class from file MyPluginTest1.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .xjsplugin import MyPluginTest1
    return MyPluginTest1(iface)