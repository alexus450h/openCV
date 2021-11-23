a=16
b=24
c=36
def NSD(x,y):
    while y!=0:
        x,y=y,x%y
    return x
print(NSD(a,b))
NSK_1=a*b/NSD(a,b)
print(NSK_1)
NSK_2=c*NSK_1/NSD(NSK_1,c)

print(NSK_2)