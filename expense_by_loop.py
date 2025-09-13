exp=[2390,1300,3145,4856,1200]
total=0
for i  in range(len(exp)):
    print("in month",i+1,"expenditure=",exp[i])
    total=total+exp[i]
print("total expenditure=",total)
