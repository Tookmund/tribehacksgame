# Objects
from PyQt5.QtGui import QPen, QColor

class Object:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def paint(self, qp):
		print("You Can't Draw Me!")	
