def is_prime(n):
    for i in range (2,n-1):
        if n%i==0:
            return "it is not a prime number"
    return "It is a prime number"  

print(is_prime(975))   
