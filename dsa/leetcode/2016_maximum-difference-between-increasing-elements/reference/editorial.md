[TOC]

## Solution

---

### Approach: Prefix Minimum Value

#### Intuition

When we fix $j$, the chosen index $i$ must satisfy $0 \leq i < j$ and $\textit{nums}[i]$ must be the smallest among those indices. Therefore, we can iterate over $j$ while maintaining the prefix minimum of $\textit{nums}[0..j-1]$, denoted as $\textit{premin}$. In this way:

- If $\textit{nums}[j] > \textit{premin}$, we update the answer with $\textit{nums}[j] - \textit{premin}$.

- Otherwise, we update the prefix minimum value $\textit{premin}$ using $\textit{nums}[j]$.

#### Implementation

```python
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        ans, premin = -1, nums[0]

        for i in range(1, n):
            if nums[i] > premin:
                ans = max(ans, nums[i] - premin)
            else:
                premin = nums[i]

        return ans
```

#### Complexity Analysis

- Time complexity: $O(n)$.

  We only need to traverse the array $\textit{nums}$ once.

- Space complexity: $O(1)$.