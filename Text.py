from Object import Object

class Text(Object):
	def __init__(self,x,y,text):
		super().__init__(x,y)
		self.text = text
	
	def paint(self, qp):
		qp.drawText(self.x,self.y,self.text)
