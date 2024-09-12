import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from main_window import MainWindow
from display import Display
from info import Info
from buttons import Button, ButtonsGrid
from styles import setupTheme
from utils import ICON_PATH

if __name__ == "__main__":
    app = QApplication(sys.argv)
    setupTheme(app)

    window = MainWindow()

    info = Info('20 + 7')
    window.addWidgetToVBoxLayout(info)

    display = Display()
    display.setPlaceholderText('Digite um texto')
    window.addWidgetToVBoxLayout(display)

    buttons_grid = ButtonsGrid()
    window.vbox_layout.addLayout(buttons_grid)


    icon = QIcon(str(ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    window.adjustFixedSize()
    window.show()
    app.exec()