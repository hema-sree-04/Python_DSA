'''
Mr. Code Stark went on a space mission and landed on Planet X which uses a different number system.
Instead of having the least significant digit on the extreme right, they have the least significant digit on the extreme left.
So, 321 on our planet is 123 on the Planet X.
Mr. Code Stark wanted to find numbers that are same on both the planet Earth and Planet X. Help him find such numbers.
Input Format:
One line containing the integer
Output Format:
True - If the number is same on Planet X.
False - If the number is different on Planet X
Constraints:
1<=number<=10^19
Sample Input-1:
123
Sample Output-1:
False
Explanation:
On Planet X, the number 123 will be written as 321 so the output is False
Sample Input-2:
121
Sample Output-2:
True
Explanation:
On Planet X, the number 121 will be written as 121 so the output is True
'''
CODE:
n=int(input())
st=str(n)
l,r=0,n-1
while l<r:
  if st[l]!=st[r]:
    print("False")
    break
  l+=1
  r-=1
else:
  print("True")
