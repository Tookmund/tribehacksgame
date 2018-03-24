#!/usr/bin/python3
# Main Window

from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QWidget
from PyQt5.QtCore import Qt, QBasicTimer
from PyQt5.QtGui import QPainter, QColor
import sys, random

from Shape import Rect
from Player import Player
from Text import Text

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
		self.timer = QBasicTimer()
		self.stuckTimer = QBasicTimer()
		self.show()
		self.timer.start(500,self)
		self.stuckTimer.start(2000,self)

	def paintEvent(self, event):
		qp = QPainter(self)
		for obj in self.objects:
			obj.paint(qp)

	def timerEvent(self, event):
		self.objects.append(Rect(random.randint(0,649),random.randint(0,481)))
		if event.timerId() == 2:
			if not self.player.move(0,0,self.objects):
				self.objects.append(Text(self.width()/2,self.height()/2,"You Deaded"))
		self.repaint()

	def keyPressEvent(self, event):
		d = 10
		if event.key() == Qt.Key_W:
			self.player.move(0,-d,self.objects)
		elif event.key() == Qt.Key_S:
			self.player.move(0,d,self.objects)
		elif event.key() == Qt.Key_A:
			self.player.move(-d,0,self.objects)
		elif event.key() == Qt.Key_D:
			self.player.move(d,0,self.objects)
		self.repaint()


if __name__ == "__main__":
	app = QApplication([])
	win = Window()
	sys.exit(app.exec_())
