import numpy as np
# a=np.array([10,20,30])
# print(type(a))

b=np.array([[10,20,30],[40,50,60],[1,2,3]])
#print(b)
# print(b[:2,0:2])
# print(b[:2,0:3])
# print(b[0,0])

#atribute
# print(np.shape(b)) #gives shape 3*3=9
# print(np.size(b)) #gives size 3*3
# print(np.ndim(b)) #gives dimension of array
# print(b.dtype) # gives data type of array
# print(len(b))
#print(b.astype(float))



#mathematical operation on array
a = np.array([[10,20],[30,40]])
c=np.array([[70,60],[90,80]])
print(np.add(a,c))
print(np.subtract(c,a))
print(np.multiply(a,c))
print(np.divide(c,a))
print(np.divmod(c,a)) # this function gives the quotent and remender simultaniously in array form.
d=np.array([3])
print(np.power(a,d))
print(np.power(c,2))
