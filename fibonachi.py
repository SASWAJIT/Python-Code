def fibonacci_recursion(n):
    if n==0:
        return 0
    elif n==1:
        return 0
    elif n==2:
        return 1
    else :
        return  fibonacci_recursion(n-1)+fibonacci_recursion(n-2)
    
n=int(input("enter fibonaci number you want:"))
while n>0:
 fibonacci_number=fibonacci_recursion(n)
 print("fibbonacci series is",fibonacci_number)
 n=n-1