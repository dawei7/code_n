class Solution:
 def lexicographicallySmallestString(self,s):
  n=len(s);d=[[0]*(n+1)for _ in range(n+1)]
  for i in range(n+1):d[i][i]=1
  for l in range(2,n+1,2):
   for i in range(n-l+1):
    j=i+l
    for k in range(i+1,j,2):
     if abs(ord(s[i])-ord(s[k]))in(1,25)and d[i+1][k]and d[k+1][j]:d[i][j]=1;break
  a=['']*(n+1)
  for i in range(n-1,-1,-1):
   if not d[i][n]:a[i]=min(s[j]+a[j+1]for j in range(i,n)if d[i][j])
  return a[0]
