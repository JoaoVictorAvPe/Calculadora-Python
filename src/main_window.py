from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.central_widget = QWidget()
        self.vbox_layout = QVBoxLayout()

        self.central_widget.setLayout(self.vbox_layout)
        self.setCentralWidget(self.central_widget)
        self.setWindowTitle('Calculadora')

    
    def adjustFixedSize(self) -> None:
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def addWidgetToVBoxLayout(self, widget: QWidget) -> None:
        self.vbox_layout.addWidget(widget)