def amstrong(n):
    m=n
    sum=0
    while n>0:
        r=n%10
        a=pow(r,3)
        sum +=a
        n=n//10
    if sum==m:
     print(m,"is amstrong")
    else:
     print(m,"is not amstrong")

n=int(input("enter a number :"))
amstrong(n)
