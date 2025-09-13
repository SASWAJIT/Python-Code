def fibonacci(n,a,b,sum):

    if n != 0:
        print(a)
        sum=a+b
        a=b
        b=sum
        n=n-1
        return fibonacci(n,a,b,sum)

# n=int(input("enter a number you want :"))
# fibonacci(n,0,1,0)


#  check pallindrum number
n=int(input("enter a number :"))
m=n
rev=0
while n>0:
    rem=n%10
    rev=10*rev + rem
    n=n//10
if m==rev:
    print(m,"is a pallindrum number")
else:print(m,"is not a pallindrum number")

