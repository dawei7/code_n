class Solution:
 def minSubarraySort(self,nums:List[int],k:int)->List[int]:
  z=[]
  for s in range(len(nums)-k+1):
   a=nums[s:s+k];l=0
   while l+1<k and a[l]<=a[l+1]:l+=1
   if l==k-1:z.append(0);continue
   r=k-1
   while a[r-1]<=a[r]:r-=1
   x,y=min(a[l:r+1]),max(a[l:r+1])
   while l and a[l-1]>x:l-=1
   while r+1<k and a[r+1]<y:r+=1
   z.append(r-l+1)
  return z
