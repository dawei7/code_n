# Painting a Grid With Three Different Colors

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1931 |
| Difficulty | Hard |
| Topics | Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/painting-a-grid-with-three-different-colors/) |

## Problem Description
### Goal
An $M \times N$ grid begins with every cell unpainted. Paint every cell with
exactly one of three colors: red, green, or blue. Two cells are adjacent when
they share a horizontal or vertical side, and adjacent cells are not allowed
to receive the same color.

Count all complete colorings that satisfy this adjacency rule. Colorings are
different when at least one cell has a different color. Because the number of
valid grids can be large, return the count modulo $10^9 + 7$.

### Function Contract
**Inputs**

- `m`: the row count $M$, where $1 \le M \le 5$.
- `n`: the column count $N$, where $1 \le N \le 1000$.

For a fixed height $M$, let

$$
S = 3 \cdot 2^{M-1}
$$

be the number of column colorings whose vertically adjacent cells differ.

**Return value**

- The number of valid colorings of the entire grid, reduced modulo
  $10^9 + 7$.

### Examples
**Example 1**

- Input: `m = 1, n = 1`
- Output: `3`

**Example 2**

- Input: `m = 1, n = 2`
- Output: `6`

**Example 3**

- Input: `m = 5, n = 5`
- Output: `580986`

### Required Complexity
- **Time:** $O(NS^2)$
- **Space:** $O(S^2)$

<details>
<summary>Approach</summary>

#### General

**Represent one column as a state**

The small row limit makes an entire column a practical dynamic-programming
state. Generate every length-$M$ sequence over the three colors whose
consecutive entries differ. The first cell has three choices and each later
cell has two choices other than the color immediately above it, giving
$S = 3 \cdot 2^{M-1}$ valid states.

**Precompute which columns may be neighbors**

Two valid column states are compatible when their colors differ in every row.
That condition enforces all horizontal adjacencies between the two columns;
the construction of each state already enforces its vertical adjacencies.
Precompute the compatible successor states for every state once.

**Extend the grid from left to right**

For the first column, each valid state contributes one coloring. For every
later column, transfer the count of each current state to all compatible next
states, reducing additions modulo $10^9 + 7$. After processing $N$ columns,
sum the counts of all final states.

Every counted transition joins two internally valid columns and checks every
new horizontal edge, so it produces a valid larger grid. Conversely, removing
the last column from any valid grid leaves a valid prefix and a compatible
last state. Thus each valid grid follows exactly one sequence of state
transitions and is counted once.

#### Complexity detail

There are $S$ valid column states. Building their compatibility relation takes
$O(MS^2)$ time and stores at most $O(S^2)$ transitions. Each of the $N-1$
column extensions examines at most $S^2$ compatible-state candidates, for
$O(NS^2)$ total time because $M \le 5$. The transition relation uses
$O(S^2)$ space and the two count arrays use $O(S)$ additional space.

#### Alternatives and edge cases

- **Recursive cell-by-cell enumeration:** Trying all three colors and
  backtracking around conflicts is correct, but the number of partial grids
  grows exponentially with $MN$ and cannot support $N=1000$.
- **Transfer-matrix exponentiation:** Treat the compatibility relation as a
  matrix and raise it to the $(N-1)$st power. This reduces the dependence on
  $N$ to logarithmic but introduces cubic state operations and is unnecessary
  for the given limits.
- With one column, every vertically valid state is a complete grid, so the
  answer is exactly $S$.
- With one row, the first cell has three choices and every later cell has two;
  the count is $3\cdot2^{N-1}$ before applying the modulus.
- Diagonal cells are not adjacent and may share a color.
- The modulus must be applied during transitions so intermediate counts remain
  bounded.

</details>
