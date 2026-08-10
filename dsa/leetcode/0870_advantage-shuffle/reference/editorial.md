
## Solution
---
### Approach 1: Greedy

**Intuition**

If the smallest card `a` in `A` beats the smallest card `b` in `B`, we should pair them.  Otherwise, `a` is useless for our score, as it can't beat any cards.

Why should we pair `a` and `b` if `a > b`?  Because every card in `A` is larger than `b`, any card we place in front of `b` will score a point.  We might as well use the weakest card to pair with `b` as it makes the rest of the cards in `A` strictly larger, and thus have more potential to score points.

**Algorithm**

We can use the above intuition to create a greedy approach.  The current smallest card to beat in `B` will always be $b = \text{sortedB}[j]$.  For each card `a` in `sortedA`, we will either have `a` beat that card `b` (put `a` into $\text{assigned}[b]$), or throw `a` out (put `a` into `remaining`).

Afterwards, we can use our annotations `assigned` and `remaining` to reconstruct the answer.  Please see the comments for more details.

```python
class Solution(object):
    def advantageCount(self, A, B):
        sortedA = sorted(A)
        sortedB = sorted(B)

        # assigned[b] = list of a that are assigned to beat b
        # remaining = list of a that are not assigned to any b
        assigned = {b: [] for b in B}
        remaining = []

        # populate (assigned, remaining) appropriately
        # sortedB[j] is always the smallest unassigned element in B
        j = 0
        for a in sortedA:
            if a > sortedB[j]:
                assigned[sortedB[j]].append(a)
                j += 1
            else:
                remaining.append(a)

        # Reconstruct the answer from annotations (assigned, remaining)
        return [assigned[b].pop() if assigned[b] else remaining.pop()
                for b in B]
```

**Complexity Analysis**

* Time Complexity:  $O(N \log N)$, where $N$ is the length of `A` and `B`.

* Space Complexity:  $O(N)$.
<br />
<br />