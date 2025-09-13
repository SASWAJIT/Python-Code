def max_product(arr):
    if len(arr)<2:
        return False
    x=arr[0]
    y=arr[1]
    for i in range(len(arr)) :
        for j in range(i+1,len(arr)):
            if (arr[i]*arr[j]>x*y):
                x=arr[i]
                y=arr[j]
    return (x,y)

nums = [1, 2, 3, 4, 7, 0, 8, 4]
print("original nums",nums)
print("max_numbers",max_product(nums))
nums2=[1]
print(max_product(nums2))

nums3 = [0, -1, -2, -4, 5, 0, -6]
print(max_product(nums3))

from array import *
a=array('i',[])
rng=int(input("enter size of array"))
# for i in range (rng):
#     a.append(int(input("enter elements{} :".format(i))))
# print(a)

a=list(map(int,input ("enter numbers by space").split()))
print(a)
