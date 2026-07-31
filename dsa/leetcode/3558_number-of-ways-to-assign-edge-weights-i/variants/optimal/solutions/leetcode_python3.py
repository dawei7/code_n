class Solution:
 def assignEdgeWeights(self,edges):
  g=[[]for _ in range(len(edges)+2)]
  for a,b in edges:g[a]+=[b];g[b]+=[a]
  q=[(1,0,0)];d=0
  while q:
   x,p,h=q.pop();d=max(d,h)
   for y in g[x]:
    if y!=p:q+=[(y,x,h+1)]
  return pow(2,d-1,1000000007)
