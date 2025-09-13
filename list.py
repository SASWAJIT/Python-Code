
L=[]
print("enter 10 elements")
for i in range(10):
    num=int(input())
    L.append(num)
print(L)
print("last five elements ",L[-5:]) # print(L[n-5:])
print("number from 3rd to 8th position ",L[2:8])
print(L[:-1])
print("largest elements in  the list ",max(L))
print("smallest elements in the list:",min(L))
print("sum of elements in list ",sum(L))
print(8 in L)
print(L.index(8))
print(len(L))
print("remove elements is",7)
L.remove(7)
print("element added to list",12)
L.append(12)
l=[14,15]
L.extend(l)
print(L)
L.sort(reverse=True)
print("descending order:",L)
L.sort(reverse=False)
print("ascending oorder",L)

