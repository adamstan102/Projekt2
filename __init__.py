# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Wtyczk1
                                 A QGIS plugin
 Wtyczk1
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-11
        copyright            : (C) 2023 by adamstan102@wp.pl
        email                : adamstan102@wp.pl
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
    """Load Wtyczk1 class from file Wtyczk1.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Wtyczk1 import Wtyczk1
    return Wtyczk1(iface)