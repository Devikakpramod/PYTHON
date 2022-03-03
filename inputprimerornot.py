a=int(input("enter a number"))
x=1
c=0
for i in range(1,a+1):
    if(a%i==0):
        
        c=c+1
    

print(c)
if(c==2):
    print("it is prime")
else:
    print("it is not a prime")
