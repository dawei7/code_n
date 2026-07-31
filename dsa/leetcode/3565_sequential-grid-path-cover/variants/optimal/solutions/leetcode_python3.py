class Solution:
 def findPath(self,g,k):
  m,n=len(g),len(g[0]);N=m*n;q=[];v=[[0]*n for _ in g]
  def f(x,y,t):
   z=g[x][y]
   if z:
    if z!=t:return
    t+=1
   v[x][y]=1;q.append([x,y])
   if len(q)==N:return q[:]
   for a,b in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
    if 0<=a<m and 0<=b<n and not v[a][b]:
     r=f(a,b,t)
     if r:return r
   q.pop();v[x][y]=0
  for i in range(m):
   for j in range(n):
    r=f(i,j,1)
    if r:return r
  return []
