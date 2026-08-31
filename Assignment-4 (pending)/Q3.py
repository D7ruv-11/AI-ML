class student:
    def __init__(self,name,rollno,marks):
        self.set_name(name)
        self.set_rollno(rollno)1
        self.set_marks(marks)

    def set_name(self,name):
        if name.strip()== "":
            print("name should not be empty")
        else :
            self.__name = name 


    def set_rollno(self,rollno):
        if rollno in range(1,101):
            self.__rollno = rollno
        else:
            print("roll number must be between 1 - 100")

    def set_marks(self,marks):
        if marks>=0:
            self.__marks = marks 
        else:
            print("marks must be postive")

    def get_name(self):
        return self.__name
    
    def get_rollno(self):
        return self.__rollno
    
    def get_marks(self):
        return self.__marks
    
    def display(self):
        print("name",self.__name)
        print("rollno:",self.__marks)
        print("marks:",self.__marks)

b = student("Dhruv",10,99)

print(b.get_name())

b.display()

    


    



    