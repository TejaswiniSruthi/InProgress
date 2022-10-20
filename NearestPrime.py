from math import sqrt

def isPrime(n):
    if(n<=1):
        return False
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0):
            return False
    return True

def near(k):
    i=1
    while(True):
        if(isPrime(k+i)):
            if(isPrime(k-i) and ((k-i)>1)):
                return(k-i)
            return(k+i)
        if(isPrime(k-i) and ((k-i)>1)):
            return(k-i)
        i+=1


t=int(input())
for _ in range(t):
    k=int(input())
    print(near(k))
