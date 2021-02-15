#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from functools import partial

__version__ = 0.1
__author__ = "Jed Solomon Gorman Martinez"

ERROR_MSG = 'ERROR'

# Note, we're using the MVC design pattern here.  Model, view, and controller

# This first part of the code sets up the skeleton of the calculator's GUI
class PyCalcUi(QMainWindow):
   def __init__(self):
      super().__init__()
      
      # Here we set some of the main window's properties
      self.setWindowTitle('PyCalc')
      self.setFixedSize(235, 235)
      
      # Now we set the general properties
      self.generalLayout = QVBoxLayout()
      self._centralWidget = QWidget(self)
      self.setCentralWidget(self._centralWidget)
      self._centralWidget.setLayout(self.generalLayout)
      
      # Now we create the display and the buttons
      self._createDisplay()
      self._createButtons()
      
   def _createDisplay(self):
      # Create the display 
      # Display widget
      self.display = QLineEdit()
      
      # Set some of the display's properties
      self.display.setFixedHeight(35)
      self.display.setAlignment(Qt.AlignRight)
      self.display.setReadOnly(True)
      
      # Add the display to the general layout
      self.generalLayout.addWidget(self.display)
      
   def setDisplayText(self, text):
      self.display.setText(text)
      self.display.setFocus()
      
   def displayText(self):
      return self.display.text()
   
   def clearDisplay(self):
      self.setDisplayText('')
      
   def _createButtons(self):
      # Now we set the buttons up.  We will use a dict to store the button/name/placemen combos
      self.buttons = {}
      buttonsLayout = QGridLayout()
      # Buttons Text | Position on the Q Grid.
      buttons = {
         '7': (0, 0),
         '8': (0, 1),
         '9': (0, 2),
         '/': (0, 3),
         'C': (0, 4),
         '4': (1, 0),
         '5': (1, 1),
         '6': (1, 2),
         '*': (1, 3),
         '(': (1, 4),
         '1': (2, 0),
         '2': (2, 1),
         '3': (2, 2),
         '-': (2, 3),
         ')': (2, 4),
         '0': (3, 0),
         '00':(3, 1),
         '.':(3, 2),
         '+':(3, 3),
         '=':(3, 4)
      }
      for btnText, pos in buttons.items():
         self.buttons[btnText] = QPushButton(btnText)
         self.buttons[btnText].setFixedSize(40, 40)
         buttonsLayout.addWidget(self.buttons[btnText], pos[0], pos[1])
      
      # Now we add the buttons to the general layout
      self.generalLayout.addLayout(buttonsLayout)


# Here we create a controller class to connect the GUI and the model
class PyCalcControl:
   # PyCalc controller class
   def __init__(self, model, view):
      # Initialize controller
      self._evaluate = model
      self._view = view
      
      # Connect signals and slots
      self._connectSignals()
      
   def _calculateResult(self):
      # Evaluate expressions
      result = self._evaluate(expression=self._view.displayText())
      self._view.setDisplayText(result)
      
   def _buildExpression(self, sub_exp):
      # Build Expression (what does that mean?)
      if self._view.displayText() == ERROR_MSG:
         self._view.clearDisplay()
      
      expression = self._view.displayText() + sub_exp
      self._view.setDisplayText(expression)
      
   def _connectSignals(self):
      # Connect signals and slots
      for btnText, btn in self._view.buttons.items():
         if btnText not in {'=','C'}:
            btn.clicked.connect(partial(self._buildExpression, btnText))
      
      self._view.buttons['='].clicked.connect(self._calculateResult)
      self._view.display.returnPressed.connect(self._calculateResult)
      self._view.buttons['C'].clicked.connect(self._view.clearDisplay)

# The model is just this single function definition...
def evaluateExpression(expression):
   # Evaluate an expression
   try:
      result = str(eval(expression, {}, {}))
   except Exception:
      result = ERROR_MSG
   return result

# Now we get to client code
def main():
   # Main Function
   # Create an instance of QApplication
   pycalc = QApplication(sys.argv)
   
   
   buttonsLayout = QGridLayout()
   display = QLineEdit()
   
   # Show the calculator's GUI
   view = PyCalcUi()
   view.show()
   
   # Create instances of the model and the controller
   model = evaluateExpression
   PyCalcControl(model=model, view=view)
   
   # Execute the calculator's event loop
   sys.exit(pycalc.exec())
   
if __name__ == '__main__':
   main()