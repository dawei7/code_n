[TOC]

## Solution

---

### Approach 1: Traverse number pairs

#### Intuition

We use $n$ to represent the length of the array $\textit{nums}$. To count the number of pairs that meet the requirements, we can use two nested loops to traverse all pairs (i, j) that satisfy $0 \leq i < j < n$, and check individually whether $i \times j \bmod k$ is equal to $0$ and whether $\textit{nums}[i]$ is equal to $\textit{nums}[j]$.

At the same time, we use $\textit{res}$ to count the number of pairs of numbers that meet the requirements. If a pair of numbers $(i, j)$ meets the requirements, we add $1$ to $\textit{res}$. Finally, we return $\textit{res}$ as the number of pairs of numbers that meet the requirements.

#### Implementation

```python
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0  # number of pairs meeting the requirements
        for i in range(n - 1):
            for j in range(i + 1, n):
                if (i * j) % k == 0 and nums[i] == nums[j]:
                    res += 1
        return res
```

#### Complexity Analysis

Let $n$ be the length of the array $\textit{nums}$.

- Time complexity: $O(n^2)$.

This is the time complexity for traversing number pairs and counting the number of pairs that meet the requirements.

- Space complexity: $O(1)$.

Only a few additional variables are needed.