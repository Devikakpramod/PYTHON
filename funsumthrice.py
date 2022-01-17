def sumThrice(a,b,c):
    sum=0
    Thrice=0
    if a==b==c:
        sum=a+b+c
        Thrice=sum*3
        print("sum is ",sum)
        print("sum Thrice is",Thrice)
    else:
        sum=a+b+c
        print(sum)
a=int(input("enter a number"))
b=int(input("enter another number"))
c=int(input("enter yet another number"))
sumThrice(a,b,c)
