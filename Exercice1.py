from PySide2.QtWidgets import *
import random

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Différents cycles dans l'ISEN Yncréa Ouest")
        self.setMinimumSize(500, 300)
        self.data = ["CSI", "CIR", "BIOST", "CENT", "BIAST", "EST"]

        self.layout = QVBoxLayout()

        self.label = QLabel(random.choice(self.data))
        self.button = QPushButton("Changer de cycle")

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.change_cycle)

        self.setLayout(self.layout)

    def change_cycle(self):
        rnd = random.choice(self.data)
        self.label.setText(rnd)

if __name__ == "__main__":
   app = QApplication([])
   window = Window()
   window.show()
   app.exec_()
