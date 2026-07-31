class Solution:
 def checkEqualPartitions(self,a,t):
  from math import prod
  if prod(a)!=t*t:return False
  n=len(a)
  def f(i,p,c):
   if p==t:return c
   if i==n or p>t or t%p:return False
   return f(i+1,p*a[i],True)or f(i+1,p,c)
  return f(0,1,False)
