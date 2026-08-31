class shape :
    def area(self):
        print("calculating area....")

class circle(shape):
    def area(self,r):
            return 3.14*r*r
    
class rectangle(shape):
    def area(self,l,b):
        return l*b
    
class triangle(shape):
    def area(self,l,h):
        return 0.5*l*h
    
s = shape()
c = circle()
t = triangle()
r = rectangle()
print(r.area(4,5))
print(c.area(3))
print(t.area(8,7))