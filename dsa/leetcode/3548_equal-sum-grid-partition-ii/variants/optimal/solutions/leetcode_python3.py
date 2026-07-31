class Solution:
 def canPartitionGrid(self,g):
  def f(a):
   s=sum(map(sum,a));p=0;v=set();w=len(a[0])
   for i in range(len(a)-1):
    p+=sum(a[i]);v.update(a[i]);d=2*p-s
    if d==0:return True
    if d>0:
     if i==0:
      if d in (a[0][0],a[0][-1]):return True
     elif w==1:
      if d in (a[0][0],a[i][0]):return True
     elif d in v:return True
   return False
  t=list(map(list,zip(*g)))
  return f(g)or f(g[::-1])or f(t)or f(t[::-1])
