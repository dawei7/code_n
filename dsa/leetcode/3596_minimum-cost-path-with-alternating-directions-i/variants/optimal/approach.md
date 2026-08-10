## General

Although the grid dimensions can be enormous, the alternating direction rule traps every path near the origin.

The start cell is entered with cost one. The first actual movement must go right or down. From either adjacent cell, the next movement must go left or up, and the only in-bounds choice returns to the origin.

Therefore the only reachable destinations are:

- the origin itself;
- the cell directly below it;
- the cell directly to its right.

**Origin destination**

When `m=1` and `n=1`, start and destination are both `(0,0)`. Its entrance cost is:

`(0+1)(0+1)=1`.

No movement is needed, so one is returned.

**Directly below**

For `m=2,n=1`, destination is `(1,0)`. The first allowed movement goes down.

Total cost is:

$$
cost(0,0)+cost(1,0)=1+2=3.
$$

The destination is reached before an even movement is required.

**Directly right**

For `m=1,n=2`, the symmetric first move goes right to `(0,1)`. Its cost is two, again giving total three.

**Why nothing farther is reachable**

After first moving right to `(0,1)`, the next movement must be left or up. Up leaves the grid because row is zero, so left to origin is forced.

After first moving down to `(1,0)`, the next movement must be left or up. Left leaves the grid because column is zero, so up to origin is forced.

Back at origin, the same situation repeats. Every movement path alternates between origin and one adjacent cell. It can never reach:

- row two or greater;
- column two or greater;
- `(1,1)`, because that would require two consecutive right/down moves.

Thus every other destination is impossible regardless of costs, and the source returns `-1`.

**Why cost optimization disappears**

For each reachable non-origin destination, it is reached on the first move through one forced edge. No alternative legal path can arrive with a different cost.

For unreachable destinations, comparing path costs is meaningless. This is why the solution needs only dimension classification rather than dynamic programming or shortest paths.

**Move-number wording**

The description says the path begins by entering `(0,0)` and also calls odd-numbered moves right/down. The examples treat the first movement after entering the start as the odd directional move. The source follows that example semantics.

If entering the start itself consumed the odd directional parity and the first displacement were even, no move could leave the top-left corner. The local examples disambiguate the intended behavior.

## Complexity detail

The method performs a fixed number of dimension comparisons. Time complexity is `O(1)` and auxiliary space is `O(1)`, independent of grid size.

No grid is allocated, which is essential when dimensions may reach `10^6`.

## Alternatives and edge cases

- **Breadth-first search:** It would discover the same tiny reachable set but allocating or exploring a huge grid is unnecessary.
- **Dynamic programming:** Alternating moves include backward edges, so ordinary directional grid DP is not natural; the reachability invariant eliminates the problem entirely.
- **One row with more than two columns:** The path alternates between columns zero and one and cannot reach farther right.
- **One column with more than two rows:** It alternates between rows zero and one.
- **Both dimensions at least two:** Destination `(m-1,n-1)` is not one of the three reachable cells, even for a `2x2` grid.
- **Origin:** Entrance cost is paid exactly once and returned as one.
- **Adjacent destination:** Start cost plus destination cost gives three.
- **Repeated cycles:** Revisiting cells only adds positive cost and never expands reachability.
- **No waiting move:** The rules require adjacent movement; staying still cannot change parity.
- **Boundary directions:** At origin, left and up are invalid; at a first-step neighbor, the even move back is forced.
- **Large dimensions:** They do not affect runtime because only equality with one or two matters.
- **Cell costs:** Positive products cannot make a longer cycle beneficial even if the destination were already reached.
- **Return type:** Impossible cases use integer `-1` exactly as required.
- **Symmetry:** Swapping `m` and `n` exchanges the down and right cases without changing cost.
- **Induction on movement count:** After every even number of displacements, the path is back at the origin. After every odd number, it is at one of the two valid adjacent cells. The forced-return argument establishes the base and transition, proving no unlisted coordinate can ever appear at any later time.
- **Why a 2x2 destination fails:** Cell `(1,1)` has Manhattan distance two and needs one down plus one right move. Both are forward directions, but consecutive movements must alternate forward and backward, so the two required steps cannot occur consecutively.
- **Entrance accounting:** The source’s value three includes the start cost one and one adjacent-cell cost two. It does not treat the starting entrance as a directional displacement, consistent with both reference examples.
- **Destination reached immediately:** Once an adjacent destination is entered, the task ends; the path is not required to perform the following forced return to the origin.
