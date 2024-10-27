import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QColor

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QColor Background Example")
        self.setGeometry(100, 100, 300, 200)

        # Initialize the background color using QColor
        self.background_color = QColor(173, 216, 230)  # Light blue color

        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Set the background color using QColor converted to string
        self.set_background_color(central_widget)

        # Create a layout and add a button
        layout = QVBoxLayout()
        button = QPushButton("Click Me")
        layout.addWidget(button)

        central_widget.setLayout(layout)

    def set_background_color(self, widget):
        # Convert QColor to a string in hex format
        color_string = self.background_color.name()  # This will give you the hex color code
        widget.setStyleSheet(f"background-color: {color_string};")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
