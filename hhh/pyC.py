import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QPushButton, QLabel, QLineEdit


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('NZiLANTUZU')
        self.setGeometry(100, 100, 300, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QGridLayout()
        central_widget.setLayout(layout)

        self.label = QLabel()
        self.label.setAlignment(Qt.AlignRight)
        layout.addWidget(self.label, 0, 0, 1, 4)

        self.input_field = QLineEdit()
        self.input_field.setAlignment(Qt.AlignRight)
        layout.addWidget(self.input_field, 1, 0, 1, 4)

        self.add_button('1', 2, 0, 1, 1)
        self.add_button('2', 2, 1, 1, 1)
        self.add_button('3', 2, 2, 1, 1)
        self.add_button('+', 2, 3, 1, 1)
        self.add_button('4', 3, 0, 1, 1)
        self.add_button('5', 3, 1, 1, 1)
        self.add_button('6', 3, 2, 1, 1)
        self.add_button('-', 3, 3, 1, 1)
        self.add_button('7', 4, 0, 1, 1)
        self.add_button('8', 4, 1, 1, 1)
        self.add_button('9', 4, 2, 1, 1)
        self.add_button('*', 4, 3, 1, 1)
        self.add_button('C', 5, 0, 1, 1)
        self.add_button('0', 5, 1, 1, 1)
        self.add_button('=', 5, 2, 1, 1)
        self.add_button('/', 5, 3, 1, 1)

    def add_button(self, label, row, col, rowspan, colspan):
        button = QPushButton(label)
        button.clicked.connect(lambda: self.button_click(label))
        layout = self.centralWidget().layout()
        layout.addWidget(button, row, col, rowspan, colspan)

    def button_click(self, label):
        if label == 'C':
            self.input_field.setText('')
        elif label == '=':
            self.label.setText(self.input_field.text())
            self.input_field.setText('')
        else:
            self.input_field.setText(self.input_field.text() + label)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
