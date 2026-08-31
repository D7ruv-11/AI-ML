l1 = input("enter the elements saperated by , :").split(",")
l2 = input("enter the elements saperated by , :").split(",")

s1 = set(l1)
s2 = set(l2)

if s1.intersection(s2) == 0:
    print("NO elements are common")
else:
    print("these elements are commom: ",s1.intersection(s2))    