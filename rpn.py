#!/usr/bin/env python3

import readline
import operator
import sys
from termcolor import colored, cprint

OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
}


def calculate(arg):
	stack = list()
	for operand in arg.split():
		if operand == 'q':
			quit()
		try:
			operand = float(operand)
			stack.append(operand)
		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			operator_fn = OPERATORS[operand]
			result = operator_fn(arg1, arg2)
			stack.append(result)
	return stack.pop()

def main():
	while True:
		result = calculate(input('rpn calc> '))
		if result < 0:
			result = colored(result, 'red', attrs=['bold'])
		elif result > 0:
			result = colored(result, 'green', attrs=['bold'])
		print("Result:", result)

if __name__ == '__main__':
	main()
