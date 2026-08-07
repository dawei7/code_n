### Approach: Traversal

#### Intuition

For any integer $x$, there are two possible ways to make it divisible by $3$:

1. The number of operations required to increase $x$ to the next multiple of $3$ is $3 - (x \bmod 3)$.
2. The number of operations required to decrease $x$ to the nearest multiple of $3$ is $x \bmod 3$.

Choose the option that requires fewer operations.

For each number in $\textit{nums}$, calculate the minimum number of operations and sum them up to obtain the result.

#### Implementation

```python
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(min(x % 3, 3 - x % 3) for x in nums)
```

#### Complexity Analysis

Let $n$ be the length of $\textit{nums}$.

- Time complexity: $O(n)$.
- Space complexity: $O(1)$.