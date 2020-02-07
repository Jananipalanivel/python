n=int(input())
for i in range(1,n+1,2):
    print(" "*(n-i)+" *"*i+" "*(n-i))
for i in range(1,n,2)[::-1]:
        print(" "*(n-i)+" *"*i+" "*(n-i))
        
