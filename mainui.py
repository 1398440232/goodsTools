# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys,clipboard 
from dbapi import dbprocess
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHeaderView, QLabel,QPlainTextEdit,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableWidget, QSpinBox,QTableWidgetItem,QDialog, QMessageBox ,
    QTextEdit, QWidget)


class Ui_Form(QDialog):
    def __init__(self):  
        super().__init__()  
        self.db = dbprocess()
        self.connection = self.db.dbconnect()
        self.data_list = []
        #self.setupUi(self)  
        
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.tableWidget_list = QTableWidget(Form)
        self.tableWidget_list.setObjectName(u"tableWidget_list")
        self.tableWidget_list.setGeometry(QRect(40, 20, 321, 111))
        self.tableWidget_list.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.tableWidget_list.setAlternatingRowColors(False)
        self.tableWidget_list.setColumnCount(4)
        self.tableWidget_list.setHorizontalHeaderLabels(['名称', '价格', '数量','规格'])  # 设置列标题  
        
        self.tableWidget_list.setRowCount(len(self.data_list))   
        # 填充QTableWidget  
        for row_index, row_data in enumerate(self.data_list):  
            for column_index, column_data in enumerate(row_data):  
                # 创建一个新的QTableWidgetItem，并设置其文本  
                item = QTableWidgetItem(str(column_data))  
                # 将item添加到表格的指定位置  
                self.tableWidget_list.setItem(row_index, column_index, item)  
        self.tableWidget_list.resizeColumnsToContents() # 自动调整列宽
        self.tableWidget_list.setEditTriggers(QAbstractItemView.NoEditTriggers)
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
        #button bind
        self.pushButton_shengcheng.clicked.connect(self.func_pushButton_shengcheng)
        self.pushButton_copy.clicked.connect(self.func_pushButton_copy)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)


    # func button
    def func_pushButton_shengcheng(self):
        message = ''
        total_price = 0
        for i in self.data_list:
            total_price = total_price + float(i[1])*int(i[2])
            message = message + (i[0] +' '+ i[3] + ' ' + i[2] + '件 ' + str(float(i[1])*int(i[2])) + '元' + '\n')
        message = message + '一共' + str(total_price) + '元'
        self.plainTextEdit_copy_area.appendPlainText(message) 
    def func_pushButton_copy(self):
        content = self.plainTextEdit_copy_area.toPlainText()
        clipboard.copy(content)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8d27\u7269\u7ed3\u7b97\u4fe1\u606f", None))
        self.label_jiesuan_list.setText(QCoreApplication.translate("Form", u"\u6e05\u5355", None))
        self.pushButton_shengcheng.setText(QCoreApplication.translate("Form", u"\u751f\u6210", None))
        self.pushButton_copy.setText(QCoreApplication.translate("Form", u"\u590d\u5236", None))
        self.label_jiesuan_shengcheng.setText(QCoreApplication.translate("Form", u"\u751f\u6210\u4fe1\u606f", None))
    # retranslateUi






