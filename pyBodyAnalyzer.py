#  Copyright (c) 2020.
#  Created by Zhbert.
#  Licensed by GPLv3.

print("Please answer a few question:")
height = float(input("Your height (cm): "))
weight = float(input("Your weight (kg): "))
age = float(input("Your age (years): "))
gender = input("What gender are you (male, female)? ")
print("Select your physical activity coefficient, where:")
print("1 - No or minimal load")
print("2 - 1-3 times a week")
print("3 - 4-5 times a week")
print("4 - Intensively 4-5 times a week")
print("5 - Every day")
print("6 - Every day is intense")
print("7 - Heavy physical work")
physical = float(input("Your physical activity: "))
print("What is your goal?")
print("1 - Lose weight")
print("2 - To gain weight")
target = int(input("Your goal: "))


def check_data():
    if type(height) == float \
            and type(weight) == float \
            and type(age) == float \
            and type(physical) == float \
            and type(target) == int \
            and gender == "male" or gender == "female":
        return True
    else:
        return False


def get_coefficient():
    if physical == 1:
        return 1.2
    elif physical == 2:
        return 1.375
    elif physical == 3:
        return 1.4625
    elif physical == 4:
        return 1.550
    elif physical == 5:
        return 1.6375
    elif physical == 6:
        return 1.725
    elif physical == 7:
        return 1.9


def male_count():
    def get_male_muffin_geore():
        return 10 * weight + 6.25 * height - 5 * age + 5

    def get_male_harris_benedict():
        return 66.5 + 13.75 * weight + 5.003 * height - 6.775 * age

    return (((get_male_harris_benedict() - get_male_muffin_geore()) / 2)
            + get_male_muffin_geore()) * 1.1 * get_coefficient()


def female_count():
    def get_female_muffin_geore():
        return 10 * weight + 6.25 * height - 5 * age - 161

    def get_female_harris_benedict():
        return 655.1 + 9.563 * weight + 1.85 * height - 4.676 * age

    return (get_female_harris_benedict() - get_female_muffin_geore()) / 2 \
           + get_female_muffin_geore() * 1.1 * get_coefficient()


def get_imt():
    return weight / ((height / 100) * (height / 100))


def view_state_of_body():
    if get_imt() < 15:
        return "You have an acute shortage of weight"
    elif 15 <= get_imt() <= 19:
        return "You have an shortage of weight"
    elif 20 <= get_imt() <= 24:
        return "You have a normal weight"
    elif 25 <= get_imt() <= 29:
        return "You have an overweight"
    elif 30 <= get_imt():
        return "You have an obesity"


def get_male_ideal_weight():
    def get_male_broke():
        return (height - 100) * 1.15

    def get_male_hamvi():
        return 48 + 2.7 * (0.393701 * height - 60)

    def get_male_devin():
        return 50 + 2.3 * (0.393701 * height - 60)

    return (get_male_devin() + get_male_hamvi() + get_male_broke()) / 3


def get_female_ideal_weight():
    def get_female_broke():
        return (height - 110) * 1.15

    def get_female_hamvi():
        return 45.5 + 2.2 * (0.393701 * height - 60)

    def get_female_devin():
        return 45.5 + 2.3 * (0.393701 * height - 60)

    return (get_female_devin() + get_female_broke() + get_female_hamvi()) / 3


def print_male_info():
    print("You daily rate of kcal: " "%.0f" % male_count())
    if target == 1:
        print("Your maximum value kcal per day: " "%.0f" % float(male_count() * 0.8))
    print("Your body mass index: " "%.0f" % get_imt())
    print(view_state_of_body())
    print("You ideal weight is " "%.0f" % get_male_ideal_weight())
    if weight < get_male_ideal_weight():
        print("You need to gain " "%.0f" % float(get_male_ideal_weight() - weight) + " kg")
    else:
        print("You need to lose " "%.0f" % float(weight - get_male_ideal_weight()) + " kg")


def print_female_info():
    print("You daily rate of kcal: " "%.0f" % female_count())
    if target == 1:
        print("Your maximum value kcal per day: " "%.0f" % float(female_count() * 0.8))
    print("Your body mass index: " "%.0f" % get_imt())
    print(view_state_of_body())
    print("You ideal weight is " "%.0f" % get_female_ideal_weight())
    if weight < get_female_ideal_weight():
        print("You need to gain " "%.0f" % float(get_female_ideal_weight() - weight) + " kg")
    else:
        print("You need to lose " "%.0f" % float(weight - get_female_ideal_weight()) + " kg")


if check_data():
    if gender == "male":
        print_male_info()
    elif gender == "female":
        print_female_info()
else:
    print("Error in entering data! Please try again.")

input()
