x=int(input("enter first number"))
y=int(input("enter second number"))
try :
    z=x/y
    print(z)
except Exception as e:
    print(e)
    print(type(e))