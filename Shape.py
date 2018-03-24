from PyQt5.QtGui import QPainter, QColor, QPen 
import random

# Shapes
from Object import Object

def randomcolor():
	return QColor(random.randint(0,255),random.randint(0,255),random.randint(0,255))

class Rect(Object):
	def __init__(self, x, y, width=None, height=None, outline=None, fill=None):
		super().__init__(x, y)
		if width is None:
			width = random.randint(10,100)
		self.width = width
		if height is None:
			height = random.randint(10,100)
		self.height = height
		if outline is None:
			outline = randomcolor()
		if fill is None:
			fill = randomcolor()
		self.outline = QPen(outline)
		self.fill = QColor(fill)

	def paint(self, qp):
		qp.setPen(self.outline)
		qp.setBrush(self.fill)
		qp.drawRect(self.x, self.y, self.width, self.height)		
