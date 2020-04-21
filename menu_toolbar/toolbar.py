#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This program creates a toolbar.
The toolbar has one action, which
terminates the application, if triggered.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMessageBox
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):               
        
        exitAct = QAction(QIcon('exit48.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        #exitAct.triggered.connect(qApp.quit)
        exitAct.triggered.connect(self.close)

        self.statusBar()
       
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')    
        self.setWindowIcon(QIcon('favicon.ico'))        

        self.show()


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
