from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem  
  
class MainWindow(QMainWindow):  
    def __init__(self):  
        super().__init__()  
        self.initUI()  
  
    def initUI(self):  
        # 创建一个 QTableWidget，假设有三列  
        self.tableWidget = QTableWidget(0, 3)  # 0行3列，行数动态添加  
        self.tableWidget.setHorizontalHeaderLabels(['属性1', '属性2', '属性3'])  # 设置列标题  
  
        # 假设这是你的数据列表，每个元素是一个包含三个属性的列表或元组  
        data = [  
            ['数据1', '数据2', '数据3'],  
            ['数据4', '数据5', '数据6'],  
            # ... 更多数据  
        ]  
  
        # 遍历数据列表，将每个元素添加到表格的一行中  
        for row_data in data:  
            row_count = self.tableWidget.rowCount()  # 获取当前行数  
            self.tableWidget.insertRow(row_count)  # 插入新行  
  
            # 遍历行数据，将每个属性值设置到对应的单元格中  
            for column, value in enumerate(row_data):  
                item = QTableWidgetItem(value)  # 创建表格项  
                self.tableWidget.setItem(row_count, column, item)  # 设置单元格内容  
  
        # 设置表格的其他属性（可选）  
        self.tableWidget.setRowCount(len(data))  # 设置行数（如果数据列表长度固定的话）  
        self.tableWidget.resizeColumnsToContents()  # 根据内容调整列宽  
  
        # 将 QTableWidget 添加到主窗口中（或其他布局中）  
        self.setCentralWidget(self.tableWidget)  
  
        # 设置窗口标题和大小  
        self.setWindowTitle('PySide6 QTableWidget 示例')  
        self.setGeometry(300, 300, 400, 300)  
  
if __name__ == '__main__':  
    app = QApplication([])  
    mainWindow = MainWindow()  
    mainWindow.show()  
    app.exec()