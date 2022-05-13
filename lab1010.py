

# 1
# checked_books = 0
# needed_book = input()
# while 1:
#     book = input()
#     if book == "No More Books":
#         print("The book you search is not here!")
#         print(f"You checked {checked_books} books.")
#         break
#     elif book == needed_book:
#         print(f"You checked {checked_books} books and found it.")
#         break
#     checked_books += 1

# 2
# allowed_nok_grades = int(input())
# last_name = ''
# strikes = 0
# sum_of_eval = 0
# number_of_tasks = 0
# average = 0
# while 1:
#     current_task_name = input()
#     if current_task_name == "Enough":
#         average = sum_of_eval / number_of_tasks
#         print(f"Average score: {average:.2f}")
#         print(f"Number of problems: {number_of_tasks}")
#         print(f"Last problem: {last_name}")
#         break
#     current_task_eval = float(input())
#     number_of_tasks += 1
#     sum_of_eval += current_task_eval
#     last_name = current_task_name
#     if current_task_eval <= 4:
#         strikes += 1
#         if strikes == allowed_nok_grades:
#             print(f"You need a break, {strikes} poor grades.")
#             break

# 3
# vacation_cost = float(input())
# saved_money = float(input())
# days_elapsed = 0
# days_been_spending = 0
# while saved_money < vacation_cost and days_been_spending < 5:
#     daily_action = input()
#     daily_amount = float(input())
#     days_elapsed += 1
#     if daily_action == "save":
#         saved_money += daily_amount
#         days_been_spending = 0
#     elif daily_action == "spend":
#         saved_money -= daily_amount
#         days_been_spending += 1
#         if saved_money < 0:
#             saved_money = 0
# if days_been_spending == 5:
#     print(f"You can't save the money.")
#     print(f"{days_elapsed}")
# elif saved_money >= vacation_cost:
#     print(f"You saved the money for {days_elapsed} days.")

# 4
# daily_steps_total = 0
# is_goal_reached = True
# while 1:
#     command = (input())
#     if command == "Going home":
#         command = (input())
#         daily_steps_entry = int(command)
#         daily_steps_total += daily_steps_entry
#         if daily_steps_total < 10000:
#             is_goal_reached = False
#             break
#         else:
#             break
#     else:
#         daily_steps_entry = int(command)
#         daily_steps_total += daily_steps_entry
#         if daily_steps_total >= 10000:
#             break
# difference = abs(10000 - daily_steps_total)
# if is_goal_reached:
#     print("Goal reached! Good job!")
#     print(f"{difference} steps over the goal!")
# else:
#     print(f"{difference} more steps to reach goal.")

# 5
# change_money = float(input())
# change_money = int(100 * change_money)
# coins = 0
# coins += change_money // 200
# change_money %= 200
# coins += change_money // 100
# change_money %= 100
# coins += change_money // 50
# change_money %= 50
# coins += change_money // 20
# change_money %= 20
# coins += change_money // 10
# change_money %= 10
# coins += change_money // 5
# change_money %= 5
# coins += change_money // 2
# change_money %= 2
# coins += change_money // 1
# change_money %= 1
# print(coins)

# 6
# cake_width = int(input())
# cake_length = int(input())
# cake = cake_width * cake_length
# is_there_more_cake = True
# while 1:
#     command = input()
#     if command == "STOP":
#         break
#     else:
#         pieces_taken = int(command)
#         if pieces_taken < cake:
#             cake -= pieces_taken
#         else:
#             needed = pieces_taken - cake
#             is_there_more_cake = False
#             break
# if is_there_more_cake:
#     print(f"{cake} pieces are left.")
# else:
#     print(f"No more cake left! You need {needed} pieces more.")

# 7
# free_width = int(input())
# free_length = int(input())
# free_height = int(input())
# free_total = free_width * free_length * free_height
# allocated_space = 0
# command = ''
# is_there_free_space = True
# temp = 0
# insufficient = 0
# while 1:
#     command = input()
#     if command == "Done":
#         break
#     temp = allocated_space + int(command)
#     if temp < free_total:
#         allocated_space += int(command)
#     else:
#         is_there_free_space = False
#         allocated_space += int(command)
#         insufficient = abs(allocated_space - free_total)
#         break
# leftover = abs(free_total - allocated_space)
# if is_there_free_space:
#     print(f"{leftover} Cubic meters left.")
# else:
#     print(f"No more free space! You need {insufficient} "
#           f"Cubic meters more.")









