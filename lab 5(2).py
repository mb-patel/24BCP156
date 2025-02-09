import random
numbers=random.sample(range(1,50),20) 
print(numbers)
search_numbers=int(input("enetr a num to find its position:"))
for i in range(0,20):
    if numbers[i]==search_numbers:
        print("the numbers position is",i)
        break
    


    
