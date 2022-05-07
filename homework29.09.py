
# lab
# 1
# number = int(input())
# if number == 1:
#     print('Monday')
# elif number == 2:
#     print('Tuesday')
# elif number == 3:
#     print('Wednesday')
# elif number == 4:
#     print('Thursday')
# elif number == 5:
#     print('Friday')
# elif number == 6:
#     print('Saturday')
# elif number == 7:
#     print('Sunday')
# else:
#     print("Error")

# 2
# day = input()
# if day == 'Monday' or day == 'Tuesday' \
#         or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
#     print('Working day')
# elif day == 'Saturday' or day == 'Sunday':
#     print('Weekend')
# else:
#     print("Error")

# 3
# animal = input()
# if animal == 'dog':
#     print('mammal')
# elif animal == 'crocodile' or animal == 'tortoise' or animal == 'snake':
#     print('reptile')
# else:
#     print("unknown")

# 4
# age = float(input())
# gender = input()
# if age >= 16:
#     if gender == 'm':
#         print('Mr.')
#     elif gender == 'f':
#         print('Ms.')
# elif age < 16:
#     if gender == 'm':
#         print('Master')
#     elif gender == 'f':
#         print('Miss')

# 5
# product = input()
# city = input()
# quantity = float(input())
# price = 0
# if city == 'Sofia':
#     if product == "coffee":
#         price = 0.50
#     elif product == 'water':
#         price = 0.80
#     elif product == 'beer':
#         price = 1.20
#     elif product == 'sweets':
#         price = 1.45
#     elif product == 'peanuts':
#         price = 1.60
# elif city == 'Plovdiv':
#     if product == "coffee":
#         price = 0.40
#     elif product == 'water':
#         price = 0.70
#     elif product == 'beer':
#         price = 1.15
#     elif product == 'sweets':
#         price = 1.30
#     elif product == 'peanuts':
#         price = 1.50
# elif city == 'Varna':
#     if product == "coffee":
#         price = 0.45
#     elif product == 'water':
#         price = 0.70
#     elif product == 'beer':
#         price = 1.10
#     elif product == 'sweets':
#         price = 1.35
#     elif product == 'peanuts':
#         price = 1.55
# total = quantity * price
# print(total)

# 6
# number = int(input())
# if -100 <= number <= 100 and number != 0:
#     print("Yes")
# else:
#     print('No')

# 7
# hour = int(input())
# day = input()
# if (day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' \
#         or day == 'Thursday' or day == 'Friday' or day == 'Saturday') \
#         and 10 <= hour <= 18:
#     print("open")
# else:
#     print("closed")

# 8
# day = input()
# price = 0
# if day == 'Monday' or day == 'Tuesday' or day == 'Friday':
#     price = 12
# elif day == 'Wednesday' or day == 'Thursday':
#     price = 14
# elif day == 'Saturday' or day == 'Sunday':
#     price = 16
# print(price)

# 9
# product_name = input()
# if product_name == 'banana' or product_name == "apple" or product_name == 'kiwi' \
#         or product_name == "cherry" or product_name == 'lemon' \
#         or product_name == 'grapes':
#     print('fruit')
# elif product_name == 'tomato' or product_name == "cucumber" \
#         or product_name == 'pepper' or product_name == "carrot":
#     print('vegetable')
# else:
#     print("unknown")

# 10
# number = int(input())
# if not (100 <= number <= 200 or number == 0):
#     print("invalid")

# 11
# fruit = input()
# weekday = input()
# quantity = float(input())
# price = 0
# condition = True
# if weekday == "Monday" or weekday == "Tuesday" or weekday == "Wednesday" \
#         or weekday == "Thursday" or weekday == "Friday":
#     if fruit == "banana":
#         price = 2.50
#     elif fruit == "apple":
#         price = 1.20
#     elif fruit == "orange":
#         price = 0.85
#     elif fruit == "grapefruit":
#         price = 1.45
#     elif fruit == "kiwi":
#         price = 2.70
#     elif fruit == "pineapple":
#         price = 5.50
#     elif fruit == "grapes":
#         price = 3.85
#     else:
#         condition = False
# elif weekday == "Saturday" or weekday == "Sunday":
#     if fruit == "banana":
#         price = 2.70
#     elif fruit == "apple":
#         price = 1.25
#     elif fruit == "orange":
#         price = 0.90
#     elif fruit == "grapefruit":
#         price = 1.60
#     elif fruit == "kiwi":
#         price = 3.00
#     elif fruit == "pineapple":
#         price = 5.60
#     elif fruit == "grapes":
#         price = 4.20
#     else:
#         condition = False
# else:
#     condition = False
# total = price * quantity
# if condition:
#     print(f"{total:.2f}")
# else:
#     print("error")

