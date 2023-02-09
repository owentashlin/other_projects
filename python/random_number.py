import random

rand_int = random.randint(1, 10)
print(rand_int)

random_float = 
random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

coin_toss = random.randint(0,1)
if coin_toss == 0:
    print("Heads")
else:
    print("Tails")

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
num_names = len(names)
rand_name = random.randint(0, num_names - 1)
person_who_will_pay = names[rand_name]

print(person_who_will_pay + " is going to buy the meal today!")