'''
QPainter performs low-level painting on widgets and other paint devices. 
It can draw everything from simple lines to complex shapes.

The painting is done within the paintEvent() method. The painting code is 
placed between the begin() and end() methods of the QPainter object. 
It performs low-level painting on widgets and other paint devices.
'''

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5.QtCore import Qt

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      
        
        self.text = "Лев Николаевич Толстой\nАнна Каренина"

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Drawing text')
        self.show()
        

    def paintEvent(self, event):

        qp = QPainter()
        qp.begin(self)
        self.drawText(event, qp)
        qp.end()
        
        
    def drawText(self, event, qp):
      
        qp.setPen(QColor(168, 34, 3))
        qp.setFont(QFont('Decorative', 10))
        qp.drawText(event.rect(), Qt.AlignCenter, self.text)        
                
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    exit_code = app.exec_()
    sys.exit(exit_code)

