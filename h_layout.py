#!/usr/bin/env python3

# Horizontal Layout Example

import sys

from PyQt5.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('PyQt5 Horizontal Box Layout Example')
layout = QHBoxLayout()
layout.addWidget(QPushButton('Left'))
layout.addWidget(QPushButton('Center'))
layout.addWidget(QPushButton('Right'))
window.setLayout(layout)
window.show()
sys.exit(app.exec_())