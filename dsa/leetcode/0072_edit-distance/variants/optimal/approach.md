## General

**Define a subproblem by two prefix lengths**

Let `f[i][j]` be the minimum number of permitted operations needed to transform the prefix `word1[:i]` into the prefix `word2[:j]`. Prefix lengths are used rather than character indices, so row zero and column zero naturally represent empty strings. The requested answer is `f[m][n]`, where `m = len(word1)` and `n = len(word2)`.

This definition works because an edit near the end of the two prefixes reduces the question to shorter prefixes. It also prevents the algorithm from modifying real strings. Each table entry is only a number summarizing the best transformation for that pair of prefixes.

**Establish the empty-prefix boundaries**

Transforming the empty source into `word2[:j]` requires inserting its `j` characters. No fewer operations can create `j` characters, so `f[0][j] = j`. The first loop fills this top row.

Transforming `word1[:i]` into the empty destination requires deleting its `i` characters, giving `f[i][0] = i`. The outer loop fills each first-column entry just before calculating the rest of that row.

The cell `f[0][0]` remains its initialized zero, representing the zero operations needed to transform an empty string into itself. These boundaries are not arbitrary initialization; they are complete solutions to subproblems in which only one type of edit is possible.

**When the final prefix characters match**

In row `i` and column `j`, the local variables `a` and `b` are `word1[i - 1]` and `word2[j - 1]`. The offset by one comes from using prefix lengths as table coordinates.

If `a == b`, those equal final characters already correspond and require no new operation. Any optimal transformation of `word1[:i-1]` into `word2[:j-1]` can leave the matching characters untouched, so

$$
f[i][j]=f[i-1][j-1].
$$

There is no need to pay for insertion, deletion, or replacement at this position. Keeping an already matching pair is at least as good as disturbing it and later repairing the disturbance, and the diagonal subproblem has already found the cheapest way to handle everything before the pair.

**When the final prefix characters differ**

If `a != b`, an optimal transformation can be classified by the edit that resolves the boundary mismatch:

- Delete `a` from the source prefix. The remaining task is `word1[:i-1]` to `word2[:j]`, so the cost is `f[i-1][j] + 1`.
- Insert `b` after transforming the source into `word2[:j-1]`. The cost is `f[i][j-1] + 1`.
- Replace `a` with `b`. Both last characters are then resolved, leaving `word1[:i-1]` to `word2[:j-1]`, for `f[i-1][j-1] + 1`.

Every legal final edit belongs to one of these three cases, and each case creates a valid transformation when appended to the corresponding optimal subproblem. Taking their minimum therefore gives exactly the best possible cost:

$$
f[i][j]=1+\min\bigl(f[i-1][j],f[i][j-1],f[i-1][j-1]\bigr).
$$

It is useful to keep the directions attached to their meanings. The cell above removes one source character, so it represents deletion. The cell to the left lacks one destination character, so reaching the current destination requires insertion. The diagonal consumes one character from each string, so it represents replacement when those characters differ.

**Why the table order satisfies every dependency**

Rows are processed from smaller source prefixes to larger ones, and columns within a row are processed from left to right. When `f[i][j]` is calculated, the cell above belongs to the completed previous row, the cell to the left was completed earlier in the current row, and the diagonal belongs to the previous row and column. All three needed subproblems are therefore already final.

For `word1 = "horse"` and `word2 = "ros"`, the table does not commit greedily to the first visually attractive edit. At each mismatch it retains the minimum costs arising from all three possible boundary operations. The final value three corresponds to a cheapest path through the table, such as replacing `h` with `r` and deleting the extra `r` and `e` through later states.

**Why the final cell is globally optimal**

The boundary entries are correct by direct necessity. Assume all dependencies of a non-boundary cell contain optimal prefix distances. If the final characters match, extending a diagonal optimal transformation without an edit is optimal. If they differ, every valid transformation must ultimately resolve the boundary through an insertion, deletion, or replacement, and the recurrence checks the optimal cost of each exhaustive category. Thus the cell is optimal.

Induction over the row-major processing order proves that every filled cell has its stated meaning. In particular, `f[m][n]` is the minimum edit count for the complete strings.

**The source stores more history than the transition needs**

The implementation allocates all `(m + 1) * (n + 1)` entries. This is convenient for visualizing the recurrence and would allow later path reconstruction if predecessor choices were also retained. However, the source returns only the distance, and one transition reads only the current row's left cell plus the previous row's current and previous cells. The complete table is not necessary for this output.

## Complexity detail

There are $(m+1)(n+1)$ table cells, and the nested loops calculate $mn$ non-boundary cells with constant work each. Time is $O(mn)$, matching the manifest's time bound.

The exact source allocates a two-dimensional table with $(m+1)(n+1)$ integers, so its auxiliary space is $O(mn)$. This does not match the manifest's declared $O(\min(m,n))$ space. That smaller bound requires rolling rows and arranging for the shorter string to determine the row width, as the competitive variant does. The discrepancy should be corrected in either the implementation or the manifest; the full table must not be described as linear-space storage.

## Alternatives and edge cases

- **One rolling row:** Preserve the previous diagonal in a scalar and overwrite one row in place. This reduces auxiliary space to the destination length while keeping $O(mn)$ time.
- **Choose the shorter row dimension:** Edit distance is symmetric, so swapping inputs before rolling gives $O(\min(m,n))$ space.
- **Two rolling rows:** Keep the previous and current rows separately. It is easier to reason about than in-place overwrite and uses $O(n)$ rather than $O(mn)$ space.
- **Memoized recursion:** It follows the three edit choices directly but uses a two-dimensional cache and recursion stack.
- **Naive recursion:** Exploring all three choices without caching repeats prefix pairs exponentially often.
- **Reconstruct edit operations:** A complete table can support backtracking, but this contract requests only the count and the source records no explicit predecessor choices.
- **Both strings empty:** `f[0][0]` is zero.
- **Empty source:** The top-row boundary returns the destination length, all insertions.
- **Empty destination:** The first-column boundary returns the source length, all deletions.
- **Identical strings:** Every compared pair follows the zero-cost diagonal, yielding zero.
- **One-character mismatch:** Replacement costs one and beats an insertion plus deletion.
- **Different lengths:** Boundary values and insertion/deletion transitions account for all unmatched characters.
- **Repeated characters:** States are identified by prefix positions, not character values alone, so duplicates cause no ambiguity.
- **Source preservation:** No actual edit is applied to either immutable input string; only numeric costs are computed.
