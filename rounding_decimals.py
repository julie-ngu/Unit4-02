# Created by: Julie Nguyen
# Created on: November 2017
# Created for: ICS3U
# This program rounds off an inputted decimal number to however many decimals the user wants.

def calculate_decimal(number, decimal_points):
    # rounds off inputted decimal number
    
    answer = number * (10 ** decimal_points)
    answer_2 = answer + 0.5
    answer_3 = int(answer_2)
    final_answer = answer_3 / (10 ** decimal_points)
    print (final_answer)

user_number = float(input("Enter a decimal number: "))
user_decimal_points = int(input("Enter how may decimals points you want to round off to: "))
calculate_decimal(user_number, user_decimal_points)
