[TOC]

## Video Solution

---

<div>
    <div class="video-container">
        <iframe src="https://player.vimeo.com/video/557813461" width="640" height="360" frameborder="0" allow="autoplay; fullscreen" allowfullscreen></iframe>
    </div>
</div>

<div>
</div>

## Solution Article
---
### Approach 1: Two Pass

**Intuition and Algorithm**

Read all the even integers and put them into places $\text{ans}[0]$, $\text{ans}[2]$, $\text{ans}[4]$, and so on.

Then, read all the odd integers and put them into places $\text{ans}[1]$, $\text{ans}[3]$, $\text{ans}[5]$, etc.

```python
class Solution(object):
    def sortArrayByParityII(self, A):
        N = len(A)
        ans = [None] * N

        t = 0
        for i, x in enumerate(A):
            if x % 2 == 0:
                ans[t] = x
                t += 2

        t = 1
        for i, x in enumerate(A):
            if x % 2 == 1:
                ans[t] = x
                t += 2

        # We could have also used slice assignment:
        # ans[::2] = (x for x in A if x % 2 == 0)
        # ans[1::2] = (x for x in A if x % 2 == 1)

        return ans
```

**Complexity Analysis**

* Time Complexity:  $O(N)$, where $N$ is the length of `A`.

* Space Complexity:  $O(N)$.
<br />
<br />

---
### Approach 2: Read / Write Heads

**Intuition**

We are motivated (perhaps by the interviewer) to pursue a solution where we modify the original array `A` in place.

First, it is enough to put all even elements in the correct place, since all odd elements will be in the correct place too.  So let's only focus on $A[0], A[2], A[4], ...$

Ideally, we would like to have some partition where everything to the left is already correct, and everything to the right is undecided.

Indeed, this idea works if we separate it into two slices $even = A[0], A[2], A[4], ...$ and $odd = A[1], A[3], A[5], ...$.  Our invariant will be that everything less than `i` in the even slice is correct, and everything less than `j` in the odd slice is correct.

**Algorithm**

For each even `i`, let's make $A[i]$ even.  To do it, we will draft an element from the odd slice.  We pass `j` through the odd slice until we find an even element, then swap.  Our invariant is maintained, so the algorithm is correct.

```python
class Solution(object):
    def sortArrayByParityII(self, A):
        j = 1
        for i in xrange(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A
```

**Complexity Analysis**

* Time Complexity:  $O(N)$, where $N$ is the length of `A`.

* Space Complexity:  $O(1)$.
<br />
<br />