class Ui_MainWindow(object):
    def __init__(self) -> None:
        self.db = dbprocess()
    def loadData(self):
        self.connection = self.db.dbconnect()
        try:  
            with self.connection.cursor() as cursor:  
                # 执行SQL查询  
                sql = "SELECT category, name, price, spec, remarks, modified_date, previous_price, image_url, id FROM goods.goods;"  # category, name, price, spec, remarks,  modified_date,previous_price, image_url
                cursor.execute(sql)  
  
                # 获取查询结果  
                results = cursor.fetchall()  
                # 设置QTableWidget的行数  
                self.tableWidget_info.setRowCount(len(results))  
  
                # 填充QTableWidget  
                for row_number, row_data in enumerate(results):  
                    for column_number, (column_name, data) in enumerate(row_data.items()):  
                        item = QTableWidgetItem(str(data))  # 将数据转换为字符串并添加到QTableWidgetItem  
                        self.tableWidget_info.setItem(row_number, column_number, item)  
        except Exception as e:
            print(str(e))
        finally:  
            self.connection.close() 
    def getData(self):
        self.connection = self.db.dbconnect()
        try:  
            with self.connection.cursor() as cursor:  
                # 执行SQL查询  
                sql = "SELECT category, name, price, spec, remarks, modified_date, previous_price, image_url, id FROM goods.goods;"  # category, name, price, spec, remarks,  modified_date,previous_price, image_url
                cursor.execute(sql)  
                results = cursor.fetchall()  
                return results
        except Exception as e:
            print(str(e))
        finally:  
            self.connection.close() 
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1032, 608)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit_search = QTextEdit(self.centralwidget)
        self.textEdit_search.setObjectName(u"textEdit_search")
        self.textEdit_search.setGeometry(QRect(40, 350, 451, 21))
        self.textEdit_search.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # 商品价格表
        self.tableWidget_info = QTableWidget(self.centralwidget)
        self.tableWidget_info.setObjectName(u"tableWidget_info")
        self.tableWidget_info.setGeometry(QRect(40, 30, 531, 311))
        self.tableWidget_info.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.tableWidget_info.setColumnCount(9)
        self.tableWidget_info.setHorizontalHeaderLabels(['种类', '名称', '价格', '规格', '备注', '上次修改时间', '之前价格', '图片url', '数据编号'])  # 设置列标题  
        self.loadData()
        self.tableWidget_info.resizeColumnsToContents() # 自动调整列宽
        
        # 
        self.label_info_table = QLabel(self.centralwidget)
        self.label_info_table.setObjectName(u"label_info_table")
        self.label_info_table.setGeometry(QRect(40, 10, 61, 16))
        self.pushButton_keyword_search = QPushButton(self.centralwidget)
        self.pushButton_keyword_search.setObjectName(u"pushButton_keyword_search")
        self.pushButton_keyword_search.setGeometry(QRect(496, 350, 75, 21))

        self.pushButton_showallgoods = QPushButton(self.centralwidget)
        self.pushButton_showallgoods.setObjectName(u"pushButton_showallgoods")
        self.pushButton_showallgoods.setGeometry(QRect(580, 350, 91, 21))
        #结算表
        self.tableWidget_jiesuan = QTableWidget(self.centralwidget)
        self.tableWidget_jiesuan.setObjectName(u"tableWidget_jiesuan")
        self.tableWidget_jiesuan.setGeometry(QRect(630, 30, 351, 311))
        self.tableWidget_jiesuan.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.tableWidget_jiesuan.setColumnCount(4)
        self.tableWidget_jiesuan.setHorizontalHeaderLabels(['名称', '价格', '数量','规格'])  # 设置列标题  
        self.tableWidget_jiesuan.resizeColumnsToContents() # 自动调整列宽
        #结算添加按钮
        self.pushButton_jiesuan_add = QPushButton(self.centralwidget)
        self.pushButton_jiesuan_add.setObjectName(u"pushButton_jiesuan_add")
        self.pushButton_jiesuan_add.setGeometry(QRect(575, 120, 51, 23))
        self.pushButton_remove = QPushButton(self.centralwidget)
        self.pushButton_remove.setObjectName(u"pushButton_remove")
        self.pushButton_remove.setGeometry(QRect(575, 190, 51, 23))
        self.label_jiesuan_table = QLabel(self.centralwidget)
        self.label_jiesuan_table.setObjectName(u"label_jiesuan_table")
        self.label_jiesuan_table.setGeometry(QRect(630, 10, 61, 16))
        #结算
        self.pushButton_jiesuan = QPushButton(self.centralwidget)
        self.pushButton_jiesuan.setObjectName(u"pushButton_jiesuan")
        self.pushButton_jiesuan.setGeometry(QRect(686, 350, 75, 21))
        #清空
        self.pushButton_jiesuan_clear = QPushButton(self.centralwidget)
        self.pushButton_jiesuan_clear.setObjectName(u"pushButton_jiesuan_clear")
        self.pushButton_jiesuan_clear.setGeometry(QRect(686, 370, 75, 21))
        #种类标签
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
        #数据添加
        self.pushButton_info_add = QPushButton(self.centralwidget)
        self.pushButton_info_add.setObjectName(u"pushButton_info_add")
        self.pushButton_info_add.setGeometry(QRect(686, 390, 75, 21))
        #数据删除
        self.pushButton_delete = QPushButton(self.centralwidget)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setGeometry(QRect(770, 390, 75, 21))
        #数据修改
        self.pushButton_modify = QPushButton(self.centralwidget)
        self.pushButton_modify.setObjectName(u"pushButton_modify")
        self.pushButton_modify.setGeometry(QRect(686, 410, 75, 21))
        #
        self.spinBox_add_quantity = QSpinBox(self.centralwidget)
        self.spinBox_add_quantity.setObjectName(u"spinBox_add_quantity")
        self.spinBox_add_quantity.setGeometry(QRect(575, 156, 51, 23))
        self.spinBox_add_quantity.setMinimum(1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #button bind
        self.pushButton_jiesuan.clicked.connect(self.func_pushButton_jiesuan) 
        self.pushButton_showallgoods.clicked.connect(self.func_pushButton_showallgoods) 
        self.pushButton_keyword_search.clicked.connect(self.func_pushButton_keyword_search)
        self.pushButton_info_add.clicked.connect(self.func_pushButton_info_add)
        self.pushButton_jiesuan_add.clicked.connect(self.func_pushButton_jiesuan_add)
        self.pushButton_jiesuan_clear.clicked.connect(self.func_pushButton_jiesuan_clear)
        self.pushButton_remove.clicked.connect(self.func_pushButton_remove)
        self.pushButton_delete.clicked.connect(self.func_pushButton_delete)
        self.pushButton_modify.clicked.connect(self.func_pushButton_modify)
        # 翻译转换
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        
    # func button
    def func_pushButton_jiesuan(self,):
        all_content = []  
        for row in range(self.tableWidget_jiesuan.rowCount()):  
            row_data = []  
            for col in range(self.tableWidget_jiesuan.columnCount()):  
                item = self.tableWidget_jiesuan.item(row, col)  
                if item is not None:  
                    row_data.append(item.text())  
                else:  
                    row_data.append("")  # 或者其他默认值  
            all_content.append(row_data)
        popup = Ui_Form()  
        popup.data_list = all_content
        popup.setupUi(popup)
        popup.exec()  # 使用exec()显示模态对话框，或者show()显示非模态窗口  

    def func_pushButton_showallgoods(self,):
        self.loadData()
        self.tableWidget_info.resizeColumnsToContents()

    def func_pushButton_keyword_search(self):
        search_term = self.textEdit_search.toPlainText()
        results = self.getData()
        filtered_data = [row for row in results if any(search_term.lower() in str(value).lower() for value in row.values())]
        # 填充QTableWidget  
        self.tableWidget_info.clearContents() 
        for row_number, row_data in enumerate(filtered_data):  
            for column_number, (column_name, data) in enumerate(row_data.items()): 
                item = QTableWidgetItem(str(data))  # 将数据转换为字符串并添加到QTableWidgetItem 
                self.tableWidget_info.setItem(row_number, column_number, item)  
    def func_pushButton_info_add(self,):
        self.connection = self.db.dbconnect()
        category = None if not self.lineEdit_category.text() else self.lineEdit_category.text()
        name = None if not self.lineEdit_name.text() else self.lineEdit_name.text()
        price = None if not self.lineEdit_price.text() else self.lineEdit_price.text()
        spec = None if not self.lineEdit_spec.text() else self.lineEdit_spec.text()
        remarks = None if not self.lineEdit_remarks.text() else self.lineEdit_remarks.text()
        image_url = None if not self.lineEdit_img_url.text() else self.lineEdit_img_url.text()
        previous_price = None # 不知道咋写
        self.db.adddata(self.connection,category=category,name=name,price=price,spec=spec,remarks=remarks,image_url=image_url,previous_price=previous_price)
        self.func_pushButton_showallgoods()
    
    def func_pushButton_jiesuan_add(self,):
        items= self.tableWidget_info.selectedItems()
        for item in items:
            if item.column() == 1:  # 检查列索引是否为第二列（索引为1）  
                item_name = item.text() # 货物名称
            if item.column() == 2:
                item_price = item # 价格
            if item.column() == 3:# 规格
                item_spec = item
        quantity = self.spinBox_add_quantity.value()
        data = [
            [item_name,item_price,str(quantity),item_spec]
        ]
        for row_data in data:  
            row_count = self.tableWidget_jiesuan.rowCount()  # 获取当前行数  
            self.tableWidget_jiesuan.insertRow(row_count)  # 插入新行  
  
            # 遍历行数据，将每个属性值设置到对应的单元格中  
            for column, value in enumerate(row_data):  
                item = QTableWidgetItem(value)  # 创建表格项  
                self.tableWidget_jiesuan.setItem(row_count, column, item)  # 设置单元格内容  
        if row_count >= 1:
            self.mergeRows()
        # 设置表格的其他属性（可选）   
        self.tableWidget_jiesuan.resizeColumnsToContents()  # 根据内容调整列宽  
    def mergeRows(self):  #结算表格合并函数
        # 使用字典来存储合并后的数据  
        merged_data = {}  
          
        # 遍历所有行  
        for row in range(self.tableWidget_jiesuan.rowCount()):  
            name = self.tableWidget_jiesuan.item(row, 0).text()  
            price = self.tableWidget_jiesuan.item(row, 1).text()  
            quantity = int(self.tableWidget_jiesuan.item(row, 2).text()) 
            spec = self.tableWidget_jiesuan.item(row, 3).text()  
             
              
            # 生成唯一键  
            key = (name, spec, price)  
              
            # 如果键已存在，更新数量  
            if key in merged_data:  
                merged_data[key]['quantity'] += quantity  
            else:  
                # 如果键不存在，则创建新条目  
                merged_data[key] = {  
                    'name': name,  
                    'price': price,  
                    'quantity': quantity  ,
                    'spec': spec,  
                    
                }  
          
        # 清空表格并添加合并后的数据  
        self.tableWidget_jiesuan.clear()  
        self.tableWidget_jiesuan.setRowCount(len(merged_data))  
        self.tableWidget_jiesuan.setHorizontalHeaderLabels(['名称', '价格', '数量','规格'])  # 设置列标题  
        # 填充合并后的数据到表格  
        for row_index, (key, data) in enumerate(merged_data.items()):  
            self.tableWidget_jiesuan.setItem(row_index, 0, QTableWidgetItem(data['name']))  
            self.tableWidget_jiesuan.setItem(row_index, 1, QTableWidgetItem(data['price'])) 
            self.tableWidget_jiesuan.setItem(row_index, 2, QTableWidgetItem(str(data['quantity'])))
            self.tableWidget_jiesuan.setItem(row_index, 3, QTableWidgetItem(data['spec']))  

    def errorMessageBox(self,error_msg):
        # 创建一个错误提示框  
        msg_box = QMessageBox()  
        msg_box.setWindowTitle("错误")  # 设置对话框标题  
        msg_box.setIcon(QMessageBox.Icon.Critical)  # 设置图标为错误（或称为关键）图标
        msg_box.setText(error_msg)  # 设置对话框的主要文本  
        msg_box.setStandardButtons(QMessageBox.Ok)  # 设置对话框只有一个“确定”按钮  
        msg_box.setDefaultButton(QMessageBox.Ok)  # 设置默认按钮为“确定” 
        msg_box.exec() 

    def func_pushButton_remove(self,):
        selected_items= self.tableWidget_jiesuan.selectedItems()
        row_index = self.tableWidget_jiesuan.row(selected_items[0])  # 行索引
        item = self.tableWidget_jiesuan.item(row_index, 2)
        quantity = int(item.text())
        beijianshu = self.spinBox_add_quantity.value()
        if quantity >= 1 and quantity > beijianshu:
            item.setText(str(quantity - beijianshu)  )
        elif quantity == beijianshu:
            self.tableWidget_jiesuan.removeRow(row_index) 
        else:
            self.errorMessageBox('数量设置有误！')
        
    def func_pushButton_jiesuan_clear(self,):#清空按钮
        self.tableWidget_jiesuan.clearContents()
        self.tableWidget_jiesuan.setRowCount(0)
        pass

    def func_pushButton_delete(self,):
        self.connection = self.db.dbconnect()
        items= self.tableWidget_info.selectedItems()
        for item in items:
            if item.column() == 8:
                data_numbering = item.text() #该行数据库编号
        self.db.deletedata(self.connection,data_numbering)
        self.func_pushButton_showallgoods()

    def func_pushButton_modify(self,):
        pass

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u8d27\u7269\u7ba1\u7406\u5de5\u5177", None))
        self.label_info_table.setText(QCoreApplication.translate("MainWindow", u"\u5546\u54c1\u4ef7\u683c\u8868", None))
        self.pushButton_keyword_search.setText(QCoreApplication.translate("MainWindow", u"\u5173\u952e\u8bcd\u641c\u7d22", None))
        self.pushButton_showallgoods.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u5168\u90e8\u8d27\u7269", None))
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
        self.pushButton_jiesuan_clear.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.pushButton_delete.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.pushButton_modify.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539", None))
    # retranslateUi

