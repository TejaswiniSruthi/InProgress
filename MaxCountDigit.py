n=input()
arr=list(map(int,input().split()))
x=len(str(max(arr)))
ar=[]
for i in arr:
    if(len(str(abs(i)))==x and i not in ar):
        ar.append(i)
for i in ar:
    print(i,end=' ')
