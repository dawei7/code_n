[TOC]

### Approach #1: Count Corners [Accepted]

**Intuition**

We ask the question: for each additional row, how many more rectangles are added?

For each pair of 1s in the new row (say at $\text{new}_{row}[i]$ and $\text{new}_{row}[j]$), we could create more rectangles where that pair forms the base. The number of new rectangles is the number of times some previous row had $\text{row}[i] = \text{row}[j] = 1$.

**Algorithm**

Let's maintain a count `count[i, j]`, the number of times we saw $\text{row}[i] = \text{row}[j] = 1$. When we process a new row, for every pair $\text{new}_{row}[i] = \text{new}_{row}[j] = 1$, we add `count[i, j]` to the answer, then we increment `count[i, j]`.

```python
class Solution(object):
    def countCornerRectangles(self, grid):
        count = collections.Counter()
        ans = 0
        for row in grid:
            for c1, v1 in enumerate(row):
                if v1:
                    for c2 in xrange(c1+1, len(row)):
                        if row[c2]:
                            ans += count[c1, c2]
                            count[c1, c2] += 1
        return ans
```

**Complexity Analysis**

* Time Complexity: $O(R*C^2)$ where $R, C$ is the number of rows and columns.

* Space Complexity: $O(C^2)$ in additional space.

---
### Approach #2: Heavy and Light Rows [Accepted]

**Intuition and Algorithm**

Can we improve on the ideas in *Approach #1*? When a row is filled with $X$ 1s, we do $O(X^2)$ work to enumerate every pair of 1s.  This is okay when $X$ is small, but expensive when $X$ is big.

Say the entire top row is filled with 1s. When looking at the next row with say, `f` 1s that match the top row, the number of rectangles created is just the number of pairs of 1s, which is $f * (f-1) / 2$. We could find each `f` quickly using a Set and a simple linear scan of each row.

Let's call a row to be *heavy* if it has more than $\sqrt N$ points. The above algorithm changes the complexity of counting a heavy row from $O(C^2)$ to $O(N)$, and there are at most $\sqrt N$ heavy rows.

```python
class Solution(object):
    def countCornerRectangles(self, grid):
        rows = [[c for c, val in enumerate(row) if val]
                for row in grid]
        N = sum(len(row) for row in grid)
        SQRTN = int(N**.5)

        ans = 0
        count = collections.Counter()
        for r, row in enumerate(rows):
            if len(row) >= SQRTN:
                target = set(row)
                for r2, row2 in enumerate(rows):
                    if r2 <= r and len(row2) >= SQRTN:
                        continue
                    found = sum(1 for c2 in row2 if c2 in target)
                    ans += found * (found - 1) / 2
            else:
                for pair in itertools.combinations(row, 2):
                    ans += count[pair]
                    count[pair] += 1

        return ans
```

**Complexity Analysis**

* Time Complexity: $O(N \sqrt N + R*C)$ where $N$ is the number of ones in the grid.

* Space Complexity: $O(N + R + C^2)$ in additional space, for `rows`, `target`, and `count`.