import BMI

weight=float(input("Enter your weight in kg:"))
height=float(input("Enter your height(meter):"))

bmi=BMI.BMI(weight,height)
BMI.bmi_result(bmi)