n=int(input())
res=n//5
x=n%5
print(res)
if x==1:
    res+=2
elif x==2:
    res+=2
elif x==3:
    res+=4
else:
    res+=4
print(res)