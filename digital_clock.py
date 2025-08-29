# Project 15 : Digital clock

import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QIcon

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(700,300,500,200)
        self.setWindowIcon(QIcon("N:\Python Projects\8992.jpg"))
        self.setStyleSheet("background-color:black;")

        self.time_label.setStyleSheet("font-size:100px;"
                                      "font-family:Arial;"
                                      "color:green;")
        self.time_label.setAlignment(Qt.AlignCenter)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)

def main():
    app = QApplication(sys.argv)
    window = DigitalClock()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
