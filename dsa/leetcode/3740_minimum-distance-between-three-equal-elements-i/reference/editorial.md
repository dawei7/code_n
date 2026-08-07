### Approach: Brute Force

#### Intuition

This problem is a simplified version of [3741. Minimum Distance Between Three Equal Elements II](https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/). Since the constraints are smaller, a brute force approach is feasible.

First, consider the formula for the sum of absolute differences. It can be observed that this value is equivalent to the sum of the three sides of a generalized triangle. Regardless of the order of the three selected indices, the total distance always simplifies to twice the length of the segment formed by the two endpoints. In other words, if the leftmost index is $i$ and the rightmost index is $k$, then the required distance is $2 \times (k - i)$.

Therefore, we use three nested loops to enumerate all possible ordered triplets. If the elements at the selected indices in $\textit{nums}$ are equal, we compute the distance as described above and update the global minimum.

#### Implementation

```python
class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                if nums[i] != nums[j]:
                    continue
                for k in range(j + 1, n):
                    if nums[j] == nums[k]:
                        ans = min(ans, k - i)
                        break

        return -1 if ans == n + 1 else ans * 2
```

#### Complexity Analysis

Let $n$ be the length of $\textit{nums}$.

- Time complexity: $O(n^3)$.

  The solution uses three nested loops, each taking $O(n)$ time.

- Space complexity: $O(1)$.

  Only a constant amount of extra space is used.

---