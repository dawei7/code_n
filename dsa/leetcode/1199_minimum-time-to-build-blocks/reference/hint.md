## Hint

**Hint 1:** The examples show that a direct greedy scheduling choice is not sufficient.

**Hint 2:** Try dynamic programming that considers every available action.

**Hint 3:** Define `dp[i][j]` as the minimum time needed to build the first `i` blocks when `j` workers are available.

**Hint 4:** At one step, either assign a worker to a block or choose some workers to split.

**Hint 5:** When assigning a worker to a block, assigning the maximum-time remaining block is always preferable; sort the array before applying the dynamic program.

**Hint 6:** To improve the dynamic program from $O(n^3)$ to $O(n^2)$, observe that whenever splitting is chosen, splitting every currently available worker is optimal.
