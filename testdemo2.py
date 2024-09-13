from PySide6.QtWidgets import QApplication, QMainWindow  
import mainui  # 导入转换后的 UI 文件  

class MyMainWindow(QMainWindow, mainui.Ui_MainWindow):  # 假设你的主窗口类名是 Ui_MainWindow  
    def __init__(self):  
        super().__init__()  
        self.setupUi(self)  # 初始化 UI  

if __name__ == "__main__":  
    app = QApplication([])  
    window = MyMainWindow()  
    window.show()  
    app.exec()