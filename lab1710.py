# 1
# n = int(input())
# counter = 1
# all_is_printed = False
# for row in range(1, n + 1):
#     for column in range(1, row + 1):
#         print(counter, end=' ')
#         counter += 1
#         if counter > n:
#             all_is_printed = True
#             break
#     if all_is_printed:
#         break
#     print()

# 2
# first_number = int(input())
# second_number = int(input())
# for current_number in range(first_number, second_number + 1):
#     odd_digits_sum = 0
#     even_digits_sum = 0
#     current_number_as_string = str(current_number)
#     for index, digit in enumerate(current_number_as_string):
#         if index % 2 == 0:
#             odd_digits_sum += int(digit)
#         else:
#             even_digits_sum += int(digit)
#     if odd_digits_sum == even_digits_sum:
#         print(current_number, end=' ')

# 3
# sum_of_prime = 0
# sum_of_nonprime = 0
# while 1:
#     entry_as_string = (input())
#     if entry_as_string == "stop":
#         break
#     entry_as_number = int(entry_as_string)
#     if entry_as_number < 0:
#         print("Number is negative.")
#     else:
#         it_is_prime = True
#         for i in range(2, entry_as_number):
#             if entry_as_number % i == 0:
#                 it_is_prime = False
#                 break
#         if it_is_prime:
#             sum_of_prime += entry_as_number
#         else:
#             sum_of_nonprime += entry_as_number
# print(f"Sum of all prime numbers is: {sum_of_prime}")
# print(f"Sum of all non prime numbers is: {sum_of_nonprime}")

# 4
# number_of_judges = int(input())
# total_presentations = 0
# total_sum = 0
# while 1:
#     title_of_presentation = input()
#     if title_of_presentation == "Finish":
#             break
#     total_presentations += 1
#     sum_of_evaluations = 0
#     for i in range(1, number_of_judges + 1):
#         current_evaluation = float(input())
#         sum_of_evaluations += current_evaluation
#     average_evaluation = sum_of_evaluations / number_of_judges
#     print(f"{title_of_presentation} - {average_evaluation:.2f}.")
#     total_sum += average_evaluation
# total_average = total_sum / total_presentations
# print(f"Student's final assessment is {total_average:.2f}.")

# 5
# n = int(input())
# for i in range(1111, 9999 + 1):
#     i_as_string = str(i)
#     number_is_special = True
#     for j in i_as_string:
#         if int(j) == 0 or n % int(j) != 0:
#             number_is_special = False
#             break
#     if number_is_special:
#         print(i, end=' ')

# 6
# tickets_all_movies = 0
# student_current_movie = 0
# standard_current_movie = 0
# kid_current_movie = 0
# command = input()
# while command != "Finish":
#     movie_name = command
#     free_places = int(input())
#     total_places = free_places
#     sold_tickets = 0
#     while free_places > 0:
#         ticket_type = input()
#         if ticket_type == "End":
#             break
#         elif ticket_type == "student":
#             student_current_movie += 1
#         elif ticket_type == "standard":
#             standard_current_movie += 1
#         elif ticket_type == "kid":
#             kid_current_movie += 1
#         free_places -= 1
#         sold_tickets += 1
#         tickets_all_movies += 1
#     percent = sold_tickets / total_places * 100
#     print(f"{movie_name} - {percent:.2f}% full.")
#     command = input()
# print(f"Total tickets: {tickets_all_movies}")
# print(f"{student_current_movie / tickets_all_movies * 100:.2f}% student tickets.")
# print(f"{standard_current_movie / tickets_all_movies * 100:.2f}% standard tickets.")
# print(f"{kid_current_movie / tickets_all_movies * 100:.2f}% kids tickets.")
