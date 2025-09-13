# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
#
# x=int(input("enter a number "))
# print(fact(x))

# fibonacci using recursion

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input("enter number of terms"))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))