from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from utils import SMALL_FONT_SIZE

class Info(QLabel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setInfoStyle()

    def setInfoStyle(self) -> None:
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px;')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)