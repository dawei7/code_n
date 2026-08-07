### Approach: Dynamic Programming

#### Intuition

Let the sum of the elements in array $\textit{nums}$ be $\textit{numSum}$. According to the formula, we can obtain:

- $F(0) = 0 \times \textit{nums}[0] + 1 \times \textit{nums}[1] + \ldots + (n-1) \times \textit{nums}[n-1]$
- $F(1) = 1 \times \textit{nums}[0] + 2 \times \textit{nums}[1] + \ldots + 0 \times \textit{nums}[n-1] = F(0) + \textit{numSum} - n \times \textit{nums}[n-1]$

More generally, when $1 \le k \lt n$, $F(k) = F(k-1) + \textit{numSum} - n \times \textit{nums}[n-k]$. We can iteratively calculate different $F(k)$ values and find the maximum.

#### Implementation

```python
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f, n, numSum = 0, len(nums), sum(nums)
        for i, num in enumerate(nums):
            f += i * num
        res = f
        for i in range(n - 1, 0, -1):
            f = f + numSum - n * nums[i]
            res = max(res, f)
        return res
```

#### Complexity Analysis

Let $n$ be the length of the array $\textit{nums}$.

- Time complexity: $O(n)$.

  Computing $\textit{numSum}$ takes $O(n)$ time, and computing the initial value $F(0)$ also takes $O(n)$ time since we iterate through the array once. After that, we perform $n - 1$ iterations to compute the remaining values of $F(k)$. Each iteration updates the value using the recurrence relation:

$F(k) = F(k-1) + \textit{numSum} - n \cdot \textit{nums}[n-k]$

This update only involves a constant number of arithmetic operations, so each iteration takes $O(1)$ time. Therefore, the total time complexity is:

$O(n) +$\mathcal{O}(n)$+$\mathcal{O}(n)$= O(n)$

Overall, the algorithm runs in linear time.

- Space complexity: $O(1)$.

  Only a few variables were used.

---