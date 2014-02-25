#!/usr/bin/python
# Filename : firstPyside.py

import sys
from PySide.QtCore import*
from PySide.QtGui import*
def sayHello():
    print "Hello World"

app = QApplication(sys.argv)
#label = QLabel("Hello World")
#label.show()
button = QPushButton("Click")
button.clicked.connect(sayHello)
button.show()
    
app.exec_()
sys.exit()
