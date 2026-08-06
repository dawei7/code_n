## Hint

**Hint 1:** Look for a mathematical greedy formulation.

**Hint 2:** If `(i, j)` is set to `1`, every `(x, y)` with `i % sideLength == x % sideLength` and `j % sideLength == y % sideLength` can also be set to `1` without increasing the maximum number of ones in any constrained square.

**Hint 3:** Treat setting every cell in one residue pair `(i % sideLength, j % sideLength)` to `1` as a single choice.

**Hint 4:** Prefer the residue choices that occur most frequently in the full matrix.
