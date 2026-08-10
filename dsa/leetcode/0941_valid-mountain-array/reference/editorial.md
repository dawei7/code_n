
## Solution
---
### Approach 1: One Pass

**Intuition**

If we walk along the mountain from left to right, we have to move strictly up, then strictly down.

**Algorithm**

Let's walk up from left to right until we can't: that has to be the peak.  We should ensure the peak is not the first or last element.  Then, we walk down.  If we reach the end, the array is valid, otherwise its not.

```python
class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1
```

**Complexity Analysis**

* Time Complexity:  $O(N)$, where $N$ is the length of `A`.

* Space Complexity:  $O(1)$.
<br />
<br />