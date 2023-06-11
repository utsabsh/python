height = float(input("enter your height in cm:"))
weight = float(input("enter your weight in kg:"))
bmi = weight/(height/100) ** 2

if bmi > 18.5:
    print(f"your bmi is {bmi}. you are underweight.")
elif 18.5< bmi > 25:
    print(f"your bmi is {bmi}. you are normal weight.")
elif 25< bmi > 30:
    print(f"your bmi is {bmi}. you are overweight.")
elif 30< bmi > 35:
    print(f"your bmi is {bmi}. you are obese.")
else:
    print(f"your bmi is {bmi}. you are clinically obese.")
