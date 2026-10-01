class vehical:
    brand = "BMW"
    model= "M-4"

class car(vehical):
    def __init__(self,seats):
        self.seats = seats 

class bike(vehical):
    def __init__(self,engine__cc):
        self.engine__cc = engine__cc

b = bike(8)
c = car(7)
print(c.brand,c.seats)
