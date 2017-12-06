###
# The captcha requires you to review a sequence of digits (your puzzle input) and
# find the sum of all digits that match the next digit in the list.
# The list is circular, so the digit after the last digit is the first digit in the list.
#
# Sample test cases
# 1111 -> 4
# 1110 -> 2
# 234872 -> 2
# 87327329 -> 0
# 0 -> 0
# 6 -> 0
# 88 -> 16
###
input_number = int(input("Enter a number:-"))

previous_digit = input_number % 10
input_number //= 10
sum_of_same_digits = 0
last_digit = previous_digit

while input_number > 9:
    current_digit = input_number % 10
    if current_digit == previous_digit:
        sum_of_same_digits += current_digit
    previous_digit = current_digit
    input_number //= 10

if previous_digit == input_number:
    sum_of_same_digits += input_number

if input_number == last_digit:
    sum_of_same_digits += input_number

print ("Your final answer is:\n" + str(sum_of_same_digits))