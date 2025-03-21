from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


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

        # Main Menu Text
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

        # Digital Clock Label (Top Left)
        self.clock_label = QLabel(self)
        self.clock_label.setFont(QFont("DS Digital", 27, QFont.Bold))
        self.clock_label.setStyleSheet("""
            color: white;
            background-color: #333;
            border: 2px solid #555;
            border-radius: 10px;
            padding: 5px;
        """)
        self.clock_label.setAlignment(Qt.AlignCenter)
        self.clock_label.setFixedSize(230, 60)
        self.clock_label.move(20, 20)  # Position in the top-left corner

        # Start the clock update timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every second
        self.update_time()  # Update the clock immediately

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
        self.add_battery_button.setFixedSize(200, 50)
        self.add_battery_button.move(780, 350)
        self.add_battery_button.clicked.connect(self.add_battery)

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
        self.total_batteries_label.setAlignment(Qt.AlignCenter)  # Center the text
        self.update_total_batteries()

    def show_keyboard(self, event):
        try:
            if self.keyboard is None or not self.keyboard.isVisible():
                print("Showing keyboard")
                self.keyboard = OnScreenKeyboard(self.battery_id_input, self)
                self.keyboard.move(320, 470)  # Position the keyboard below the input field
                self.keyboard.show()
        except Exception as e:
            print(f"Error in show_keyboard: {e}")

    def update_time(self):
        """ Updates the digital clock every second. """
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.clock_label.setText(current_time)

    def close_window(self):
        """ Close this window and show the main window again """
        self.close()
        self.main_window.show()

    def add_battery(self):
        """ Add the new battery with the entered ID """
        dock = self.dock_combo.currentText()
        battery_id = self.battery_id_input.text()
        if dock != "Select Dock" and battery_id:
            # Implement the logic to add the battery with the given ID to the selected dock
            # For example, you can add the battery to a list or database
            print(f"Adding battery with ID: {battery_id} to {dock}")
            # Show a message box to confirm addition
            QMessageBox.information(self, "Battery Added", f"Battery with ID {battery_id} has been added to {dock}.")
            # Clear the input fields
            self.dock_combo.setCurrentIndex(0)
            self.battery_id_input.clear()
            self.update_total_batteries()
        else:
            QMessageBox.warning(self, "Input Error", "Please select a dock and enter a valid Battery ID.")

    def update_total_batteries(self):
        """ Update the total number of batteries label """
        # For now, just a placeholder count. You can replace this with actual logic later.
        total_batteries = 6  # Placeholder value
        self.total_batteries_label.setText(f"TOTAL NUMBER \n OF BATTERIES\n{total_batteries}")

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

        # Digital Clock Label (Top Left)
        self.clock_label = QLabel(self)
        self.clock_label.setFont(QFont("DS Digital", 27, QFont.Bold))
        self.clock_label.setStyleSheet("""
            color: white;
            background-color: #333;
            border: 2px solid #555;
            border-radius: 10px;
            padding: 5px;
        """)
        self.clock_label.setAlignment(Qt.AlignCenter)
        self.clock_label.setFixedSize(230, 60)
        self.clock_label.move(20, 20)  # Position in the top-left corner

        # Start the clock update timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every second
        self.update_time()  # Update the clock immediately

        # Battery ID ComboBox
        self.battery_id_combo = QComboBox(self)
        self.battery_id_combo.setFont(QFont("Arial", 20))
        self.battery_id_combo.setFixedSize(400, 50)
        self.battery_id_combo.move(560, 300)
        self.battery_id_combo.addItems(["BP01", "BP02", "BP03", "BP04", "BP05", "BP06"])  # Add battery IDs

        # Delete Button
        self.delete_button = QPushButton("Delete Battery", self)
        self.delete_button.setFont(QFont("Arial", 20))
        self.delete_button.setFixedSize(300, 50)
        self.delete_button.move(620, 400)
        self.delete_button.clicked.connect(self.delete_battery)

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

         # Total Batteries Label
        self.total_batteries_label = QLabel(self)
        self.total_batteries_label.setFont(QFont("Arial", 30, QFont.Bold))
        self.total_batteries_label.setFixedSize(500, 500)
        self.total_batteries_label.move(1060, 120)
        self.update_total_batteries()

    def update_time(self):
        """ Updates the digital clock every second. """
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.clock_label.setText(current_time)

    def close_window(self):
        """ Close this window and show the main window again """
        self.close()
        self.main_window.show()

    def delete_battery(self):
        """ Delete the battery with the selected ID """
        battery_id = self.battery_id_combo.currentText()
        if battery_id:
            # Show a confirmation dialog
            reply = QMessageBox.question(self, 'Confirm Deletion',
                                         f"Are you sure you want to delete battery with ID {battery_id}?",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                # Implement the logic to delete the battery with the given ID
                # For example, you can remove the battery from a list or database
                print(f"Deleting battery with ID: {battery_id}")
                # Show a message box to confirm deletion
                QMessageBox.information(self, "Battery Deleted", f"Battery with ID {battery_id} has been deleted.")
            else:
                print("Deletion cancelled.")
        else:
            QMessageBox.warning(self, "Input Error", "Please select a valid Battery ID.")

    def update_total_batteries(self):
            """ Update the total number of batteries label """
            total_batteries = self.battery_id_combo.count()
            self.total_batteries_label.setText(f"TOTAL NUMBER \n OF BATTERIES\n              {total_batteries}")

class IDWindow(QDialog):  # Generic Dock Window for all docks
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

        # Digital Clock Label (Top Left)
        self.clock_label = QLabel(self)
        self.clock_label.setFont(QFont("DS Digital", 27, QFont.Bold))
        self.clock_label.setStyleSheet("""
            color: white;
            background-color: #333;
            border: 2px solid #555;
            border-radius: 10px;
            padding: 5px;
        """)
        self.clock_label.setAlignment(Qt.AlignCenter)
        self.clock_label.setFixedSize(230, 60)
        self.clock_label.move(20, 20)  # Position in the top-left corner

        # Start the clock update timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every second
        self.update_time()  # Update the clock immediately

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
    
    def update_time(self):
        """ Updates the digital clock every second. """
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.clock_label.setText(current_time)

    def close_window(self):
        """ Close this window and show the main window again """
        self.close()
        self.main_window.show()  
