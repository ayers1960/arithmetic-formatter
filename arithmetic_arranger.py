#!/usr/bin/env python
import re

def intCheck(val):
	x = re.match(r"^\d+$", val)
	if x == None:
		return "Error: Numbers must only contain digits."

	if len(str(val)) > 4:
		return "Error: Numbers cannot be more than four digits."
	return "" 

def arithmetic_arranger( input ) :

	if len(input) > 5:
		return "Error: Too many problems."
	
	pad = "+"*4

	probs = []
	for prob in input:
		probs.append( re.findall("\S+", prob))

	operators = [ '+', '-' ]
	for p in probs:
		ret = intCheck(p[0])
		if ( len(ret) ):
			return ret
		ret = intCheck(p[2])
		if ( len(ret) ):
			return ret
		if p[1] not in operators:
			return "Error: Operator must be '+' or '-'."

	for p in probs:
		print(p[0].rjust(7)+pad,end="")
	print()
	for p in probs:
		print(p[1] + " " + p[2].rjust(5) + pad, end="")
	print()
	for p in probs:
		print('-'*8 +pad,end="")
	print()

def main():
	answer = arithmetic_arranger([
						        "1 + 2"
										,"33 - 44"
										,"555 + 66"
										,"7777 - 888"
										,"7777 - 8"
										])
	print(answer)

if __name__ ==  "__main__":
				main()

