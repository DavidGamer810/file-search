
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QListWidget,
    QVBoxLayout, QHBoxLayout
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("File Viewer")
        self.setGeometry(100, 100, 800, 600)
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout(self)

        # Top layout
        top_layout = QHBoxLayout()

        # --- Smaller left panel (Files button + list)
        left_panel = QVBoxLayout()
        self.files_button = QPushButton("Files")
        left_panel.addWidget(self.files_button)

        self.file_list = QListWidget()
        self.file_list.setFixedWidth(150)  # Make file list narrower
        left_panel.addWidget(self.file_list)

        # Combine with "Image" label
        left_side = QHBoxLayout()
        left_side.addLayout(left_panel)

        self.image_text_label = QLabel("Image")
        self.image_text_label.setAlignment(Qt.AlignCenter)
        self.image_text_label.setFixedWidth(80)
        left_side.addWidget(self.image_text_label)

        top_layout.addLayout(left_side)

        # --- Image display area
        self.image_display = QLabel()
        self.image_display.setAlignment(Qt.AlignCenter)
        self.image_display.setStyleSheet("border: 1px solid black;")
        self.image_display.setFixedSize(500, 400)
        top_layout.addWidget(self.image_display)

        # --- Bottom layout with buttons
        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(QPushButton("Left"))
        bottom_layout.addWidget(QPushButton("Right"))
        bottom_layout.addWidget(QPushButton("Button 3"))
        bottom_layout.addWidget(QPushButton("Button 4"))
        bottom_layout.addWidget(QPushButton("Button 5"))

        # Add layouts to main layout
        main_layout.addLayout(top_layout)
        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
