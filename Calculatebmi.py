#input
height=float(input("Enter height (inches):"))
weight=float(input("Enter weight (pounds):"))

# Processing - Calculate the BMI result:
bmi =weight/(height ** 2) * 703

#output - Display the result
print("BMI=",bmi)
#formatting the output with the f string
print(f'BMI value for a person height of {height} and {weight} formatted using the f string {bmi}')

#using the round fuction to round the BMI value to 2 decimal places
print("BMI=",round(bmi,2))
