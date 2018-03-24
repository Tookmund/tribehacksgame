from PyQt5 import QtCore
from PyQt5.QtGui import QPainter, QColor, QPen
from Object import Object

class Player(Object):

	def __init__(self, x, y):
		super().__init__(x,y)
		self.size = 100
		self.outline = QPen(QtCore.Qt.black)
		self.fill = QColor(QtCore.Qt.red)

	def paint(self, qp):
		qp.setPen(self.outline)
		qp.setBrush(self.fill)
		qp.drawRect(self.x,self.y,self.size,self.size)

	def move(self,dx,dy):
		self.x += dx
		self.y += dy
