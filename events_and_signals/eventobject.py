#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we display the x and y 
coordinates of a mouse pointer in a label widget.

Author: Jan Bodnar
Website: zetcode.com 
Last edited: August 2017
"""

'''
Event object is a Python object that contains a number of attributes 
describing the event. Event object is specific to the generated event type.
'''

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
        
        grid = QGridLayout()
        
        x, y = 0, 0
        self.text = "x: {0},  y: {1}".format(x, y)
        
        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)
        
        '''
        Mouse tracking is disabled by default, so the widget only 
        receives mouse move events when at least one mouse button is 
        pressed while the mouse is being moved. If mouse tracking is enabled, 
        the widget receives mouse move events even if no buttons are pressed.
        '''
        self.setMouseTracking(True)
        
        self.setLayout(grid)
        
        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()
        
        
    def mouseMoveEvent(self, e):
        
        x, y = e.x(), e.y()
        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)
    
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    ec = app.exec_()
    sys.exit(ec)