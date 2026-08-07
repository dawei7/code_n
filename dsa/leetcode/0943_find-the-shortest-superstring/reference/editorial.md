[TOC]

## Solution
---
### Approach 1: Dynamic Programming

**Intuition**

We have to put the words into a row, where each word may overlap the previous word.  This is because no word is contained in any word.

Also, it is sufficient to try to maximize the total overlap of the words.

Say we have put some words down in our row, ending with word $A[i]$.  Now say we put down word $A[j]$ as the next word, where word `j` hasn't been put down yet.  The overlap increases by $overlap(A[i], A[j])$.

We can use dynamic programming to leverage this recursion.  Let `dp(mask, i)` be the total overlap after putting some words down (represented by a bitmask `mask`), for which $A[i]$ was the last word put down.  Then, the key recursion is $dp(mask ^ (1<<j), j) = max(overlap(A[i], A[j]) + dp(mask, i))$, where the `j`th bit is not set in mask, and `i` ranges over all bits set in `mask`.

Of course, this only tells us what the maximum overlap is for each set of words.  We also need to remember each choice along the way (ie. the specific `i` that made $dp(mask ^ (1<<j), j)$ achieve a minimum) so that we can reconstruct the answer.

**Algorithm**

Our algorithm has 3 main components:

* Precompute $overlap(A[i], A[j])$ for all possible `i, j`.
* Calculate $\text{dp}[mask][i]$, keeping track of the "`parent`" `i` for each `j` as described above.
* Reconstruct the answer using `parent` information.

Please see the implementation for more details about each section.

```python
class Solution(object):
    def shortestSuperstring(self, A):
        N = len(A)

        # Populate overlaps
        overlaps = [[0] * N for _ in xrange(N)]
        for i, x in enumerate(A):
            for j, y in enumerate(A):
                if i != j:
                    for ans in xrange(min(len(x), len(y)), -1, -1):
                        if x.endswith(y[:ans]):
                            overlaps[i][j] = ans
                            break

        # dp[mask][i] = most overlap with mask, ending with ith element
        dp = [[0] * N for _ in xrange(1<<N)]
        parent = [[None] * N for _ in xrange(1<<N)]
        for mask in xrange(1, 1 << N):
            for bit in xrange(N):
                if (mask >> bit) & 1:
                    # Let's try to find dp[mask][bit].  Previously, we had
                    # a collection of items represented by pmask.
                    pmask = mask ^ (1 << bit)
                    if pmask == 0: continue
                    for i in xrange(N):
                        if (pmask >> i) & 1:
                            # For each bit i in pmask, calculate the value
                            # if we ended with word i, then added word 'bit'.
                            value = dp[pmask][i] + overlaps[i][bit]
                            if value > dp[mask][bit]:
                                dp[mask][bit] = value
                                parent[mask][bit] = i

        # Answer will have length sum(len(A[i]) for i) - max(dp[-1])
        # Reconstruct answer:

        # Follow parents down backwards path that retains maximum overlap
        perm = []
        mask = (1<<N) - 1
        i = max(xrange(N), key = dp[-1].__getitem__)
        while i is not None:
            perm.append(i)
            mask, i = mask ^ (1<<i), parent[mask][i]

        # Reverse path to get forwards direction; add all remaining words
        perm = perm[::-1]
        seen = [False] * N
        for x in perm:
            seen[x] = True
        perm.extend([i for i in xrange(N) if not seen[i]])

        # Reconstruct answer given perm = word indices in left to right order
        ans = [A[perm[0]]]
        for i in xrange(1, len(perm)):
            overlap = overlaps[perm[i-1]][perm[i]]
            ans.append(A[perm[i]][overlap:])

        return "".join(ans)
```

**Complexity Analysis**

* Time Complexity:  $O(N^2 (2^N + W))$, where $N$ is the number of words, and $W$ is the maximum length of each word.

* Space Complexity:  $O(N (2^N + W))$.
<br />
<br />