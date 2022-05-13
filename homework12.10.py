# 1
# number_of_bottles = int(input())
# liquid_in_ml = number_of_bottles * 750
# plates_counter = 0
# pots_counter = 0
# is_enough = True
# counter = 0
# while 1:
#     command = input()
#     if command == "End":
#         break
#     dishes_to_be_washed = int(command)
#     counter += 1
#     if counter % 3 == 0:
#         liquid_in_ml -= dishes_to_be_washed * 15
#         pots_counter += dishes_to_be_washed
#     else:
#         liquid_in_ml -= dishes_to_be_washed * 5
#         plates_counter += dishes_to_be_washed
#     if liquid_in_ml < 0:
#         is_enough = False
#         break
# leftover = abs(liquid_in_ml)
# if is_enough:
#     print("Detergent was enough!")
#     print(f"{plates_counter} dishes "
#           f"and {pots_counter} pots were washed.")
#     print(f"Leftover detergent {leftover} ml.")
# else:
#     print(f"Not enough detergent, {leftover} "
#           f"ml. more necessary!")

# 2
# needed_amount = int(input())
# achieved_amount = 0
# achieved_amount_cash = 0
# times_paid_in_cash = 0
# achieved_amount_card = 0
# times_paid_with_card = 0
# counter = 1
# is_it_achieved = False
# while 1:
#     if achieved_amount >= needed_amount:
#         is_it_achieved = True
#         break
#     command = input()
#     if command == "End":
#         break
#     current_price = int(command)
#     if counter % 2 == 0:
#         if current_price < 10:
#             print("Error in transaction!")
#         else:
#             print("Product sold!")
#             times_paid_with_card += 1
#             achieved_amount_card += current_price
#             achieved_amount += current_price
#     else:
#         if current_price > 100:
#             print("Error in transaction!")
#         else:
#             print("Product sold!")
#             times_paid_in_cash += 1
#             achieved_amount_cash += current_price
#             achieved_amount += current_price
#     counter += 1
# average_cash = achieved_amount_cash / times_paid_in_cash
# average_card = achieved_amount_card / times_paid_with_card
# if is_it_achieved:
#     print(f"Average CS: {average_cash:.2f}")
#     print(f"Average CC: {average_card:.2f}")
# else:
#     print(f"Failed to collect required money for charity.")
