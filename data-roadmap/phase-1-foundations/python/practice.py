def bmi_category(weight_kg, height_m):
    
    bmi = weight_kg / (height_m ** 2)
    
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        return "Normal"
    elif bmi >= 25 and bmi <= 29.9:
        return "Overweight"
    elif bmi >= 30:
        return "Obese"
    
print(bmi_category(50, 1.7))   # "Underweight"
print(bmi_category(70, 1.7))   # "Normal"
print(bmi_category(85, 1.7))   # "Overweight"
print(bmi_category(100, 1.7))  # "Obese"