india=['mumbai','delhi','hyderabad']
bangladesh=['dhaka','khulna','rangpur']
pakistan=['lahore','karachi','islamabad']
city1=input("enter city name ")
city2=input("enter city name ")
if city1 in india and city2 in india:
    print("both city is in india ")
elif city1 in bangladesh and city2 in bangladesh:
    print("both city in bangladesh ")
elif city1 in pakistan and city2 in pakistan:
    print("both city pakistan")
else:
    print("city not belongs to any country")
