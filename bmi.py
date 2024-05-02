def calculate_bmi(height,weight):
    print("Height = " ,height)
    print("Weight = " ,weight)
    bmi = weight/(height*height)
    print("BMI = ", bmi)
    if bmi < 18.5:
        print("You are underweight")
    elif bmi > 25.0:
        print("You are overweight")
    else:
        print("Across the boundless galaxy and universes, you alone is the normal weight")

calculate_bmi(1.73,30)