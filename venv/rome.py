x=int(input('Chislo'))
def rome():
    return res
d={100:'C',
   50:'L',
   10:'X',
   5:'V',
   1:'I'
}
if x==100:
    res=(d[100])
else:
    cile = x // 10
    ost = x % 10
    if ost>8:
        ost=d[1]+d[10]
        res=cile*d[10]+ost
    elif ost>=5:
        res=cile*d[10]+(ost-5)*d[1]+d[5]
    else:
        res = cile * d[10] + ost* d[1]
print(res)