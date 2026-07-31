from cmath import*
class Solution:
 def multiply(self,a,b):
  def F(x,s):
   n=len(x)
   if n<2:return
   e=x[::2];o=x[1::2];F(e,s);F(o,s);w=1;r=exp(s*2j*pi/n)
   for i in range(n//2):x[i]=e[i]+w*o[i];x[i+n//2]=e[i]-w*o[i];w*=r
  l=len(a)+len(b)-1;n=1
  while n<l:n*=2
  x=[complex(a[i]if i<len(a)else 0,b[i]if i<len(b)else 0)for i in range(n)]
  F(x,-1);y=x[:]
  for i in range(n):u=y[i];v=y[-i%n].conjugate();x[i]=-.25j*(u+v)*(u-v)
  F(x,1)
  return[round(x[i].real/n)for i in range(l)]
