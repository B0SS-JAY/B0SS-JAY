from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class AddBatteryWindow(QDialog):  # Add battery Window
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle("Add New Battery")
        self.setFixedSize(1920, 1080)  # Set smaller window size
        self.main_window = main_window  # Store reference to MainWindow

        # Example Label
        label = QLabel("This is the Add Battery Window!", self)
        label.setFont(QFont("Arial", 14))
        label.setAlignment(Qt.AlignCenter)
        label.setFixedSize(400, 50)  # Set size
        label.move(340, 100)  # Move to (x=340, y=100)

        # Clickable Button
        button = QPushButton("Return to Main Window", self)
        button.setFont(QFont("Arial", 14))
        button.setFixedSize(300, 50)  # Set button size
        button.move(1600, 950)  # Move button
        button.clicked.connect(self.button_clicked)  # Connect button to function

    def button_clicked(self):
        print("Returning to Main Window!")  
        self.close()  # Close the dialog
        self.main_window.show()  # Show the main window again
#Text Outline
class OutlinedLabel(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)

    def setOutlineColor(self, color):
        self.outline_color = QColor(color)

    def setTextColor(self, color):
        self.text_color = QColor(color)

    def setOutlineThickness(self, thickness):
        self.outline_thickness = thickness

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        path = QPainterPath()
        font = self.font()
        text_rect = self.rect()
        #outline placement
        path.addText(text_rect.center().x() - self.width() // 2.402, 
                     text_rect.center().y() + self.height() // 3.1, 
                     font, self.text())
        pen = QPen(self.outline_color)
        pen.setWidth(self.outline_thickness)
        painter.setPen(pen)
        painter.drawPath(path)
        painter.setPen(self.text_color)
        painter.drawText(text_rect, self.alignment(), self.text())

        painter.end()

class DeleteBatteryWindow(QDialog):  # Add battery Window
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle("Delete Battery")
        self.setFixedSize(1920, 1080)  # Set smaller window size
        self.main_window = main_window  # Store reference to MainWindow

        # Example Label
        label = QLabel("This is the delete Battery Window!", self)
        label.setFont(QFont("Arial", 14))
        label.setAlignment(Qt.AlignCenter)
        label.setFixedSize(400, 50)  # Set size
        label.move(340, 100)  # Move to (x=340, y=100)

        # Clickable Button
        button = QPushButton("Return to Main Window", self)
        button.setFont(QFont("Arial", 14))
        button.setFixedSize(300, 50)  # Set button size
        button.move(1600, 950)  # Move button
        button.clicked.connect(self.button_clicked)  # Connect button to function

    def button_clicked(self):
        print("Returning to Main Window!")  
        self.close()  # Close the dialog
        self.main_window.show()  # Show the main window again

class DockWindow(QDialog):  # Generic Dock Window for all docks
    def __init__(self, BP_ID, main_window):
        super().__init__()
        self.setWindowTitle(f"{BP_ID} Details")
        self.setFixedSize(1920, 1080)
        self.main_window = main_window  # Store reference to MainWindow

        # ✅ Top Background
        bg_widget = QWidget(self)
        bg_widget.setFixedSize(1920, 1080 // 10)
        bg_widget.setStyleSheet("background-color: rgb(189, 221, 252); border: 2px solid black;")

        # ✅ Side Background
        self.side_bg_widget = QWidget(self)
        self.side_bg_widget.setFixedSize(1920 // 7, 1080)
        self.side_bg_widget.setStyleSheet("background-color: rgb(102, 178, 214); border: 2px solid black;")
        self.side_bg_widget.move(0, 0)  

        # ✅ Digital Clock Label
        self.clock_label = QLabel(self)
        self.clock_label.setFont(QFont("DS Digital", 27, QFont.Bold))
        self.clock_label.setStyleSheet("color: black; background: transparent;")  
        self.clock_label.setAlignment(Qt.AlignCenter)
        self.clock_label.setFixedSize(210, 50)
        self.clock_label.move(30, 20)  

        # ✅ Start Timer for Clock Update
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  
        self.update_time()  

        # ✅ Dock Status Overview Title
        self.title_label = QLabel(f"{BP_ID} - STATUS OVERVIEW", self)
        self.title_label.setFont(QFont("Arial", 40, QFont.Bold))
        self.title_label.setStyleSheet("background: transparent; color: black;")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFixedSize(1900, 50)
        self.title_label.move(175, 30)  

        # ✅ Return Button
        self.close_button = QPushButton("Return to Main Window", self)
        self.close_button.setFont(QFont("Arial", 14))
        self.close_button.setFixedSize(300, 50)
        self.close_button.move(1600, 950)
        self.close_button.clicked.connect(self.close_window)

    def update_time(self):
        """ Updates the digital clock every second. """
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.clock_label.setText(current_time)

    def close_window(self):
        """ Close this window and show the main window again """
        self.close()
        self.main_window.show()  
