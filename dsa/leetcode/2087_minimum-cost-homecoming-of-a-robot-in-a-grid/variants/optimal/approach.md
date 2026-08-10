## General

**Separate the row movement from the column movement**

A vertical move costs only according to the row entered. A horizontal move costs only according to the column entered. The cost of entering a row does not depend on the current column, and the cost of entering a column does not depend on the current row.

This separability means horizontal and vertical steps may be interleaved in any order without changing the sum, as long as they enter the same required rows and columns. The solution therefore calculates the vertical cost `dx` and horizontal cost `dy` independently and returns `dx + dy`.

Let `startPos = [x0, y0]` and `homePos = [x1, y1]`.

**Sum exactly the destination rows crossed**

If `x0 < x1`, the robot must move downward. Its successive destination rows are

$$
x_0+1,x_0+2,\ldots,x_1.
$$

The Python slice `rowCosts[x0 + 1 : x1 + 1]` contains exactly those entries. The upper slice endpoint is exclusive, so `x1 + 1` is needed to include the home row.

If `x0 > x1`, the robot moves upward. Its destination rows are

$$
x_0-1,x_0-2,\ldots,x_1.
$$

The order does not matter to a sum. The slice `rowCosts[x1:x0]` contains the same row-cost entries: indices `x1` through `x0 - 1`. It includes the target row and excludes the starting row, precisely matching the cells entered.

If `x0 == x1`, the source takes the second branch, but `rowCosts[x1:x0]` is an empty slice. Its sum is zero, correctly representing no vertical movement.

**Apply the same logic to destination columns**

For rightward movement, `y0 < y1`, the entered columns are `y0 + 1` through `y1`. The slice is `colCosts[y0 + 1 : y1 + 1]`.

For leftward movement, the entered columns are `y1` through `y0 - 1`, represented by `colCosts[y1:y0]`. Equal columns again produce an empty slice and zero cost.

This endpoint handling is a common source of mistakes. The cost belongs to the row or column entered, not the one departed. The starting row and starting column must not be charged merely for the robot already occupying them.

**Why a monotone path is always optimal**

Any path from row `x0` to row `x1` must cross every intermediate row boundary and enter each row between them at least once. Likewise, it must enter every required intermediate column between `y0` and `y1` at least once.

A monotone path does exactly this:

- it moves only toward the target row, never reversing vertically;
- it moves only toward the target column, never reversing horizontally.

Any detour introduces extra row or column entries. All costs are nonnegative, so those additional moves cannot reduce the total cost. At best a zero-cost detour ties the direct route; it can never improve it.

Therefore, summing each necessary destination row and column once gives a lower bound that every path must pay, and a monotone path attains that bound. The computed cost is minimum.

**Why move order does not matter**

Suppose one vertical move enters row `r` and one horizontal move enters column `c`. Performing the vertical move first costs `rowCosts[r] + colCosts[c]`. Performing the horizontal move first costs `colCosts[c] + rowCosts[r]`. These sums are equal.

By repeatedly swapping adjacent horizontal and vertical moves, any monotone interleaving can be rearranged into all vertical moves followed by all horizontal moves without changing its cost. This justifies computing the two dimensions separately even though the source does not build an explicit path.

For the first example, moving from row 1 to row 2 charges `rowCosts[2] = 3`. Moving from column 0 to column 3 charges `colCosts[1] + colCosts[2] + colCosts[3] = 2 + 6 + 7`. Their sum is 18.

**Why the slicing formulas are correct**

Every slice excludes the starting coordinate and includes the destination coordinate in the direction of travel:

- downward: `x0 + 1 : x1 + 1`;
- upward: `x1 : x0`;
- rightward: `y0 + 1 : y1 + 1`;
- leftward: `y1 : y0`.

Although upward and leftward slices list costs in increasing index order rather than actual travel order, addition is commutative, so the total is identical.

The algorithm reads the positions and cost arrays only. It does not mutate them or require the grid to be materialized.

## Complexity detail

Let

$$
D=\lvert x_1-x_0\rvert+\lvert y_1-y_0\rvert,
$$

the Manhattan distance from the starting cell to home.

The two `sum` operations process one cost per required move, so total time complexity is $O(D)$. Since $D\le m+n-2$, this is also $O(m+n)$ in the broad grid dimensions.

The branch manifest states $O(1)$ auxiliary space, which would be correct for index loops or iterator-based summation. However, the exact Python source uses list slicing. Each slice creates a temporary list containing the selected cost entries before `sum` processes it. The executable implementation therefore uses $O(D)$ auxiliary space in the worst case, with peak storage proportional to the larger selected segment.

The returned scalar and coordinate variables themselves use constant space. Replacing slices with loops over index ranges would preserve the same logic and time while achieving actual $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Dijkstra's algorithm:** General weighted-grid shortest paths suggest Dijkstra, but these costs depend only on the destination row or column and are nonnegative. Separability makes graph search unnecessary.
- **Dynamic programming over the rectangle:** A DP can compute path costs but uses work and storage proportional to an area. The minimum is simply the sum over mandatory row and column crossings.
- **Explicit coordinate simulation:** Moving one step at a time and adding the entered cost is correct and also $O(D)$. Slicing expresses the same sum compactly.
- **Iterator-based summation:** Using loops or generator expressions avoids slice copies and realizes the manifest's $O(1)$ auxiliary-space claim.
- **Already at home:** All four coordinates match, both slices are empty, and the result is zero.
- **Same row:** `dx` is zero; only the destination columns are charged.
- **Same column:** `dy` is zero; only the destination rows are charged.
- **Moving upward:** Include the home row's cost and exclude the starting row's cost. `rowCosts[x1:x0]` has exactly that membership.
- **Moving left:** Include the home column's cost and exclude the starting column's cost. `colCosts[y1:y0]` does so.
- **Zero costs:** Detours through zero-cost entries may tie a monotone route, but they cannot make the minimum lower than the mandatory-crossing sum.
- **Nonnegative-cost assumption:** The no-detour proof relies on every cost being at least zero. Negative entry costs could make repeated detours beneficial, but they are outside the constraints.
- **Slice-space subtlety:** Python slicing is not a constant-space view. Complexity documentation must distinguish the mathematical path method from the memory behavior of this exact implementation.
- **No grid construction:** Only row and column cost arrays are needed; an $m$ by $n$ matrix would duplicate information without helping the calculation.
