a=int(input("enter first number"))
b=int(input("enter second number"))
def swap(a,b):
    a=a^b
    b=a^b
    a=a^b
    print(a)
    print(b)
swap(a,b)