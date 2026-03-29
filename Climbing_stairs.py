'''
Mr. Code Stark was climbing the stairs of the CodeTantra building, a very tall structure. During his climb, he observed that at each move, he could either take 1 step or 2 steps.
Curious about the number of distinct ways to reach the top of the stairs, he created a puzzle for his secretary, Ms. Tracy.
Given the total number of steps , determine how many distinct ways Mr. Code Stark can reach the top if at each step he can either take 1 step or 2 steps.
Input Format:
A single integer  representing the number of steps to reach the destination.
Output Format:
A single integer representing the total number of distinct ways to reach the top.
Constraints:
1<=n<=50
The solution should be efficient enough to handle values of up to 50.
Sample Input-1:
2
Sample Output-1:
2
Explanation:
Option 1: 1 Step + 1 Step
Option 2: 2 Steps
Sample Input-2:
3
Sample Output-2:
3
Explanation:
Option 1: 1 Step + 1 Step + 1 Step
Option 2: 2 Steps + 1 Step
Option 3: 1 Step + 2 Steps
'''
CODE:
n=int(input())
a,b=0,1
for i in range(0,n):
  c=a+b
  a=b
  b=c
print(b)
