[TOC]

---
### Approach #1: Two Pointer [Accepted]

**Intuition**

We scan through the string to identify the start and end of each group.  If the size of the group is at least 3, we add it to the answer.

**Algorithm**

Maintain pointers `i, j` with $i \le j$.  The `i` pointer will represent the start of the current group, and we will increment `j` forward until it reaches the end of the group.

We know that we have reached the end of the group when `j` is at the end of the string, or $S[j] \neq S[j+1]$.  At this point, we have some group `[i, j]`; and after, we will update $i = j+1$, the start of the next group.

```python
class Solution(object):
    def largeGroupPositions(self, S):
        ans = []
        i = 0 # The start of each group
        for j in xrange(len(S)):
            if j == len(S) - 1 or S[j] != S[j+1]:
                # Here, [i, j] represents a group.
                if j-i+1 >= 3:
                    ans.append([i, j])
                i = j+1
        return ans
```

**Complexity Analysis**

* Time Complexity:  $O(N)$, where $N$ is the length of `S`.

* Space Complexity: $O(N)$, the space used by the answer.