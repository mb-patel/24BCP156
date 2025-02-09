import random
odd_numbers=random.sample(range(1,100,2),5)
print("list of 5 random odd numbers",odd_numbers)
even_numbers=random.sample(range(2,100,2),4)
print("list of 4 random even numbers",even_numbers)
odd_numbers.insert(2,even_numbers)
print("list after replacing",odd_numbers)
