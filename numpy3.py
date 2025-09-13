# to add,delete,insert element to the array

import  numpy as np
a=np.array([10,20,30,40,50])
print(np.append(a,70))

b=np.array([[10,20],[30,40]])
# print(np.append(b,[78,80]))
#
# print(np.insert(a,1,62))
# print(np.insert(b,1,[60,70]))
# print(np.insert(b,2,[58,60],axis=1))
# print(np.insert(b,[0,2],[50],axis=0))


#for deleting elements
print(np.delete(a,3))
#print(np.delete(b,1))
print(np.delete(b,1,axis=0))


