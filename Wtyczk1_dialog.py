# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Wtyczk1Dialog
                                 A QGIS plugin
 Wtyczk1
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-11
        git sha              : $Format:%H$
        copyright            : (C) 2023 by adamstan102@wp.pl
        email                : adamstan102@wp.pl
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
import math
import os

from qgis.PyQt import QtWidgets
from qgis.PyQt import uic
from qgis._core import QgsWkbTypes
from qgis.utils import iface

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'Wtyczk1_dialog_base.ui'))


class Wtyczk1Dialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(Wtyczk1Dialog, self).__init__(parent)
        self.setupUi(self)

        self.textBrowser_notice = self.textBrowser_komunikaty

        self.pushButton_Roz_H.clicked.connect(self.calculate_height_difference)
        self.pushButton_Pole.clicked.connect(self.calculate_area)

    def calculate_height_difference(self):
        active_layer = iface.activeLayer()

        self.is_valid_point_count()

        # Check if exactly 2 points are selected
        selected_features = active_layer.selectedFeatures()
        if len(selected_features) != 2:
            self.show_message("Musisz zaznaczyć dokładnie 2 punkty.")
            return


        height_difference = selected_features[1]['h_plevrf2007nh'] - selected_features[0]['h_plevrf2007nh']



        self.show_message(f"Różnica wysokości między punktami {selected_features[0]['id']}, {selected_features[1]['id']} wynosi: {round(height_difference, 3)} [m]")

    def calculate_area(self):

        self.is_valid_point_count()

        selected_layer = self.mMapLayerComboBox_warstwy.currentLayer()

        selected_features = selected_layer.selectedFeatures()
        if len(selected_features) < 3:
            self.show_message("Musisz zaznaczyć co najmniej 3 punkty.")
            return

        area, txt = self.calculate_area_using_gauss(selected_features)

        self.show_message(f"Pole powierzchni figury o wierzchołkach w punktach o numerach {', '.join(txt)} wynosi: {area} [m2]")

    def calculate_area_using_gauss(self, selected_features):
        sum1 = 0
        sum2 = 0
        txt = []

        for i, feature in enumerate(selected_features):
            geom = feature.geometry()
            if geom.type() != QgsWkbTypes.PointGeometry:
                continue

            point = geom.asPoint()
            x = point.x()
            y = point.y()
            txt.append(str(feature.id()))

            next_feature = selected_features[(i + 1) % len(selected_features)]
            prev_feature = selected_features[(i - 1) % len(selected_features)]
            next_geom = next_feature.geometry()
            prev_geom = prev_feature.geometry()

            if next_geom.type() != QgsWkbTypes.PointGeometry or prev_geom.type() != QgsWkbTypes.PointGeometry:
                continue

            next_point = next_geom.asPoint()
            prev_point = prev_geom.asPoint()

            sum1 += x * (next_point.y() - prev_point.y())
            sum2 += y * (next_point.x() - prev_point.x())

        if math.isclose(sum1, sum2, abs_tol=1e-9):
            self.show_message("Nie można obliczyć pola powierzchni.")

        area = 0.5 * math.fabs(sum1 - sum2)
        return round(area, 3), txt

    def show_message(self, message):
        iface.messageBar().pushMessage(message)
        self.textBrowser_notice.append(message)

    def is_valid_point_count(self):
        active_layer = iface.activeLayer()
        selected_features = active_layer.selectedFeatures()

        if len(selected_features) < 2 or selected_features is None:
            print(type(selected_features))
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Błąd")
            msg_box.setText("Musisz zaznaczyć więcej niż 1 punkt.")
            msg_box.exec_()
            return
