import numpy as np
# l1=[20,30,40]
# l2=[50,60,70]
# print(l1+l2)


a=np.array([10,20,30])
b=np.array([40,50,60])
# print(a)
# print(b)
# print(a+b)
# print(b-a)
# print(b/a)
# print(a*b)

# a=np.array([40,50,"60"]) # all element becomes string.
# print(a)
# a=np.array([40,50,60.2])
# print(a)



#combaining and spliting arrays
c=np.array([[10,20],[40,30]])
d=np.array([[3,4],[6,5]])
# print(np.concatenate([c,d]))
# print(np.concatenate([c,d],axis=1))#if axis=0 then output is in vertical form if axis=1 then output is in horizontal form

#for  spliting
e=np.array([10,20,30,40,50,60])
#print(np.split(e,2))


#numpy sort,search,filter
f=np.array([[12,25,18,14,13],[5,8,6,4,2]])
#print(np.sort(f))

#search
g=np.array([12,25,18,14,13])
h=np.where(g%2==0)
#print(h)

#filter
i=np.array([20,30,40,50])
#ar=[True,False,True,False]
arr=i>35
fa=i[arr]
#print(fa)


#aggregating functions in numpy
x=np.array([20,40,60,80])
# print(np.sum(x))
# print(np.max(x))
# print(np.min(x))
# print(np.size(x))
# print(np.mean(x))
# print(np.cumsum(x))

#quntity and price sum
l=[100,150,160,200,250,130]
m=[10,20,40,30,15,25]
price=np.array([l])
quantity=np.array([m])
print(price,"\n",quantity)
n=np.cumprod([price,quantity],axis=0)
#print(np.sum(n))
print(n[1].sum())
