[TOC]

## Solution

--- 

### Approach: One-Time Traversal

#### Intuition

Let $n$ be the length of the array $\textit{nums}$, and perform a traversal of the indices in the range $[1, n-2]$. When traversing to index $i$, if $\textit{nums}[i]$ is equal to $(\textit{nums}[i-1] + \textit{nums}[i+1]) \times 2$, then the answer increases by $1$.

#### Implementation


```python
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n - 1):
            if nums[i] == (nums[i - 1] + nums[i + 1]) * 2:
                ans += 1
        return ans
```


#### Complexity Analysis

Let $n$ be the length of the $\textit{nums}$.

- Time complexity: $O(n)$.

- Space complexity: $O(1)$.