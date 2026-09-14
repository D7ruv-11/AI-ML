def calc(a,b,opp):
    match opp:
        case "+":
            return a+b
        case "-":
            return a-b
        case "*":
            return a*b
        case "/":
            if b==0 :
                return "cannot be divide by zero"
            else:
                return a/b
                        

print(calc(4,5,"+"))

