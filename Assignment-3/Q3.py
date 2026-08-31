l1 = [int(x) for x in input("enter the numbers separated by commas: ").split(",")]
l2 = [int(y) for y in input("enter the numbers separated by commas: ").split(",")]

l3 = l1 + l2
l3.sort()
 
print(l3)