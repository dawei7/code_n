## General

**Compress backward dynamic programming into one row**

The competitive source uses the same state meaning as the full-table solution:
the stored number for a cell is the minimum health required before entering it
to guarantee survival to the destination.

Only the row below and the current row's value to the right are needed. A
one-dimensional list `DP` with one entry per column can therefore be reused:

- before updating column `j`, `DP[j]` is the requirement from the cell below;
- after updating column `j + 1`, `DP[j + 1]` is the requirement from the cell
  to the right in the current row.

Scanning columns right-to-left preserves both meanings exactly when they are
needed.

**Initialize the destination boundary**

`DP` begins with infinity in every column, then `DP[-1] = 1`.

For the bottom row, this one means the health required after the destination:
the knight must finish with at least one. For columns left of the destination,
the infinity entries represent unavailable downward moves until they are
overwritten by real states.

At the start of each row, the source updates the final column separately:

`DP[-1] = max(DP[-1] - dungeon[i][-1], 1)`.

There is no right neighbor at that boundary, so only the previously stored
below requirement is valid. On the bottom row, its initial value one produces
the destination base case.

**Update interior columns**

For each remaining column in reverse order:

`min_HP_on_exit = min(DP[j], DP[j + 1])`.

`DP[j]` still belongs to the row below because it has not yet been overwritten
in the current row. `DP[j + 1]` was just updated and belongs to the right
neighbor. Their minimum chooses the easier valid continuation.

The new entry requirement is:

`max(min_HP_on_exit - dungeon[i][j], 1)`.

A damaging negative room increases the required entry health. A beneficial
positive room reduces it, but the maximum with one enforces the rule that
health may never be zero or negative.

**Trace the rolling meanings**

For the sample destination `-5`, bottom-row `DP[-1]` changes from one to six.
Moving left to the room containing 30 uses the right requirement six and an
infinite below state. One health is sufficient because the power-up supplies
the remaining need.

After the bottom row is complete, each `DP[j]` describes that row. Moving to
the row above, the last column is updated from its below requirement. Interior
updates then combine below values not yet overwritten with current-row right
values already overwritten.

By the end of the top row, `DP[0]` represents the top-left room and is seven.

**Why overwriting does not destroy needed data**

The current update at column `j` never again needs the old below value for a
column to its right. Movement from any remaining earlier column can go right
into the current row or down in its own column; it cannot go down into a
rightward column without first using the already computed current-row state.

Thus right-to-left order makes each overwritten value obsolete at the moment
of replacement. Scanning left-to-right would be wrong because `DP[j + 1]`
would still refer to the row below rather than the current right neighbor.

**Why backward requirements solve survival**

Forward path sums cannot tell whether health fell to zero before a later gain.
The backward state asks exactly how much must be present before each room to
survive all future losses.

At a cell, the smaller successor requirement represents a feasible best path.
Subtracting the current room value determines the entry amount needed to reach
that successor requirement, and clamping to one enforces immediate survival.
Backward induction across the scan proves `DP[0]` is minimal and feasible.

**Clarify the source space comment**

The source comment says `O(m + n)` space, but the selected method stores only
one array whose length equals the number of columns. Its tight auxiliary-space
bound is $O(n)$, matching the manifest. It does not store a row-sized structure
for every dungeon row.

## Complexity detail

Every one of the $mn$ cells is updated once with constant-time arithmetic and
comparisons. Time is $O(mn)$.

`DP` contains $n$ numbers and all other variables are scalar. Auxiliary space
is $O(n)$, matching the manifest and improving on a full $O(mn)$ table.

## Alternatives and edge cases

- **Full two-dimensional table:** Directly mirrors the recurrence and is easier to visualize, but uses $O(mn)$ space.
- **Use the smaller dimension:** With careful orientation, rolling storage can be reduced to $O(\min(m,n))$, though movement semantics and indexing become less direct.
- **Forward feasibility for a guessed health:** Supports binary search but takes an extra logarithmic factor.
- **Single room:** The final-column update alone calculates the correct requirement.
- **One column:** Only the separate final-column update runs for each row.
- **One row:** Reverse interior updates use right neighbors and ignore infinity below.
- **Positive orb:** Requirement is never allowed below one.
- **Negative first or last room:** Both are included because every cell is processed.
- **Update order:** Columns must run right-to-left so `DP[j + 1]` belongs to the current row.
- **Space comment:** The exact tight bound is $O(n)$ rather than $O(m+n)$.
