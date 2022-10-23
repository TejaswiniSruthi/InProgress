s=input().replace(' ','').lower()
v=['a','e','i','o','u']
for i in s:
    if i in v:
        v.remove(i)
print(5-len(v))
