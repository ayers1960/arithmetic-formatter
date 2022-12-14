#!/usr/bin/env python
import re

def intCheck(val):
	x = re.match(r"^\d+$", val)
	if x == None:
		return "Error: Numbers must only contain digits."

	if len(str(val)) > 4:
		return "Error: Numbers cannot be more than four digits."
	return "" 

def arithmetic_arranger( input, showResults=False ) :

	if len(input) > 5:
		return "Error: Too many problems."
	
	pad = " "*4

	probs = []
	for prob in input:
		probs.append( re.findall("\S+", prob))

	widths = []
	results = []
	for (i,p) in enumerate(probs):
		widths.append( max(len(str(p[0])),len(str(p[2]))) )
	print(widths)
	operators = [ '+', '-' ]
	for p in probs:
		ret = intCheck(p[0])
		if len(ret):
			return ret
		ret = intCheck(p[2])
		if ( len(ret) ):
			return ret
		if p[1] not in operators:
			return "Error: Operator must be '+' or '-'."

		if p[1] == "+":
			results.append(int(p[0])+int(p[2]))
		else:
			results.append(int(p[0])-int(p[2]))


	answer = ""
	for (i,p) in enumerate(probs):
		if i > 0:
			answer += pad
		answer += p[0].rjust(widths[i]+2)
	answer += "\n"

	for (i,p) in enumerate(probs):
		if i > 0:
			answer += pad
		answer += p[1] + " " + p[2].rjust(widths[i])
	answer += "\n"

	for (i,p) in enumerate(probs):
		if i > 0:
			answer += pad
		answer += '-'*(widths[i]+2)

	if showResults:
		answer += "\n"
		for (i,p) in enumerate(probs):
			if i > 0:
				answer += pad
			answer += str(results[i]).rjust(widths[i]+2)

	return answer

def main():
	answer = arithmetic_arranger([
			        "1 + 2"
				,"33 - 44"
				,"555 + 45"
				,"7777 - 888"
				,"7777 - 8"
		],True)
	print(answer)

if __name__ ==  "__main__":
				main()

