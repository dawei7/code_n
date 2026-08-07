### Approach: Greedy

#### Intuition

Since the same subarray can be selected multiple times, we only need to find the subarray with the maximum possible value and select it $k$ times.

For any subarray $\textit{nums}[l..r]$, its value is defined as $\max(\textit{nums}[l..r]) - \min(\textit{nums}[l..r])$. The maximum value within a subarray cannot exceed the maximum value of the entire array, and the minimum value within a subarray cannot be smaller than the minimum value of the entire array. Therefore, the value of any subarray cannot exceed $\max(\textit{nums}) - \min(\textit{nums})$.

This upper bound is achievable by selecting a subarray that contains both the global maximum and global minimum values, such as the entire array itself. Therefore, the maximum value of a single subarray is $\max(\textit{nums}) - \min(\textit{nums})$.

Since we can select the same subarray repeatedly, the maximum total value is $k \times (\max(\textit{nums}) - \min(\textit{nums}))$.

#### Implementation

```python
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        m1 = min(nums)
        m2 = max(nums)
        return (m2 - m1) * k
```

#### Complexity Analysis

Let $n$ be the length of the array $\textit{nums}$.

- Time complexity: $O(n)$.

  We find the maximum and minimum values in a single traversal of the array.

- Space complexity: $O(1)$.

  Only a constant amount of extra space is used.

---