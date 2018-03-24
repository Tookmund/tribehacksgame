from PyQt5.QtGui import QPainter, QColor, QPen
import random

# Shapes
from Object import Object


class Shape(Object):
	def _randomcolor(self):
		return QColor(random.randint(0,255),random.randint(0,255),random.randint(0,255))

	def __init__(self, x, y, width=None, height=None, outline=None, fill=None):
		super().__init__(x, y)
		if width is None:
			width = random.randint(10,100)
		self.width = width
		if height is None:
			height = random.randint(10,100)
		self.height = height
		if outline is None:
			outline = self._randomcolor()
		if fill is None:
			fill = self._randomcolor()
		self.outline = QPen(outline)
		self.fill = QColor(fill)

	def paint(self, qp):
		qp.setPen(self.outline)
		qp.setBrush(self.fill)

class Rect(Shape):
	def paint(self, qp):
		super().paint(qp)
		qp.drawRect(self.x, self.y, self.width, self.height)

class Circle(Shape):
	def __init__(self, x, y, size=None, outline=None, fill=None):
		if size is None:
			size = random.randint(10,100)
		super().__init__(x, y, size, size, outline, fill)

	def paint(self, qp):
		super().paint(qp)
		qp.drawEllipse(self.x, self.y, self.width, self.height)
