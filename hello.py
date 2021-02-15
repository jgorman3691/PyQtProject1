#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QLabel

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
helloMsg = QLabel('<h1>Hello, World!</h1>', parent=window)
helloMsg.move(60, 15)
window.show()
sys.exit(app.exec_())
