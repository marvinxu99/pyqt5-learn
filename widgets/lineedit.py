'''
QLineEdit is a widget that allows to enter and edit a single 
line of plain text. There are undo and redo, cut and paste, 
and drag & drop functions available for the widget.
'''

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QApplication


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        self.lbl = QLabel(self)
        qle = QLineEdit(self)
        
        qle.move(60, 100)
        self.lbl.move(60, 40)

        qle.textChanged[str].connect(self.onChanged)
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QLineEdit')
        self.show()
        
        
    def onChanged(self, text):
        
        self.lbl.setText(text)
        self.lbl.adjustSize()        
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    exit_code = app.exec_() 
    sys.exit(exit_code)

