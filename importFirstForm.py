#!/usr/bin/python
# Filename : importFirstForm.py

import sys

from PySide.QtCore import *
from PySide.QtGui import *

from firstForm_ui import Ui_Form

class firstForm(QWidget):
    def __init__(self, parent=None):
         QWidget.__init__(self, parent)
         self.ui = Ui_Form()
         self.ui.setupUi(self)

def main():
    app = QApplication(sys.argv)
    w = firstForm()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
