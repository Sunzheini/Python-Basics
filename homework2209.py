
# additional excersizes from previous time
# 1
# b1 = float(input())
# b2 = float(input())
# h = float(input())
# area = (b1 + b2) * h / 2
# print(f"{area:.2f}")

# 2
# a = float(input())
# h = float(input())
# area = a * h / 2
# print(f"{area:.2f}")

# 3
# celcius = float(input())
# fahrenheit = (celcius * 9 / 5) + 32
# print(f"{fahrenheit:.2f}")

# 4
# vege_kg = float(input())
# fru_kg = float(input())
# total_vegi_kg = int(input())
# total_fru_kg = int(input())
# money = (vege_kg * total_vegi_kg + fru_kg * total_fru_kg) / 1.94
# print(f"{money:.2f}")

# 5
# w = float(input())
# h = float(input())
# if 3 <= h <= w <= 100:
#     w = w // 1.2
#     h -= 1
#     h = h // 0.7
#     work_places = w * h - 3
#     print(int(work_places))
# else:
#     print('error')

# 6
# pricekg_skumriq = float(input())
# pricekg_caca = float(input())
# kg_of_palamud = float(input())
# kg_of_safrid = float(input())
# kg_of_midi = int(input())
# pricekg_palamud = pricekg_skumriq + pricekg_skumriq * 0.6
# pricekg_safrid = pricekg_caca + pricekg_caca * 0.8
# total = kg_of_palamud * pricekg_palamud + \
#         kg_of_safrid * pricekg_safrid + \
#         kg_of_midi * 7.50
# print(f"{total:.2f}")

# 7
# height_x = float(input())
# width_y = float(input())
# roof_h = float(input())
# green_area = 2 * height_x * height_x + 2 * height_x * width_y - \
#              1.2 * 2 - 2 * 1.5 * 1.5
# red_area = 2 * height_x * width_y + 2 * ((height_x * roof_h) / 2)
# green_paint = green_area / 3.4
# print(f"{green_paint:.2f}")
# red_paint = red_area / 4.3
# print(f"{red_paint:.2f}")

# 8
# from math import pi
# radius_r = float(input())
# area = pi * radius_r * radius_r
# print(f"{area:.2f}")
# perimeter = 2 * pi * radius_r
# print(f"{perimeter:.2f}")

# 9
# hint = input()
# if hint == 'sunny':
#     print("It's warm outside!")
# else:
#     print("It's cold outside!")

# 10
# degrees = float(input())
# if 26.00 <= degrees <= 35.00:
#     print("Hot")
# elif 20.1 <= degrees <= 25.9:
#     print("Warm")
# elif 15.00 <= degrees <= 20.00:
#     print("Mild")
# elif 12.00 <= degrees <= 14.9:
#     print("Cool")
# elif 5.00 <= degrees <= 11.9:
#     print("Cold")
# else:
#     print("unknown")

# from 18.09
# 1
# grade = float(input())
# if grade >= 5.50:
#     print('Excellent!')

# 2
# number1 = int(input())
# number2 = int(input())
# if number1 >= number2:
#     print(number1)
# else:
#     print(number2)

# 3
# number = int(input())
# if number % 2 == 0:
#     print('even')
# else:
#     print('odd')

# 4
# passwort = input()
# defi = 's3cr3t!P@ssw0rd'
# if passwort == defi:
#     print('Welcome')
# else:
#     print('Wrong password!')

# 5
# number = int(input())
# if number < 100:
#     print('Less than 100')
# elif 100 <= number <= 200:
#     print('Between 100 and 200')
# else:
#     print('Greater than 200')

# 6
# speed = float(input())
# if speed <= 10:
#     print('slow')
# elif 10 < speed <= 50:
#     print('average')
# elif 50 < speed <= 150:
#     print('fast')
# elif 150 < speed <= 1000:
#     print('ultra fast')
# else:
#     print('extremely fast')

# 7
# from math import pi
# type = input()
# if type == 'square':
#     a = float(input())
#     area = a ** 2
#     print(f"{area:.3f}")
# elif type == 'rectangle':
#     a = float(input())
#     b = float(input())
#     area = a * b
#     print(f"{area:.3f}")
# elif type == 'circle':
#     a = float(input())
#     area = pi * (a ** 2)
#     print(f"{area:.3f}")
# elif type == 'triangle':
#     a = float(input())
#     b = float(input())
#     area = (a * b) / 2
#     print(f"{area:.3f}")

# from 19.09
# 1
# first = int(input())
# second = int(input())
# third = int(input())
# total = first + second + third # 140 sec
# minutes = total // 60
# seconds = total % 60
# if seconds < 10:
#     print(f"{minutes}:0{seconds}")
# else:
#     print(f"{minutes}:{seconds}")

# 2
# points = int(input())
# if points <= 100:
#     bonus = 5
# elif 100 < points <= 1000:
#     bonus = points * 0.2
# elif 1000 < points:
#     bonus = points * 0.1
# if points % 2 == 0:
#     bonus += 1
# elif points % 10 == 5:
#     bonus += 2
# total = points + bonus
# print(bonus)
# print(total)

