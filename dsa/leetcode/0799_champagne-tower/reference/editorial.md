
---
### Approach #1: Simulation [Accepted]

**Intuition**

Instead of keeping track of how much champagne should end up in a glass, keep track of the total amount of champagne that flows through a glass.  For example, if $poured = 10$ cups are poured at the top, then the total flow-through of the top glass is `10`; the total flow-through of each glass in the second row is `4.5`, and so on.

**Algorithm**

In general, if a glass has flow-through `X`, then $Q = (X - 1.0) / 2.0$ quantity of champagne will equally flow left and right.  We can simulate the entire pour for 100 rows of glasses.  A glass at `(r, c)` will have excess champagne flow towards `(r+1, c)` and `(r+1, c+1)`.

```python
class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        A = [[0] * k for k in xrange(1, 102)]
        A[0][0] = poured
        for r in xrange(query_row + 1):
            for c in xrange(r+1):
                q = (A[r][c] - 1.0) / 2.0
                if q > 0:
                    A[r+1][c] += q
                    A[r+1][c+1] += q

        return min(1, A[query_row][query_glass])
```

**Complexity Analysis**

* Time Complexity:  $O(R^2)$, where $R$ is the number of rows.  As this is fixed, we can consider this complexity to be $O(1)$.

* Space Complexity: $O(R^2)$, or $O(1)$ by the reasoning above.