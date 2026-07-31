class Solution:
 def shortestSuperstring(self,a,b):
  def f(s,t):
   x=t+'#'+s;p=[0]*len(x);c=0
   for i in range(1,len(x)):
    j=p[i-1]
    while j and x[i]!=x[j]:j=p[j-1]
    p[i]=j+(x[i]==x[j])
    c|=i>len(t)and p[i]==len(t)
   return c,p[-1]
  c,x=f(a,b)
  if c:return a
  c,y=f(b,a)
  if c:return b
  return min((a+b[x:],b+a[y:]),key=len)