# 3
# hour = int(input())
# minutes = int(input())
# minutes += 15
# add_to_h = minutes // 60
# hour += add_to_h
# if hour == 24:
#     hour = 0
# if minutes > 59:
#     minutes = minutes % 60
# if minutes < 10:
#     print(f"{hour}:0{minutes}")
# else:
#     print(f"{hour}:{minutes}")

# 4
# puzzle = 2.60
# doll = 3
# bear = 4.10
# minion = 8.20
# truck = 2
# vacation = float(input())
# order_puzzle = int(input())
# order_doll = int(input())
# order_bear = int(input())
# order_minion = int(input())
# order_truck = int(input())
# order_total = order_puzzle + order_doll + \
#               order_bear + order_minion + order_truck
# amount = order_puzzle * puzzle + order_doll * doll + order_bear * \
#          bear + order_minion * minion + order_truck * truck
# if order_total >= 50:
#     amount -= amount * 0.25
# amount -= amount * 0.1
# leftover = abs(amount - vacation)
# if amount >= vacation:
#     print(f"Yes! {leftover:.2f} lv left.")
# else:
#     print(f"Not enough money! {leftover:.2f} lv needed.")

# 5
# budget = float(input())
# statists = int(input())
# garment_price = float(input())
# garment_total = statists * garment_price
# decor = budget * 0.1
# if statists > 150:
#     garment_total -= garment_total * 0.1
# expenses = garment_total + decor
# difference = abs(budget - expenses)
# if expenses > budget:
#     print('Not enough money!')
#     print(f"Wingard needs {difference:.2f} leva more.")
# else:
#     print("Action!")
#     print(f"Wingard starts filming with {difference:.2f} leva left.")

# 6
# current_record = float(input())
# distance = float(input())
# seconds_per_meter = float(input())
# time = distance * seconds_per_meter
# times_slowed = distance // 15
# time += times_slowed * 12.5
# difference = abs(current_record - time)
# if time < current_record:
#     print(f"Yes, he succeeded! The new world record is {time:.2f} seconds.")
# else:
#     print(f"No, he failed! He was {difference:.2f} seconds slower.")

# 7
# budget = float(input())
# number_of_gpu = int(input())
# number_of_cpu = int(input())
# number_of_ram = int(input())
# total_gpu = number_of_gpu * 250
# price_cpu = total_gpu * 0.35
# total_cpu = number_of_cpu * price_cpu
# price_ram = total_gpu * 0.1
# total_ram = number_of_ram * price_ram
# amount = total_gpu + total_cpu + total_ram
# if number_of_gpu > number_of_cpu:
#     amount -= amount * 0.15
# difference = abs(budget - amount)
# if amount <= budget:
#     print(f"You have {difference:.2f} leva left!")
# else:
#     print(f"Not enough money! You need {difference:.2f} leva more!")

# 8
# from math import ceil
# name = input()
# duration = int(input())
# timeout = int(input())
# lunch = timeout / 8
# rest = timeout / 4
# total = duration + lunch + rest
# difference = abs(timeout - total)
# difference = ceil(difference)
# if timeout >= total:
#     print(f"You have enough time to watch {name} "
#           f"and left with {difference} minutes free time.")
# else:
#     print(f"You don't have enough time to watch {name}, "
#           f"you need {difference} more minutes.")

# additional
# 1
# volume_in_liters = int(input())
# first_debit = int(input())
# second_debit = int(input())
# time = float(input())
# first_work = first_debit * time
# second_work = second_debit * time
# first_percent = first_work / (first_work + second_work) * 100
# second_percent = second_work / (first_work + second_work) * 100
# fullness_in_percent = (first_work + second_work) / volume_in_liters * 100
# difference = abs(volume_in_liters - (first_work + second_work))
# if fullness_in_percent <= 100:
#     print(f"The pool is {fullness_in_percent}% full. "
#       f"Pipe 1: {first_percent:.2f}%. "
#       f"Pipe 2: {second_percent:.2f}%.")
# else:
#     print(f"For {time} hours "
#       f"the pool overflows with {difference:.2f} liters.")

# 2
# holidays = int(input())
# workdays = 365 - holidays
# time_played = holidays * 127 + workdays * 63
# difference = abs(time_played - 30000)
#
# hours = difference // 60
# minutes = difference % 60
#
# if time_played > 30000:
#     print("Tom will run away")
#     print(f"{hours} hours and {minutes} minutes more for play")
# elif time_played <= 30000:
#     print("Tom sleeps well")
#     print(f"{hours} hours and {minutes} minutes less for play")

