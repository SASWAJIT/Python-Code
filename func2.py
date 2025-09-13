def calculate_income(exp):
    total=0
    for i in exp:
        total=total+i
    return total

john=[2000,1200,2500,1300]
jak=[1200,1500,1000,3000]
print("total income of john:",calculate_income(john))
print("total income of jak:",calculate_income(jak))
