stu = {
    "Dhruv":"100",
    "shourya":"90",
    "tanay":"70",
    "vasu":"30"
}
print("A - add a student")
print("B - update marks")
print("C - search for a student")
print("D - Display all students and marks")

user = input("Enter the A/B/C/D: ").upper()

if user=="A":
    stu1 = input("Enter the name of student")
    marks = int(input("Enter the number: "))
    stu.update({stu1:marks})
    print("Student added successfully!",stu)
elif user=="B" : 
    name = input("enter student name: ")
    if name in stu:
        marks =input("enter the marks updates: ")
        stu[name] = marks  #===> this line broke ur head
        print(stu)
    else:
        print("student does not exits!")
elif user=="C" :
    name1 =input("enter the student name your searching for: ")
    if name1 in stu:
        print("student found", ({name1}))
    else:
        print("try other name")  
else :
    print(stu)











