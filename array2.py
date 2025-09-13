from array import *
# print("array to bytes")
x=array("b",[15,14,25,20,18])
# s=x.tobytes()
# print(s)      # it returns the machine values of array



# list=[1,5,7,-4]
# arre_num=array('i',[])
# arre_num.fromlist(list)
# print("element from array to lst",arre_num)


arr=array("i",[1,2,5,7,8,9])
# print("insert 4  brfore 5")
# arr.insert(2,4)
# print(arr)
# arr.remove(7) 
# print(arr)
l=[]
l=arr.tolist()
#print(l)
   

def test_duplicate(array_nums):
    nums_set = set(array_nums)    
    # print(len(nums_set))
    return len(array_nums) != len(nums_set)     
# print(test_duplicate([1,2,3,4,5]))
# print(test_duplicate([1,2,3,4, 4]))
# print(test_duplicate([1,1,2,2,3,3,4,4,5]))


def test(arr_nums):
    return (sorted(set(arr_nums),key=arr_nums.index))

arr=array("i",[1,5,1,6,5,4,3])
result=test(arr)
for i in result:
    print(i)