# 12
# city = input()
# sales = float(input())
# commission_in_percent = 0
# condition = True
# if city == "Sofia":
#     if 0 <= sales <= 500:
#         commission_in_percent = 5
#     elif 500 < sales <= 1000:
#         commission_in_percent = 7
#     elif 1000 < sales <= 10000:
#         commission_in_percent = 8
#     elif sales > 10000:
#         commission_in_percent = 12
#     else:
#         condition = False
# elif city == "Varna":
#     if 0 <= sales <= 500:
#         commission_in_percent = 4.5
#     elif 500 < sales <= 1000:
#         commission_in_percent = 7.5
#     elif 1000 < sales <= 10000:
#         commission_in_percent = 10
#     elif sales > 10000:
#         commission_in_percent = 13
#     else:
#         condition = False
# elif city == "Plovdiv":
#     if 0 <= sales <= 500:
#         commission_in_percent = 5.5
#     elif 500 < sales <= 1000:
#         commission_in_percent = 8
#     elif 1000 < sales <= 10000:
#         commission_in_percent = 12
#     elif sales > 10000:
#         commission_in_percent = 14.5
#     else:
#         condition = False
# else:
#     condition = False
# total_commission = sales * commission_in_percent / 100
# if condition:
#     print(f"{total_commission:.2f}")
# else:
#     print("error")

# exercise
# 1
# type_of_projection = input()
# rows = int(input())
# columns = int(input())
# income = 0
# total_places = rows * columns
# price = 0
# if type_of_projection == "Premiere":
#     price = 12.00
# elif type_of_projection == "Normal":
#     price = 7.50
# elif type_of_projection == "Discount":
#     price = 5.00
# income = total_places * price
# print(f"{income:.2f} leva")

# 2
# degrees = int(input())
# time_of_day = input()
# outfit = ''
# shoes = ''
# if time_of_day == "Morning":
#     if 10 <= degrees <= 18:
#         outfit = 'Sweatshirt'
#         shoes = 'Sneakers'
#     elif 18 < degrees <= 24:
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#     elif degrees >= 25:
#         outfit = 'T-Shirt'
#         shoes = 'Sandals'
# if time_of_day == "Afternoon":
#     if 10 <= degrees <= 18:
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#     elif 18 < degrees <= 24:
#         outfit = 'T-Shirt'
#         shoes = 'Sandals'
#     elif degrees >= 25:
#         outfit = 'Swim Suit'
#         shoes = 'Barefoot'
# if time_of_day == "Evening":
#     if 10 <= degrees <= 18:
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#     elif 18 < degrees <= 24:
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
#     elif degrees >= 25:
#         outfit = 'Shirt'
#         shoes = 'Moccasins'
# print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

# 3
# type_of_flowers = input()
# number_of_flowers = int(input())
# budget = int(input())
# total_price = 0
#
# if type_of_flowers == "Roses":
#     total_price = number_of_flowers * 5
# elif type_of_flowers == "Dahlias":
#     total_price = number_of_flowers * 3.80
# elif type_of_flowers == "Tulips":
#     total_price = number_of_flowers * 2.80
# elif type_of_flowers == "Narcissus":
#     total_price = number_of_flowers * 3
# elif type_of_flowers == "Gladiolus":
#     total_price = number_of_flowers * 2.50
#
# if type_of_flowers == "Roses" and number_of_flowers > 80:
#     total_price -= total_price * 0.1
# if type_of_flowers == "Dahlias" and number_of_flowers > 90:
#     total_price -= total_price * 0.15
# if type_of_flowers == "Tulips" and number_of_flowers > 80:
#     total_price -= total_price * 0.15
# if type_of_flowers == "Narcissus" and number_of_flowers < 120:
#     total_price += total_price * 0.15
# if type_of_flowers == "Gladiolus" and number_of_flowers < 80:
#     total_price += total_price * 0.20
#
# difference = abs(total_price - budget)
# if budget >= total_price:
#     print(f"Hey, you have a great garden with {number_of_flowers} "
#           f"{type_of_flowers} and {difference:.2f} leva left.")
# else:
#     print(f"Not enough money, you need {difference:.2f} leva more.")

