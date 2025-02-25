import random

# example 1
print(random.random())

# example 2: generate random integers
print(random.randint(1, 100))

# example 3: generate random numbers within range
print(random.randrange(1, 10))
print(random.randrange(1, 10, 2))
print(random.randrange(0, 101, 10))

# example 4: select random elements
print(random.choice('computer'))
print(random.choice([12, 23, 45, 67, 65, 43]))
print(random.choice((12, 23, 46, 67, 65, 53)))

# example 5: select random items from data set
# 5.1
aList = [20, 40, 80, 100, 120]
sampled_list = random.sample(aList, 3)
print(sampled_list)
      
# 5.2
# create list of 5 random numbers
num_list = random.sample(range(100), 5)
print(num_list)