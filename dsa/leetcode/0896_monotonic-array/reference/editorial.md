[TOC]

## Solution
---
### Approach 1: Two Pass

**Intuition**

An array is *monotonic* if it is monotone increasing, or monotone decreasing.  Since $a \le b$ and $b \le c$ implies $a \le c$, we only need to check adjacent elements to determine if the array is monotone increasing (or decreasing, respectively).  We can check each of these properties in one pass.

**Algorithm**

To check whether an array `A` is monotone increasing, we'll check $A[i] \le A[i+1]$ for all `i`.  The check for monotone decreasing is similar.

```python
class Solution(object):
    def isMonotonic(self, A):
        return (all(A[i] <= A[i+1] for i in xrange(len(A) - 1)) or
                all(A[i] >= A[i+1] for i in xrange(len(A) - 1)))
```

**Complexity Analysis**

* Time Complexity:  $O(N)$, where $N$ is the length of `A`.

* Space Complexity:  $O(1)$.
<br />
<br />

---
### Approach 2: One Pass

**Intuition**

To perform this check in one pass, we want to handle a stream of comparisons from $\{-1, 0, 1\}$, corresponding to `<`, `==`, or `>`.  For example, with the array `[1, 2, 2, 3, 0]`, we will see the stream `(-1, 0, -1, 1)`.

**Algorithm**

Keep track of `store`, equal to the first non-zero comparison seen (if it exists.)  If we see the opposite comparison, the answer is `False`.

Otherwise, every comparison was (necessarily) in the set $\{-1, 0\}$, or every comparison was in the set $\{0, 1\}$, and therefore the array is monotonic.

```python
class Solution(object):
    def isMonotonic(self, A):
        store = 0
        for i in xrange(len(A) - 1):
            c = cmp(A[i], A[i+1])
            if c:
                if c != store != 0:
                    return False
                store = c
        return True
```

**Complexity Analysis**

* Time Complexity:  $O(N)$, where $N$ is the length of `A`.

* Space Complexity:  $O(1)$.
<br />
<br />

---
### Approach 3: One Pass (Simple Variant)

**Intuition and Algorithm**

To perform this check in one pass, we want to remember if it is monotone increasing or monotone decreasing.

It's monotone increasing if there aren't some adjacent values $A[i], A[i+1]$ with $A[i] > A[i+1]$, and similarly for monotone decreasing.

If it is either monotone increasing or monotone decreasing, then `A` is monotonic.

```python
class Solution(object):
    def isMonotonic(self, A):
        increasing = decreasing = True

        for i in xrange(len(A) - 1):
            if A[i] > A[i+1]:
                increasing = False
            if A[i] < A[i+1]:
                decreasing = False

        return increasing or decreasing
```

**Complexity Analysis**

* Time Complexity:  $O(N)$, where $N$ is the length of `A`.

* Space Complexity:  $O(1)$.
<br />
<br />