# 4
# budget = int(input())
# season = input()
# number_of_fishermen = int(input())
# rent = 0
#
# if season == "Spring":
#     rent = 3000
# elif season == "Summer" or season == "Autumn":
#     rent = 4200
# elif season == "Winter":
#     rent = 2600
#
# if number_of_fishermen <= 6:
#     rent -= rent * 0.1
# elif 7 <= number_of_fishermen <= 11:
#     rent -= rent * 0.15
# elif number_of_fishermen >= 12:
#     rent -= rent * 0.25
#
# if number_of_fishermen % 2 == 0 and season != "Autumn":
#     rent -= rent * 0.05
#
# difference = abs(budget - rent)
#
# if budget >= rent:
#     print(f"Yes! You have {difference:.2f} leva left.")
# else:
#     print(f"Not enough money! You need {difference:.2f} leva.")

# 5
# budget = float(input())
# season = input()
# expenses = 0
# destination = ''
# place = ''
# if budget <= 100:
#     destination = 'Bulgaria'
#     if season == 'summer':
#         expenses = budget * 0.30
#         place = 'Camp'
#     elif season == "winter":
#         expenses = budget * 0.70
#         place = 'Hotel'
# elif budget <= 1000:
#     destination = 'Balkans'
#     if season == 'summer':
#         expenses = budget * 0.40
#         place = 'Camp'
#     elif season == "winter":
#         expenses = budget * 0.80
#         place = 'Hotel'
# elif budget > 1000:
#     destination = 'Europe'
#     expenses = budget * 0.90
#     place = 'Hotel'
# print(f"Somewhere in {destination}")
# print(f"{place} - {expenses:.2f}")

# 6
# n1 = int(input())
# n2 = int(input())
# operator = input()
# result = 0
# result_type = ''
# condition = True
#
# if operator == "+":
#     result = n1 + n2
# elif operator == "-":
#     result = n1 - n2
# elif operator == "*":
#     result = n1 * n2
# elif operator == "/":
#     if n2 == 0:
#         condition = False
#     else:
#         result = n1 / n2
# elif operator == "%":
#     if n2 == 0:
#         condition = False
#     else:
#         result = n1 % n2
#
# if result % 2 == 0:
#     result_type = 'even'
# else:
#     result_type = 'odd'
#
# if not condition:
#     print(f"Cannot divide {n1} by zero")
# else:
#     if operator == "+" or operator == "-" or operator == "*":
#         print(f"{n1} {operator} {n2} = {result} - {result_type}")
#     elif operator == "/":
#         print(f"{n1} / {n2} = {result:.2f}")
#     elif operator == "%":
#         print(f"{n1} % {n2} = {result}")

# 7
# month_of_stay = input()
# days_of_stay = int(input())
# price_studio = 0
# price_apartment = 0
#
# if month_of_stay == "May" or month_of_stay == "October":
#     price_studio = 50
#     price_apartment = 65
# elif month_of_stay == "June" or month_of_stay == "September":
#     price_studio = 75.20
#     price_apartment = 68.70
# elif month_of_stay == "July" or month_of_stay == "August":
#     price_studio = 76
#     price_apartment = 77
#
# total_studio = days_of_stay * price_studio
# total_apartment = days_of_stay * price_apartment
#
# if 7 < days_of_stay <= 14 and (month_of_stay == "May" or month_of_stay == "October"):
#     total_studio -= total_studio * 0.05
# if days_of_stay > 14 and (month_of_stay == "May" or month_of_stay == "October"):
#     total_studio -= total_studio * 0.30
# if days_of_stay > 14 and (month_of_stay == "June" or month_of_stay == "September"):
#     total_studio -= total_studio * 0.20
# if days_of_stay > 14:
#     total_apartment -= total_apartment * 0.10
#
# print(f"Apartment: {total_apartment:.2f} lv.")
# print(f"Studio: {total_studio:.2f} lv.")

