# Body mass imdex
def BMI(weight,height)->float:
    return weight/(height**2)
def bmi_result(bmi):
    if bmi<18.5:
        print(f"Your BMI is {bmi:.2f} ,you're underweight")
    elif 18.5<= bmi <24.9:
        print(f"Your BMI is {bmi:.2f}, you're normaly weight")
    elif 24.9<= bmi <29.9:
        print(f"You BMI is {bmi:.2f},you're overweight")
    else:
        print(f"Your BMI is {bmi:.2f} ,you're obese.")



# weight=float(input("Enter your weight:"))
# height=float(input("Enter your height(meter):"))
# bmi=BMI(weight,height)



