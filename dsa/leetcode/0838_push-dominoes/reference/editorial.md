
---
### Approach #1: Adjacent Symbols [Accepted]

**Intuition**

Between every group of vertical dominoes (`'.'`), we have up to two non-vertical dominoes bordering this group.  Since additional dominoes outside this group do not affect the outcome, we can analyze these situations individually: there are 9 of them (as the border could be empty). Actually, if we border the dominoes by `'L'` and `'R'`, there are only 4 cases.  We'll write new letters between these symbols depending on each case.

**Algorithm**

Continuing our explanation, we analyze cases:

* If we have say `"A....B"`, where A = B, then we should write `"AAAAAA"`.

* If we have `"R....L"`, then we will write `"RRRLLL"`, or `"RRR.LLL"` if we have an odd number of dots.  If the initial symbols are at positions `i` and `j`, we can check our distance `k-i` and `j-k` to decide at position `k` whether to write `'L'`, `'R'`, or `'.'`.

* (If we have `"L....R"` we don't do anything.  We can skip this case.)

```python
class Solution(object):
    def pushDominoes(self, dominoes):
        symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
        symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]

        ans = list(dominoes)
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            if x == y:
                for k in xrange(i+1, j):
                    ans[k] = x
            elif x > y: #RL
                for k in xrange(i+1, j):
                    ans[k] = '.LR'[cmp(k-i, j-k)]

        return "".join(ans)
```

**Complexity Analysis**

* Time and Space Complexity:  $O(N)$, where $N$ is the length of `dominoes`.

---
### Approach #2: Calculate Force [Accepted]

**Intuition**

We can calculate the net force applied on every domino.  The forces we care about are how close a domino is to a leftward `'R'`, and to a rightward `'L'`: the closer we are, the stronger the force.

**Algorithm**

Scanning from left to right, our force decays by 1 every iteration, and resets to `N` if we meet an `'R'`, so that $\text{force}[i]$ is higher (than $\text{force}[j]$) if and only if $\text{dominoes}[i]$ is closer (looking leftward) to `'R'` (than $\text{dominoes}[j]$).

Similarly, scanning from right to left, we can find the force going rightward (closeness to `'L'`).

For some domino $\text{answer}[i]$, if the forces are equal, then the answer is `'.'`.  Otherwise, the answer is implied by whichever force is stronger.

**Example**

Here is a worked example on the string $S = '\text{R.R}...L'$:  We find the force going from left to right is `[7, 6, 7, 6, 5, 4, 0]`.  The force going from right to left is `[0, 0, 0, -4, -5, -6, -7]`.  Combining them (taking their vector addition), the combined force is `[7, 6, 7, 2, 0, -2, -7]`, for a final answer of `RRRR.LL`.

```python
class Solution(object):
    def pushDominoes(self, dominoes):
        N = len(dominoes)
        force = [0] * N

        # Populate forces going from left to right
        f = 0
        for i in xrange(N):
            if dominoes[i] == 'R': f = N
            elif dominoes[i] == 'L': f = 0
            else: f = max(f-1, 0)
            force[i] += f

        # Populate forces going from right to left
        f = 0
        for i in xrange(N-1, -1, -1):
            if dominoes[i] == 'L': f = N
            elif dominoes[i] == 'R': f = 0
            else: f = max(f-1, 0)
            force[i] -= f

        return "".join('.' if f==0 else 'R' if f > 0 else 'L'
                       for f in force)
```

**Complexity Analysis**

* Time and Space Complexity:  $O(N)$.