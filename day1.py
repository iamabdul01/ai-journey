# 1. BMI Calculator
def bmi_calculator(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

# 2. Tip Splitter


def tip_splitter(bill, tip_percent, people):
    total = bill + (bill * tip_percent / 100)
    return round(total / people, 2)

# 3. Celsius to Fahrenheit


def celsius_to_fahrenheit(celsius):
    return round((celsius * 9/5) + 32, 2)

# 4. Simple Grade Checker


def grade_checker(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

# 5. Word Counter


def word_counter(sentence):
    return len(sentence.split())


print(bmi_calculator(65, 1.83))
print(tip_splitter(100, 10, 4))
print(celsius_to_fahrenheit(150))
print(grade_checker(90))
print(word_counter("I am Abdul and I just started my AI/ML journey wish me luck"))
