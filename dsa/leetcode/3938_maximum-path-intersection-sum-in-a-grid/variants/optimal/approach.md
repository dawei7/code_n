## General

**Classify the shape of an intersection.** The first path moves downward as it progresses from left to right, while the second path moves upward. If two shared cells differed in both row and column, the order forced by one path would conflict with the order forced by the other. Consequently, all shared cells lie in one row or in one column. Monotonic movement also prevents gaps between shared cells, so an intersection is a contiguous horizontal or vertical segment.

Every horizontal or vertical segment of length at least two can be realized by a suitable pair of paths. A one-cell intersection is also realizable, but only when that cell is strictly inside the matrix: it cannot lie in the first or last row or the first or last column. At a boundary, the two endpoint directions force an adjacent cell to be shared as well. Therefore the answer is exactly the maximum among:

- every contiguous row segment of length at least two;
- every contiguous column segment of length at least two; and
- every strictly interior single cell.

**Run Kadane's recurrence with a minimum length of two.** For one row, initialize `ending` to the sum of its first two values. When the scan reaches a later value, the best valid segment ending there either extends the previous valid segment or starts with the immediately preceding value. Thus the update is `ending = max(ending + current, previous + current)`. Recording the largest `ending` examines every horizontal segment of length at least two. Apply the same recurrence top-to-bottom in each column, then compare all strictly interior cells individually.

The structural classification proves that every feasible intersection is considered. Conversely, each candidate examined by the scans is realizable by two valid paths, so taking the largest candidate returns exactly the greatest possible intersection score.

## Complexity detail

Let $M$ be the number of rows, $N$ the number of columns, and define the matrix area

$$
A=MN.
$$

The row scans visit all $A$ cells once, the column scans visit them once more, and the interior-singleton scan visits at most $A$ cells. The total time is $O(A)=O(MN)$. Only loop indices, the current segment sum, and the best score are stored, so the auxiliary space is $O(1)$.

The scaling benchmark fixes $M=4$ and uses $N=64$, $256$, and $1000$, giving legal workload sizes $A=256$, $1024$, and $4000$. The accepted scan grows linearly with $A$. A correct comparison implementation that enumerates every contiguous row and column segment using prefix sums grows as $O(MN(M+N))$; with four fixed rows, its dominant row work is quadratic in $A$. The all-positive rows force that implementation to complete its full enumeration while keeping each expected answer unambiguous.

## Alternatives and edge cases

- **Enumerate both paths:** Generating every monotone path pair and scoring its intersection is correct only for tiny matrices; the number of paths is combinatorial.
- **Enumerate all row and column segments:** Prefix sums make each segment score constant-time, but checking every possible segment still costs $O(MN(M+N))$ time.
- **Ordinary Kadane scan:** Allowing a length-one segment everywhere is incorrect because a singleton on the matrix boundary cannot be the complete intersection. The recurrence must enforce length at least two, with interior singletons checked separately.
- **Horizontal segments only:** A best intersection may be vertical, so rows and columns require symmetric scans.
- **All-negative values:** Initializing the answer or a running sum to zero would invent an empty intersection. Initialize from a real two-cell candidate and compare genuine interior cells.
- **Two rows or two columns:** Such a matrix has no strictly interior cell in the missing dimension, but its length-at-least-two row and column segments remain valid.
- **Large rectangular matrices:** The scans access the existing matrix directly and do not copy rows, columns, or prefix arrays, preserving $O(1)$ auxiliary space at the maximum area.
