from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from add_battery_window import *  # Import the AddBatteryWindow


class MainWindow(QMainWindow): #Main Window
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BATTERY SWAPPING SYSTEM")

        # Window Size
        self.setFixedSize(1920, 1080)

        # Create a central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        central_widget_layout = QVBoxLayout(central_widget)

        # top Background
        bg_widget = QWidget(self)
        bg_widget.setFixedSize(1920, 1080 // 10)
        bg_widget.setStyleSheet("""
            background-color: rgb(189, 221, 252);
            border: 2px solid black;  /* Border color and thickness */
        """)

        # Text inside the background
        layout = QVBoxLayout(bg_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        # Main Menu Text with Outline
        text_label = OutlinedLabel("            BATTERY INFORMATION SYSTEM", self)
        text_label.setFont(QFont("Berlin Sans FB", 55))
        text_label.setAlignment(Qt.AlignCenter)
        text_label.setOutlineColor("white")  # outline color
        text_label.setTextColor("black")     # main text color
        text_label.setOutlineThickness(5)    # outline thickness

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

        # Table setup
        layout = QVBoxLayout(bg_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        # Create and position table
        self.table_widget = self.create_tables()
        self.table_widget.setParent(self)  
        self.table_widget.move(285, 120)   #Table Position
        self.table_widget.show()          


        # TOTAL BATTERY AVAILABLE
        self.battery_available = QLabel("TOTAL BATTERY \nAVAILABLE", self)
        self.battery_available.setFont(QFont("Arial", 15, QFont.Bold))
        self.battery_available.setStyleSheet("""
            color: black;
            background-color: #f0f0f0;
            border: 2px solid #000;
            border-radius: 10px;
            padding: 10px;
            margin: 5px;
        """)
        self.battery_available.setAlignment(Qt.AlignCenter)
        self.battery_available.setFixedSize(250, 100)  # Adjust height to fit text only
        self.battery_available.move(15, 360)
        self.battery_available.raise_()

        # TOTAL BATTERY AVAILABLE DISPLAY
        self.available_display = QLabel("1", self)
        self.available_display.setFont(QFont("Arial", 50, QFont.Bold))
        self.available_display.setStyleSheet("""
            color: black;
            background-color: #e0e0e0;
            border: 2px solid #000;
            border-radius: 10px;
            padding: 10px;
            margin: 5px;
        """)
        self.available_display.setAlignment(Qt.AlignCenter)
        self.available_display.setFixedSize(250, 100)  # Adjust height to fit text only
        self.available_display.move(15, 470)
        self.available_display.raise_()


        # TOTAL BATTERY CHARGING
        self.battery_charging = QLabel("TOTAL BATTERY \nCHARGING", self)
        self.battery_charging.setFont(QFont("Arial", 15, QFont.Bold))
        self.battery_charging.setStyleSheet("""
            color: black;
            background-color: #f0f0f0;
            border: 2px solid #000;
            border-radius: 10px;
            padding: 10px;
            margin: 5px;
        """)
        self.battery_charging.setAlignment(Qt.AlignCenter)
        self.battery_charging.setFixedSize(250, 100)  # Adjust height to fit text only
        self.battery_charging.move(15, 590)
        self.battery_charging.raise_()

        # TOTAL BATTERY CHARGING DISPLAY
        self.charging_display = QLabel("2", self)
        self.charging_display.setFont(QFont("Arial", 50, QFont.Bold))
        self.charging_display.setStyleSheet("""
            color: black;
            background-color: #e0e0e0;
            border: 2px solid #000;
            border-radius: 10px;
            padding: 10px;
            margin: 5px;
        """)
        self.charging_display.setAlignment(Qt.AlignCenter)
        self.charging_display.setFixedSize(250, 100)  # Adjust height to fit text only
        self.charging_display.move(15, 700)
        self.charging_display.raise_()


        # TOTAL EMPTY BATTERY DOCK
        self.battery_dock = QLabel("EMPTY BATTERY \nDOCK", self)
        self.battery_dock.setFont(QFont("Arial", 15, QFont.Bold))
        self.battery_dock.setStyleSheet("""
            color: black;
            background-color: #f0f0f0;
            border: 2px solid #000;
            border-radius: 10px;
            padding: 10px;
            margin: 5px;
        """)
        self.battery_dock.setAlignment(Qt.AlignCenter)
        self.battery_dock.setFixedSize(250, 100)  # Adjust height to fit text only
        self.battery_dock.move(15, 820)
        self.battery_dock.raise_()

        # BATTERY DOCK DISPLAY
        self.dock_display = QLabel("2", self)
        self.dock_display.setFont(QFont("Arial", 50, QFont.Bold))
        self.dock_display.setStyleSheet("""
            color: black;
            background-color: #e0e0e0;
            border: 2px solid #000;
            border-radius: 10px;
            padding: 10px;
            margin: 5px;
        """)
        self.dock_display.setAlignment(Qt.AlignCenter)
        self.dock_display.setFixedSize(250, 100)  # Adjust height to fit text only
        self.dock_display.move(15, 930)
        self.dock_display.raise_()

        # Line between TOTAL EMPTY BATTERY DOCK and BATTERY DOCK DISPLAY
        self.line_dock = QFrame(self)
        self.line_dock.setFrameShape(QFrame.HLine)
        self.line_dock.setFrameShadow(QFrame.Sunken)
        self.line_dock.setStyleSheet("background-color: black;")
        self.line_dock.setGeometry(15, 580, 250, 3)  # Adjust position and size of the line

        # Line
        self.line_dock = QFrame(self)
        self.line_dock.setFrameShape(QFrame.HLine)
        self.line_dock.setFrameShadow(QFrame.Sunken)
        self.line_dock.setStyleSheet("background-color: black;")
        self.line_dock.setGeometry(15, 580, 250, 3)  # Adjust position and size of the line

        # Line 
        self.line_dock = QFrame(self)
        self.line_dock.setFrameShape(QFrame.HLine)
        self.line_dock.setFrameShadow(QFrame.Sunken)
        self.line_dock.setStyleSheet("background-color: black;")
        self.line_dock.setGeometry(15, 810, 250, 3)  # Adjust position and size of the line

        # Add Image (Clickable)
        self.battery_image = QLabel(self)
        pixmap = QPixmap(r"C:\Users\jayro\Desktop\BATTERY SWAPING FILES\add.png")
        self.battery_image.setPixmap(pixmap)
        self.battery_image.setScaledContents(True)
        self.battery_image.setFixedSize(100, 100)   # Set exact size
        self.battery_image.move(10, 120)  # Center it below the text
        self.battery_image.setCursor(Qt.PointingHandCursor)  # Make it show a clickable cursor
        self.battery_image.mousePressEvent = self.add_battery_clicked  # Assign event

        # Remove Battery (Clickable QLabel)
        self.remove_battery = QLabel("DELETE \nBATTERY", self)
        self.remove_battery.setFont(QFont("Arial", 20, QFont.Bold))
        self.remove_battery.setStyleSheet("color: black;")
        self.remove_battery.setAlignment(Qt.AlignCenter)
        self.remove_battery.setFixedSize(300, 80)  # Reduce height to fit text only
        self.remove_battery.move(20, 230)
        self.remove_battery.raise_()
        self.remove_battery.setAttribute(Qt.WA_Hover)
        self.remove_battery.setCursor(Qt.PointingHandCursor)
        self.remove_battery.mousePressEvent = self.remove_battery_clicked  # Assign event

        # Add Battery (Clickable QLabel)
        self.add_battery = QLabel("ADD NEW \nBATTERY", self)
        self.add_battery.setFont(QFont("Arial", 20, QFont.Bold))
        self.add_battery.setStyleSheet("color: black;")
        self.add_battery.setAlignment(Qt.AlignCenter)
        self.add_battery.setFixedSize(300, 80)  # Reduce height to fit text only
        self.add_battery.move(20, 130)
        self.add_battery.raise_()
        self.add_battery.setAttribute(Qt.WA_Hover)
        self.add_battery.setCursor(Qt.PointingHandCursor)
        self.add_battery.mousePressEvent = self.remove_battery_clicked  # Assign event

        # Make only the text clickable
        self.add_battery.setAttribute(Qt.WA_Hover)
        self.add_battery.setCursor(Qt.PointingHandCursor)
        self.add_battery.mousePressEvent = self.add_battery_clicked  # Assign event

        # Remove Image (Clickable)
        self.remove_image = QLabel(self)
        pixmap = QPixmap(r"C:\Users\jayro\Desktop\BATTERY SWAPING FILES\remove.png")
        self.remove_image.setPixmap(pixmap)
        self.remove_image.setScaledContents(True)
        self.remove_image.setFixedSize(100, 100)   # Set exact size
        self.remove_image.move(10, 220)  # Center it below the text
        self.remove_image.setCursor(Qt.PointingHandCursor)  # Make it show a clickable cursor
        self.remove_image.mousePressEvent = self.remove_battery_clicked  # Assign event

        # CSU LOGO
        self.CSU_LOGO = QLabel(self)
        pixmap = QPixmap(r"C:\Users\jayro\Desktop\BATTERY SWAPING FILES\csulogo.png")
        self.CSU_LOGO.setPixmap(pixmap)
        self.CSU_LOGO.setScaledContents(True)
        self.CSU_LOGO.setFixedSize(100, 100)   # Set exact size
        self.CSU_LOGO.move(1155, 935)  # Center it below the text

        # PCIEERD LOGO
        self.CSU_LOGO = QLabel(self)
        pixmap = QPixmap(r"C:\Users\jayro\Desktop\BATTERY SWAPING FILES\PCIEERD.png")
        self.CSU_LOGO.setPixmap(pixmap)
        self.CSU_LOGO.setScaledContents(True)
        self.CSU_LOGO.setFixedSize(100, 100)   # Set exact size
        self.CSU_LOGO.move(850, 935)  # Center it below the text

        # NICER LOGO
        self.CSU_LOGO = QLabel(self)
        pixmap = QPixmap(r"C:\Users\jayro\Desktop\BATTERY SWAPING FILES\NICER.png")
        self.CSU_LOGO.setPixmap(pixmap)
        self.CSU_LOGO.setScaledContents(True)
        self.CSU_LOGO.setFixedSize(230, 100)   # Set exact size
        self.CSU_LOGO.move(950, 935)  # Center it below the text

        # EMRDC LOGO
        self.CSU_LOGO = QLabel(self)
        pixmap = QPixmap(r"C:\Users\jayro\Desktop\BATTERY SWAPING FILES\EMRDC.png")
        self.CSU_LOGO.setPixmap(pixmap)
        self.CSU_LOGO.setScaledContents(True)
        self.CSU_LOGO.setFixedSize(130, 130)   # Set exact size
        self.CSU_LOGO.move(1250, 920)  # Center it below the text
        

    def add_battery_clicked(self, event):
        self.hide()  # Hide main window instead of closing it
        self.add_battery_window = AddBatteryWindow(self)  # Pass reference to main window
        self.add_battery_window.exec_()  # Open AddBatteryWindow as modal

    def remove_battery_clicked(self, event):
        self.hide()  # Hide main window instead of closing it
        self.delete_battery_window = DeleteBatteryWindow(self)  # Pass reference to main window
        self.delete_battery_window.exec_()  # Open AddBatteryWindow as modal

    def update_time(self):
        """ Updates the digital clock every second. """
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.clock_label.setText(current_time)

    def create_tables(self):
        """ Creates and returns a QTableWidget with sample data. """
        table_widget = QTableWidget()
        table_widget.setRowCount(6)
        table_widget.setColumnCount(10)
        table_widget.setHorizontalHeaderLabels([
            "BATTERY\nDOCK", "BATTERY\nID", "BATTERY\nSTATUS", "CHARGING\nSTATUS",
            "VOLTAGE\n(V)", "BATTERY\nPERCENTAGE\n(%)", "BATTERY\nTEMPERATURE\n(°C)",
            "CURRENT\n(A)", "CYCLE\nCOUNT", "CHARGING\nTIME"
        ])
        
        # ✅ Connect click event
        table_widget.cellClicked.connect(self.cell_clicked)

        header_font = QFont("Arial", 12, QFont.Bold)  # Header font and size
        header = table_widget.horizontalHeader()
        header.setFont(header_font)
        table_widget.verticalHeader().setDefaultSectionSize(100)  # Adjust row height
        table_widget.horizontalHeader().setDefaultSectionSize(161)  # Adjust column width
        table_widget.setFixedSize(1620, 800)
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
            ["DOCK 1", "BP01", "Available", "85%"],
            ["DOCK 2", "BP02", "In Use", "50%"],
            ["DOCK 3", "BP03", "Charging", "30%"],
            ["DOCK 4", "BP04", "Charging", "30%"],
            ["DOCK 5",],
            ["DOCK 6",]
        ]

        for row, rowData in enumerate(data):
            for col, value in enumerate(rowData):
                item = QTableWidgetItem(value)
                item.setTextAlignment(Qt.AlignCenter) 
                # Check if the value is "DOCK 1", "DOCK 2", "DOCK 3", or "DOCK 4"
                if col == 0 and value.startswith("DOCK"):
                    font = QFont()
                    font.setPointSize(15)  # Set font size for dock names
                    font.setBold(True)  # Make it bold
                    item.setFont(font)

                table_widget.setItem(row, col, item)

        return table_widget

    def cell_clicked(self, row, column):
            """ Open a new window when a DOCK is clicked and hide MainWindow """
            if column == 1:  
                item = self.table_widget.item(row, column)
                if item:
                    BP_ID = item.text()  
                    if BP_ID in ["BP01", "BP02", "BP03", "BP04"]:  
                        self.hide()  # Hide the main window
                        self.ID_window = IDWindow(BP_ID, self)  
                        self.ID_window.exec_()  # Open as modal dialog


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
