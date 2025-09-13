#iteration in dictionaries
student={"name":"john","class":"6th","roll":14}

# for x,y in student.items():
#     print(x,"-",y)
#
# #to print keys
# for i in student:
#     print(i)
#
# #to print values
# for i in student.values():
#       print(i)


# function in dictionary
#get()
# x=student.get("name")
# print(x)

# items()
# x=student.items()
# print(x)

#keys
# x=student.keys()
# print(x)

#values
# x=student.values()
# print(x)

#copy
# x=student.copy()
# print(x)

#setdefault
# x=student.setdefault("roll",24)
# print(x)

#nested dictionary

employees={1:{"name":"john","age":24,"gender":"male"},
           2:{"name":"Gudi","age":22,"gender":"female"},
           3:{"name":"peter","age":23,"gender":"male"}}
print(employees[1])
print(employees[2]["age"])