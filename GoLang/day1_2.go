//Not suitable for large variables > uint64 for now
package main

import (
	"fmt"
	"math"
	"strconv"
)

func countDigits(number uint64) float64 {
	number_of_digits := 0.0
	for number > 0 {
    		number_of_digits += 1.0
    		number /= 10
	}
	return number_of_digits
}

func main() {
	// Replace input number with your value
	var input_number uint64 = 12341234
	number_of_digits := countDigits(input_number)
	var forward_steps uint64= uint64(math.Pow(10,number_of_digits/2))
	var sum_of_same_digits uint64= 0
	var double_digit uint64
	double_digit,_ = strconv.ParseUint(fmt.Sprintf("%v%v",input_number, input_number / forward_steps),10,64)
	
	// Calculate the sum
	for input_number > 0{
    		var current_digit uint64= input_number % 10
    		if current_digit == double_digit % 10 {
        		sum_of_same_digits += current_digit
		}
    		input_number /= 10
    		double_digit /= 10
	}
	fmt.Println("Answer is \n",sum_of_same_digits)
}
