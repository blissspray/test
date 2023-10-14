from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout

app = QApplication([])

window = QWidget()
window.setWindowTitle('first project')
window.move(600, 250)
window.resize(500, 500)

button = QPushButton('push me')
text = QLabel('push this button pls')

line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)

window.setLayout(line)

def change_text():
    text.setText('meh')

button.clicked.connect(change_text)

window.show()
app.exec_()