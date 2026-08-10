## General

**Translate the diagonal rule into a property of each row**

In zero-based coordinates, row `i` is valid when every column strictly greater than `i` contains zero. Those cells lie above the main diagonal.

Instead of repeatedly checking many suffix cells, the solution records `pos[i]`, the column of the rightmost one in row `i`. It scans each row from right to left and stops at the first one it finds. An all-zero row keeps the initial value negative one.

Row `r` can occupy final position `i` exactly when `pos[r] <= i`. If its rightmost one is at or before column `i`, every later column is zero. If its rightmost one is after `i`, that one would lie above the diagonal and violate validity.

The negative-one value for an all-zero row naturally satisfies every requirement because $-1 \le i$ for all valid positions.

**Fill final positions from top to bottom**

The top row is most restrictive: it may contain a one only in column zero. Each lower position is weaker because it allows the rightmost one one column farther right.

For each target position `i`, the solution searches current rows `i` through `n - 1` for the first row whose `pos` value is at most `i`. Call its current position `k`.

Choosing the first such row means choosing the nearest eligible row. Bringing it upward requires exactly `k - i` adjacent swaps. The code adds this amount to `ans`.

It then performs those swaps on `pos` itself. Swapping `pos[k]` with `pos[k - 1]` repeatedly moves the chosen row to position `i` and shifts every intervening row down by one. The original grid does not need to be rearranged because all later decisions depend only on each row's rightmost-one position.

**Why adjacent swaps cost k minus i**

An adjacent swap changes a row's position by exactly one. A row beginning at `k` must cross the boundaries between `k` and `k-1`, then `k-1` and `k-2`, continuing until it reaches `i`. There are exactly `k-i` such boundaries.

No sequence of adjacent row swaps can move that row upward using fewer steps, so the amount added is both achievable and necessary for this choice.

**Why the nearest eligible row is optimal**

At target position `i`, any valid final grid must place some currently remaining row with `pos <= i` there. If none exists, no future swapping can invent a suitable row, so returning negative one is correct.

Suppose several eligible rows exist. Every row eligible for position `i` is also eligible for every later position because later indices allow the rightmost one to be farther right. Therefore, using the nearest eligible row now does not consume a uniquely flexible resource needed later.

Choosing a farther eligible row would cross all boundaries crossed by the nearest candidate and at least one additional boundary. The nearest choice minimizes the immediate number of necessary adjacent swaps.

An exchange view makes this global: take any valid arrangement that brings a farther eligible row to `i` while a nearer eligible row remains below. Put the nearer eligible row at `i` instead and leave the farther eligible row for the later position occupied by the nearer one. Both satisfy those positions because the later requirement is weaker, and the nearer row requires no more upward crossings. Thus an optimal arrangement exists with the greedy choice.

**Why earlier rows remain fixed**

The search starts at `i`, never above it. The bubbling loop also stops at `i`. Consequently, positions zero through `i-1` are never touched after being finalized.

This gives a useful invariant: before processing `i`, every earlier row meets its diagonal requirement, and `pos[i:]` describes the remaining rows in their actual relative order. The selected swaps establish validity at `i` while preserving the invariant for the next iteration.

**Detecting impossibility**

If the search leaves `k = -1`, all remaining rows have a rightmost one after column `i`. None can legally occupy the current position. Since earlier fixed rows are already required for even stricter positions, rearranging the same remaining rows cannot solve the deficit. The whole grid is impossible.

The final row requirement is always weak enough for any binary row because every rightmost one is at most `n-1`. Failure therefore normally appears at an earlier, stricter position.

**Why the answer is correct**

Preprocessing turns validity into the exact condition `pos <= i`. At every position, the algorithm selects the nearest feasible remaining row, pays the minimum adjacent-swap distance for that selection, and updates row order exactly.

The exchange argument proves this greedy selection can be part of an optimal completion. Induction across positions therefore proves that, when a completion exists, the accumulated `ans` is minimum. If no eligible row exists, the current requirement cannot be satisfied by any arrangement, proving the negative-one result.

## Complexity detail

Let $N$ be the grid dimension. Finding each rightmost one can scan $N$ columns across $N$ rows, costing $O(N^2)$ time.

For every target position, searching for the nearest eligible row can scan $O(N)$ entries. Bubbling a selected row upward can also take $O(N)$ swaps. Across all positions, these operations remain $O(N^2)$.

The `pos` list contains one integer per row, so auxiliary space is $O(N)$. The grid itself is not copied or modified. Scalar loop variables and the accumulator use constant additional space.

## Alternatives and edge cases

- **Swap complete grid rows:** It produces the same answer but moves $N$ cells per adjacent swap; updating only `pos` is sufficient.
- **Recount trailing zeros repeatedly:** It is correct but repeats work that one preprocessing pass avoids.
- **Choose any eligible row:** Feasibility may survive, but choosing a farther row can add unnecessary adjacent swaps; the nearest eligible row is the minimum-cost greedy choice.
- **All-zero row:** Its `pos` value is negative one, so it is eligible for every target position.
- **Already valid grid:** Every current row satisfies its position and each chosen `k` equals `i`, giving zero swaps.
- **Identical invalid rows:** If no row satisfies an early requirement, row swaps cannot help and the result is negative one.
- **One-by-one grid:** Its sole row is automatically valid and requires zero swaps.
- **Rightmost one on the diagonal:** `pos == i` is legal because only cells strictly above the diagonal must be zero.
- **Rightmost one just beyond the diagonal:** `pos == i + 1` is illegal for that position.
- **Adjacent-only rule:** The distance `k-i` would not be the correct cost if arbitrary row swaps counted as one operation.
- **Column swaps:** They are not allowed and are never used.
- **Last target row:** Every row is eligible there because no column lies to the right of the last diagonal cell.
