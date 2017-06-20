import math
class shape(object):
	def __init__(self):
		self.color="red"
	def area(self):
		return 0
class quadrilateral(shape):
	def __init__(self,w,l):
		self.width=w
		self.length=l
	def area(self):
		return self.width * self.length
class square(quadrilateral):
	def __init__(self,l,c):
		self.color=c
		super(square,self).__init__(l,l)
class circle(shape):
	def __init__(self,r,col):
		super(circle,self).__init__()
		self.radius=r
		self.color=col
	def area(self):
		return math.pi*(self.radius**2)
sq1=square(5,"blue")
c1=circle(5,"white")
q1=quadrilateral(4,5)
print('Side lenth=>',sq1.width,'\tcolor=>',sq1.color,'\tArea=>',sq1.area())
print('radius=>',c1.radius,'\tcolor=>',c1.color,'\tArea=>',c1.area())
print('width=>',q1.width,'\tlength=>',q1.length,'\tArea=>',q1.area())
