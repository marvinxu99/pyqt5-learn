#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we show how to 
emit a custom signal. 

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox


class Communicate(QObject):
    
    closeApp = pyqtSignal() 
    

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.c = Communicate()
        self.c.closeApp.connect(self.close)       
        
        self.setGeometry(300, 300, 390, 350)
        self.setWindowTitle('Emit signal')
        self.show()
        
        
    def mousePressEvent(self, event):
        
        self.c.closeApp.emit()


    def closeEvent(self, event):
        '''
        The first string appears on the titlebar. The second string is the message text 
        displayed by the dialog. The third argument specifies the combination of buttons 
        appearing in the dialog. The last parameter is the default button.
        '''
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()        

        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    ec = app.exec_() 
    sys.exit(ec)