# 3
# from math import ceil, floor
# area_in_sqm = int(input())
# grape_per_sqm = float(input())
# needed_liters_wine = int(input())
# workers = int(input())
# produced_wine = ((area_in_sqm * 0.4) * grape_per_sqm) / 2.5
# difference = abs(produced_wine - needed_liters_wine)
# if produced_wine < needed_liters_wine:
#     difference = floor(difference)
#     print(f"It will be a tough winter! "
#           f"More {difference} liters wine needed.")
# else:
#     ratio = difference / workers
#     produced_wine = floor(produced_wine)
#     print(f"Good harvest this year! Total wine: {produced_wine} liters.")
#     difference = ceil(difference)
#     ratio = ceil(ratio)
#     print(f"{difference} liters left -> {ratio} "
#           f"liters per person.")

# 4
# number_of_km = int(input())
# time_of_day = input()
# taxi_day = 0.70 + 0.79 * number_of_km
# taxi_night = 0.70 + 0.90 * number_of_km
# bus = 0.09 * number_of_km
# train = 0.06 * number_of_km
# if time_of_day == 'day':
#     if number_of_km < 20:
#         print(f"{taxi_day:.2f}")
#     elif 20 <= number_of_km < 100:
#         print(f"{bus:.2f}")
#     else:
#         print(f"{train:.2f}")
# elif time_of_day == 'night':
#     if number_of_km < 20:
#         print(f"{taxi_night:.2f}")
#     elif 20 <= number_of_km < 100:
#         print(f"{bus:.2f}")
#     else:
#         print(f"{train:.2f}")

# 5
# from math import floor
# needed_hours = int(input())
# available_days = int(input())
# employees = int(input())
# actual_days = available_days * 0.9
# manhours = actual_days * 8
# additional = employees * 2 * available_days
# actual_manhours = manhours + additional
# actual_manhours = floor(actual_manhours)
# difference = abs(needed_hours - actual_manhours)
# if actual_manhours >= needed_hours:
#     print(f"Yes!{difference} hours left.")
# else:
#     print(f"Not enough time!{difference} hours needed.")

# 6
# from math import floor, ceil
# absence = int(input())
# left_food = int(input())
# dog = float(input())
# cat = float(input())
# turtle = float(input())
# turtle = turtle /1000
# eaten = absence * (dog + cat + turtle)
# difference = abs(left_food - eaten)
# if left_food >= eaten:
#     difference = floor(difference)
#     print(f"{difference} kilos of food left.")
# else:
#     difference = ceil(difference)
#     print(f"{difference} more kilos of food are needed.")

# 7
# from math import floor, ceil
# number_of_magnos = int(input())
# number_of_zumbuls = int(input())
# number_of_roses = int(input())
# number_of_cactuses = int(input())
# price_of_gift = float(input())
# order = number_of_magnos * 3.25 + number_of_zumbuls * 4 + \
#         number_of_roses * 3.50 + number_of_cactuses * 8
# order -= order * 0.05
# difference = abs(price_of_gift - order)
# if order >= price_of_gift:
#     difference = floor(difference)
#     print(f"She is left with {difference} leva.")
# else:
#     difference = ceil(difference)
#     print(f"She will have to borrow {difference} leva.")

# 8a
# type = input()
# liters = float(input())
# if liters >= 25 and (type == 'Diesel' or type == 'Gasoline' or type == 'Gas'):
#     if type == 'Diesel':
#         print("You have enough diesel.")
#     elif type == 'Gasoline':
#         print("You have enough gasoline.")
#     else:
#         print("You have enough gas.")
# elif liters < 25 and (type == 'Diesel' or type == 'Gasoline' or type == 'Gas'):
#     if type == 'Diesel':
#         print("Fill your tank with diesel!")
#     elif type == 'Gasoline':
#         print("Fill your tank with gasoline!")
#     else:
#         print("Fill your tank with gas!")
# else:
#     print("Invalid fuel!")

# 8b (9)
# fuel_type = input()
# fuel_quantity = float(input())
# card_available = input()
# if fuel_type == 'Gas':
#     if card_available == "Yes":
#         total = fuel_quantity * 0.85
#     else:
#         total = fuel_quantity * 0.93
#     if 20 <= fuel_quantity <= 25:
#         total -= total * 0.08
#     elif fuel_quantity > 25:
#         total -= total * 0.10
#     print(f"{total:.2f} lv.")
# elif fuel_type == 'Gasoline':
#     if card_available == "Yes":
#         total = fuel_quantity * 2.04
#     else:
#         total = fuel_quantity * 2.22
#     if 20 <= fuel_quantity <= 25:
#         total -= total * 0.08
#     elif fuel_quantity > 25:
#         total -= total * 0.10
#     print(f"{total:.2f} lv.")
# elif fuel_type == 'Diesel':
#     if card_available == "Yes":
#         total = fuel_quantity * 2.21
#     else:
#         total = fuel_quantity * 2.33
#     if 20 <= fuel_quantity <= 25:
#         total -= total * 0.08
#     elif fuel_quantity > 25:
#         total -= total * 0.10
#     print(f"{total:.2f} lv.")
