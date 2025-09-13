total=0
def sum(a,b):
    print("a=",a)
    print("b=",b)
    total=a+b
    print("total inside the function:",total)
    return total
n=sum(5,6)   
print("total outside function:",total)
