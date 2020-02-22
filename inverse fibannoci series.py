n=int(input())
l=[2,3,5,7,11,13]
c=n
for i in l:
    if n%i==0:
        c=c-(c//i)
print(c)
