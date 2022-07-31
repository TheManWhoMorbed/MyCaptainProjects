inp=int(input("How many terms? "))
n=0
n1=1
for i in range(inp):    
    prv=n+n1
    print(n)
    n=n1
    n1=prv
