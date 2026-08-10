
## Solution

---

### Approach 1: Binary Search

This question is easy in the sense that one could run an **exhaustive iteration** to obtain the result. That could work, except that it would run out of time when the input becomes too large. So let us take a step back to look at the problem, before rushing to the implementation.

Assume that the answer is $k$, _i.e._ we've managed to complete $k$ rows of coins. These completed rows contain in total $1 + 2 + ... + k = \frac{k (k + 1)}{2}$ coins.

We could now reformulate the problem as follows:

> Find the maximum $k$ such that $\frac{k (k + 1)}{2} \le N$.

The problem seems to be one of those **search** problems. Instead of naive iteration, one could resort to another more efficient algorithm called [**_binary search_**](https://en.wikipedia.org/wiki/Binary_search_algorithm), as we can find in another similar problem called [search insert position](https://leetcode.com/articles/search-insert-position/).

**Implementation**

```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            k = (right + left) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if n < curr:
                right = k - 1
            else:
                left = k + 1
        return right
```

**Complexity Analysis**

* Time complexity : $\mathcal{O}(\log N)$.

* Space complexity : $\mathcal{O}(1)$.
<br />
<br />

---
### Approach 2: Math

If we look deeper into the formula of the problem, we could actually solve it with the help of mathematics, without using any iteration.

As a reminder, the constraint of the problem can be expressed as follows:

$k(k + 1) \le 2N$

This could be solved by [completing the square](https://en.wikipedia.org/wiki/Completing_the_square) technique,

$\left(k + \frac{1}{2}\right)^2 - \frac{1}{4} \le 2N$

that results in the following answer:

$k = \left[\sqrt{2N + \frac{1}{4}} - \frac{1}{2}\right]$

**Implementation**

```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return (int)((2 * n + 0.25)**0.5 - 0.5)
```

**Complexity Analysis**

* Time complexity : $\mathcal{O}(1)$.

* Space complexity : $\mathcal{O}(1)$.
<br />
<br />