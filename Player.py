from PyQt5 import QtCore  
from Object import Object

class Player(Object):

	def __init__(self, x, y):
		super().__init__(x,y)
		self.size = 50

	def paint(self, qp):
		qp.drawRect(self.x,self.y,self.size,self.size)

	def move(self,dx,dy):
		self.x += dx
		self.y += dy
	
	def keypress(self, key):
		if key == QtCore.Qt.Key_W:
			print("w")
		print(key)
