## General

**Decompose each move into one coordinate.** A rook at $(x,y)$ can move to an adjacent vertical or horizontal cell. A vertical move changes only $x$ by one; a horizontal move changes only $y$ by one. If that rook eventually reaches $(r,c)$, every route needs at least

$$
\lvert x-r\rvert+\lvert y-c\rvert
$$

moves, and a monotone route using exactly that many vertical and horizontal steps exists when considered geometrically.

A peaceful $n\times n$ board with exactly $n$ rooks has exactly one rook in every row and every column. Therefore its final row coordinates must be the multiset $\{0,1,\ldots,n-1\}$, and its final column coordinates must be the same multiset. The total cost separates:

$$
\sum \lvert x_i-r_i\rvert+\sum \lvert y_i-c_i\rvert.
$$

The row assignment affects only the first sum, and the column assignment affects only the second. Thus the minimum total is the minimum row cost plus the minimum column cost. We do not need to guess complete destination cells all at once.

**Match sorted coordinates to sorted targets.** The target rows are already sorted as $0,1,\ldots,n-1$. Sort the rooks by current row, obtaining row coordinates

$$
x_0\le x_1\le\cdots\le x_{n-1}.
$$

The minimum row cost is

$$
\sum_{i=0}^{n-1}\lvert x_i-i\rvert.
$$

In the exact source, `rooks.sort()` performs a lexicographic sort. Row is the first element of each pair, so this gives the required nondecreasing row order; column merely breaks ties and does not change the row-cost calculation. The generator `sum(abs(x - i) for i, (x, _) in enumerate(rooks))` pairs the $i$th smallest current row with target row $i$.

The source then sorts the same list by column using `rooks.sort(key=lambda x: x[1])`. If the sorted columns are $y_0\le\cdots\le y_{n-1}$, the second sum pairs $y_j$ with target column $j$ and adds `abs(y - j)`.

**Why crossing assignments cannot be better.** The crucial fact is the optimality of sorted matching for absolute distance on a line. Suppose two current coordinates satisfy $a\le b$, but an assignment crosses them by sending $a$ to the larger target $d$ and $b$ to the smaller target $c$, where $c\le d$. Then

$$
\lvert a-c\rvert+\lvert b-d\rvert
\le
\lvert a-d\rvert+\lvert b-c\rvert.
$$

In words, uncrossing the two assignments never increases total travel. This can be seen by placing $a,b,c,d$ on a number line: a crossing assignment traverses the middle separation unnecessarily. Repeatedly uncrossing every inverted pair produces the sorted-to-sorted assignment. Hence matching the $i$th smallest current row to row $i$ is optimal. The identical argument proves the column sum.

This proof handles duplicate coordinates too. If several rooks share a row, they occupy consecutive positions after sorting and are assigned to different target rows. Tie order is irrelevant to the value of the row sum because their $x$ coordinates are equal. Their identities can later receive column targets according to the independent column ordering.

**Why independent row and column assignments form valid destinations.** Every rook receives exactly one target row from the row ranking and exactly one target column from the column ranking. The row targets form a permutation of $0$ through $n-1$, and so do the column targets. Combining each rook's assigned row and assigned column creates $n$ endpoints. Two rooks cannot share an endpoint because that would require sharing both a target row and a target column, while each coordinate target is unique. The resulting board therefore has exactly one rook per row and per column.

For any such assignment, a rook's necessary vertical and horizontal distances add. Summing all independently minimized row distances and column distances gives both a lower bound on every possible peaceful arrangement and the cost of the constructed coordinate assignment. Therefore no solution can use fewer moves.

The “no two rooks in the same cell at any point” rule constrains the order in which elementary moves are carried out, but it does not increase this minimum count. The standard rearrangement can be scheduled by moving rooks toward deficient rows and columns while postponing a move whose next cell is temporarily occupied; the blocking rook is moved first. There are only $n$ rooks among $n^2$ cells, and the target row and column assignments are unique, so for $n>1$ empty cells permit the moves to be ordered without placing two rooks together. For $n=1$, the sole rook is already peaceful. The calculation counts only the necessary coordinate changes, not any collision-causing simultaneous motion.

**A row-heavy example.** For `rooks = [[0,0],[0,1],[0,2],[0,3]]`, sorted rows are `[0,0,0,0]`. Matching them to `[0,1,2,3]` costs $0+1+2+3=6$. Columns are already `[0,1,2,3]`, so their cost is zero. The answer is six. Any peaceful board must fill rows $1$, $2$, and $3$, and those vertical displacements prove that fewer than six moves is impossible.

## Complexity detail

Let $n$ be both the number of rooks and the board dimension. The source sorts the list twice. Each Python sort takes $O(n\log n)$ worst-case time, and each following sum scans all rooks in $O(n)$ time. Constants from two sorts do not change the asymptotic result, so total time is $O(n\log n)$.

Python's Timsort can use $O(n)$ temporary auxiliary memory in the worst case. The generators consumed by `sum` hold only constant iteration state, and the numeric accumulator is constant-sized in asymptotic terms. Thus the implementation's auxiliary space is $O(n)$, matching the manifest's Python-specific bound. Both sorts mutate the caller-provided `rooks` list; after the method returns, it is left ordered by column rather than in its original order.

Because coordinates lie in $0$ through $n-1$, an alternative counting method can compute the same transport costs in $O(n)$ time and $O(n)$ space. Consequently, the checked-in sorting source is optimal in its matching rule but is not the best possible asymptotic running time under the bounded-coordinate constraint. The complexity stated here describes the exact Optimal-variant source, not that faster editorial alternative.

## Alternatives and edge cases

- **Counting rows and columns:** Count how many rooks occupy each row and column, then sweep the imbalance. If a prefix has $b$ excess rooks, exactly $\lvert b\rvert$ rooks must cross the next boundary; summing these absolute imbalances gives the minimum. This runs in $O(n)$ time and $O(n)$ space and is asymptotically faster than the exact sorting implementation.
- **Minimum-cost bipartite matching:** One could build assignment costs from rooks to complete destination cells and run a general matching algorithm. That obscures the separable one-dimensional structure and is dramatically more expensive.
- **Greedily move a rook to the nearest currently empty row and column:** Without sorted global matching, local tie choices can cross and increase later travel. The exchange argument is what justifies the rank-based assignment.
- **Duplicate rows:** Sorting places all equal row coordinates together and assigns them distinct target rows. No special duplicate handling is needed.
- **Duplicate columns:** The second sort handles them symmetrically and assigns distinct target columns.
- **Initially peaceful board:** Sorted row coordinates and column coordinates are both exactly $0,1,\ldots,n-1$, so every absolute difference is zero.
- **Single rook:** With $n=1$, its only legal position is $(0,0)$ under the coordinate constraints. Both sums are zero, and there is no collision issue.
- **Rooks may exchange relative identity:** The goal does not prescribe which rook must occupy which final square. Sorting exploits this freedom; assigning fixed labeled destinations could force unnecessary moves.
- **Collision restriction:** The arithmetic result assumes moves are sequenced, never that rooks pass through one another simultaneously. A temporarily blocked rook can wait while the blocking rook advances. Waiting costs no move, so it does not alter the minimum coordinate-distance total.
- **No initial duplicate cells:** This input guarantee is important for legal starting state and collision-free scheduling. Duplicate rows or columns are allowed; only the complete coordinate pair must be unique.
- **Input mutation:** The first lexicographic sort and second column-key sort both reorder `rooks`. Callers that need its original order must pass a copy.
- **Integer size:** The maximum total is safely small for the stated $n\le500$, and Python integer arithmetic would remain exact even without that small bound.
