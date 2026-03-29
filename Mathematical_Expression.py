'''
Ms. Tracy wants to help her cousin who is studying at school. She wants to build a calculator for her cousin who is not good at maths.
She decided to take help of an intern at CodeTantra.
Input Format:
A single line containing the mathematical expression
Output Format:
A single integer containing the result. Print "Invalid" as per the constraints mentioned below.
Constraints:
The mathematical expression can consists of spaces, digits and these operators '+', '-', '(' and ')'.
The mathematical expression represents a valid expression i.e. parenthesis will be balanced.
If the mathematical expression contains non-integer numbers, print "Invalid"
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is Invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
Test Cases
Test case 1
1 + 3	
4	
Test case 2
+(2 + 3)	
Invalid	
Test case 3
(1 + (4 + 5 + 2) - 3) + (6 + 8)	
23	
Test case 4
1.5 + 3.5	
Invalid
'''
CODE:
def is_valid_exp(exp):
  for ch in exp:
    if not (ch.isdigit() or ch in "+-() "):
      return False
  if "." in exp:
    return False
  res=exp.replace(" ","")
  if res.startswith("+"):
    return False
  if "(+" in res:
    return False
  stack=[]
  for ch in res:
    if ch=='(':
      stack.append(ch)
    elif ch==')':
      if not stack:
        return False
      stack.pop()
  if stack:
    return False
  else:
    return True
def evaluate_exp(exp):
  if not is_valid_exp(exp):
    return "Invalid"
  result=eval(exp)
  if isinstance(result,int):
    return str(result)
  return "Invalid"
exp=input().strip()
print(evaluate_exp(exp))
