#!/usr/bin/env python3

# Vertical Layout Example

import sys

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('PyQt5 QVBoxLayout Example')
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Center'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
sys.exit(app.exec_())