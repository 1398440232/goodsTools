# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'huowujiesuan.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.tableWidget_list = QTableWidget(Form)
        self.tableWidget_list.setObjectName(u"tableWidget_list")
        self.tableWidget_list.setGeometry(QRect(40, 20, 321, 111))
        self.tableWidget_list.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.tableWidget_list.setAlternatingRowColors(False)
        self.tableWidget_list.setColumnCount(0)
        self.label_jiesuan_list = QLabel(Form)
        self.label_jiesuan_list.setObjectName(u"label_jiesuan_list")
        self.label_jiesuan_list.setGeometry(QRect(40, 3, 53, 15))
        self.plainTextEdit_copy_area = QPlainTextEdit(Form)
        self.plainTextEdit_copy_area.setObjectName(u"plainTextEdit_copy_area")
        self.plainTextEdit_copy_area.setGeometry(QRect(40, 180, 321, 81))
        self.pushButton_shengcheng = QPushButton(Form)
        self.pushButton_shengcheng.setObjectName(u"pushButton_shengcheng")
        self.pushButton_shengcheng.setGeometry(QRect(310, 140, 51, 23))
        self.pushButton_copy = QPushButton(Form)
        self.pushButton_copy.setObjectName(u"pushButton_copy")
        self.pushButton_copy.setGeometry(QRect(310, 270, 51, 23))
        self.label_jiesuan_shengcheng = QLabel(Form)
        self.label_jiesuan_shengcheng.setObjectName(u"label_jiesuan_shengcheng")
        self.label_jiesuan_shengcheng.setGeometry(QRect(40, 160, 53, 15))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8d27\u7269\u7ed3\u7b97\u4fe1\u606f", None))
        self.label_jiesuan_list.setText(QCoreApplication.translate("Form", u"\u6e05\u5355", None))
        self.pushButton_shengcheng.setText(QCoreApplication.translate("Form", u"\u751f\u6210", None))
        self.pushButton_copy.setText(QCoreApplication.translate("Form", u"\u590d\u5236", None))
        self.label_jiesuan_shengcheng.setText(QCoreApplication.translate("Form", u"\u751f\u6210\u4fe1\u606f", None))
    # retranslateUi

