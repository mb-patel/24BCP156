list1=[1,2,3,4,5,6,7,8,9]
list2=[2,4,6,8]
list3=[]
for i in list1:
    for j in list2:
        if i==j:
            break
    else:
        list3.append(i)
print("list3:",list3)
