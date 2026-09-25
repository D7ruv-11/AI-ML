l1 = input("enter the number  saperated by , :").split(",")

s1 = set()
repeated = set()
for i in l1:
    if i in s1:
        repeated.add(i)
    else:
        s1.add(i)  

print(repeated)