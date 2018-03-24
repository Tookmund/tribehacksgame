#!/usr/bin/python3
# Main Window

from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QWidget
from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt5.QtGui import QPainter, QColor 
import sys, random

from Shape import Rect
from Player import Player
class Window(QMainWindow):
	def __init__(self):
		super().__init__()
		self.resize(640,480)
		self.setWindowTitle("GAME")
		self.frame = Frame(self)
		self.show()

class Frame(QWidget):
	def __init__(self, parent):
		super().__init__(parent)
		self.player = Player(50,50)
		self.objects = [self.player]
		self.grabKeyboard()
		self.show()

	def paintEvent(self, event):
		qp = QPainter(self)
		qp.begin(self)
		for obj in self.objects:
			obj.paint(qp)
		qp.end()

	def keyPressEvent(self, event):
		self.player.keypress(event.key())

if __name__ == "__main__":
	app = QApplication([])
	win = Window()
	win.create()
	sys.exit(app.exec_())
