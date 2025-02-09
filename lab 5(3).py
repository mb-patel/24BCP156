import random
numbers = random.choices(range(1,30),k=50)
print("the generated numbers is:",numbers)
unique_numbers=list(set(numbers))
print("list after removing duplicates:",unique_numbers)
