#!/usr/bin/env python3

import sys, functools
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

def greeting(who):
   # Slot function
   if msg.text():
      msg.setText("")
   else:
      msg.setText(f"Hello, {who}!")
      
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Signals and Slots')
layout = QVBoxLayout()

btn = QPushButton('Greet')
btn.clicked.connect(functools.partial(greeting, 'World!')) # Connect clicked to greeting
# btn.clicked.connect(lambda x: greeting, 'World!') # Stumped

layout.addWidget(btn)
msg = QLabel('')
layout.addWidget(msg)
window.setLayout(layout)
window.show()
sys.exit(app.exec())