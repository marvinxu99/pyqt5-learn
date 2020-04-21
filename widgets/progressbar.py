'''
A progress bar is a widget that is used when we process lengthy tasks. 
It is animated so that the user knows that the task is progressing. 
The QProgressBar widget provides a horizontal or a vertical progress bar 
in PyQt5 toolkit. The programmer can set the minimum and maximum value 
for the progress bar. The default values are 0 and 99.
'''

from PyQt5.QtWidgets import (QWidget, QProgressBar, 
    QPushButton, QApplication)
from PyQt5.QtCore import QBasicTimer
import sys

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()
        
        
    def timerEvent(self, e):
        '''
        Each QObject and its descendants have a timerEvent() event handler. 
        In order to react to timer events, we reimplement the event handler.
        '''
        if self.step >= 100:
            
            self.timer.stop()
            self.btn.setText('Finished')
            return
            
        self.step = self.step + 1
        self.pbar.setValue(self.step)
        

    def doAction(self):
      
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')
            
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    exit_code = app.exec_()
    sys.exit(exit_code)
