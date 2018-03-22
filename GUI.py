import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QDesktopWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from user_path import UserPath
from pyhooked import Hook, KeyboardEvent


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.input = QLineEdit(self)
        self.hk = Hook()
        self.init_ui()

    def init_ui(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlags(Qt.SplashScreen | Qt.WindowStaysOnTopHint)

        self.resize(500, 110)
        self.center()

        self.setAutoFillBackground(True)
        widget_colour = self.palette()
        color = QColor('#1D1F21')
        widget_colour.setColor(self.backgroundRole(), color)
        self.setPalette(widget_colour)

        # input
        self.input.resize(450, 70)
        self.input.move(self.rect().center() - self.input.rect().center())
        self.input.returnPressed.connect(self.search)

        self.input.setStyleSheet("border: 0px;  background: #282a2e; color: #969896; font-size : 30px")

        self.hk.handler = self.on_keyboard_event
        self.hk.hook()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.input.setText("")
            self.destroy_gui()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def on_keyboard_event(self, args):
        if isinstance(args, KeyboardEvent):
            if args.current_key == 'Space' and args.event_type == 'key down' and 'Lcontrol' in args.pressed_key:
                self.display_gui()

    def search(self):
        if self.input.text() == "close":
            sys.exit()

        path = UserPath(self.input.text()).match()
        if path != "":
            self.destroy_gui()
            subprocess.Popen(path)
            self.input.setText("")

    def destroy_gui(self):
        self.hide()

    def display_gui(self):
        self.show()
        self.input.activateWindow()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

