# 1
# inheritance = float(input())
# last_year = int(input())
# money_spent = 0
# age = 17
# for i in range(1800, last_year + 1):
#     age += 1
#     if i % 2 == 0:
#         money_spent += 12000
#     else:
#         money_spent = money_spent + 12000 + 50 * age
# difference = abs(money_spent - inheritance)
# if inheritance >= money_spent:
#     print(f"Yes! He will live a carefree life and will "
#           f"have {difference:.2f} dollars left.")
# else:
#     print(f"He will need {difference:.2f} dollars to survive.")

# 2
# period = int(input())
# daily_patients = 0
# treated_patients = 0
# untreated_patients = 0
# number_of_doctors = 7
# for i in range(1, period + 1):
#     if i % 3 == 0:
#         if untreated_patients > treated_patients:
#             number_of_doctors += 1
#     daily_patients = int(input())
#     if daily_patients <= number_of_doctors:
#         treated_patients += daily_patients
#     else:
#         treated_patients += number_of_doctors
#         untreated_patients += (daily_patients - number_of_doctors)
# print(f"Treated patients: {treated_patients}.")
# print(f"Untreated patients: {untreated_patients}.")

# 3
# number_of_cargos = int(input())
# cargo_tonnage = 0
# tonnage_microbus = 0
# tonnage_truck = 0
# tonnage_train = 0
# for i in range(number_of_cargos):
#     cargo_tonnage = int(input())
#     if cargo_tonnage <= 3:
#         tonnage_microbus += cargo_tonnage
#     elif 4 <= cargo_tonnage <= 11:
#         tonnage_truck += cargo_tonnage
#     elif cargo_tonnage >= 12:
#         tonnage_train += cargo_tonnage
# total_tonnage = tonnage_microbus + tonnage_truck + tonnage_train
# total_cost = tonnage_microbus * 200 + \
#              tonnage_truck * 175 + tonnage_train * 120
# average = total_cost / total_tonnage
# tonnage_microbus = tonnage_microbus / total_tonnage * 100
# tonnage_truck = tonnage_truck / total_tonnage * 100
# tonnage_train = tonnage_train / total_tonnage * 100
# print(f"{average:.2f}")
# print(f"{tonnage_microbus:.2f}%")
# print(f"{tonnage_truck:.2f}%")
# print(f"{tonnage_train:.2f}%")

# 4
# number_of_students = int(input())
# students_group_1 = 0
# students_group_2 = 0
# students_group_3 = 0
# students_group_4 = 0
# sum_of_grades = 0
# for i in range(number_of_students):
#     current_grade = float(input())
#     sum_of_grades += current_grade
#     if 2.00 <= current_grade <= 2.99:
#         students_group_1 += 1
#     elif 3.00 <= current_grade <= 3.99:
#         students_group_2 += 1
#     elif 4.00 <= current_grade <= 4.99:
#         students_group_3 += 1
#     elif current_grade >= 5.00:
#         students_group_4 += 1
# students_group_1 = students_group_1 / number_of_students * 100
# students_group_2 = students_group_2 / number_of_students * 100
# students_group_3 = students_group_3 / number_of_students * 100
# students_group_4 = students_group_4 / number_of_students * 100
# average = sum_of_grades / number_of_students
# print(f"Top students: {students_group_4:.2f}%")
# print(f"Between 4.00 and 4.99: {students_group_3:.2f}%")
# print(f"Between 3.00 and 3.99: {students_group_2:.2f}%")
# print(f"Fail: {students_group_1:.2f}%")
# print(f"Average: {average:.2f}")

# 5
# number_of_turns = int(input())
# group_0_to_9 = 0
# group_10_to_19 = 0
# group_20_to_29 = 0
# group_30_to_39 = 0
# group_40_to_50 = 0
# invalid = 0
# total_points = 0
# for i in range(number_of_turns):
#     current_turn = int(input())
#     if 0 <= current_turn <= 9:
#         total_points += current_turn * 0.2
#         group_0_to_9 += 1
#     elif 10 <= current_turn <= 19:
#         total_points += current_turn * 0.3
#         group_10_to_19 += 1
#     elif 20 <= current_turn <= 29:
#         total_points += current_turn * 0.4
#         group_20_to_29 += 1
#     elif 30 <= current_turn <= 39:
#         total_points += 50
#         group_30_to_39 += 1
#     elif 40 <= current_turn <= 50:
#         total_points += 100
#         group_40_to_50 += 1
#     else:
#         total_points /= 2
#         invalid += 1
# group_0_to_9 = group_0_to_9 / number_of_turns * 100
# group_10_to_19 = group_10_to_19 / number_of_turns * 100
# group_20_to_29 = group_20_to_29 / number_of_turns * 100
# group_30_to_39 = group_30_to_39 / number_of_turns * 100
# group_40_to_50 = group_40_to_50 / number_of_turns * 100
# invalid = invalid / number_of_turns * 100
# print(f"{total_points:.2f}")
# print(f"From 0 to 9: {group_0_to_9:.2f}%")
# print(f"From 10 to 19: {group_10_to_19:.2f}%")
# print(f"From 20 to 29: {group_20_to_29:.2f}%")
# print(f"From 30 to 39: {group_30_to_39:.2f}%")
# print(f"From 40 to 50: {group_40_to_50:.2f}%")
# print(f"Invalid numbers: {invalid:.2f}%")

# 6
# number_of_months = int(input())
# electricity = 0
# water = 0
# internet = 0
# other = 0
# for i in range(number_of_months):
#     current_electricity = float(input())
#     electricity += current_electricity
#     water += 20
#     internet += 15
#     other += current_electricity + 20 + 15 + (current_electricity + 20 + 15) * 0.2
# total_expenses = electricity + water + internet + other
# average = total_expenses / number_of_months
# print(f"Electricity: {electricity:.2f} lv")
# print(f"Water: {water:.2f} lv")
# print(f"Internet: {internet:.2f} lv")
# print(f"Other: {other:.2f} lv")
# print(f"Average: {average:.2f} lv")

# 7
# stadium_capacity = int(input())
# number_of_fans = int(input())
# fans_in_a = 0
# fans_in_b = 0
# fans_in_v = 0
# fans_in_g = 0
# for i in range(number_of_fans):
#     current_sector = input()
#     if current_sector == "A":
#         fans_in_a += 1
#     elif current_sector == "B":
#         fans_in_b += 1
#     elif current_sector == "V":
#         fans_in_v += 1
#     elif current_sector == "G":
#         fans_in_g += 1
# fans_in_a = fans_in_a / number_of_fans * 100
# fans_in_b = fans_in_b / number_of_fans * 100
# fans_in_v = fans_in_v / number_of_fans * 100
# fans_in_g = fans_in_g / number_of_fans * 100
# filled_in = number_of_fans / stadium_capacity * 100
# print(f"{fans_in_a:.2f}%")
# print(f"{fans_in_b:.2f}%")
# print(f"{fans_in_v:.2f}%")
# print(f"{fans_in_g:.2f}%")
# print(f"{filled_in:.2f}%")

# 8
# n = int(input())
# the_range = 2 * n
# for i in range(1, the_range + 1):
#     current_number = int(input())





