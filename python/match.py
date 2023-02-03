print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = name1 + name2
names_lower = names.lower()

t = names_lower.count("t")
r = names_lower.count("r")
u = names_lower.count("u")
e = names_lower.count("e")
true_score = t + r + u + e

l = names_lower.count("l")
o = names_lower.count("o")
v = names_lower.count("v")
e = names_lower.count("e")
love_score = l + o + v + e

compatibility_score = int(str(true_score) + str(love_score))

if (compatibility_score < 10) or (compatibility_score > 90):
    print(f"Your score is {compatibility_score}, you go together like coke and mentos.")
elif (compatibility_score >= 40) and (compatibility_score <= 50):
    print(f"Your score is {compatibility_score}, you are alright together.")
else:
    print(f"Your score is {compatibility_score}.")