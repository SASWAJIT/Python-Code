l=["apple","sweet","banana","coconut","orange"]
l2=[]
for i in l:
    for j in (i) :
        if j=="a":
            if i in l2 :
                pass
            else :
                l2.append(i)
print(l2)

