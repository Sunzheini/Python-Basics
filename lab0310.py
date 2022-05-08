
# 1
# for number in range(1, 1001):
#     if number % 10 == 7:
#         print(number)

# 2
# import sys
# number_count = int(input())
# max_number = -sys.maxsize
# total = 0
# for i in range(number_count):
#     current_number = int(input())
#     if current_number > max_number:
#         max_number = current_number
#     total += current_number
# total -= max_number
# if total == max_number:
#     print("Yes")
#     print(f"Sum = {total}")
# else:
#     difference = abs(total - max_number)
#     print("No")
#     print(f"Diff = {difference}")

# 3
# number_count = int(input())
# p1 = 0
# p2 = 0
# p3 = 0
# p4 = 0
# p5 = 0
# for i in range(number_count):
#     current_number = int(input())
#     if current_number < 200:
#         p1 += 1
#     elif 200 <= current_number <= 399:
#         p2 += 1
#     elif 400 <= current_number <= 599:
#         p3 += 1
#     elif 600 <= current_number <= 799:
#         p4 += 1
#     elif current_number >= 800:
#         p5 += 1
# p1 = p1 / number_count * 100
# p2 = p2 / number_count * 100
# p3 = p3 / number_count * 100
# p4 = p4 / number_count * 100
# p5 = p5 / number_count * 100
# print(f"{p1:.2f}%")
# print(f"{p2:.2f}%")
# print(f"{p3:.2f}%")
# print(f"{p4:.2f}%")
# print(f"{p5:.2f}%")

# 4
# age = int(input())
# washing_machine = float(input())
# toy_price = int(input())
# money = 0
# toys = 0
# total = 0
# times_money = 0
# for i in range(1, age + 1):
#     if i % 2 == 0:
#         times_money += 1
#         money += times_money * 10
#     else:
#         toys += 1
# total = (money - times_money) + toys * toy_price
# difference = abs(total - washing_machine)
# if total >= washing_machine:
#     print(f"Yes! {difference:.2f}")
# else:
#     print(f"No! {difference:.2f}")

# 5
# open_tabs = int(input())
# salary = float(input())
# website = ''
# for i in range(open_tabs):
#     if salary > 0:
#         website = input()
#         if website == "Facebook":
#             salary -= 150
#         elif website == "Instagram":
#             salary -= 100
#         elif website == "Reddit":
#             salary -= 50
# if salary > 0:
#     print(int(salary))
# else:
#     print("You have lost your salary.")

# 6
# actor_name = input()
# academy_points = float(input())
# number_of_judges = int(input())
# total_points = academy_points
# for i in range(number_of_judges):
#     judge_name = input()
#     judge_points = float(input())
#     name_length = len(judge_name)
#     total_points += name_length * judge_points / 2
#     if total_points > 1250.5:
#         break
# if total_points <= 1250.5:
#     difference = 1250.5 - total_points
#     print(f"Sorry, {actor_name} you need {difference:.1f} more!")
# else:
#     print(f"Congratulations, {actor_name} got a "
#           f"nominee for leading role with {total_points:.1f}!")

# 7
# number_of_groups = int(input())
# musala_group = 0
# monblan_group = 0
# kili_group = 0
# k2_group = 0
# evrest_group = 0
# total = 0
# for i in range(number_of_groups):
#     members_in_group = int(input())
#     if members_in_group <= 5:
#         musala_group += members_in_group
#     elif 6 <= members_in_group <= 12:
#         monblan_group += members_in_group
#     elif 13 <= members_in_group <= 25:
#         kili_group += members_in_group
#     elif 26 <= members_in_group <= 40:
#         k2_group += members_in_group
#     elif members_in_group >= 41:
#         evrest_group += members_in_group
# total = musala_group + monblan_group + kili_group + k2_group + evrest_group
# musala_group = musala_group / total * 100
# monblan_group = monblan_group / total * 100
# kili_group = kili_group / total * 100
# k2_group = k2_group / total * 100
# evrest_group = evrest_group / total * 100
# print(f"{musala_group:.2f}%")
# print(f"{monblan_group:.2f}%")
# print(f"{kili_group:.2f}%")
# print(f"{k2_group:.2f}%")
# print(f"{evrest_group:.2f}%")

# 8
# from math import floor
# contests_participated_in = int(input())
# starting_points = int(input())
# final_points = starting_points
# position_in_contest = ''
# number_of_wins = 0
# for i in range(contests_participated_in):
#     position_in_contest = input()
#     if position_in_contest == "W":
#         number_of_wins += 1
#         final_points += 2000
#     elif position_in_contest == "F":
#         final_points += 1200
#     elif position_in_contest == "SF":
#         final_points += 720
# average_per_contest = (final_points - starting_points) / contests_participated_in
# percent_won_contests = number_of_wins / contests_participated_in * 100
# print(f"Final points: {final_points}")
# print(f"Average points: {floor(average_per_contest)}")
# print(f"{percent_won_contests:.2f}%")









