class Solution:
 def minMoves(self,a,E):
  n=len(a[0])+2;a=['X'*n,*('X'+r+'X'for r in a),'X'*n];z={};c=0
  for i,r in enumerate(a):
   for j,v in enumerate(r):
    if v=='S':s=i*n+j
    elif v=='L':z[i*n+j]=1<<c;c+=1
  q=[(s,0,E,0)];b={(s,0):E};F=2**c-1;h=0
  while h<len(q):
   p,x,e,d=q[h];h+=1
   if x==F:return d
   for P in(p-1,p+1,p-n,p+n):
    v=a[P//n][P%n]
    if e and v!='X':
     y=x|z.get(P,0);f=E if v=='R'else e-1;t=P,y
     if f>b.get(t,-1):b[t]=f;q.append((P,y,f,d+1))
  return -1
