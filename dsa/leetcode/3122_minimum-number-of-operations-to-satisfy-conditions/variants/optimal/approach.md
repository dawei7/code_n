## General

**Reduce the matrix to one choice per column.** The vertical condition forces every cell in a column to have one common final value. If column $j$ is assigned digit $d$, every existing occurrence of $d$ in that column can remain unchanged, while every other cell costs one operation. Although an operation may write any non-negative integer, an optimal solution can restrict choices to digits 0 through 9: an outside value preserves no cells, and one of the nine input digits different from the previous column preserves at least as many.

**Maximize preserved cells instead of minimizing changes.** For each column, count the occurrences of all ten digits. Maintain `best[d]`, the maximum number of unchanged cells across the processed prefix when its final column uses digit $d$. For the next column and chosen digit $d$, add that column's frequency of $d$ to the largest previous state whose digit is not $d$. This transition enforces the horizontal inequality while considering every legal final digit.

The initial state contains ten zeros, so the same transition also handles the first column without a special predecessor. By induction, every state stores the best preserved-cell count among all valid assignments ending in its digit: the transition examines every permitted preceding digit, and every valid assignment has exactly one such predecessor. After the final column, subtract the largest preserved count from the total number of cells to obtain the minimum number changed.

## Complexity detail

Let $m$ and $n$ be the row and column counts. Building column frequencies visits each cell once. Each column then evaluates 10 choices against 9 different predecessor digits; because the digit alphabet is fixed, this is constant work per column. The total time is therefore $O(mn)$, and the two ten-entry dynamic-programming arrays use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Minimum-change dynamic programming:** Store the least cost rather than the greatest preserved count and add `m - frequency[d]` at each transition. It is algebraically equivalent and has the same bounds.
- **Two-minimum transition:** Track the smallest and second-smallest previous costs to reduce the fixed 100 transition comparisons per column. This improves the constant factor but not the $O(mn)$ bound.
- **Recomputing every prefix:** Solving the dynamic program independently for each prefix is correct, but repeats earlier work and takes $O(mn+n^2)$ time when the number of rows is fixed.
- **Single column:** There is no horizontal restriction; choosing its most frequent digit is optimal.
- **Single row:** Vertical equality is automatic, but adjacent equal entries may still require changes.
- **Tied frequencies:** A locally best digit can conflict with the next column, so greedy independent column choices are not sufficient.
- **Values outside 0 through 9:** They cannot preserve an original cell and are never necessary because at most one of the ten input digits is forbidden by the preceding column.
