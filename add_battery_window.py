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

class AddBatteryWindow(QDialog):  # Add battery Window
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle("Add New Battery")
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

    def update_time(self):
        """ Updates the digital clock every second. """
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.clock_label.setText(current_time)

    def close_window(self):
        """ Close this window and show the main window again """
        self.close()
        self.main_window.show()
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
            self.total_batteries_label.setText(f"TOTAL NUMBER \nOF BATTERIES\n              {total_batteries}")

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
