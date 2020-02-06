a=int(input())
b=[]
for i in range(1,a):
    if a%i==0:
        b.append(i)
c=sum(b)
print(c)
if c==a:
    print("perfect number")
else:
    print("Not a perfect number")
            
        
        
