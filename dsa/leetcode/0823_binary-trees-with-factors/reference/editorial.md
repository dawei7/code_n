[TOC]

---
### Approach #1: Dynamic Programming [Accepted]

**Intuition**

For any valid tree, the largest value `v`, in that tree, must be the root. So, let's say that `dp(v)` is the number of ways to make a tree with root node `v`.

If the root node of the tree (with value `v`) has children with values `x` and `y` (where $x * y = v$ must be true), then there are $dp(x) * dp(y)$ ways to make this tree.

Each unique value in `A` is a valid *root* value for *at least one* tree - a tree containing just that node.

To get the total number of valid trees, we should calculate how many valid trees there are with each possible root value, and then add them all together.

**Algorithm**

Let $\text{dp}[i]$ be the number of ways to have a root node with value $A[i]$.

Since in the above example we always have `x < v` and `y < v`, we can calculate the values of $\text{dp}[i]$ in increasing order using dynamic programming.

For some root value $A[i]$, let's try to find candidates for the children with values $A[j]$ and $A[i] / A[j]$ (so that evidently $A[j] * (A[i] / A[j]) = A[i]$).  To do this quickly, we will need `index` which looks up this value: if $A[k] = A[i] / A[j]$, then $index[A[i] / A[j]] = k$.

After, we'll add all possible $\text{dp}[j] * \text{dp}[k]$ (with `j < i, k < i`) to our answer $\text{dp}[i]$.  In our Java implementation, we carefully used `long` so avoid overflow issues.

```python
class Solution(object):
    def numFactoredBinaryTrees(self, A):
        MOD = 10 ** 9 + 7
        N = len(A)
        A.sort()
        dp = [1] * N
        index = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for j in xrange(i):
                if x % A[j] == 0: #A[j] will be left child
                    right = x / A[j]
                    if right in index:
                        dp[i] += dp[j] * dp[index[right]]
                        dp[i] %= MOD

        return sum(dp) % MOD
```

**Complexity Analysis**

* Time Complexity:  $O(N^2)$, where $N$ is the length of `A`.  This comes from the two for-loops iterating `i` and `j`.

* Space Complexity: $O(N)$, the space used by `dp` and `index`.