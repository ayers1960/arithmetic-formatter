1 #!/usr/bin/env python
  2 import re
  3
  4 def intCheck(val):
  5   x = re.match(r"^\d+$", val)
  6   if x == None:
  7     return "Error: Numbers must only contain digits."
  8
  9   if len(str(val)) > 4:
 10     return "Error: Numbers cannot be more than four digits."
 11   return ""
 12
 13 def arithmetic_arranger( input ) :
 14
 15   if len(input) > 5:
 16     return "Error: Too many problems."
 17
 18   pad = "+"*4
 19
 20   probs = []
 21   for prob in input:
  22     probs.append( re.findall("\S+", prob))
 23
 24   operators = [ '+', '-' ]
 25   for p in probs:
 26     ret = intCheck(p[0])
 27     if ( len(ret) ):
 28       return ret
 29     ret = intCheck(p[2])
 30     if ( len(ret) ):
 31       return ret
 32     if p[1] not in operators:
 33       return "Error: Operator must be '+' or '-'."
 34
 35   for p in probs:
 36     print(p[0].rjust(7)+pad,end="")
 37   print()
 38   for p in probs:
 39     print(p[1] + " " + p[2].rjust(5) + pad, end="")
 40   print()
 41   for p in probs:
 42     print43   print()
 44
 45 def main():
 46   answer = arithmetic_arranger([
 47                     "1 + 2"
 48                     ,"33 - 44"
 49                     ,"555 + 6"
 50                     ,"7777 - 888"
 51                     ,"7777 - 8"
 52                     ])
 53   print(answer)
 54
 55 if __name__ ==  "__main__":
 56         main()
 57('-'*8 +pad,end="")
 
