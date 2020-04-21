#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we create a bit
more complicated window layout using
the QGridLayout manager. 

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QTextEdit, \
                QGridLayout, QApplication, QPushButton


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        # create a grid layout and set spacing between widgets
        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        # add a widget to a grid, we can provide row span and column span of the widget. 
        # In our case, we make the reviewEdit widget span 4 rows.
        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 4, 1)

        grid.addWidget(okButton, 7, 0)
        grid.addWidget(cancelButton, 7, 1)

        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 350)
        self.setWindowTitle('Review')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    ec = app.exec_()
    sys.exit(ec)