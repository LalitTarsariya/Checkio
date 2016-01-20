FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

def checkio(number):
	
	
	result=""
	
	
	if number//100 > 0:
		result+=FIRST_TEN[number//100-1]+HUNDRED
	if number//10%10 == 1:
		result+=SECOND_TEN[number//10%100]
print checkio(200)
