import random
list1=[]
list2=[]
numbers=random.choices(range(-50,50),k=30)
print("list:",numbers)
for i in range(0,30):
    if numbers[i]<0:
        list1.append(numbers[i])
        
    else:
        list2.append(numbers[i])
print("list1:",list1)
print("list2:",list2)
        