# 8
# hour_of_exam = int(input())
# minute_of_exam = int(input())
# hour_of_arrival = int(input())
# minute_of_arrival = int(input())
# exam_time_in_minutes = hour_of_exam * 60 + minute_of_exam
# arrival_time_in_minutes = hour_of_arrival * 60 + minute_of_arrival
# difference = abs(arrival_time_in_minutes - exam_time_in_minutes)
# difference_hours = difference // 60
# difference_minutes = difference % 60
#
# if arrival_time_in_minutes > exam_time_in_minutes:
#     print("Late")
# elif exam_time_in_minutes - 30 <= arrival_time_in_minutes <= exam_time_in_minutes:
#     print("On time")
# elif arrival_time_in_minutes < exam_time_in_minutes - 30:
#     print("Early")
#
# if difference != 0:
#     if exam_time_in_minutes - 60 < arrival_time_in_minutes < exam_time_in_minutes:
#         print(f"{difference} minutes before the start")
#     elif exam_time_in_minutes - 60 >= arrival_time_in_minutes:
#         if difference_minutes < 10:
#             print(f"{difference_hours}:0{difference_minutes} hours before the start")
#         else:
#             print(f"{difference_hours}:{difference_minutes} hours before the start")
#     elif exam_time_in_minutes < arrival_time_in_minutes < exam_time_in_minutes + 60:
#         print(f"{difference} minutes after the start")
#     elif arrival_time_in_minutes >= exam_time_in_minutes + 60:
#         if difference_minutes < 10:
#             print(f"{difference_hours}:0{difference_minutes} hours after the start")
#         else:
#             print(f"{difference_hours}:{difference_minutes} hours after the start")

# 9
# days_of_stay = int(input())
# type_of_premise = input()
# evaluation = input()
# total = 0
#
# if type_of_premise == "room for one person":
#     total = (days_of_stay - 1) * 18
# elif type_of_premise == "apartment":
#     total = (days_of_stay - 1) * 25
#     if days_of_stay < 10:
#         total -= total * 0.30
#     elif 10 <= days_of_stay <= 15:
#         total -= total * 0.35
#     elif days_of_stay > 15:
#         total -= total * 0.50
# elif type_of_premise == "president apartment":
#     total = (days_of_stay - 1) * 35
#     if days_of_stay < 10:
#         total -= total * 0.10
#     elif 10 <= days_of_stay <= 15:
#         total -= total * 0.15
#     elif days_of_stay > 15:
#         total -= total * 0.20
#
# if evaluation == "positive":
#     total += total * 0.25
# elif evaluation == "negative":
#     total -= total * 0.10
#
# print(f"{total:.2f}")

# additional
# 1
# budget = float(input())
# category = input()
# number_of_people = int(input())
# transport = 0
# difference = 0
#
# if 1 <= number_of_people <= 4:
#     transport = budget * 0.75
# elif 5 <= number_of_people <= 9:
#     transport = budget * 0.60
# elif 10 <= number_of_people <= 24:
#     transport = budget * 0.50
# elif 25 <= number_of_people <= 49:
#     transport = budget * 0.40
# elif number_of_people >= 50:
#     transport = budget * 0.25
#
# if category == "VIP":
#     difference = abs(budget - transport - number_of_people * 499.99)
#     if budget >= (transport + number_of_people * 499.99):
#         print(f"Yes! You have {difference:.2f} leva left.")
#     elif budget < (transport + number_of_people * 499.99):
#         print(f"Not enough money! You need {difference:.2f} leva.")
# elif category == "Normal":
#     difference = abs(budget - transport - number_of_people * 249.99)
#     if budget >= (transport + number_of_people * 249.99):
#         print(f"Yes! You have {difference:.2f} leva left.")
#     elif budget < (transport + number_of_people * 249.99):
#         print(f"Not enough money! You need {difference:.2f} leva.")

# 2
# juniors = int(input())
# seniors = int(input())
# track_type = input()
# total = 0
# if track_type == "trail":
#     total = juniors * 5.50 + seniors * 7
# elif track_type == "cross-country":
#     total = juniors * 8 + seniors * 9.50
# elif track_type == "downhill":
#     total = juniors * 12.25 + seniors * 13.75
# elif track_type == "road":
#     total = juniors * 20 + seniors * 21.50
# if track_type == "cross-country" and (juniors + seniors) >= 50:
#     total -= total * 0.25
# total -= total * 0.05
# print(f"{total:.2f}")

# 3
# number_of_chrysanthemum = int(input())
# number_of_roses = int(input())
# number_of_tulips = int(input())
# season = input()
# is_it_holiday = input()
# total = 0
#
# if season == "Summer" or season == "Spring":
#     total = number_of_chrysanthemum * 2.00 + number_of_roses * \
#             4.10 + number_of_tulips * 2.50
# elif season == "Autumn" or season == "Winter":
#     total = number_of_chrysanthemum * 3.75 + number_of_roses * \
#             4.50 + number_of_tulips * 4.15
#
# if is_it_holiday == "Y":
#     total += total * 0.15
#
# if season == "Spring" and number_of_tulips > 7:
#     total -= total * 0.05
#
# if season == "Winter" and number_of_roses >= 10:
#     total -= total * 0.10
#
# if (number_of_chrysanthemum + number_of_roses + number_of_tulips) > 20:
#     total -= total * 0.20
#
# total += 2
#
# print(f"{total:.2f}")

