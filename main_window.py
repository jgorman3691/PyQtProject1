#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QStatusBar, QToolBar

class Window(QMainWindow):
   # The main window
   def __init__(self, parent=None):
      # Now the initializer
      super().__init__(parent)
      self.setWindowTitle('Main Window')
      self.setCentralWidget(QLabel("I'm the Central Widget!"))
      self._createMenu()
      self._createToolBar()
      self._createStatusBar()
      
   def _createMenu(self):
      self.menu = self.menuBar().addMenu("&Menu")
      self.menu.addAction('&Exit', self.close)
      
   def _createToolBar(self):
      tools = QToolBar()
      self.addToolBar(tools)
      tools.addAction('Exit', self.close)
      
   def _createStatusBar(self):
      status = QStatusBar()
      status.showMessage("I'm the status bar!")
      self.setStatusBar(status)
      
if __name__ == '__main__':
   app = QApplication(sys.argv)
   win = Window()
   win.show()
   sys.exit(app.exec_())