## General

**Count valid leaves instead of constructing boards**

The search places one queen in each row from top to bottom. At recursion depth `i`, rows 0 through `i - 1` already contain conceptual queens, and the loop chooses the column for row `i`. Because a row is handled exactly once, row conflicts are impossible without any explicit row marker.

Unlike N-Queens I, this problem asks only for the number of configurations. The algorithm does not need a grid or a list of chosen columns. It records which attack lines are occupied, explores every safe placement sequence, and increments a counter whenever all $n$ rows have been assigned.

**Three marker families cover every attack**

`cols[j]` says whether an earlier queen occupies column `j`. Cells with equal row-plus-column values lie on the same top-right-to-bottom-left diagonal, so `dg[i + j]` identifies that direction.

Cells with equal row-minus-column values lie on the other diagonal direction. Since `i - j` may be negative, the source adds `n` and uses `udg[i - j + n]`. For an $n \times n$ board, the sum ranges from 0 through $2n-2$, and the shifted difference ranges from 1 through $2n-1$.

The code computes those two indices once as `a` and `b`. A candidate is safe only when its column, sum diagonal, and shifted-difference diagonal are all false. These constant-time checks cover every way a queen in an earlier row could attack the new position.

**Fixed marker capacities rely on the stated constraint**

Rather than allocating arrays from `n`, the source uses lengths 10, 20, and 20. The contract limits $n$ to at most 9. Therefore, column index `j` is at most 8, `i+j` is at most 16, and `i-j+n` is at most 17. Every access fits.

This is safe for the official domain but not a general implementation for arbitrary board sizes. If `n` were greater than 10, the fixed arrays could be too short. Allocating `n` columns and roughly `2n` entries per diagonal family would express the generalized relationship directly.

**The recursive invariant**

At entry to `dfs(i)`, exactly one queen has been chosen for each earlier row, those queens do not attack one another, and the three marker arrays describe exactly their occupied columns and diagonals.

The initial call satisfies the invariant because all markers are false and no rows are filled. For a safe column `j`, setting the three relevant markers to true adds the new queen's attacks before calling `dfs(i + 1)`. The child therefore cannot place a conflicting queen.

After the child returns, the same three entries are reset to false. No other active queen uses them: the candidate was allowed only when they were previously false, and all descendants have already restored their own markers. This rollback reconstructs the parent state exactly for the next column trial.

**Why the base case adds one**

When `i == n`, the recursive path has selected one safe column in every row. The invariant guarantees no shared column or diagonal, so this path represents one complete valid arrangement. `ans += 1` counts it.

The declaration `nonlocal ans` tells Python that assignment should update the `ans` created in the enclosing `totalNQueens` method rather than create a new local name. Although the declaration appears inside the base-case block, it applies to the entire nested function at compile time.

The function then returns, allowing its parent to restore the last queen and search for another completion.

**A counting trace rather than a board trace**

For $n=4$, choosing a column in row 0 establishes three markers. Each next row tries only columns outside those attacks. Some branches reach a row with no safe choice and contribute zero because no base case is reached. The two branches that successfully place four queens each reach `dfs(4)` once and increment `ans`. The final result is 2.

No explicit “failure value” is needed. A dead-end call simply finishes its loop and returns; because it never increments the shared counter, it adds nothing to the answer.

**Why the final count is exact**

Every counted leaf is valid by the marker invariant and has exactly $n$ queens because it assigns every row. For completeness, take any valid configuration. Its row-0 column is tried by the root. Given that prefix, its row-1 queen conflicts with none of the markers and is tried by the child. Repeating this argument follows a search path to a counted leaf.

Two distinct configurations differ in at least one row's column. Their recursion paths diverge at that row and reach separate base-case calls, so each is counted once and none is merged or duplicated.

## Complexity detail

Let $V$ be the number of partial non-attacking states reached. Each such state scans $n$ candidate columns and performs constant-time checks, so a precise traversal expression is $O(nV)$. Column uniqueness bounds depth by $n$ and limits complete column orders to $n!$; diagonal pruning reduces the actual search drastically.

The manifest's $O(n!)$ is the conventional simplified description of this permutation-like search. If every candidate test is accounted for separately, a conservative broad bound is $O(n \cdot n!)$. Counting a leaf is $O(1)$ because no board strings are built, which makes this problem cheaper per solution than the board-returning version.

The recursion stack has depth at most $n$. Under a generalized allocation, column and diagonal markers also occupy $O(n)$ space, matching the manifest. In this exact constraint-specific source, the arrays have fixed capacities and are technically $O(1)$ with respect to runtime `n`, while the stack remains $O(n)$. There is no proportional output collection; the answer is one integer.

## Alternatives and edge cases

- **Return subtree counts:** Have each recursive call sum counts returned by its children instead of mutating a nonlocal counter. This makes data flow explicit and is the competitive branch's style.
- **Bit masks:** Store occupied columns and diagonals in integers and recurse over available set bits. It uses compact state and is often substantially faster.
- **Symmetry reduction:** Explore only half of the first-row columns and double mirrored counts, handling a center column separately for odd `n`. It improves constants but complicates the proof.
- **Full board construction:** It is unnecessary when only a count is requested and would add $O(n^2)$ active or per-leaf work.
- **`n = 1`:** The sole position is safe, one base case is reached, and the answer is 1.
- **A dead-end row:** Its loop finds no safe column and returns without changing `ans`, correctly contributing zero.
- **Fixed array sizes:** They are valid only because $n \le 9$. General-purpose code should allocate from `n`.
- **Unused diagonal slot:** The shifted-difference formula starts at 1, leaving index 0 unused; this is harmless.
- **No input mutation:** The integer argument is unchanged, and all search state is internal.
- **No result-order issue:** Only a scalar count is returned, so traversal order has no observable significance.
