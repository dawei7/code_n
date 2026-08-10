## General

**Turn “surrounded” into the easier opposite question**

The board contains only `X` and `O`. A region is a group of `O` cells joined through horizontal or vertical moves. An `O` must remain unchanged exactly when its region can reach an edge of the board. Therefore, instead of examining every region and trying to prove that it is enclosed, the solution starts from the edge and marks every `O` that is known to be safe.

This reversal is the central idea. A region may have an irregular shape, so directly checking whether `X` surrounds it requires exploring the whole region and remembering whether any visited cell touches the edge. Starting at the edge removes that uncertainty: every `O` reached from a border `O` is automatically part of a non-surrounded region.

The solution temporarily changes every safe cell from `O` to `.`. The placeholder is unambiguous because the contract says that the original board contains only `X` and `O`.

**What the nested depth-first search means**

For coordinates `(i, j)`, `dfs(i, j)` has one job: if this position is an unmarked `O` inside the board, mark it safe and continue to all four orthogonal neighbors.

The guard rejects three kinds of calls:

- coordinates outside the matrix;
- an original `X`, which blocks connectivity;
- a cell already changed to `.`, which has already been discovered.

Rejecting an already marked cell is essential. Adjacent cells can point back to one another, so an unrestricted recursive search would revisit the same positions indefinitely. Marking before making recursive calls establishes the visited state immediately and ensures that every real `O` is processed at most once.

The expression `pairwise((-1, 0, 1, 0, -1))` produces the four direction pairs `(-1, 0)`, `(0, 1)`, `(1, 0)`, and `(0, -1)`. These are precisely up, right, down, and left. Diagonal cells are intentionally absent because the problem defines connectivity only horizontally and vertically.

**Why all four borders are search origins**

The first pair of loops invokes the search on column `0` and column `n - 1` for every row. The second pair invokes it on row `0` and row `m - 1` for every column. Together, these calls cover every border position.

Corners are passed to `dfs` more than once, and a one-row or one-column board causes still more overlap. That does not affect correctness. The first successful visit changes an `O` to `.`, and every later visit immediately returns because that cell is no longer `O`. Avoiding duplicate border calls could save a few constant-time checks, but it would complicate otherwise direct loops without changing the asymptotic cost.

After all border searches finish, the board has a useful classification:

- `X` is an original blocking cell;
- `.` is an original `O` connected to at least one border;
- `O` is an original `O` not connected to any border.

There cannot be an unmarked `O` that belongs to a border-connected region. If such a cell existed, there would be a horizontal-or-vertical path of `O` cells from a searched border cell to it. The depth-first search follows every such edge, so it would have reached and marked that cell.

Conversely, every `.` is safe. The search can create a `.` only while walking from a border origin through original `O` cells, so its region has a path to the edge and is not surrounded.

**Why the final sweep performs exactly the required mutation**

The last nested loop examines every cell. A `.` is restored to `O`, because its temporary mark proved that it escaped to the border. An `O` is changed to `X`, because remaining unmarked proves that no path from it reaches the border. Original `X` cells match neither branch and remain `X`.

For the larger example, the isolated `O` on the bottom edge is marked first. Any `O` connected to it would also be marked. The three interior `O` cells have no path to a border, so they retain `O` until the final sweep and are then captured as `X`.

The order of the two phases is important. Capturing interior `O` cells before completing all border traversals could erase paths needed to discover safe cells. This implementation first completes the entire safety classification and only then converts the captured cells.

At the end, every original `O` has been placed into exactly one of two exhaustive groups: reachable from the border and restored, or unreachable from the border and captured. That is exactly the problem’s definition.

## Complexity detail

Let $m$ be the number of rows and $n$ be the number of columns.

Each cell can be successfully entered by `dfs` only once, because that visit immediately changes `O` to `.`. Neighbor calls and unsuccessful border calls add only constant work per cell or border position. The final sweep examines all $mn$ cells once. Therefore, total time is $O(mn)$.

The board itself stores the visited state, so there is no separate visited matrix. However, recursive calls still occupy memory. In a board whose safe `O` cells form a long winding path, the recursion can contain as many as $mn$ active calls before unwinding. The worst-case auxiliary space is therefore $O(mn)$, matching the manifest. The fixed loop variables use only constant additional space.

The mutation is in place in the problem’s sense: the algorithm does not allocate another board, and the required answer is written into `board`. “In place” does not imply $O(1)$ auxiliary space when recursion is used; the call stack must still be counted.

## Alternatives and edge cases

- **Breadth-first search from the border:** Use a queue of safe `O` cells and mark each cell when it is enqueued. It proves the same reachability fact without recursive calls, but the queue can require $O(mn)$ memory.
- **Explicit depth-first stack:** Replacing recursion with a stack preserves depth-first traversal while avoiding Python’s recursion-depth limit. It still has $O(mn)$ worst-case auxiliary space.
- **Region-by-region search:** One can start from every unvisited `O`, collect its complete component, and record whether the component touches a border. This works, but it needs component storage and solves a harder classification problem than the border-first method.
- **Union-find:** Treat each `O` as a vertex and union adjacent `O` cells, with a virtual vertex representing the border. This is valid but needs $O(mn)$ parent/rank storage and is more machinery than a single traversal.
- **Single row or single column:** Every cell lies on the border, so every `O` must survive. Duplicate border calls are harmless because marked cells are rejected.
- **All `X`:** Every DFS call returns immediately, and the final sweep leaves the board unchanged.
- **All `O`:** Every cell is connected to a border and becomes `.`, then every cell is restored to `O`; nothing is captured.
- **Diagonal contact:** An interior `O` touching a border `O` only diagonally is not connected to it. The four direction pairs correctly exclude that diagonal move.
- **Temporary-character safety:** Using `.` is correct only because the input alphabet is restricted to `X` and `O`. With a broader alphabet, the marker would need to be chosen or tracked differently.
- **Runtime dependencies:** The selected source refers to `List` and `pairwise` without importing them. A standalone Python file needs `from typing import List` and `from itertools import pairwise`; `pairwise` also requires a sufficiently recent Python version.
- **Recursion depth:** Although the algorithm is mathematically correct for boards up to $200 \times 200$, a large connected component can exceed Python’s default recursion limit. An iterative queue or stack is safer when the execution environment does not raise that limit.
