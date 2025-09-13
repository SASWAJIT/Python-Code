#local variables
# x=24
# print("first value",x)
# def hello():
#     x=25
#     return x
# print(hello())

#global variables
x=24
print("first value",x)
def hello():
    global x
    x=25
    return x
print(hello())

x=x+5
print(x)