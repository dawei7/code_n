from heapq import *
from math import isqrt


class Solution:
 def maximumCount(self,a,Q):
  M=max(max(a),max(v for _,v in Q));p=bytearray(b'\1')*(M+1);p[:2]=b'\0\0'
  for x in range(2,isqrt(M)+1):
   if p[x]:s=x*x;p[s:M+1:x]=b'\0'*((M-s)//x+1)
  H={}
  for i,x in enumerate(a):
   if p[x]:H.setdefault(x,[set(),[],[]])[0].add(i)
  for S,L,R in H.values():L[:]=S;R[:]=(-i for i in S);heapify(L);heapify(R)
  n=len(a)-1;t=[0]*(4*n);z=[0]*(4*n)
  def A(l,r,v,o=1,L=0,R=n-1):
   if l>r:return
   if l<=L and R<=r:t[o]+=v;z[o]+=v;return
   m=(L+R)//2
   if l<=m:A(l,r,v,o*2,L,m)
   if m<r:A(l,r,v,o*2+1,m+1,R)
   t[o]=z[o]+max(t[o*2],t[o*2+1])
  def B(x):
   S,L,R=H[x]
   while L[0] not in S:heappop(L)
   while -R[0] not in S:heappop(R)
   return L[0],-R[0]
  def C(x,v):
   if H[x][0]:l,r=B(x);A(l,r-1,v)
  for x in H:C(x,1)
  d=len(H);ans=[]
  for i,x in Q:
   y=a[i]
   if x!=y:
    if p[y]:
     C(y,-1);H[y][0].remove(i)
     if not H[y][0]:d-=1
     C(y,1)
    if p[x]:
     if x not in H:H[x]=[set(),[],[]]
     C(x,-1);S,L,R=H[x]
     if not S:d+=1
     S.add(i);heappush(L,i);heappush(R,-i);C(x,1)
    a[i]=x
   ans.append(d+t[1])
  return ans
