
## Solution

---

### Approach: Traversal

#### Intuition

First, calculate the absolute difference between the first and last elements to initialize the maximum absolute difference. Then, traverse the array to calculate the absolute difference between adjacent elements and update the answer.

Finally, return the maximum absolute difference in the circular array.

#### Implementation

```python
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        res = abs(nums[0] - nums[n - 1])
        for i in range(n - 1):
            res = max(res, abs(nums[i] - nums[i + 1]))
        return res
```

#### Complexity Analysis

Let $n$ be the length of the array.

- Time complexity: $O(n)$.

  Only need to traverse the array once.

- Space complexity: $O(1)$.

  Only a few additional variables are needed.