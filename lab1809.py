
# # zadacha1
# first_time = int(input())
# second_time = int(input())
# third_time = int(input())
# total_time = first_time + second_time + third_time
# minutes = total_time // 60
# seconds = total_time % 60
# if seconds < 10:
#     print(f"{minutes}:0{seconds}")
# else:
#     print(f"{minutes}:{seconds}")

# # zadacha 2
# number = int(input())
# bonus_points = 0
# if number <= 100:
#     bonus_points += 5
# elif 100 < number <= 1000:
#     bonus_points += number * 0.2
# else:
#     bonus_points += number * 0.1
# if number % 2 == 0:
#     bonus_points += 1
# elif number % 10 == 5:
#     bonus_points += 2
# print(bonus_points)
# print(number + bonus_points)

# # zadacha 3
# hour = int(input())
# minutes = int(input())
# minutes += 15
# hour += minutes // 60
# minutes %= 60
# if hour > 23:
#     hour = 0
# if minutes <= 9:
#     print(f"{hour}:0{minutes}")
# else:
#     print(f"{hour}:{minutes}") #stava i print(f"{hour}:{minutes:02d}")

# # zadacha 5
# budget = float(input())
# statists = int(input())
# price_dress = float(input())
#
# decor = budget * 0.1
# all_dresses = statists * price_dress
# if statists > 150:
#     all_dresses *= 0.9
# needed_money = decor + all_dresses
# difference = abs(needed_money - budget)
#
# if needed_money > budget:
#     print("Not enough money!")
#     print(f"Wingard needs {difference:.2f} leva more")
# else:
#     print("Action!")
#     print(f"Wingard starts filming with {difference:.2f} leva left")

# # zadacha 6
# old_record = float(input())
# distance = float(input())
# time_per_meter = float(input())
# delay = distance // 15 * 12.5 # int(distance / 15), floor(dist / 15)
# total_time = distance * time_per_meter + delay
# if total_time < old_record:
#     print(f" {total_time:.2f}")
# else:
#     difference = old_record - total_time
#     print(f"{difference:.2f}")







