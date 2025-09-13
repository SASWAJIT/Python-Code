from array import *
arr_el=array('i',[1,3,5,7,9])
# for i in arr_el :
#     print(i)


# arr_el.append(4)
# for i in arr_el :
#     print(i)

# print("size of array",arr_el.itemsize)
# print(arr_el[::-1])

#print("current address and  length of the array ",arr_el.buffer_info())
# print(" size of the memory buffer in array",arr_el.buffer_info()[1]* arr_el.itemsize)

# extended function
# arr_el.extend(arr_el)
# print("Extended array from original array",arr_el)

 
def first_duplicate(arr_nums):
 nums_set=set()
 no_duplicate=-1
 for i in range (len(arr_nums)):
    if arr_nums[i] in nums_set:
        return arr_nums[i]
    else:
        nums_set.add(arr_nums[i])
 return no_duplicate

print(first_duplicate([1, 2, 3, 4, 4, 5]))
print(first_duplicate([1, 2, 3, 4]))
print(first_duplicate([1, 1, 2, 3, 3, 2, 2]))
