###
# Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list.
# That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward\
# matches it.
# Fortunately, your list has an even number of elements.
#
# ############## Sample Test Cases ######################
# 1212 -> 6
# 12341234 ->20
# 123145 -> 2
# 0 -> 0
# 70 -> 0
# 4444 -> 16
# 12345674 -> 8
###

input_number = int(input("Enter a number:-"))
sum_of_same_digits = 0
copy_input_number = input_number
number_of_digits = 0

# Get total number of digits O(n)
while copy_input_number > 0:
    number_of_digits += 1
    copy_input_number //= 10

forward_steps = 10 ** (number_of_digits // 2)

# Spread out the circular list 1234 as 123412
double_digit = int(str(input_number)+str(input_number // forward_steps))

# Calculate the sum
while input_number > 0:
    current_digit = input_number % 10
    if current_digit == double_digit % 10:
        sum_of_same_digits += current_digit
    input_number //= 10
    double_digit //= 10

print("Your final answer is:\n" + str(sum_of_same_digits))