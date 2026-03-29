'''
Ms. Tracy, an expert in generating permutations, decided to create a puzzle for Mr. Code Stark. She designed the following problem to test his problem-solving skills.
Mr. Code Stark will be given an integer n(1<=n<=9)
For the string formed by the digits "123...n", there will be a total of n! unique permutations. These permutations are to be considered in sorted lexicographical order.
For example, if n=3, the string "123" will have the following permutations in sorted order:
123
132
213
231
312
321
In addition, Ms. Tracy will give Mr. Code Stark another number k such that 1<=k<=n!. Mr. Code Stark must then determine the k-th permutation possible for the string "123...n".
Input Format:
One line containing two integers n and k separated by a space where:
-n represents the length of the string (from 1 to 9). 
-k represents the k-th permutation to find (where 1<=k<=n!).
Output Format:
The output should be the k-th permutation of the string "123...n".
Sample Input-1:
3 4
Sample Output-1:
231
Explanation:
The 4th permutation of the string 123 is 231.'''
CODE:
import math
n,k=map(int,input().split())
digits=list(map(str,range(1,n+1)))
res=[]
k=k-1
for i in range(n,0,-1):
  fact=math.factorial(i-1)
  ind=k//fact
  res.append(digits.pop(ind))
  k=k%fact
print("".join(res))
