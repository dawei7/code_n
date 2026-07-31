from collections import*
class Solution:
 def minMoves(s,a):
  m,n=len(a),len(a[0]);p=defaultdict(list)
  for i in range(m):
   for j in range(n):p[a[i][j]]+=(i,j),
  q=deque([(0,0,0)]);v=set()
  while q:
   i,j,d=q.popleft()
   if (i,j) in v:continue
   v.add((i,j))
   if i==m-1 and j==n-1:return d
   c=a[i][j]
   if c>'@':
    for x,y in p.pop(c,()):q.appendleft((x,y,d))
   for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
    if 0<=x<m and 0<=y<n and a[x][y]!='#':q.append((x,y,d+1))
  return -1
