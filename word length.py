a=list(map(str,input().split()))
l=[]
for i in range(len(a)):
    l.append(len(a[i]))
    if len(a[i])<10:
        print(l[i],end="")
    else:
        d=len(a[i])
        while d>=10:
            d=sum(list(map(int,str(d))))
        print(d,end="")
