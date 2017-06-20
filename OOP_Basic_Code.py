class Dog():
    species = 'mammal'
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
sam = Dog(breed='lab', name='Tommy')
print sam.species
print sam.breed
print sam.name
print'\n'
class Circle():
    pi = 3.14
    def __init__(self,rad):
        self.rad = rad
    def Area(self):
        return (self.rad**2)*Circle.pi
    def set_rad(self,newrad):
        self.rad=newrad
c=Circle(1)
A=c.Area()
print A
c.set_rad(2)
print c.rad

print '\n'
class Animal():
    def __init__(self):
        print 'animal created'
    def whoAmI(self):
        print 'animal'
    def eat(self):
        print 'eating'
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print 'Dog created'
    def whoAmI(self):
        print 'Dog'
    def bark(self):
        print 'woof!!!'
D=Dog()
D.whoAmI()
D.bark()
print '\n'

class Book():
    def __init__(self, Title, Author, Pages):
        print 'A book has been created'
        self.Title = Title
        self.Author = Author
        self.Pages = Pages

    def __str__(self):
        return 'Title:%s, Author:%s, Pages:%s' %(self.Title, self.Author, self.Pages)
    def __len__(self):
        return self.Pages

b = Book('Python', 'Jose', 100)
print len(b)
print '\n'

class Line():
    def __init__(self,coor1,coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        return ( (x2-x1)**2 + (y2-y1)**2 )**0.5
    def slope(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return float((y2-y1))/(x2-x1)
coor1 = (3,2)
coor2 = (8,10)
li = Line(coor1,coor2)
print li.distance()
print li.slope()