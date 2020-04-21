'''
ézier curve is a cubic line. Bézier curve in PyQt5 can be 
created with QPainterPath. A painter path is an object 
composed of a number of graphical building blocks, 
such as rectangles, ellipses, lines, and curves.
'''
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPainterPath
from PyQt5.QtCore import Qt
import sys

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.setGeometry(300, 300, 380, 250)
        self.setWindowTitle('Bézier curve')
        self.show()
        

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        self.drawBezierCurve(qp)
        qp.end()
        
        
    def drawBezierCurve(self, qp):
      
        # create a Bézier curve with QPainterPath path. The curve is 
        # created with cubicTo() method, which takes three 
        # points: starting point, control point, and ending point.
        path = QPainterPath()
        path.moveTo(30, 30)
        path.cubicTo(30, 30, 200, 350, 350, 30)
        
        qp.drawPath(path)
              
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    exit_code = app.exec_()
    sys.exit(exit_code)
