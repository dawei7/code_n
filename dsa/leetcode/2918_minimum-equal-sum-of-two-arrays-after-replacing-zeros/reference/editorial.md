[TOC]

## Solution

---

### Approach: Minimum Sum Matching

#### Intuition

The task requires us to replace all $0$s in the two arrays with positive integers and make their sums equal. It is not difficult to imagine that replacing all $0$s in an array with $1$s will make the sum of its elements as small as possible.

Let $\textit{sum}_1$ and $\textit{sum}_2$ be the sums of $\textit{nums}_1$ and $\textit{nums}_2$, respectively. Let $\textit{zero}_1$ and $\textit{zero}_2$ be the number of zeros in the two arrays. The minimum sums that the two arrays can reach are $\textit{sum}_1 + \textit{zero}_1$ and $\textit{sum}_2 + \textit{zero}_2$, respectively.

When there is at least one $0$ in both arrays, a solution always exists, and the minimum possible equal sum is $\max(\textit{sum}_1 + \textit{zero}_1, \textit{sum}_2 + \textit{zero}_2)$. However, if there are no $0$s in one of the arrays, and the minimum possible sum of the other array exceeds the fixed sum of this array, then it is impossible to make the sums equal, so we return $-1$.

#### Implementation

```python
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum2 = 0
        zero1 = zero2 = 0

        for i in nums1:
            sum1 += i
            if i == 0:
                sum1 += 1
                zero1 += 1

        for i in nums2:
            sum2 += i
            if i == 0:
                sum2 += 1
                zero2 += 1

        if (zero1 == 0 and sum2 > sum1) or (zero2 == 0 and sum1 > sum2):
            return -1

        return max(sum1, sum2)
```

#### Complexity Analysis

Let $n$ and $m$ be the lengths of $\textit{nums}_1$ and $\textit{nums}_2$, respectively.

- Time complexity: $O(n + m)$.

We need to traverse both arrays once.

- Space complexity: $O(1)$.

Only a few additional variables are needed.