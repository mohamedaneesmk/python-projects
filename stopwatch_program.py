# Step 1: Import required modules
import sys
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QVBoxLayout, QHBoxLayout
)
from PyQt5.QtCore import QTimer, Qt


# Step 2: Create the main StopWatch class
class StopWatch(QWidget):
    def __init__(self):
        super().__init__()
        self.milliseconds = 0     # stores elapsed time in milliseconds
        self.running = False      # flag to check if stopwatch is running

        # Step 3: Create widgets
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)

        # Step 4: Create a timer (runs every few ms to update time)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_display)

        # Step 5: Call function to build UI
        self.initUI()

    # Step 6: Setup UI
    def initUI(self):
        self.setWindowTitle("Stopwatch")
        self.setGeometry(700, 300, 600, 300)

        # Layouts
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)
        self.setLayout(vbox)

        # Step 7: Styling for buttons and label
        self.setStyleSheet("""
            QPushButton, QLabel {
                font-family: Calibri;
                font-weight: bold;
            }
            QPushButton {
                font-size: 24px;
                padding: 10px 20px;
                border-radius: 10px;
                background-color: #444;
                color: white;
            }
            QPushButton:hover {
                background-color: #666;
            }
            QLabel {
                font-size: 60px;
                color: lime;
                background-color: black;
                padding: 20px;
            }
        """)
        self.time_label.setAlignment(Qt.AlignCenter)

        # Step 8: Connect button clicks to functions
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

    # Step 9: Start stopwatch
    def start(self):
        if not self.running:
            self.timer.start(10)  # update every 10 ms
            self.running = True

    # Step 10: Stop stopwatch
    def stop(self):
        if self.running:
            self.timer.stop()
            self.running = False

    # Step 11: Reset stopwatch
    def reset(self):
        self.timer.stop()
        self.running = False
        self.milliseconds = 0
        self.update_display()

    # Step 12: Format time into hh:mm:ss.ms
    def format_time(self, ms):
        hours = ms // (3600 * 100)
        minutes = (ms // (60 * 100)) % 60
        seconds = (ms // 100) % 60
        milliseconds = ms % 100
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    # Step 13: Update display on screen
    def update_display(self):
        self.milliseconds += 1
        self.time_label.setText(self.format_time(self.milliseconds))


# Step 14: Run the application
def main():
    app = QApplication(sys.argv)
    window = StopWatch()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
