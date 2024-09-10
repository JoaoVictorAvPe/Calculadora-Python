from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt
from utils import BIG_FONT_SIZE, TEXT_MARGIN, MINIMUN_WIDTH

class Display(QLineEdit):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setDisplayStyle()

    def setDisplayStyle(self) -> None:
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE)
        self.setMinimumWidth(MINIMUN_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*[TEXT_MARGIN for _ in range(4)])