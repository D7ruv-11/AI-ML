import random 

s= random.randint(1,1000)

while True:
    guess = int(input("enter number:"))
    if guess==s:
        print("Got it baby!")
        break
    elif guess<s:
        print("Too low — try a higher number.")
    else:
        print("Too high — try a lower number.")
      