'''
Mr. Code Stark was surprised to hear about the Roman numerals. The Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M each representing a value as shown below. These symbols are connected together to represent any number.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 
2 is written as II in Roman numeral, just two one's added together.
12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Now Help Mr. Code Stark write the logic to convert a given number to roman numeral.
Input Format:
One line containing the integer number
Output Format:
The roman numeral for the integer given in the input.
Sample Input-1:
14
Sample Output-1:
XIV
Explanation: The roman literal for the number 14 is XIV.
Instruction: To run your custom test cases strictly map your input and output layout with the visible test cases.
'''
CODE:
def num_to_rom(n):
  values=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
  symbols=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
  roman=''
  i=0
  while n!=0:
    while n>=values[i]:
      roman+=symbols[i]
      n-=values[i]
    i+=1
  return roman
  n=int(input())
  print(num_to_rom(n))
