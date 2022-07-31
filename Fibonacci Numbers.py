#Program for Fibonacci Series
inp=int(input("How many terms? "))
n=0
n1=1
for i in range(inp):    
    prv=n+n1
    print(n)
    n=n1
    n1=prv
#Program for finding positive values in a list
list1=[-1,2,3,-6,-45,12]
list2=[]
for i in range(len(list1)):
    if list1[i]>0:
        list2.insert(i,list1[i])
print(list2)
