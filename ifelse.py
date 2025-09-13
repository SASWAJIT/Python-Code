india=['mumbai','delhi','hyderabad']
bangladesh=['dhaka','khulna','rangpur']
pakistan=['lahore','karachi','islamabad']
city=input("enter city name ")
if city in india:
    print("city is in india")
elif city in bangladesh:
    print("city in bangladesh")
elif city in pakistan:
    print("city in pakistan")
else:
    print("city not belongs to any country")
