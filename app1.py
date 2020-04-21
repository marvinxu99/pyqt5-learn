from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QMessageBox
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt


app = QApplication([])
#label = QLabel("&hello world!")
#label.show()

app.setStyleSheet("QPushButton { margin: 10ex; }")
palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.red)
app.setPalette(palette)
button = QPushButton("Click me")

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()

button.clicked.connect(on_button_clicked)

button.show()

app.exec_()