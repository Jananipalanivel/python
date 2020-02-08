n="Sweth129@001a@@"
l1=[]
l2=[]
l3=[]
for i in n:
    if i.isalpha():
        l1.append(i)
    elif i.isdigit():
        l2.append(i)
    else:
        l3.append(i)
c=len(l3)
l4=[]
e=[]
o=[]
for i in range(len(l2)):
    l4.append(int(l2[i]))
d=len(l4)
for i in range(d):
    if l4[i]%2==0:
        e.append(l4[i])
    else:
        o.append(l4[i])
s=""
if c%2==0:
    for i in range(0,len(e)):
        s=s+str(e[i])+str(o[i])
else:
    for i in range(0,len(o)):
        s=s+str(o[i])+str(e[i])
print(s)
        
