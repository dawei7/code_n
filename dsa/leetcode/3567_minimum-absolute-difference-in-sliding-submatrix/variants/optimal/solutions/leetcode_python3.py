class Solution:
 def minAbsDiff(self,g,k):
  m,n=len(g),len(g[0]);r=[]
  for i in range(m-k+1):
   q=[]
   for j in range(n-k+1):
    a=sorted({g[x][y]for x in range(i,i+k)for y in range(j,j+k)})
    q.append(min((y-x for x,y in zip(a,a[1:])),default=0))
   r.append(q)
  return r
