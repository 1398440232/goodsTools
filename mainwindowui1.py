# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpinBox, QStatusBar, QTableWidget,
    QTableWidgetItem, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(804, 608)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit_search = QTextEdit(self.centralwidget)
        self.textEdit_search.setObjectName(u"textEdit_search")
        self.textEdit_search.setGeometry(QRect(40, 350, 451, 21))
        self.textEdit_search.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_info = QTableWidget(self.centralwidget)
        self.tableWidget_info.setObjectName(u"tableWidget_info")
        self.tableWidget_info.setGeometry(QRect(40, 30, 531, 311))
        self.tableWidget_info.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_info.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.tableWidget_info.setColumnCount(0)
        self.label_info_table = QLabel(self.centralwidget)
        self.label_info_table.setObjectName(u"label_info_table")
        self.label_info_table.setGeometry(QRect(40, 10, 61, 16))
        self.pushButton_keyword_search = QPushButton(self.centralwidget)
        self.pushButton_keyword_search.setObjectName(u"pushButton_keyword_search")
        self.pushButton_keyword_search.setGeometry(QRect(496, 350, 75, 21))
        self.tableWidget_jiesuan = QTableWidget(self.centralwidget)
        self.tableWidget_jiesuan.setObjectName(u"tableWidget_jiesuan")
        self.tableWidget_jiesuan.setGeometry(QRect(630, 30, 131, 311))
        self.tableWidget_jiesuan.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.pushButton_jiesuan_add = QPushButton(self.centralwidget)
        self.pushButton_jiesuan_add.setObjectName(u"pushButton_jiesuan_add")
        self.pushButton_jiesuan_add.setGeometry(QRect(575, 120, 51, 23))
        self.pushButton_remove = QPushButton(self.centralwidget)
        self.pushButton_remove.setObjectName(u"pushButton_remove")
        self.pushButton_remove.setGeometry(QRect(575, 190, 51, 23))
        self.label_jiesuan_table = QLabel(self.centralwidget)
        self.label_jiesuan_table.setObjectName(u"label_jiesuan_table")
        self.label_jiesuan_table.setGeometry(QRect(630, 10, 61, 16))
        self.pushButton_jiesuan = QPushButton(self.centralwidget)
        self.pushButton_jiesuan.setObjectName(u"pushButton_jiesuan")
        self.pushButton_jiesuan.setGeometry(QRect(686, 350, 75, 21))
        self.label_category = QLabel(self.centralwidget)
        self.label_category.setObjectName(u"label_category")
        self.label_category.setGeometry(QRect(40, 370, 61, 16))
        self.label_name = QLabel(self.centralwidget)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setGeometry(QRect(140, 370, 61, 16))
        self.label_price = QLabel(self.centralwidget)
        self.label_price.setObjectName(u"label_price")
        self.label_price.setGeometry(QRect(240, 370, 61, 16))
        self.label_spec = QLabel(self.centralwidget)
        self.label_spec.setObjectName(u"label_spec")
        self.label_spec.setGeometry(QRect(340, 370, 61, 16))
        self.label_remarks = QLabel(self.centralwidget)
        self.label_remarks.setObjectName(u"label_remarks")
        self.label_remarks.setGeometry(QRect(440, 370, 61, 16))
        self.label_img_url = QLabel(self.centralwidget)
        self.label_img_url.setObjectName(u"label_img_url")
        self.label_img_url.setGeometry(QRect(540, 370, 81, 16))
        self.lineEdit_category = QLineEdit(self.centralwidget)
        self.lineEdit_category.setObjectName(u"lineEdit_category")
        self.lineEdit_category.setGeometry(QRect(40, 390, 91, 21))
        self.lineEdit_name = QLineEdit(self.centralwidget)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setGeometry(QRect(140, 390, 91, 21))
        self.lineEdit_price = QLineEdit(self.centralwidget)
        self.lineEdit_price.setObjectName(u"lineEdit_price")
        self.lineEdit_price.setGeometry(QRect(240, 390, 91, 21))
        self.lineEdit_spec = QLineEdit(self.centralwidget)
        self.lineEdit_spec.setObjectName(u"lineEdit_spec")
        self.lineEdit_spec.setGeometry(QRect(340, 390, 91, 21))
        self.lineEdit_remarks = QLineEdit(self.centralwidget)
        self.lineEdit_remarks.setObjectName(u"lineEdit_remarks")
        self.lineEdit_remarks.setGeometry(QRect(440, 390, 91, 21))
        self.lineEdit_img_url = QLineEdit(self.centralwidget)
        self.lineEdit_img_url.setObjectName(u"lineEdit_img_url")
        self.lineEdit_img_url.setGeometry(QRect(540, 390, 131, 21))
        self.pushButton_info_add = QPushButton(self.centralwidget)
        self.pushButton_info_add.setObjectName(u"pushButton_info_add")
        self.pushButton_info_add.setGeometry(QRect(686, 390, 75, 21))
        self.pushButton_show_all = QPushButton(self.centralwidget)
        self.pushButton_show_all.setObjectName(u"pushButton_show_all")
        self.pushButton_show_all.setGeometry(QRect(580, 350, 91, 21))
        self.spinBox_add_quantity = QSpinBox(self.centralwidget)
        self.spinBox_add_quantity.setObjectName(u"spinBox_add_quantity")
        self.spinBox_add_quantity.setGeometry(QRect(575, 90, 51, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 804, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_keyword_search.clicked.connect(self.centralwidget.show)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8d27\u7269\u7ba1\u7406\u5de5\u5177", None))
        self.label_info_table.setText(QCoreApplication.translate("MainWindow", u"\u5546\u54c1\u4ef7\u683c\u8868", None))
        self.pushButton_keyword_search.setText(QCoreApplication.translate("MainWindow", u"\u5173\u952e\u8bcd\u641c\u7d22", None))
        self.pushButton_jiesuan_add.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0->", None))
        self.pushButton_remove.setText(QCoreApplication.translate("MainWindow", u"<-\u79fb\u9664", None))
        self.label_jiesuan_table.setText(QCoreApplication.translate("MainWindow", u"\u8d27\u7269\u7ed3\u7b97\u8868", None))
        self.pushButton_jiesuan.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u7b97", None))
        self.label_category.setText(QCoreApplication.translate("MainWindow", u"\u8d27\u7269\u79cd\u7c7b", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"\u8d27\u7269\u540d\u79f0", None))
        self.label_price.setText(QCoreApplication.translate("MainWindow", u"\u8d27\u7269\u4ef7\u683c", None))
        self.label_spec.setText(QCoreApplication.translate("MainWindow", u"\u8d27\u7269\u89c4\u683c", None))
        self.label_remarks.setText(QCoreApplication.translate("MainWindow", u"\u8d27\u7269\u5907\u6ce8", None))
        self.label_img_url.setText(QCoreApplication.translate("MainWindow", u"\u8d27\u7269\u56fe\u7247\u94fe\u63a5", None))
        self.pushButton_info_add.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.pushButton_show_all.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u5168\u90e8\u8d27\u7269", None))
    # retranslateUi

