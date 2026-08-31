salary = int(input("enter the amount:"))

if salary <= 30000:
    print("Your tax rate is 5%")
elif(salary in range(30000,70000)):
    print("Your applied tax is 10%")
elif salary >= 70000:
    print("Your tax rate is 25%")
else:
    print("enter a valid amount")
