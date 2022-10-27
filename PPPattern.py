#pg 5 sub:981

n=int(input())
for i in range(n):
    for j in range(n):
        if(j==i or j==n-i-1):
            print(n-i,end=' ')
        else:
            print(' ',end=' ')
    print()
