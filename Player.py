from PyQt5 import QtCore
from PyQt5.QtGui import QPainter, QColor, QPen
from Object import Object

class Player(Object):

	def __init__(self, x, y):
		super().__init__(x,y)
		self.size = 10
		self.outline = QPen(QtCore.Qt.black)
		self.fill = QColor(QtCore.Qt.red)

	def paint(self, qp):
		qp.setPen(self.outline)
		qp.setBrush(self.fill)
		qp.drawEllipse(self.x,self.y,self.size,self.size)

	def move(self,dx,dy,objs):
		newx = self.x + dx
		newy = self.y + dy
		if self._check(newx, newy, objs[0]):
			return 10
		for obj in objs[1:]:
			if self._check(newx, newy, obj):
				return False
		self.x += dx
		self.y += dy
		return 1

	def _check(self, newx, newy, obj):
		if self == obj:
			return
		return (obj.x <= (newx+(self.size/2)) <= (obj.x+obj.width) and obj.y <= (newy+self.size/2) <= (obj.y+obj.height))
