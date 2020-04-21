from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
import sys, random

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.setGeometry(300, 300, 400, 390)
        self.setWindowTitle('Points')
        self.show()
        

    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()
        
        
    def drawPoints(self, qp):
      
        qp.setPen(Qt.red)
        size = self.size()
        
        for i in range(500):
            x = random.randint(1, size.width()-1)
            y = random.randint(1, size.height()-1)
            # qp.drawPoint(x, y) 
            qp.drawRect(x, y, 10, 10)    
                
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    exit_code = app.exec_()
    sys.exit(exit_code)
