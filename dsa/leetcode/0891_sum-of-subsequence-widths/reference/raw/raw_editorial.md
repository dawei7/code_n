[TOC]

## Solution
---
### Approach 1: Mathematical

**Intuition**

Let's try to count the number of subsequences with minimum `A[i]` and maximum `A[j]`.

**Algorithm**

We can sort the array as it doesn't change the answer.  After sorting the array, this allows us to know that the number of subsequences with minimum `A[i]` and maximum `A[j]` is $$2^{j-i-1}$$.  Hence, the desired answer is:

$$
\sum\limits_{j > i} (2^{j-i-1}) (A_j - A_i)
$$

$$
= \big( \sum\limits_{i = 0}^{n-2} \sum\limits_{j = i+1}^{n-1} (2^{j-i-1}) (A_j) \big) - \big( \sum\limits_{i = 0}^{n-2} \sum\limits_{j = i+1}^{n-1} (2^{j-i-1}) (A_i) \big)
$$

$$
= \big( (2^0 A_1 + 2^1 A_2 + 2^2 A_3 + \cdots) + (2^0 A_2 + 2^1 A_3 + \cdots) + (2^0 A_3 + 2^1 A_4 + \cdots) + \cdots \big)
$$
$$
 - \big( \sum\limits_{i = 0}^{n-2} (2^0 + 2^1 + \cdots + 2^{N-i-2}) (A_i) \big)
$$

$$
= \big( \sum\limits_{j = 1}^{n-1} (2^j - 1) A_j \big) - \big( \sum\limits_{i = 0}^{n-2} (2^{N-i-1} - 1) A_i \big)
$$

$$
= \sum\limits_{i = 0}^{n-1} \big(((2^i - 1) A_i) - ((2^{N-i-1} - 1) A_i)\big)
$$

$$
= \sum\limits_{i = 0}^{n-1} (2^i - 2^{N-i-1}) A_i
$$


```python
class Solution(object):
    def sumSubseqWidths(self, A):
        MOD = 10**9 + 7
        N = len(A)
        A.sort()

        pow2 = [1]
        for i in xrange(1, N):
            pow2.append(pow2[-1] * 2 % MOD)

        ans = 0
        for i, x in enumerate(A):
            ans = (ans + (pow2[i] - pow2[N-1-i]) * x) % MOD
        return ans
```


**Complexity Analysis**

* Time Complexity:  $$O(N \log N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(N)$$, the space used by `pow2`.  (We can improve this to $$O(1)$$ space by calculating these powers on the fly.)
<br />
<br />