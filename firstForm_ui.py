# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstForm.ui'
#
# Created: Tue Feb 18 13:52:18 2014
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(763, 530)
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtGui.QWidget(Form)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_4 = QtGui.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget_4)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_5 = QtGui.QWidget(self.widget_4)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_5)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtGui.QLabel(self.widget_5)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.lineEdit_2 = QtGui.QLineEdit(self.widget_5)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(120, 0))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.pushButton_3 = QtGui.QPushButton(self.widget_5)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.widget_5)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.treeView = QtGui.QTreeView(self.widget_4)
        self.treeView.setObjectName("treeView")
        self.verticalLayout_2.addWidget(self.treeView)
        self.horizontalLayout_3.addWidget(self.widget_4)
        self.tabWidget = QtGui.QTabWidget(self.widget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_3.addWidget(self.tabWidget)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout.addWidget(self.widget)
        self.line = QtGui.QFrame(Form)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.widget_2 = QtGui.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtGui.QLineEdit(self.widget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtGui.QPushButton(self.widget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.widget_2)
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.widget_3 = QtGui.QWidget(Form)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(583, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_2 = QtGui.QPushButton(self.widget_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.widget_3)
        self.verticalLayout.setStretch(0, 5)
        self.verticalLayout.setStretch(3, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "主机：", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form", "本地", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Form", "USB", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("Form", "命令", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("Form", "Tab 2", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "执行", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "退出", None, QtGui.QApplication.UnicodeUTF8))

