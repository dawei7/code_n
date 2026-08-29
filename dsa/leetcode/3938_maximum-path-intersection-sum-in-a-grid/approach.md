## General

The source never constructs either player's path. Instead, it uses a geometric property of the two monotone paths: their shared cells can only form one of three shapes:

1. a contiguous horizontal segment containing at least two cells;
2. a contiguous vertical segment containing at least two cells;
3. one interior cell.

Once this property is understood, the path problem becomes a maximum contiguous-segment problem over every row and column, plus a scan of interior singleton cells.

**Why the paths must meet**

At the left edge, player 1 begins above player 2. At the right edge, player 1 ends below player 2. Player 1's row can only stay the same or increase as columns advance, while player 2's row can only stay the same or decrease. On the grid, these two left-to-right routes cannot exchange their vertical order without sharing at least one cell.

This matters when all values are negative. Choosing paths with an empty intersection is not an available way to obtain score zero; some nonempty shared shape must be selected.

**Why the shared shape cannot bend or split**

Both players move right horizontally, but their vertical directions are opposite. If they share two or more consecutive cells in one row, they traverse that horizontal segment in the same direction. Before and after that interval, player 1 can lie above and then below player 2, so they do not need to meet elsewhere.

If they share two or more cells in one column, player 1 traverses the segment downward while player 2 traverses it upward. Because they reach opposite endpoints of that shared vertical segment, they cannot then continue together around a corner as one common path.

More generally, as movement progresses from left to right, player 1 never moves upward and player 2 never moves downward. Their relative vertical order changes only one way. They cannot cross, separate, and later cross again. Therefore the intersection is connected and cannot contain two disjoint segments.

A meeting that does not include a shared grid edge is a singleton. Such a one-cell crossing can occur only in the interior: each path needs room to arrive and depart on the appropriate sides. At a boundary, the endpoint and monotone-movement restrictions force an adjacent shared cell as well. That is why the source considers boundary intersections only through row or column segments of length at least two, while singleton candidates are restricted to rows `1` through `rows - 2` and columns `1` through `cols - 2`.

Conversely, each shape examined by the source can be realized by routing the first path to the segment from above or left and away toward the bottom-right, while routing the second from below or left and away toward the top-right. The surrounding portions can be kept on opposite sides. Thus maximizing over these shapes is equivalent to maximizing over valid path pairs.

**Maximum horizontal segment with length at least two**

For each row, the source uses a length-constrained form of Kadane's algorithm.

The variable `ending` means:

> the maximum sum of a contiguous segment in this row that ends at the current column and contains at least two cells.

At column one, there is only one valid segment ending there with length at least two: the first two cells. Hence:

`ending = row[0] + row[1]`.

For every later column `col`, an optimal qualifying segment ending there has exactly two possibilities:

- extend the previous optimal ending segment by `row[col]`;
- discard the earlier segment and start a new two-cell segment at `col - 1` and `col`.

The recurrence is therefore:

`ending = max(ending + row[col], row[col - 1] + row[col])`.

The global `best` is updated after initialization and after every recurrence. Consequently, it sees every possible right endpoint and retains the greatest sum of every horizontal contiguous segment of length at least two.

Requiring two cells changes ordinary Kadane's algorithm. Restarting from `row[col]` alone would incorrectly allow a boundary singleton and would duplicate the separate interior-cell case.

**Maximum vertical segment with length at least two**

The second nested loop applies the same recurrence down each column. It initializes `ending` with the top two cells, then either extends the best segment ending at the previous row or starts a new two-cell segment using the previous and current rows.

This covers every vertical intersection segment of length at least two. Horizontal and vertical scans both include segments on matrix boundaries, where valid intersections cannot be isolated single cells.

**Interior singleton crossings**

The final loops inspect every cell whose row and column are both strictly inside the grid. Such a cell can be the only shared position of appropriately routed paths, so its value is a valid score by itself.

The source compares each interior value with `best`. This step is particularly important when every adjacent pair has a very negative sum but one interior cell is less negative or positive.

The initial value `-(10 ** 18)` is safely below any legal intersection sum. Since the matrix has at least two rows and two columns, both segment scans have valid initial pairs and replace the sentinel even when there is no interior cell.

**Why the maximum of the three scans is the answer**

Every valid pair of paths has an intersection belonging to one of the three structural forms, and the corresponding scan considers its exact sum. Therefore no path pair can score more than `best`.

Every candidate considered by the scans is a realizable intersection shape, so `best` is attainable by some pair of paths. The value is both an upper bound on all path pairs and a feasible score, making it the required maximum.

## Complexity detail

Let $M$ be the number of rows and $N$ the number of columns.

The horizontal scan visits each matrix cell a constant number of times, for $O(MN)$ time. The vertical scan does the same, and the interior singleton scan is also $O(MN)$. Their sum remains $O(MN)$.

The source stores only dimensions, loop indices, `ending`, and `best`. It does not allocate dynamic-programming tables or path representations, so additional space is $O(1)$.

The input matrix is read but never modified. The source's manifest bounds of $O(MN)$ time and $O(1)$ space accurately describe the implementation.

## Alternatives and edge cases

- **Dynamic programming over both players' positions:** Tracking two simultaneous paths creates a much larger state space. The intersection-shape characterization eliminates path construction entirely.
- **Enumerate all path pairs:** Each player has a combinatorial number of monotone paths, so direct enumeration is infeasible even for moderately sized grids.
- **Ordinary Kadane allowing length one:** This would accept singleton cells on a boundary even though such an isolated boundary intersection is not realizable. The source enforces length two in row and column scans.
- **Only scan horizontal segments:** Paths can traverse the same column in opposite vertical directions, so vertical intersections must also be considered.
- **Only scan segments of length at least two:** A single interior crossing can be optimal, especially when its neighboring values are negative.
- **Allow an empty intersection with score zero:** The paths must cross, so this would be incorrect when all feasible intersection sums are negative.
- **All grid values negative:** The sentinel and nonempty segment initialization select the least costly realizable intersection rather than returning zero.
- **Two rows:** There are no interior singleton rows, but horizontal and vertical length-two scans cover all feasible intersections.
- **Two columns:** There are no interior singleton columns; the segment scans remain sufficient.
- **Exactly a two-cell segment:** It is considered by the initialization in its row or column and by every restart term later in that line.
- **A profitable long segment after a negative prefix:** The restart term drops the harmful prefix while still retaining the required two-cell minimum length.
- **A high-value interior singleton:** The final scan can select it even if all horizontal and vertical segments containing it have smaller sums.
- **A high-value corner alone:** A corner cannot be the sole intersection under the path endpoints and move directions; the source correctly requires an adjacent shared cell there.
