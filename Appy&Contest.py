t=int(input())
for _ in range(t):
    n,a,b,k=map(int,input().split())
    aas=bs=0
    for i in range(1,n+1):
        if(i%a==0 and i%b==0):
            continue
        elif(i%a==0):
            aas+=1
        elif(i%b==0):
            bs+=1
    if((aas+bs)>=k):
        print('Win')
    else:
        print('Lose')
    print(n,a,b,k)
    '''python numbers pg5'''
