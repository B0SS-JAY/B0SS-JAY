from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3

def create_database():
    conn = sqlite3.connect('batteries.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS batteries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dock TEXT NOT NULL,
            battery_id TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

create_database()

def setup_logos(parent):
    # CSU LOGO
    csu_logo = QLabel(parent)
    pixmap = QPixmap(r"C:\Users\jayro\Desktop\BATTERY SWAPING FILES\csulogo.png")
    csu_logo.setPixmap(pixmap)
    csu_logo.setScaledContents(True)
    csu_logo.setFixedSize(100, 100)  # Set exact size
    csu_logo.move(1155, 935)  # Center it below the text

    # PCIEERD LOGO
    pcieerd_logo = QLabel(parent)
    pixmap = QPixmap(r"C:\Users\jayro\Desktop\BATTERY SWAPING FILES\PCIEERD.png")
    pcieerd_logo.setPixmap(pixmap)
    pcieerd_logo.setScaledContents(True)
    pcieerd_logo.setFixedSize(100, 100)  # Set exact size
    pcieerd_logo.move(850, 935)  # Center it below the text

    # NICER LOGO
    nicer_logo = QLabel(parent)
    pixmap = QPixmap(r"C:\Users\jayro\Desktop\BATTERY SWAPING FILES\NICER.png")
    nicer_logo.setPixmap(pixmap)
    nicer_logo.setScaledContents(True)
    nicer_logo.setFixedSize(230, 100)  # Set exact size
    nicer_logo.move(950, 935)  # Center it below the text

    # EMRDC LOGO
    emrdc_logo = QLabel(parent)
    pixmap = QPixmap(r"C:\Users\jayro\Desktop\BATTERY SWAPING FILES\EMRDC.png")
    emrdc_logo.setPixmap(pixmap)
    emrdc_logo.setScaledContents(True)
    emrdc_logo.setFixedSize(130, 130)  # Set exact size
    emrdc_logo.move(1250, 920)  # Center it below the text

def setup_clock(parent):
    # Digital Clock Label (Top Left)
    clock_label = QLabel(parent)
    clock_label.setFont(QFont("DS Digital", 27, QFont.Bold))
    clock_label.setStyleSheet("""
        color: white;
        background-color: #333;
        border: 2px solid #555;
        border-radius: 10px;
        padding: 5px;
    """)
    clock_label.setAlignment(Qt.AlignCenter)
    clock_label.setFixedSize(230, 60)
    clock_label.move(20, 20)  # Position in the top-left corner

    def update_time():
        """ Updates the digital clock every second. """
        current_time = QTime.currentTime().toString("hh:mm:ss")
        clock_label.setText(current_time)

    # Start the clock update timer
    timer = QTimer(parent)
    timer.timeout.connect(update_time)
    timer.start(1000)  # Update every second
    update_time()  # Update the clock immediately

    return clock_label, timer

def date(parent):
    # Add current date below the clock
    date_label = QLabel(parent)
    date_label.setFont(QFont("Arial", 20, QFont.Bold))
    date_label.setStyleSheet("""
        color: white;
        background-color: #333;
        border: 2px solid #555;
        border-radius: 10px;
        padding: 5px;
    """)
    date_label.setAlignment(Qt.AlignCenter)
    date_label.setFixedSize(230, 40)
    date_label.move(20, 90)  # Position below the clock

    # Update the date label with the current date
    current_date = QDate.currentDate().toString("yyyy-MM-dd")
    date_label.setText(current_date)

    return date_label
        
def home_button(parent):
    # ✅ Return Button with Home Icon and Text
    close_button = QPushButton(parent)
    close_button.setIcon(QIcon(r"C:\Users\jayro\Desktop\BATTERY SWAPING FILES\home.png"))  # Set the path to your home icon
    close_button.setIconSize(QSize(50, 50))  # Set the icon size
    close_button.setFixedSize(200, 70)  # Set button size
    close_button.setStyleSheet("text-align: left; padding-left: 10px;")  # Align text to the left with padding
    close_button.setText("Main Menu")  # Set the text
    close_button.setFont(QFont("Arial", 14))  # Set the font for the text
    close_button.move(40, 150)
    close_button.setAttribute(Qt.WA_Hover)
    close_button.setCursor(Qt.PointingHandCursor)
    close_button.clicked.connect(parent.close_window)  # Connect to parent's close_window method
    close_button.setStyleSheet("""
            QPushButton {
            }
            QPushButton:hover {
                background-color: #e0e0e0; /* Slightly darker gray on hover */
            }
            QPushButton:pressed {
                background-color: #d0d0d0; /* Even darker gray when pressed */
            }
        """)

def history_button(parent):
    button_history = QPushButton(parent)
    button_history.setFixedSize(200, 70)  # Set button size
    button_history.setIcon(QIcon(r"C:\Users\jayro\Desktop\BATTERY SWAPING FILES\history.png"))  # Set the path to your history icon
    button_history.setIconSize(QSize(30, 30))  # Set the icon size
    button_history.setStyleSheet("text-align: left; padding-left: 10px;")  # Align text to the left with padding
    button_history.setText("History")  # Set the text
    button_history.setFont(QFont("Arial", 15))  # Set the font for the text
    button_history.move(40, 250)
    button_history.setAttribute(Qt.WA_Hover)
    button_history.setCursor(Qt.PointingHandCursor)
    button_history.clicked.connect(parent.open_history_window)  # Connect to parent's open_history_window method
    button_history.setStyleSheet("""
        QPushButton {
        }
        QPushButton:hover {
            background-color: #e0e0e0; /* Slightly darker gray on hover */
        }
        QPushButton:pressed {
            background-color: #d0d0d0; /* Even darker gray when pressed */
        }
    """)

class HistoryWindow(QDialog):  # History Window
    def __init__(self, main_window):
        super().__init__(main_window)
        self.setWindowTitle("History")
        self.setFixedSize(1920, 1080)  # Set the size of the History window
        self.main_window = main_window  # Store reference to MainWindow

        # Top Background
        bg_widget = QWidget(self)
        bg_widget.setFixedSize(1920, 1080 // 10)
        bg_widget.setStyleSheet("""
            background-color: rgb(189, 221, 252);
            border: 2px solid black;  /* Border color and thickness */
        """)

        setup_logos(self)  # Call the Logos

        # Text inside the background
        layout = QVBoxLayout(bg_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        # Main Menu Text
        text_label = QLabel("            BATTERY HISTORY", self)
        text_label.setFont(QFont("Arial", 55, QFont.Bold))
        text_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(text_label)

        # Place the background widget at the top
        bg_widget.move(0, 0)

        # Side background
        side_bg_widget = QWidget(self)
        side_bg_widget.setFixedSize(1920 // 7, 1080)
        side_bg_widget.setStyleSheet("""
            background-color: rgb(102, 178, 214);
            border: 2px solid black;  /* Border color and thickness */
        """)

        self.clock_label, self.timer = setup_clock(self)
        self.date_label = date(self)  # Call the fixed date function

        # Add a table to display history data
        self.history_table = QTableWidget(self)
        self.history_table.setRowCount(10)  # Example: 10 rows
        self.history_table.setColumnCount(3)  # Example: 3 columns
        self.history_table.setHorizontalHeaderLabels(["DATE AND \nTIME", "OPERATION", "DETAILS"])
        self.history_table.horizontalHeader().setStretchLastSection(True)
        self.history_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.history_table.setFont(QFont("Arial", 15))
        self.history_table.setFixedSize(1600, 700)
        self.history_table.move(300, 130)  # Position the table in the center
        self.history_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.history_table.setSelectionMode(QAbstractItemView.NoSelection)
        self.history_table.verticalHeader().setDefaultSectionSize(100)  # Adjust row height
        self.history_table.horizontalHeader().setDefaultSectionSize(161)  # Adjust column width

        # Hide the vertical header (row numbers)
        self.history_table.verticalHeader().setVisible(False)

        # Style the header using QStyleSheet
        self.history_table.setStyleSheet("""
                QTableWidget {
                    border: 3px solid black;
                }
                QHeaderView::section {
                    background-color: lightgray;
                    border: 2px solid black;
                    font-size: 20pt;  /* Increased font size */
                    font-weight: bold;  /* Make font bold */
                    text-align: center;  /* Center align text */
                    padding: 10px;  /* Add padding for better spacing */
                }
                QTableWidget::item {
                    border: 1px solid black;
                }
                QTableWidget::item:selected {
                    background-color: rgb(189, 221, 252);
                    color: Black;
                }
            """)

        # Add sample data to the table
        self.populate_table()
        
         # Add a "Back" button
        back_button = QPushButton("Back", self)
        back_button.setFont(QFont("Arial", 20))
        back_button.setIcon(QIcon(r"C:\Users\jayro\Desktop\BATTERY SWAPING FILES\back.png"))  # Set the path to your home icon
        back_button.setIconSize(QSize(30, 30))  # Set the icon size
        back_button.setFixedSize(200, 70)
        back_button.move(40, 250)  # Position the button
        back_button.clicked.connect(self.go_back)  # Connect to the back function
        home_button(self)

    def populate_table(self):
        """Populate the table with sample data."""
        sample_data = [
            ["2025-03-27 10:00:00", "Added Battery", "Battery ID: 12345"],
            ["2025-03-26 14:30:00", "Deleted Battery", "Battery ID: 67890"],
            ["2025-03-25 09:15:00", "Added Battery", "Battery ID: 54321"],
            ["2025-03-24 16:45:00", "Deleted Battery", "Battery ID: 98765"],
        ]

        for row, data in enumerate(sample_data):
            for col, value in enumerate(data):
                item = QTableWidgetItem(value)
                item.setTextAlignment(Qt.AlignCenter)
                self.history_table.setItem(row, col, item)

    def close_window(self):
        """ Close this window and show the main window again """
        self.close()
        self.main_window.show()
    def go_back(self):
        """Go back to the previous window."""
        self.close()  # Close the History window
        if hasattr(self, 'previous_window') and self.previous_window:  # If a previous window is provided
            self.previous_window.show()  # Show the previous window
    

class OnScreenKeyboard(QWidget):
    
    def __init__(self, target_input, parent=None):
        super().__init__(parent)
        self.target_input = target_input
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("On-Screen Keyboard")
        self.setFixedSize(1550, 450)
        self.setWindowFlags(Qt.Popup | Qt.WindowStaysOnTopHint)

        # Create a QFrame as the container
        frame = QFrame(self)
        frame.setStyleSheet("""
            QFrame {
                 background-color: rgb(188, 199, 230);
                 border: 2px solid black;  /* Border color and thickness */
            }
        """)
        frame.setGeometry(0, 0, 1550, 450)  # Match widget size

        layout = QGridLayout(frame)  # Apply layout to the frame
        self.setLayout(layout)

        # Add buttons here as before...

        buttons = [
            ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backspace'],
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\'', 'Enter'],
            ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'Shift'],
            ['Ctrl', 'Alt', 'Space', 'Alt', 'Ctrl']
        ]

        for row, keys in enumerate(buttons):
            for col, key in enumerate(keys):
                btn = QPushButton(key)
                if key == 'Space':
                    btn.setFixedSize(735, 80)
                    btn.clicked.connect(self.handle_space)
                    layout.addWidget(btn, row, col, 1, 6)
                elif key == 'Backspace':
                    btn.setFixedSize(150, 80)
                    btn.clicked.connect(self.handle_backspace)
                    layout.addWidget(btn, row, col, 1, 2)
                elif key == 'Enter':
                    btn.setFixedSize(150, 80)
                    btn.clicked.connect(self.handle_enter)
                    layout.addWidget(btn, row, col, 1, 2)
                elif key == 'Shift':
                    btn.setFixedSize(150, 80)
                    btn.clicked.connect(self.handle_special)
                    layout.addWidget(btn, row, col, 1, 2)
                elif key == 'Ctrl' and col == 0:
                    btn.setFixedSize(100, 80)
                    btn.clicked.connect(self.handle_special)
                    layout.addWidget(btn, row, col)
                elif key == 'Alt' and col == 1:
                    btn.setFixedSize(100, 80)
                    btn.clicked.connect(self.handle_special)
                    layout.addWidget(btn, row, col)
                elif key == 'Alt' and col == 3:
                    btn.setFixedSize(100, 80)
                    btn.clicked.connect(self.handle_special)
                    layout.addWidget(btn, row, col + 6)
                elif key == 'Ctrl' and col == 4:
                    btn.setFixedSize(100, 80)
                    btn.clicked.connect(self.handle_special)
                    layout.addWidget(btn, row, col + 6)
                else:
                    btn.setFixedSize(100, 80)
                    btn.clicked.connect(self.handle_button)
                    layout.addWidget(btn, row, col)

                btn.setStyleSheet("""
                    QPushButton {
                        background-color: #f0f0f0;
                        border: 2px solid #050505;
                        border-radius: 10px;
                        font-size: 18px;
                        font-weight: bold;
                        color: #333;
                        padding: 10px;
                        margin: 5px;
                    }
                    QPushButton:pressed {
                        background-color: #d0d0d0;
                    }
                """)

        # Add the Clear button below the Backspace button
        clear_btn = QPushButton("Clear")
        clear_btn.setFixedSize(150, 80)
        clear_btn.clicked.connect(self.handle_clear)
        clear_btn.setStyleSheet("""
            QPushButton {
                background-color: #f0f0f0;
                border: 2px solid black;
                border-radius: 10px;
                font-size: 18px;
                font-weight: bold;
                color: #333;
                padding: 10px;
                margin: 5px;
            }
            QPushButton:pressed {
                background-color: #d0d0d0;
            }
        """)
        layout.addWidget(clear_btn, 1, 13, 1, 2)  # Position below Backspace

        self.setLayout(layout)

    def handle_button(self):
        sender = self.sender()
        self.target_input.insert(sender.text())

    def handle_space(self):
        self.target_input.insert(' ')

    def handle_enter(self):
        self.target_input.insert('\n')

    def handle_backspace(self):
        current_text = self.target_input.text()
        self.target_input.setText(current_text[:-1])

    def handle_clear(self):
        self.target_input.clear()

    def handle_special(self):
        # Handle special keys like Shift, Ctrl, Alt, etc.
        pass

class AddBatteryWindow(QDialog):  # Add battery Window
    battery_added = pyqtSignal()  # Signal to notify when a battery is added
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle("Add New Battery")
        self.setFixedSize(1920, 1080)  # Set smaller window size
        self.main_window = main_window  # Store reference to MainWindow
        self.keyboard = None  # Initialize keyboard attribute

        # Top Background
        bg_widget = QWidget(self)
        bg_widget.setFixedSize(1920, 1080 // 10)
        bg_widget.setStyleSheet("""
            background-color: rgb(189, 221, 252);
            border: 2px solid black;  /* Border color and thickness */
        """)

        setup_logos(self)  # Call the Logos

        # Text inside the background
        layout = QVBoxLayout(bg_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        # Add New Battery Text
        text_label = QLabel("            ADD NEW BATTERY", self)
        text_label.setFont(QFont("Arial", 55, QFont.Bold))
        text_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(text_label)

        # Place the background widget at the top
        bg_widget.move(0, 0)

        # Side background
        side_bg_widget = QWidget(self)
        side_bg_widget.setFixedSize(1920 // 7, 1080)
        side_bg_widget.setStyleSheet("""
            background-color: rgb(102, 178, 214);
            border: 2px solid black;  /* Border color and thickness */
        """)

        self.clock_label, self.timer = setup_clock(self)
        self.date_label = date(self)  # Call the fixed date function
        home_button(self)
        history_button(self)


        # Dock Selection ComboBox
        self.dock_combo = QComboBox(self)
        self.dock_combo.setFont(QFont("Arial", 20))
        self.dock_combo.setFixedSize(400, 50)
        self.dock_combo.move(680, 150)
        self.dock_combo.addItems(["Select Dock", "DOCK 1", "DOCK 2", "DOCK 3", "DOCK 4", "DOCK 5", "DOCK 6"])

        # Battery ID Input
        self.battery_id_input = QLineEdit(self)
        self.battery_id_input.setPlaceholderText("Enter Battery ID")
        self.battery_id_input.setFont(QFont("Arial", 20))
        self.battery_id_input.setFixedSize(400, 50)
        self.battery_id_input.move(680, 250)
        self.battery_id_input.mousePressEvent = self.show_keyboard  # Connect mouse press event to show_keyboard

        # Add Battery Button
        self.add_battery_button = QPushButton("Add Battery", self)
        self.add_battery_button.setFont(QFont("Arial", 20))
        self.add_battery_button.setFixedSize(250, 70)
        self.add_battery_button.move(750, 330)
        self.add_battery_button.setStyleSheet("""
            QPushButton {
            }
            QPushButton:hover {
                background-color: #e0e0e0; /* Slightly darker gray on hover */
            }
            QPushButton:pressed {
                background-color: #d0d0d0; /* Even darker gray when pressed */
            }
        """)
        self.add_battery_button.clicked.connect(self.add_battery)


        # Total Batteries Label
        self.total_batteries_label = QLabel(self)
        self.total_batteries_label.setFont(QFont("Arial", 30, QFont.Bold))
        self.total_batteries_label.setFixedSize(500, 200)
        self.total_batteries_label.move(1100, 130)
        self.total_batteries_label.setStyleSheet("""
            color: Black;
            background-color: rgb(102, 178, 214);
            border: 2px solid #555;
            border-radius: 10px;
            padding: 20px;
            margin: 5px;
            font-size: 45px;
            font-weight: bold;
            text-align: center;
            box-shadow: 5px 5px 15px rgba(102, 178, 214, 0.6);
        """)
        self.total_batteries_label.setAlignment(Qt.AlignCenter)
        self.update_total_batteries()

        # List of Batteries Label
        self.list_of_batteries_label = QLabel("LIST OF \nBATTERIES", self)
        self.list_of_batteries_label.setFont(QFont("Arial", 20, QFont.Bold))
        self.list_of_batteries_label.setAlignment(Qt.AlignCenter)
        self.list_of_batteries_label.setFixedSize(250, 100)
        self.list_of_batteries_label.move(10, 350)

        # Battery ID List
        self.battery_id_list = QListWidget(self)
        self.battery_id_list.setFont(QFont("Arial", 20))
        self.battery_id_list.setFixedSize(250, 550)
        self.battery_id_list.move(10, 450)
        self.refresh_battery_id_list()  # Populate the list with battery IDs

    def close_window(self):
        """ Close this window and show the main window again """
        self.close()
        self.main_window.show()
    
    def open_history_window(self):
        """Open the History window."""
        if not hasattr(self, 'history_window_instance') or self.history_window_instance is None:
            self.history_window_instance = HistoryWindow(self)
        self.history_window_instance.show()

    def connect_db(self):
        return sqlite3.connect('batteries.db')

    def show_keyboard(self, event):
        try:
            if self.keyboard is None or not self.keyboard.isVisible():
                print("Showing keyboard")
                self.keyboard = OnScreenKeyboard(self.battery_id_input, self)
                self.keyboard.move(320, 470)  # Position the keyboard below the input field
                self.keyboard.show()
        except Exception as e:
            print(f"Error in show_keyboard: {e}")

    def add_battery(self):
        dock = self.dock_combo.currentText()
        battery_id = self.battery_id_input.text()
        if dock != "Select Dock" and battery_id:
            conn = self.connect_db()
            cursor = conn.cursor()
            cursor.execute('SELECT COUNT(*) FROM batteries WHERE battery_id = ?', (battery_id,))
            if cursor.fetchone()[0] > 0:
                QMessageBox.warning(self, "Duplicate Battery ID", f"Battery with ID {battery_id} already exists.")
                conn.close()
                return

            reply = QMessageBox.question(self, 'Confirm Addition',
                                        f"Are you sure you want to add battery with ID {battery_id} to {dock}?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                cursor.execute('INSERT INTO batteries (dock, battery_id) VALUES (?, ?)', (dock, battery_id))
                conn.commit()
                conn.close()
                QMessageBox.information(self, "Battery Added", f"Battery with ID {battery_id} has been added to {dock}.")
                self.dock_combo.setCurrentIndex(0)
                self.battery_id_input.clear()
                self.update_total_batteries()
                self.refresh_battery_id_list()  # Refresh the list after adding a new battery
                self.battery_added.emit()  # Emit the signal to notify that a battery has been added
            else:
                conn.close()
                print("Addition cancelled.")
        else:
            QMessageBox.warning(self, "Input Error", "Please select a dock and enter a valid Battery ID.")

    def update_total_batteries(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM batteries')
        total_batteries = cursor.fetchone()[0]
        conn.close()
        self.total_batteries_label.setText(f"TOTAL NUMBER \n OF BATTERIES\n{total_batteries}")

    def refresh_battery_id_list(self):
        """ Refresh the battery IDs in the list widget """
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT battery_id FROM batteries')
        battery_ids = [row[0] for row in cursor.fetchall()]
        conn.close()
        self.battery_id_list.clear()
        self.battery_id_list.addItems(battery_ids)

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
    
        # Top Background
        bg_widget = QWidget(self)
        bg_widget.setFixedSize(1920, 1080 // 10)
        bg_widget.setStyleSheet("""
            background-color: rgb(189, 221, 252);
            border: 2px solid black;  /* Border color and thickness */
        """)

        setup_logos(self) #Call the Logos

        # Text inside the background
        layout = QVBoxLayout(bg_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        # Main Menu Text
        text_label = QLabel("            DELETE EXISTING BATTERY", self)
        text_label.setFont(QFont("Arial", 55, QFont.Bold))
        text_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(text_label)

        # Place the background widget at the top
        bg_widget.move(0, 0)

        # Side background
        side_bg_widget = QWidget(self)
        side_bg_widget.setFixedSize(1920 // 7, 1080)
        side_bg_widget.setStyleSheet("""
            background-color: rgb(102, 178, 214);
            border: 2px solid black;  /* Border color and thickness */
        """)

        self.clock_label, self.timer = setup_clock(self)
        self.date_label = date(self)  # Call the fixed date function

        # Battery ID ComboBox
        self.battery_id_combo = QComboBox(self)
        self.battery_id_combo.setFont(QFont("Arial", 20))
        self.battery_id_combo.setFixedSize(400, 50)
        self.battery_id_combo.move(560, 300)
        self.refresh_battery_ids()  # Populate the combo box with battery IDs

        # Delete Button
        self.delete_button = QPushButton("Delete Battery", self)
        self.delete_button.setFont(QFont("Arial", 20))
        self.delete_button.setFixedSize(250, 70)
        self.delete_button.move(620, 400)
        self.delete_button.clicked.connect(self.delete_battery)
        self.delete_button.setStyleSheet("""
            QPushButton {
            }
            QPushButton:hover {
                background-color: #e0e0e0; /* Slightly darker gray on hover */
            }
            QPushButton:pressed {
                background-color: #d0d0d0; /* Even darker gray when pressed */
            }
        """)

        # Call the home_button function
        home_button(self)
        history_button(self)

         # Total Batteries Label
        self.total_batteries_label = QLabel(self)
        self.total_batteries_label.setFont(QFont("Arial", 30, QFont.Bold))
        self.total_batteries_label.setFixedSize(500, 200)
        self.total_batteries_label.move(1100, 280)
        self.total_batteries_label.setStyleSheet("""
            color: Black;
            background-color: rgb(102, 178, 214);
            border: 2px solid #555;
            border-radius: 10px;
            padding: 20px;
            margin: 5px;
            font-size: 45px;
            font-weight: bold;
            text-align: center;
            box-shadow: 5px 5px 15px rgba(102, 178, 214, 0.6);
        """)
        self.total_batteries_label.setAlignment(Qt.AlignCenter)
        self.update_total_batteries()

        # List of Batteries Label
        self.list_of_batteries_label = QLabel("LIST OF \nBATTERIES", self)
        self.list_of_batteries_label.setFont(QFont("Arial", 20, QFont.Bold))
        self.list_of_batteries_label.setAlignment(Qt.AlignCenter)
        self.list_of_batteries_label.setFixedSize(250, 100)
        self.list_of_batteries_label.move(10, 350)

        # Battery ID List
        self.battery_id_list = QListWidget(self)
        self.battery_id_list.setFont(QFont("Arial", 20))
        self.battery_id_list.setFixedSize(250, 550)
        self.battery_id_list.move(10, 450)
        self.refresh_battery_id_list()  # Populate the list with battery IDs

    def connect_db(self):
        return sqlite3.connect('batteries.db')
    
    def refresh_battery_ids(self):
        """ Refresh the battery IDs in the combo box """
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT battery_id FROM batteries')
        battery_ids = [row[0] for row in cursor.fetchall()]
        conn.close()
        self.battery_id_combo.clear()
        self.battery_id_combo.addItems(battery_ids)

    def close_window(self):
        """ Close this window and show the main window again """
        self.close()
        self.main_window.show()

    def open_history_window(self):
        """Open the History window."""
        if not hasattr(self, 'history_window_instance') or self.history_window_instance is None:
            self.history_window_instance = HistoryWindow(self)
        self.history_window_instance.show()

    def delete_battery(self):
        battery_id = self.battery_id_combo.currentText()
        if battery_id:
            reply = QMessageBox.question(self, 'Confirm Deletion',
                                         f"Are you sure you want to delete battery with ID {battery_id}?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                conn = self.connect_db()
                cursor = conn.cursor()
                cursor.execute('DELETE FROM batteries WHERE battery_id = ?', (battery_id,))
                conn.commit()
                conn.close()
                QMessageBox.information(self, "Battery Deleted", f"Battery with ID {battery_id} has been deleted.")
                self.refresh_battery_ids()  # Refresh the combo box after deletion
                self.update_total_batteries()
                self.refresh_battery_id_list()  # Refresh the list after adding a new battery
            else:
                print("Deletion cancelled.")
        else:
            QMessageBox.warning(self, "Input Error", "Please select a valid Battery ID.")

    def update_total_batteries(self):
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM batteries')
        total_batteries = cursor.fetchone()[0]
        conn.close()
        self.total_batteries_label.setText(f"TOTAL NUMBER \n OF BATTERIES\n{total_batteries}")
    
    def refresh_battery_id_list(self):
        """ Refresh the battery IDs in the list widget """
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute('SELECT battery_id FROM batteries')
        battery_ids = [row[0] for row in cursor.fetchall()]
        conn.close()
        self.battery_id_list.clear()
        self.battery_id_list.addItems(battery_ids)

class IDWindow(QDialog):  # ID Windows
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


        self.date_label = date(self)  # Call the fixed date function
        self.clock_label, self.timer = setup_clock(self)

        # ✅ Dock Status Overview Title
        self.title_label = QLabel(f"{BP_ID} - STATUS OVERVIEW", self)
        self.title_label.setFont(QFont("Arial", 40, QFont.Bold))
        self.title_label.setStyleSheet("background: transparent; color: black;")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFixedSize(1900, 50)
        self.title_label.move(175, 30)  

        # ✅ Return Button with Home Icon and Text
        self.close_button = QPushButton(self)
        self.close_button.setIcon(QIcon(r"C:\Users\jayro\Desktop\BATTERY SWAPING FILES\home.png"))  # Set the path to your home icon
        self.close_button.setIconSize(QSize(50, 50))  # Set the icon size
        self.close_button.setFixedSize(200, 70)  # Set button size
        self.close_button.setStyleSheet("text-align: left; padding-left: 10px;")  # Align text to the left with padding
        self.close_button.setText("Main Menu")  # Set the text
        self.close_button.setFont(QFont("Arial", 14))  # Set the font for the text
        self.close_button.move(40, 150)
        self.close_button.setAttribute(Qt.WA_Hover)
        self.close_button.setCursor(Qt.PointingHandCursor)
        self.close_button.clicked.connect(self.close_window)
                
       # ✅ Table Widget
        # Table setup
        layout = QVBoxLayout(bg_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        # Create and position table
        self.table_widget = self.create_tables()
        self.table_widget.setParent(self)  
        self.table_widget.move(285, 120)   #Table Position
        self.table_widget.show()       


    def create_tables(self):
        """ Creates and returns a QTableWidget with sample data. """
        table_widget = QTableWidget()
        table_widget.setRowCount(8)
        table_widget.setColumnCount(3)
        table_widget.setHorizontalHeaderLabels([
            "GROUP\n", "VOLTAGE\n(V)", "TEMPERATURE\n(°C)"
        ])

        header_font = QFont("Arial", 12, QFont.Bold)  # Header font and size
        header = table_widget.horizontalHeader()
        header.setFont(header_font)
        header.setDefaultAlignment(Qt.AlignCenter)  # Center text in header both horizontally and vertically
        table_widget.verticalHeader().setDefaultSectionSize(100)  # Adjust row height
        table_widget.horizontalHeader().setDefaultSectionSize(161)  # Adjust column width
        table_widget.setFixedSize(1620, 900)
        table_widget.setFont(QFont("Arial", 15))
        table_widget.verticalHeader().setVisible(False)
        table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        table_widget.setSelectionMode(QAbstractItemView.NoSelection)
        table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)  # Disable resizing columns
        table_widget.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)  # Disable resizing rows
        table_widget.setSelectionMode(QAbstractItemView.SingleSelection)
        table_widget.setSelectionBehavior(QAbstractItemView.SelectItems)
        
        # ✅ Styling
        table_widget.setStyleSheet("""
            QTableWidget {
                border: 3px solid black;
            }
            QHeaderView::section {
                background-color: lightgray;
                border: 2px solid black;
                font-weight: bold;
            }
            QTableWidget::item {
                border: 1px solid black;
            }
            QTableWidget::item:selected {
                background-color: rgb(189, 221, 252);
                color: Black;
            }
        """)

        # Sample data
        data = [
            ["GROUP 1"],
            ["GROUP 2"],
            ["GROUP 3"],
            ["GROUP 4"],
            ["GROUP 5",],
            ["GROUP 6",],
            ["GROUP 7",],
            ["GROUP 8",],
        ]

        for row, rowData in enumerate(data):
            for col, value in enumerate(rowData):
                item = QTableWidgetItem(value)
                item.setTextAlignment(Qt.AlignCenter)
                table_widget.setItem(row, col, item)
        return table_widget

    def close_window(self):
        """ Close this window and show the main window again """
        self.close()
        self.main_window.show()  
