from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from utils import MEDIUM_FONT_SIZE
from display import Display
from styles import qss
import re

def isNumOrDot(text: str) -> bool:
    return bool(re.search(r'^[0-9.]$', text))

class Button(QPushButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self) -> None:
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)

class ButtonsGrid(QGridLayout):
    def __init__(self, display: Display, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._grid_mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = display

        self._makeGrid()

    def _makeGrid(self):
        for i, row in enumerate(self._grid_mask):
            for j, button_text in enumerate(row):
                button = Button(button_text)
                if not isNumOrDot(button_text) and button_text != '':
                    button.setProperty('cssClass', 'specialButton')
                    button.setStyleSheet(button.styleSheet() + qss)
                self.addWidget(button, i, j)
                buttonSlot = self._makeButtonDisplaySlot(self._insertButtoTextToDisplay, button)
                button.clicked.connect(buttonSlot)

    def _makeButtonDisplaySlot(self, func, *args, **kwargs):
        @Slot()
        def realSlot():
            func(*args, **kwargs)
        return realSlot

    def _insertButtoTextToDisplay(self, button: Button):
        self.display.insert(button.text())

if __name__ == "__main__":
    buttons_grid = ButtonsGrid()
    buttons_grid._makeGrid()