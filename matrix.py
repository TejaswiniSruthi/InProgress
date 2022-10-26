r,c=map(int,input().split())
es=os=0
for i in range(r):
    if(r%2==0):
        for i in range(c):
            j=int(input())
            es+=j
    else:
        for i in range(c):
            j=int(input())
            os+=j
print(es,os)
