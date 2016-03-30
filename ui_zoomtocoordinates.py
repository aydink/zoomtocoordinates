# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_zoomtocoordinates.ui'
#
# Created: Wed Mar 30 22:22:28 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ZoomToCoordinates(object):
    def setupUi(self, ZoomToCoordinates):
        ZoomToCoordinates.setObjectName(_fromUtf8("ZoomToCoordinates"))
        ZoomToCoordinates.setWindowModality(QtCore.Qt.WindowModal)
        ZoomToCoordinates.resize(338, 120)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ZoomToCoordinates.sizePolicy().hasHeightForWidth())
        ZoomToCoordinates.setSizePolicy(sizePolicy)
        ZoomToCoordinates.setMinimumSize(QtCore.QSize(338, 120))
        ZoomToCoordinates.setMaximumSize(QtCore.QSize(338, 120))
        ZoomToCoordinates.setIconSize(QtCore.QSize(16, 16))
        ZoomToCoordinates.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        ZoomToCoordinates.setTabShape(QtGui.QTabWidget.Rounded)
        self.centralwidget = QtGui.QWidget(ZoomToCoordinates)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 310, 29))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.mTxtX = QtGui.QLineEdit(self.layoutWidget)
        self.mTxtX.setObjectName(_fromUtf8("mTxtX"))
        self.horizontalLayout.addWidget(self.mTxtX)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.mTxtY = QtGui.QLineEdit(self.layoutWidget)
        self.mTxtY.setObjectName(_fromUtf8("mTxtY"))
        self.horizontalLayout.addWidget(self.mTxtY)
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 44, 311, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.txtMGRS = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.txtMGRS.setObjectName(_fromUtf8("txtMGRS"))
        self.horizontalLayout_2.addWidget(self.txtMGRS)
        ZoomToCoordinates.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(ZoomToCoordinates)
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        ZoomToCoordinates.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.mActionZoomTo = QtGui.QAction(ZoomToCoordinates)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/zoom.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mActionZoomTo.setIcon(icon)
        self.mActionZoomTo.setObjectName(_fromUtf8("mActionZoomTo"))
        self.mActionPan = QtGui.QAction(ZoomToCoordinates)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/pan.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mActionPan.setIcon(icon1)
        self.mActionPan.setObjectName(_fromUtf8("mActionPan"))
        self.mActionFlash = QtGui.QAction(ZoomToCoordinates)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/flash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mActionFlash.setIcon(icon2)
        self.mActionFlash.setObjectName(_fromUtf8("mActionFlash"))
        self.toolBar.addAction(self.mActionZoomTo)
        self.toolBar.addAction(self.mActionPan)
        self.toolBar.addAction(self.mActionFlash)

        self.retranslateUi(ZoomToCoordinates)
        QtCore.QMetaObject.connectSlotsByName(ZoomToCoordinates)

    def retranslateUi(self, ZoomToCoordinates):
        ZoomToCoordinates.setWindowTitle(_translate("ZoomToCoordinates", "Zoom To Coordinates", None))
        self.label.setText(_translate("ZoomToCoordinates", "X:", None))
        self.label_2.setText(_translate("ZoomToCoordinates", "Y:", None))
        self.label_3.setText(_translate("ZoomToCoordinates", "MGRS", None))
        self.toolBar.setWindowTitle(_translate("ZoomToCoordinates", "toolBar", None))
        self.mActionZoomTo.setText(_translate("ZoomToCoordinates", "ZoomTo", None))
        self.mActionZoomTo.setToolTip(_translate("ZoomToCoordinates", "Zoom To Point", None))
        self.mActionPan.setText(_translate("ZoomToCoordinates", "Pan", None))
        self.mActionPan.setToolTip(_translate("ZoomToCoordinates", "Pan To", None))
        self.mActionFlash.setText(_translate("ZoomToCoordinates", "Flash", None))
        self.mActionFlash.setToolTip(_translate("ZoomToCoordinates", "Flash Point", None))

import resources_rc
