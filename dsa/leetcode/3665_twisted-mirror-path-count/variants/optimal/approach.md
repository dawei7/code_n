## General

**Direction is part of the state.** At an empty cell, the robot may choose either outgoing direction, so only the total number of arrivals matters there. At a mirror, however, a horizontal arrival must leave vertically and a vertical arrival must leave horizontally. Combining those counts before processing the mirror would lose essential information.

For each cell, conceptually maintain:

- the number of paths arriving from the left while moving right;
- the number of paths arriving from above while moving down.

At an empty cell, add the two arrivals modulo $10^9+7$ and send that same total both right and down. At a mirror, send the horizontal count down and the vertical count right; this is exactly a swap. Repeating this local transition automatically handles any chain of adjacent mirrors without a separate simulation.

**Roll the vertical state by columns.** Process cells in row-major order. An array `from_above[j]` stores the vertical count entering column $j$ from the previous row. A scalar `from_left` stores the horizontal count entering the current cell from its left neighbor.

After processing a cell, overwrite the scalar with its outgoing-right count and the column entry with its outgoing-down count. Reset the scalar to zero at the start of every row, which discards paths that moved right past the previous row's boundary. Downward counts written on the last row and rightward counts written at the last column are never consumed, so reflected paths leaving the grid contribute nothing.

Initialize the empty start cell with one path. The destination is guaranteed empty; when it is processed, its merged arrival count is the answer. Every valid path follows one transition at each visited cell and contributes once to the corresponding directional state. Every propagated state follows the movement and reflection rules, while out-of-bounds flows are discarded. The final count is therefore exact.

## Complexity detail

Let $m$ and $n$ be the row and column counts. Every cell performs constant work once, giving $O(mn)$ time. The rolling vertical array has $n$ entries and the horizontal state is scalar, so auxiliary space is $O(n)$.

The benchmark defines its size as the number of cells, using empty square grids with $16$, $49$, and $100$ cells. The accepted rolling DP scales linearly in this workload. A calibrated correct alternative recursively explores both choices at every empty cell without memoization, returning the same path counts but exhibiting combinatorial growth.

## Alternatives and edge cases

- **Full three-dimensional DP:** Storing both directions for every cell is correct but uses $O(mn)$ space instead of a rolling row.
- **Recursive search without memoization:** It directly follows every route but repeats subproblems and grows exponentially on empty grids.
- **Merge directions at a mirror:** This is incorrect because the two incoming directions reflect differently.
- **Consecutive mirrors:** Apply the swap at each mirror; no special chain traversal is needed.
- **Mirror on the last row:** A horizontal arrival reflects downward and becomes invalid.
- **Mirror on the last column:** A vertical arrival reflects rightward and becomes invalid.
- **Empty grid:** The recurrence reduces to the ordinary monotone-path count.
- **Modulo reduction:** Reduce merged counts throughout so large empty-grid path counts remain bounded.
- **Destination:** It is empty by contract, so both directional arrivals are accepted there.
