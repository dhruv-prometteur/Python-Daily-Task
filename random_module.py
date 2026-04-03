import random

# print(random.random())

# print(random.randint(1,10))

lst=["orange","orange","orange"]
# print(random.choice(lst))

random.shuffle(lst)
# print(lst)

# print(random.randrange(1,10,2))
# print(random.uniform(1,10))
print(random.sample(lst,2))

random.seed(5)
print(random.randint(5,10))