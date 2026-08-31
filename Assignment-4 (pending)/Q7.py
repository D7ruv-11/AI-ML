class person:
    def __init__(self,name,age=None,address=None):
        self.age = age
        self.name = name
        self.address = address

p1 = person("DHRUV")
p2 = person("Dhruv",12)
p3 = person("Dhruv", 14,)
print(p1.name)
