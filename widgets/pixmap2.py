from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication
from PyQt5.QtGui import QPixmap
import sys

def window():
   app = QApplication(sys.argv)
   win = QWidget()
   l1 = QLabel()
   l1.setPixmap(QPixmap("python.png"))
	
   vbox = QVBoxLayout()
   vbox.addWidget(l1)
   win.setLayout(vbox)
   win.setWindowTitle("QPixmap Demo")
   win.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   window()
