from abc import ABC , abstractmethod

class employee:
    @abstractmethod
    def calulate_salary():
        pass

class fulltime_employee(employee):
    def __init__(self,salary):
         self.salary = salary 

    def calculate_salary(self):
        return self.salary
    
class inter(employee):
    def __init__(self, hours_worked, rate_per_hour):
        self.hours_worked = self.hours_worked
        self.rate_per_hour = rate_per_hour

    def calculate_salary(self):
        return self.hours_worked * self.rate_per_hour
    

f1 = fulltime_employee(45)

i1 = def 

    