name = input("Enter your name: ").capitalize()
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in metre: "))

bmi = weight / (height ** 2)
print(f"{name}'s Body Mass Index (BMI) is {bmi:.2f}.")

if bmi < 18.5:
    print(f"{name} is underweight.")
elif bmi < 25:
    print(f"{name} has normal weight.")
elif bmi < 30:
    print(f"{name} is overweight.")
else:
    print(f"{name} is obese.")
