class Solution:
 def maxSumDistinctTriplet(self,x,y):
  d={}
  for p,v in zip(x,y):d[p]=max(d.get(p,0),v)
  if len(d)<3:return -1
  a=b=c=0
  for v in d.values():
   if v>a:a,b,c=v,a,b
   elif v>b:b,c=v,b
   elif v>c:c=v
  return a+b+c
