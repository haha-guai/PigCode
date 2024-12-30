import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        label1 = QLabel("账户")
        label2 = QLabel("密码")
        line1 = QLineEdit()
        line2 = QLineEdit()

        g_layout = QGridLayout()
        g_layout.addWidget(label1, 0, 0)
        g_layout.addWidget(label2, 1, 0)
        g_layout.addWidget(line1, 0, 1)
        g_layout.addWidget(line2, 1, 1)
        self.setLayout(g_layout)

if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())