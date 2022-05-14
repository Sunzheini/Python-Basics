# 1
# company_name = input()
# number_of_adult_tickets = int(input())
# number_of_children_tickets = int(input())
# net_price_adults = float(input())
# handling_tax = float(input())
#
# net_price_children = net_price_adults * 0.3
#
# sales = number_of_adult_tickets * (net_price_adults + handling_tax) + \
#         number_of_children_tickets * (net_price_children + handling_tax)
# profit = sales * 0.2
# print(f"The profit of your agency from {company_name} "
#       f"tickets is {profit:.2f} lv.")

# 2
# price_above_20_kg = float(input())
# luggage_in_kg = float(input())
# days_till_trip = int(input())
# pieces_of_luggage = int(input())
# cost_of_all_luggage = 0
# extra_payment_in_percent = 0
# total_cost = 0
# price_below_10_kg = price_above_20_kg * 0.2
# price_between_10_and_20_kg = price_above_20_kg * 0.5
#
# if luggage_in_kg < 10:
#     cost_of_all_luggage = pieces_of_luggage * price_below_10_kg
# elif 10 <= luggage_in_kg <= 20:
#     cost_of_all_luggage = pieces_of_luggage * price_between_10_and_20_kg
# elif luggage_in_kg > 20:
#     cost_of_all_luggage = pieces_of_luggage * price_above_20_kg
#
# if days_till_trip > 30:
#     extra_payment_in_percent = 10
# elif 7 <= days_till_trip <= 30:
#     extra_payment_in_percent = 15
# elif days_till_trip < 7:
#     extra_payment_in_percent = 40
#
# cost_of_all_luggage += cost_of_all_luggage * extra_payment_in_percent / 100
# print(f" The total price of bags is: {cost_of_all_luggage:.2f} lv. ")

# 3
# number_of_joineries = int(input())
# type_of_joinery = input()
# delivery_option = input()
# price = 0
#
# if number_of_joineries > 10:
#     if type_of_joinery == "90X130":
#         if 60 >= number_of_joineries > 30:
#             price = (number_of_joineries * 110) - (number_of_joineries * 110) * 0.05
#         elif number_of_joineries > 60:
#             price = (number_of_joineries * 110) - (number_of_joineries * 110) * 0.08
#     elif type_of_joinery == "100X150":
#         if 80 >= number_of_joineries > 40:
#             price = (number_of_joineries * 140) - (number_of_joineries * 140) * 0.06
#         elif number_of_joineries > 80:
#             price = (number_of_joineries * 140) - (number_of_joineries * 140) * 0.10
#     elif type_of_joinery == "130X180":
#         if 50 >= number_of_joineries > 20:
#             price = (number_of_joineries * 190) - (number_of_joineries * 190) * 0.07
#         elif number_of_joineries > 50:
#             price = (number_of_joineries * 190) - (number_of_joineries * 190) * 0.12
#     elif type_of_joinery == "200X300":
#         if 50 >= number_of_joineries > 25:
#             price = (number_of_joineries * 250) - (number_of_joineries * 250) * 0.09
#         elif number_of_joineries > 50:
#             price = (number_of_joineries * 250) - (number_of_joineries * 250) * 0.14
#     if delivery_option == "With delivery":
#         price += 60
#     if number_of_joineries > 99:
#         price -= price * 0.04
#     print(f"{price:.2f} BGN")
# else:
#     print("Invalid order")

# 4
# import math
# red_counter = 0
# orange_counter = 0
# yellow_counter = 0
# white_counter = 0
# black_counter = 0
# other_counter = 0
# points = 0
# number_of_balls = int(input())
# for i in range(number_of_balls):
#     current_colour = input()
#     if current_colour == "red":
#         points += 5
#         red_counter += 1
#     elif current_colour == "orange":
#         points += 10
#         orange_counter += 1
#     elif current_colour == "yellow":
#         points += 15
#         yellow_counter += 1
#     elif current_colour == "white":
#         points += 20
#         white_counter += 1
#     elif current_colour == "black":
#         points = math.floor(points / 2)
#         black_counter += 1
#     else:
#         other_counter += 1
# print(f"Total points: {points}")
#
# print(f"Points from red balls: {red_counter}")
# print(f"Points from orange balls: {orange_counter}")
# print(f"Points from yellow balls: {yellow_counter}")
# print(f"Points from white balls: {white_counter}")
#
# print(f"Other colors picked: {other_counter}")
#
# print(f"Divides from black balls: {black_counter}")

# 5
# import sys
#
# most_goals = -sys.maxsize
# best_player = ''
# is_there_hetrick = False
#
# while 1:
#     command = input()
#     if command == "END":
#         break
#     current_player = command
#     number_of_goals = int(input())
#     if number_of_goals > most_goals:
#         most_goals = number_of_goals
#         best_player = current_player
#         if number_of_goals >= 3:
#             is_there_hetrick = True
#             if number_of_goals >= 10:
#                 break
# print(f"{best_player} is the best player!")
# if is_there_hetrick:
#     print(f"He has scored {most_goals} goals and made a hat-trick !!!")
# else:
#     print(f"He has scored {most_goals} goals.")

# 6
# beginning = int(input())
# ending = int(input())
#
# for i in range(beginning, ending + 1):
#     number_flag = True
#     i_as_string = str(i)
#     for j in i_as_string:
#         if int(j) % 2 == 0:
#             number_flag = False
#             break
#     if number_flag:
#         print(i, end=' ')

# 6







