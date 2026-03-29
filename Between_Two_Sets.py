'''
There will be two arrays of integers. Determine all integers that satisfy the following two conditions:
The elements of the first array are all factors of the integer being considered. This means the integer is a multiple of every number in the first array.
The integer being considered is a factor of all elements of the second array. This means the integer divides every number in the second array evenly.
These numbers are referred to as being between the two arrays. Determine how many such numbers exist.
Example
Input:
a=[2,4]
b=[24,36]
Output:
2
Explanation:
Common Divisors of 24 and 36 are: 1, 2, 3, 4, 6, 12
Check each divisor:
2: Not divisible by 4, so it's invalid.
3 : Not divisible by 2 and 4, so it's invalid
4: Divisible by both 2 and 4, so it's valid.
6: Not divisible by 4, so it's invalid.
12: Divisible by both 2 and 4, so it's valid.
Valid numbers: 4, 12 so the output is 2
Input Format:
The first line contains two space-separated integers, n, and m, the number of elements in arrays a and b.
The second line contains n distinct space-separated integers a[i] where 0 <= i < n.
The third line contains m distinct space-separated integers b[j] where 0 <= j < m.
Output Format:
int: the number of integers that are between the sets
Constraints
1 <= n,m <= 10
1 <= a[i] <= 100
1 <= b[j] <= 100'''
CODE:
import math
from functools import reduce

def lcm(x,y):
  return x*y//math.gcd(x,y)
def lcm_array(a):
  return reduce(lcm,a)
def gcd_array(b):
  return reduce(math.gcd,b)
def diff_bw_sets(a,b):
  l=lcm_array(a)
  g=gcd_array(b)
  cnt=0
  i=l
  while i<=g:
    if g5i==0:
      cnt+=1
    i+=1
  return cnt
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(diff_bw_sets(a,b))
