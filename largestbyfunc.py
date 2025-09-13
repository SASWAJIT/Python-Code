def find_largest(num1,num2,num3):
    largest=max(num1,num2,num3)
    return largest
num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))
num3=int(input("enter 3rd number"))
c=find_largest(num1,num2,num3)
print("largest number is:",c)
