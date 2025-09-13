amt=int(input("enter an amount"))
print("no of 2000-1 rupees required: ")
a=amt//2000
print("2000 rupees -",a)
amt=amt%2000
b=amt//1000
print("1000 rupees -",b)
amt=amt%1000
c=amt//500
print("500 rupees -",c)
amt=amt%500
d=amt//100
print("100 rupees -",d)
amt=amt%100
e=amt//50
print("50 rupees -",e)
amt=amt%50
f=amt//20
print("20 rupees -",f)
f=f%20
g=amt//10
print("10 rupees -",g)
amt=amt%10
h=amt//5
print("5 rupees -",h)
amt=amt%5
i=amt//1
print("1 rupees -",i)
