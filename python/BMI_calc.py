height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = round(int(weight) / float(height) ** 2)

if BMI in range(0, 18):
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI in range(19, 22):
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI in range(23, 28):
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI in range(29, 33):
    print(f"Your BMI is {BMI}, you are obese.")
else:   
    print(f"Your BMI is {BMI}, you are clinically obese.")