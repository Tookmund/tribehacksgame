from PyQt5.QtGui import QPainter, QColor, QPen 

# Shapes
from Object import Object

class Rect(Object):
	def __init__(self, x, y, width, height, outline, fill):
		super().__init__(x, y)
		self.width = width
		self.height = height
		self.outline = QPen(outline)
		self.fill = QColor(fill)

	def paint(self, qp):
		qp.setPen(self.outline)
		qp.setBrush(self.fill)
		qp.drawRect(self.x, self.y, self.width, self.height)		
