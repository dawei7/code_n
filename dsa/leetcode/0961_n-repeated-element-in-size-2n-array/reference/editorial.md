
## Solution
---
### Approach 1: Count

**Intuition and Algorithm**

Let's count the number of elements.  We can use a `HashMap` or an array - here, we use a `HashMap`.

After, the element with a count larger than 1 must be the answer.

```python
class Solution(object):
    def repeatedNTimes(self, A):
        count = collections.Counter(A)
        for k in count:
            if count[k] > 1:
                return k
```

**Complexity Analysis**

* Time Complexity:  $O(N)$, where $N$ is the length of `A`.

* Space Complexity:  $O(N)$.
<br />
<br />

---
### Approach 2: Compare

**Intuition and Algorithm**

If we ever find a repeated element, it must be the answer.  Let's call this answer the *major element*.

Consider all subarrays of length 4.  There must be a major element in at least one such subarray.

This is because either:

* There is a major element in a length 2 subarray, or;
* Every length 2 subarray has exactly 1 major element, which means that a length 4 subarray that begins at a major element will have 2 major elements.

Thus, we only have to compare elements with their neighbors that are distance 1, 2, or 3 away.

```python
class Solution(object):
    def repeatedNTimes(self, A):
        for k in xrange(1, 4):
            for i in xrange(len(A) - k):
                if A[i] == A[i+k]:
                    return A[i]
```

**Complexity Analysis**

* Time Complexity:  $O(N)$, where $N$ is the length of `A`.

* Space Complexity:  $O(1)$.
<br />
<br />