# 4
# budget = float(input())
# season = input()
# car_class = ''
# car_type = ''
# expense = 0
# if budget <= 100:
#     car_class = "Economy class"
#     if season == "Summer":
#         car_type = "Cabrio"
#         expense = budget * 0.35
#     elif season == "Winter":
#         car_type = "Jeep"
#         expense = budget * 0.65
# elif 100 < budget <= 500:
#     car_class = "Compact class"
#     if season == "Summer":
#         car_type = "Cabrio"
#         expense = budget * 0.45
#     elif season == "Winter":
#         car_type = "Jeep"
#         expense = budget * 0.80
# elif budget > 500:
#     car_class = "Luxury class"
#     car_type = "Jeep"
#     expense = budget * 0.90
# print(f"{car_class}")
# print(f"{car_type} - {expense:.2f}")

# 5
# budget = float(input())
# season = input()
# location = ''
# place_to_stay = ''
# expense = 0
# if budget <= 1000:
#     place_to_stay = "Camp"
#     if season == "Summer":
#         location = "Alaska"
#         expense = budget * 0.65
#     elif season == "Winter":
#         location = "Morocco"
#         expense = budget * 0.45
# elif 1000 < budget <= 3000:
#     place_to_stay = "Hut"
#     if season == "Summer":
#         location = "Alaska"
#         expense = budget * 0.80
#     elif season == "Winter":
#         location = "Morocco"
#         expense = budget * 0.60
# elif budget > 3000:
#     place_to_stay = "Hotel"
#     if season == "Summer":
#         location = "Alaska"
#         expense = budget * 0.90
#     elif season == "Winter":
#         location = "Morocco"
#         expense = budget * 0.90
# print(f"{location} - {place_to_stay} - {expense:.2f}")

# 6
# season = input()
# km_per_month = float(input())
# salary_per_km = 0
# if km_per_month <= 5000:
#     if season == "Spring" or season == "Autumn":
#         salary_per_km = 0.75
#     elif season == "Summer":
#         salary_per_km = 0.90
#     elif season == "Winter":
#         salary_per_km = 1.05
# elif 5000 < km_per_month <= 10000:
#     if season == "Spring" or season == "Autumn":
#         salary_per_km = 0.95
#     elif season == "Summer":
#         salary_per_km = 1.10
#     elif season == "Winter":
#         salary_per_km = 1.25
# elif 10000 < km_per_month <= 20000:
#     salary_per_km = 1.45
# total = km_per_month * salary_per_km * 4
# total -= total * 0.10
# print(f"{total:.2f}")

# 7
# season = input()
# type_of_group = input()
# number_of_students = int(input())
# number_of_nights = int(input())
# price_per_night = 0
# sport = ''
# if type_of_group == "boys":
#     if season == "Winter":
#         price_per_night = 9.60
#         sport = "Judo"
#     elif season == "Spring":
#         price_per_night = 7.20
#         sport = "Tennis'"
#     elif season == "Summer":
#         price_per_night = 15
#         sport = "Football"
# elif type_of_group == "girls":
#     if season == "Winter":
#         price_per_night = 9.60
#         sport = "Gymnastics"
#     elif season == "Spring":
#         price_per_night = 7.20
#         sport = "Athletics"
#     elif season == "Summer":
#         price_per_night = 15
#         sport = "Volleyball"
# elif type_of_group == "mixed":
#     if season == "Winter":
#         price_per_night = 10
#         sport = "Ski"
#     elif season == "Spring":
#         price_per_night = 9.50
#         sport = "Cycling"
#     elif season == "Summer":
#         price_per_night = 20
#         sport = "Swimming"
# total = number_of_students * number_of_nights * price_per_night
# if number_of_students >= 50:
#     total -= total * 0.50
# elif 50 > number_of_students >= 20:
#     total -= total * 0.15
# elif 20 > number_of_students >= 10:
#     total -= total * 0.05
# print(f"{sport} {total:.2f} lv.")

# 8

















