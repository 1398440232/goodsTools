import sys  
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QDialog  
  
class PopupWindow(QDialog):  
    def __init__(self):  
        super().__init__()  
        self.initUI()  
  
    def initUI(self):  
        self.setWindowTitle('弹出窗口')  
        self.setGeometry(300, 300, 200, 100)  
          
        # 添加一个标签来显示信息  
        self.label = QLabel('这是一些信息', self)  
        self.label.move(50, 50)  
  
class MainWindow(QWidget):  
    def __init__(self):  
        super().__init__()  
        self.initUI()  
  
    def initUI(self):  
        self.setWindowTitle('主窗口')  
        self.setGeometry(300, 300, 250, 150)  
          
        # 创建一个按钮  
        self.button = QPushButton('点击弹出', self)  
        self.button.clicked.connect(self.on_button_clicked)  
        self.button.move(100, 70)  
  
        # 设置布局（可选）  
        layout = QVBoxLayout()  
        layout.addWidget(self.button)  
        self.setLayout(layout)  
  
    def on_button_clicked(self):  
        # 点击按钮时，弹出新窗口  
        popup = PopupWindow()  
        popup.exec()  # 使用exec()显示模态对话框，或者show()显示非模态窗口  
  
if __name__ == '__main__':  
    app = QApplication(sys.argv)  
    ex = MainWindow()  
    ex.show()  
    sys.exit(app.exec())