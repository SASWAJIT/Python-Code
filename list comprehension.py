l1=[20,30,40,50,60]
l2=[]
print(l1)
# for i in l1:
#     l2.append(i)
# print(l2)

#to add values on a new list we use other best option

l3=[i for  i in l1]
print(l3)

l4=[i for  i in l1 if i>45]
print(l4)
