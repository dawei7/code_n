## General

The restrictions concern rows and values: each row may contribute at most one cell, and each numeric value may be selected at most once. Columns do not matter. Since there are at most ten rows but values range only through one hundred, the solution processes values and represents row availability with a bitmask.

Dictionary `g` maps each value to the set of rows where that value occurs. A set is appropriate because multiple occurrences of the same value in one row are equivalent: selecting any one has the same score and consumes the same row.

Let `m` be the row count. A mask from zero through `(1 << m) - 1` describes rows available for selection. Bit `k` equal to one means row `k` may still be used.

`f[i][j]` is the maximum score obtainable using only numeric values from one through `i` and only rows whose bits are present in mask `j`. This “available rows” interpretation explains why selecting a row clears its bit in the previous state.

The default transition is `f[i][j] = f[i - 1][j]`, meaning value `i` is not selected. To select it from row `k`, the row must be available, tested by `j >> k & 1`. The previous state may use values only through `i-1` and must exclude row `k`:

`f[i - 1][j ^ (1 << k)] + i`.

Because bit `k` is known to be one, XOR clears it. Taking the maximum over every row containing value `i` finds the best placement of that value.

Processing a value only once enforces value uniqueness: a transition either skips `i` or adds it exactly once from one row. Clearing a row bit enforces row uniqueness across all values.

The final state uses `i = mx` and the all-ones mask `(1 << m) - 1`, making every row initially available and every grid value eligible.

For `[[1,2,3],[4,3,2],[1,1,1]]`, value four can use row one, value three row zero, and value one row two. Their row bits are distinct and values unique, producing eight.

**Why no column state exists.** The problem permits multiple selected cells from one column. Only row and value conflicts affect feasibility, so tracking columns would create unnecessary exponential state.

**Why an empty selection does not break the result.** DP entries begin at zero, which permits selecting nothing. All grid values are positive and the grid is nonempty, so an optimal all-rows state always improves by selecting at least one cell, satisfying the one-or-more requirement.

Inductively, every valid selection using values through `i` either omits value `i` or selects it in exactly one available row. The recurrence covers these disjoint cases, and every constructed transition respects both restrictions. Therefore `f[-1][-1]` is the optimum.

## Complexity detail

Let $V$ be the maximum value and $m$ the row count. There are $V2^m$ states. For each value and mask, the source can inspect up to $m$ rows in `g[i]`, giving $O(Vm2^m)$ time.

The full DP table stores $(V+1)2^m$ integers, using $O(V2^m)$ space. The value-to-row mapping stores at most the number of grid cells and is smaller under the constraints.

With $V\le100$ and $m\le10$, at most about 102,400 DP states exist.

## Alternatives and edge cases

- **Backtracking by cells:** It explores many equivalent occurrences and can be exponential in all grid cells rather than only ten rows.
- **Row-by-row mask over values:** Values range to one hundred, so a value-used mask would be far too large. Processing values as DP layers avoids that dimension.
- **Rolling DP rows:** Only `f[i-1]` is needed, so space can be reduced to $O(2^m)$, though the exact source stores all value layers.
- **Duplicate value within one row:** `g[value]` stores the row once, correctly merging equivalent choices.
- **Same value in many rows:** The transition tries every available row but can choose only one.
- **One row:** The answer is simply the greatest value in that row.
- **One column:** Rows still supply independent candidates, subject only to unique values.
- **All cells equal:** Only one occurrence of that value may be selected, so the score is that value.
- **Unused numeric values:** `g[i]` is empty and the layer simply copies `f[i-1]`.
- **Clearing with XOR:** It is safe only after checking the bit is one. Otherwise XOR would incorrectly add the row.
- **Positive-value guarantee:** It ensures the zero-initialized DP chooses a nonempty solution in the final state.
- **All-ones final mask:** It means all rows were initially available, not that all rows must be selected.
- **Why value zero has no layer:** Grid values are positive, so layers begin at one. If zero were allowed, selecting it could never improve a positive-score maximum, though the state definition would need care for a mandatory nonempty selection.
- **Mask state permits unused rows:** A transition may finish without clearing every bit. The restriction is “at most one per row,” not “exactly one from every row.”
- **Row-set construction cost:** Scanning the grid also collapses repeated same-row occurrences before DP, preventing redundant transitions that would reach identical states with identical added value.
