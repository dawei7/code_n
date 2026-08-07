### Approach: One-time Traversal

#### Intuition

We traverse the array $\textit{nums}$ once, during which we use $\textit{cnt}$ and $\textit{precnt}$ to record the length of the current strictly increasing subarray and the length of the previous strictly increasing subarray, respectively.

Initially, $\textit{cnt}$ is set to $1$, and $\textit{precnt}$ is set to $0$. While traversing $\textit{nums}$, if $\textit{nums}[i]$ is greater than $\textit{nums}[i - 1]$, we increment $\textit{cnt}$ by $1$. Otherwise, the subarray is no longer increasing and we assign the value of $\textit{cnt}$ to $\textit{precnt}$ and reset $\textit{cnt}$ to $1$.

There are two cases for two adjacent subarrays that satisfy the conditions of the problem:

1. The previous subarray corresponds to $\textit{precnt}$, and the current subarray corresponds to $\textit{cnt}$. In this case, the value of $k$ is $\min(\textit{precnt}, \textit{cnt})$.

2. Both subarrays belong to the current segment represented by $\textit{cnt}$, in which case $k = \lfloor \dfrac{\textit{cnt}}{2} \rfloor$, where $\lfloor \cdot \rfloor$ denotes the floor function.

By continuously updating the maximum value of $k$ according to these two cases, we can obtain the final answer.

#### Implementation

```python
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        cnt, precnt, ans = 1, 0, 0
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                cnt += 1
            else:
                precnt, cnt = cnt, 1
            ans = max(ans, min(precnt, cnt))
            ans = max(ans, cnt // 2)
        return ans
```

#### Complexity Analysis

- Time complexity: $O(n)$.

- Space complexity: $O(1)$.

---