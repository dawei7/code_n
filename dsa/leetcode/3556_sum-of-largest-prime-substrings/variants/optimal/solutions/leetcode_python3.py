from math import isqrt
class Solution:
 def sumOfLargestPrimes(self,s:str)->int:
  p=set()
  for i in range(len(s)):
   x=0
   for c in s[i:]:
    x=x*10+int(c)
    if x>1 and all(x%d for d in range(2,isqrt(x)+1)):p.add(x)
  return sum(sorted(p)[-3:])
