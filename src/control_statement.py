x = 10

if x > 20:
    print("x is greater than 20")
elif x > 15:
    print("x is greater than 15 but not greater than 20")
elif x > 5:
    print("x is greater than 5 but not greater than 15")
else:
    print("x is 5 or less")


#Calculate BMI
Height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight / Height**2, 2)  # Rounded to 2 decimal places for better precision
print(bmi)
if bmi < 18.5:
    print(f"Your BMI is {bmi} and you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi} and you are normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi} and you are overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi} and you are obese.")
else:
    print(f"Your BMI is {bmi} and you are clinically obese.")


#multiple if statement
Height = float(input("Enter you height in feet "))
bill =0
if Height>3:
    print("you can ride")
    age = int(input("Enter your age "))
    if age<12:
        bill = 150
        print("Ticket price is 150")
    elif 12<= age <=18:
        bill = 250
        print("Ticket price is  250")
    else:
        print("Ticket price is 500 Rs")
        bill = 500

    want_photo = input("Do you want to take photo(Y/N)?")
    if want_photo == 'y'or want_photo =='Y':
        bill+=50
        print(f"Your total bill is {bill}")

else:
    print("you can't ride")
print("Thank you!")