[TOC]

## Solution
---
### Approach: Sliding Window

**Intuition**

Evidently, we only care about the comparisons between adjacent elements.  If the comparisons are represented by `-1, 0, 1` (for `<, =, >`), then we want the longest sequence of alternating `1, -1, 1, -1, ...` (starting with either `1` or `-1`).

These alternating comparisons form contiguous blocks.  We know when the next block ends: when it is the last two elements being compared, or when the sequence isn't alternating.

For example, take an array like `A = [9,4,2,10,7,8,8,1,9]`.  The comparisons are `[1,1,-1,1,-1,0,1,-1]`.  The blocks are `[1], [1,-1,1,-1], [0], [1,-1]`.

**Algorithm**

Scan the array from left to right.  If we are at the end of a block (last elements OR it stopped alternating), then we should record the length of that block as our candidate answer, and set the start of the new block as the next element.


```python
class Solution:
    def maxTurbulenceSize(self, A):
        N = len(A)
        if N < 2:
            return N

        ans = 1
        anchor = 0

        def compare(x, y):
            if x < y:
                return -1
            if x > y:
                return 1
            return 0

        for i in range(1, N):
            c = compare(A[i - 1], A[i])
            if c == 0:
                anchor = i
            else:
                if i == N - 1 or c * compare(A[i], A[i + 1]) != -1:
                    ans = max(ans, i - anchor + 1)
                    anchor = i
        return ans
```


**Complexity Analysis**

* Time Complexity:  $$O(N)$$, where $$N$$ is the length of `A`.

* Space Complexity:  $$O(1)$$.
<br />
<br />