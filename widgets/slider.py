#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This example shows a QSlider widget.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

from PyQt5.QtWidgets import QWidget, QSlider, QLabel, QApplication, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import sys

# class Example(QWidget):
class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)
        
        # create a QLabel widget and set an initial mute image to it
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('icons8-mute-100.png'))
        self.label.setGeometry(160, 40, 100, 100)
                
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('value = 0')

        self.setGeometry(300, 300, 380, 370)
        self.setWindowTitle('QSlider')
        self.show()
        
        
    def changeValue(self, value):

        if value == 0:
            self.label.setPixmap(QPixmap('icons8-mute-100.png'))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap('icons8-low-volume-100.png'))
        elif value > 30 and value < 80:
            self.label.setPixmap(QPixmap('icons8-voice-med-80.png'))
        else:
            self.label.setPixmap(QPixmap('icons8-audio-max-96.png'))

        self.statusbar.showMessage(f'value = { value }')
            

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    exit_code = app.exec_()
    sys.exit(exit_code)     