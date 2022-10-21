from math import sqrt

def isPrime(n):
    if(n<=1):
        return False
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0):
            return False
    return True

n=int(input())
if isPrime(int(str(n)[::-1])):
    print('circular prime')
else:
    print('prime but not a circular prime')
