a=3
b=["airtel","123","16","paytm"]
c=["airtel","456","10","amazon"]
d=["jio","778","10","paytm"]
b1=[]
c1=[]
d1=[]
b1.append(int(b[1]))
b1.append(int(b[2]))
c1.append(int(c[1]))
c1.append(int(c[2]))
d1.append(int(d[1]))
d1.append(int(d[2]))
if "airtel" in b:
    b2=b1[1]*11
    if "paytm" in b:
        b3=b2*(10)
        b4=b3/100
        b5=round(b4)
        b6=b2-b5
        print(b1[0],b6)
if "airtel" in c:
     c2=c1[1]*11
     print(c1[0],c2)
     if "paytm" in c:
        c3=c2*(10)
        c4=c3/100
        c5=round(c4)
        c6=c2-c5
        print(c1[0],c6)
if "jio" in d:
    d2=d1[1]*10
print(d1[0],d2)
    
