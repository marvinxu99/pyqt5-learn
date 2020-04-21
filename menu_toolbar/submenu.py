#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This program creates a submenu.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QApplication, qApp
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):         
        
        menubar = self.menuBar()

        fileMenu = menubar.addMenu('File')
        
        impMenu = QMenu('Import', self)
        impAct = QAction('Import mail', self) 
        impAct2 = QAction('Import photos', self) 
        impMenu.addAction(impAct)
        impMenu.addAction(impAct2)
        
        newAct = QAction('New', self)        

        exitAct = QAction(QIcon('exit.png'), 'Exit', self)        
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        fileMenu.addAction(exitAct)
        
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Submenu')
        self.setWindowIcon(QIcon('favicon.ico'))        
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    ec = app.exec_()
    sys.exit(ec)
