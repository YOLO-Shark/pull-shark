import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox, QLabel
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt, QTimer, QPoint, QRect

import random

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Create a dropdown and a label to display text next to it
        self.dropdown = QComboBox(self)
        self.dropdown.addItems(['Random Position', 'Click to Close'])
        self.dropdown.currentIndexChanged.connect(self.update_dropdown_text)
        self.dropdown.move(20, 20)

        self.dropdown_label = QLabel('Current option: ' + self.dropdown.currentText(), self)
        self.dropdown_label.move(20 + self.dropdown.width() + 10, 20)

        # Create a button in the middle of the window
        self.button = QPushButton('Click me', self)
        self.button.move(self.width() // 2 - self.button.width() // 2,
                          self.height() // 2 - self.button.height() // 2)
        self.button.clicked.connect(self.on_button_clicked)

        # Set up a timer to update the button position
        self.timer = QTimer(interval=1000/30, timeout=self.update_button_position)
        self.timer.start()

    def update_dropdown_text(self, index):
        # Update the text next to the dropdown based on the current selection
        self.dropdown_label.setText('Current option: ' + self.dropdown.currentText())

    def update_button_position(self):
        # Get the position of the cursor relative to the widget
        cursor_pos = self.mapFromGlobal(QCursor.pos())

        if self.dropdown.currentIndex() == 0:
            # Option 1: don't move the button
            pass
        else:
            # Option 2: check if the cursor is over the button, and move the button to a random position
            button_rect = QRect(self.button.pos(), self.button.size())
            if button_rect.contains(cursor_pos):
                new_pos = QPoint(random.randint(0, self.width() - self.button.width()),
                                 random.randint(0, self.height() - self.button.height()))
                self.button.move(new_pos)

    def resizeEvent(self, event):
        # When the window is resized, center the button again
        self.button.move(self.width() // 2 - self.button.width() // 2,
                          self.height() // 2 - self.button.height() // 2)

    def on_button_clicked(self):
        if self.dropdown.currentIndex() == 0:
            # If option 1 is selected, close the window when the button is clicked
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())
