//Not suitable for large variables > uint64 for now
package main

import (
	"fmt"
)

func main() {
	// Replace input number with your value
	input_number := 88
	previous_digit := input_number % 10
	input_number /= 10
	sum_of_same_digits := 0
	last_digit := previous_digit 
	
	// Check for all digits neighbour but last and first
	for input_number > 9{
    		current_digit := input_number % 10
    		if current_digit == previous_digit {
        		sum_of_same_digits += current_digit
		}
    		previous_digit = current_digit
    		input_number /= 10
	}
	
	if previous_digit == input_number {
    		sum_of_same_digits += input_number
	}

	if input_number == last_digit {
   		 sum_of_same_digits += input_number
	}
		
	fmt.Println("Hello, playground",sum_of_same_digits)
}
