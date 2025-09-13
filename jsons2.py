import json
# student_data = {"name": "Saswajit", "age": 23, "marks": 87}
# data = json.dumps(student_data),
# print(data)
# print(data["age"])
# print(type(data))

# Acces the value of data from the given json data
# student_data = """{"name": "Saswajit", "age": 23, "marks": 87}"""
# data = json.loads(student_data)
# print(data["age"])
#
# pretty indentation
# student_data = {"name": "Saswajit", "age": 23, "marks": 87}
# data=json.dumps(student_data,indent=4,separators=(",","="))
# print(data)

# access the nested key marks from the neste data
student_data = """{ "student":
                 {"grade":{
                     "name": "Saswajit", "age": 23, "marks": 87}}}"""
data = json.loads(student_data)
print(data["student"]["grade"]["marks"])
