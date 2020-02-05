str=input().strip('""')

str1=str.split(";")
y=[]
for i in str1:
    l=0
    z=0
    k=i.split(":")
    l=len(k[0])
    list=[]
    for j in k[1]:
        s=int(j)
        list.append(s)
    z=max(list)
       
   
    while z>l:
        w=list.index(z)
       
        list.pop(w)
       
        if len(list)==0:
            y.append("X")
            break
        z=max(list)
        #print(z)
    if z<=l:
        y.append(k[0][z-1])
b=len(y)

y.insert(0,'"')
y.insert(b+1,'"')
print("".join(y))

