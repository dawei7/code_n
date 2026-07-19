## General
**Define optimal prefix states.** Let `dp[i]` be the minimum height needed for the first `i` books, with `dp[0] = 0`. Any arrangement counted by `dp[i]` has some final shelf containing a consecutive suffix of those books.

**Enumerate the last shelf backward.** For each endpoint `i`, scan books `i - 1`, `i - 2`, and so on. Maintain the suffix's cumulative `width` and maximum `height`. Stop as soon as the width exceeds `shelf_width`, since adding more positive thickness can never restore feasibility.

**Join the suffix to an optimal prefix.** If the last shelf begins at index `j`, the preceding books contribute `dp[j]` and this shelf contributes its maintained maximum height. Update `dp[i]` with `dp[j] + height` whenever that total is smaller.

For correctness, assume all earlier prefix states are optimal. Every feasible arrangement of the first `i` books chooses exactly one start `j` for its final shelf, and the transition examines that suffix with its exact shelf height. It combines the shelf with the optimal arrangement of the preceding prefix. Taking the minimum therefore considers the optimal arrangement and cannot produce a lower infeasible value; induction proves `dp[n]` is the answer.

## Complexity detail
For each of the $n$ endpoints, at most $n$ possible final-shelf starts are scanned, with width and height updated in constant time. This gives $O(n^2)$ time. The `dp` array contains $n+1$ values, so auxiliary space is $O(n)$.

## Alternatives and edge cases
- **Top-down recursion with memoization:** Use the same prefix or suffix state and enumerate a shelf at each call; it has the same $O(n^2)$ time and $O(n)$ state space plus recursion overhead.
- **Greedy fill each shelf:** Filling the current shelf whenever possible can be suboptimal because moving a tall book may reduce the combined heights of neighboring shelves.
- **Recompute every shelf slice:** Summing thickness and finding maximum height anew for every transition is correct but takes $O(n^3)$ time.
- **One book:** Its height is the complete answer.
- **Book as wide as the shelf:** That book must occupy a shelf alone, splitting the ordered sequence around it.
- **Order preservation:** Books may be divided only between adjacent input positions; sorting by height or thickness changes the problem.
