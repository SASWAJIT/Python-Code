A="oppo","vivo","mi","Nokia","Lava"
print(type(A))
print(A[1:])
print(A[0::2])
print(A[::-1])

# for i in A:
#     print(i)

# for i in range(len(A)):
#     print(A[i])


# to convert into a list
A=list(A)
print(type(A))
A.append("Apple")
A=tuple(A)
print(A)

# 2 function are used in tuple are written below
print(A.count("Nokia"))
print(A.index("Lava"))
