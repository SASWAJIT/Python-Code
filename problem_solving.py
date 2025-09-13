# def maximum_num(a,b,c):
#     if a>b and a>c:
#         print(a,"is greatest")
#     elif b>c and b>a:
#         print(b,"is greatest")
#     else:  print(c,"is greatest")
#
# maximum_num(12,5,14)

#square of 30 numbers in a list

# def square():
#     l=[]
#     for i in range(1,31):
#         l.append(i**2)
#     return l
# print(square())

#check prime number

# def prime(val):
#     if val==1:
#         print(val,"is not a prime number")
#     for i in range(2,val):
#         if val % i==0:
#             return 0
#         else:return 1
# n=int(input("enter a number"))
# a=prime(n)
# if a==1:
#     print(n,"is a prime number")
# else:print(n,"is not a prime number")

#sum of all number in a list

# l=[]
#
# num_element=int(input("Enter number of elements"))
# for i in range(num_element):
#     i=int(input("enter number"))
#     l.append(i)
# print(l)
# sum=0
# for i in l:
#     sum+=i
# print(sum)


# fibonacci series using recursion
def fibonacci(n):
    if n<=1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

n=int(input("enter number of terms u required"))
if n<=0:
    print("enter a valid positive number")
else:
    for i in range(n):
        print(fibonacci(i))