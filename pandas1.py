# import pandas as pd
#
# data={"Name":[ "Golu","Tulu","Lisa"],"Age":[25,28,26],"Salary":[30000,28000,32000]}
#
# df=pd.DataFrame(data)
# # print(df)
# data1=pd.read_excel("C:/Users/saswa/PycharmProjects/all  modules1/Sample-Employee-Data.xlsx")
# print(data1)


import pandas as pd
# data=pd.read_excel("C:/Users/saswa/OneDrive/Desktop/coding.python/EEID.xlsx")
# print(data)
data={"Name":[ "Golu","Tulu","Lisa"],"Age":[25,28,26],"Salary":[30000,28000,32000]}
df=pd.DataFrame(data)
print(df)
print(df[0:2]) #data slicing of a dataframe

