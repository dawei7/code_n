class Solution:
 def maxSubstrings(self,word:str)->int:
  z=0;d={}
  for i,c in enumerate(word):
   if c in d and i-d[c]>2:z+=1;d={}
   else:d.setdefault(c,i)
  return z
