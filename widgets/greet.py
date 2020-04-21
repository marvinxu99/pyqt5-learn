import sys
from PyQt5.QtWidgets import QLineEdit, QPushButton, QApplication, QVBoxLayout, QDialog, QLabel

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        # Create widgets
        self.edit = QLineEdit("Write my name here")
        self.button = QPushButton("Show Greetings")
        self.label = QLabel("no greetings yet.", self)

        # Add button signal to greetings slot
        self.button.clicked.connect(self.greetings)

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)
        layout.addWidget(self.label)
        
        # Set dialog layout
        self.setLayout(layout)
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QProgressBar')
        self.show()


    # Greets the user
    def greetings(self):
        self.label.setText(f"Hello { self.edit.text() }")
        print ("Hello %s" % self.edit.text())

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    exit_code = app.exec_()
    sys.exit(exit_code)