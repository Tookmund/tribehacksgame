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
		self.frame = Frame(self, 640, 480)
		self.show()

class Frame(QWidget):
	def __init__(self, parent, w, h):
		super().__init__(parent)
		self.player = Player(0,0)
		self.objects = [self.player]
		self.grabKeyboard()
		self.setGeometry(0, 0, w, h)
		self.show()

	def paintEvent(self, event):
		qp = QPainter(self)
		#qp.begin(self)
		for obj in self.objects:
			obj.paint(qp)
		#qp.end()
		print(self.player.x, " ", self.player.y)

	def keyPressEvent(self, event):
		d = 10
		if event.key() == Qt.Key_W:
			self.player.move(0,-d)
		elif event.key() == Qt.Key_S:
			self.player.move(0,d)
		elif event.key() == Qt.Key_A:
			self.player.move(-d,0)
		elif event.key() == Qt.Key_D:
			self.player.move(d,0)
		self.repaint()
if __name__ == "__main__":
	app = QApplication([])
	win = Window()
	win.create()
	sys.exit(app.exec_())
