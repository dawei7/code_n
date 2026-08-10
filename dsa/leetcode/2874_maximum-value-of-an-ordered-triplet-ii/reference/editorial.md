
## Solution

---

### Approach 1: Greedy + Prefix Suffix Array

#### Intuition

Let the length of the array $\textit{nums}$ be $n$. According to the value formula $(\textit{nums}[i] - \textit{nums}[j]) \times \textit{nums}[k]$, it can be known that when $j$ is fixed, the maximum value of the triplet is achieved when $\textit{nums}[i]$ and $\textit{nums}[k]$ respectively take the maximum values from $[0, j)$ and $[j + 1, n)$. We use $\textit{leftMax}[j]$ and $\textit{rightMax}[j]$ to maintain the maximum value of the prefix $[0, j)$ and the maximum value of the suffix $[j + 1, n)$, respectively, and enumerate $j$ in order, calculate the value $(\textit{leftMax}[j] - \textit{nums}[j]) \times \textit{rightMax}[j]$, and return the maximum value (if all values are negative, return $0$).

#### Implementation

```python
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        leftMax = [0] * n
        rightMax = [0] * n
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], nums[i - 1])
            rightMax[n - 1 - i] = max(rightMax[n - i], nums[n - i])
        res = 0
        for j in range(1, n - 1):
            res = max(res, (leftMax[j] - nums[j]) * rightMax[j])
        return res

```

#### Complexity Analysis

Let $n$ be the length of the array $\textit{nums}$.

- Time complexity: $O(n)$.

During the traversal of the array, the prefix and suffix arrays can be maintained, thus achieving a single traversal.

- Space complexity: $O(n)$.

Two arrays are needed to store the prefix and suffix maximum values.

### Approach 2: Greedy

#### Intuition

Similar to approach 1, if we fix $k$, then the value of the triplet is maximized when $\textit{nums}[i] - \textit{nums}[j]$ takes the maximum value. We can use $\textit{imax}$ to maintain the maximum value of $\textit{nums}[i]$, and $\textit{dmax}$ to maintain the maximum value of $\textit{nums}[i] - \textit{nums}[j]$. During the enumeration of $k$, update $\textit{dmax}$ and $\textit{imax}$.

#### Implementation

```python
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        res, imax, dmax = 0, 0, 0
        for k in range(n):
            res = max(res, dmax * nums[k])
            dmax = max(dmax, imax - nums[k])
            imax = max(imax, nums[k])
        return res
```

#### Complexity Analysis

Let $n$ be the length of the array $\textit{nums}$.

- Time complexity: $O(n)$.

We perform a single traversal of the array, maintaining the maximum value seen so far and the best difference.

- Space complexity: $O(1)$.

We only need two variables to maintain the maximum and maximum difference values.

---