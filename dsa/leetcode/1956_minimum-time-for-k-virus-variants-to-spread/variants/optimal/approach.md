## General

**Arrival time is Manhattan distance**

A virus spreads one grid edge per day in the four cardinal directions. The minimum number of days for the variant originating at $(x_i,y_i)$ to reach $(x,y)$ is therefore

$$
\lvert x-x_i\rvert+\lvert y-y_i\rvert,
$$

the Manhattan distance. Moving horizontally and vertically for that many total steps reaches the point, and no shorter cardinal path can change both coordinate differences.

At a fixed candidate point, calculate this distance for every unique variant. Even when several variants share an origin, they remain separate variants and produce separate distance entries.

**Use the $k$-th smallest arrival time**

After sorting all distances to one point, `distances[k - 1]` is the day when at least $k$ variants have arrived. Before that day, fewer than $k$ distances are small enough. On that day, the first $k$ sorted distances are all at most the selected value.

Thus the global problem becomes: minimize the $k$-th smallest Manhattan distance over candidate grid points.

The exact solution enumerates every integer point in the axis-aligned bounding rectangle of the origins. For each point, it builds and sorts the distance sequence, then minimizes the order statistic.

**Why points outside the bounding rectangle are unnecessary**

Let `min_x` and `max_x` be the smallest and largest origin $x$ coordinates, and define the analogous $y$ bounds. Suppose a candidate has $x<min_x$. Moving it one step right reduces its horizontal distance to every origin by one, so every variant arrives no later. A candidate with $x>max_x$ can similarly move left. The same argument moves an out-of-range $y$ coordinate toward the rectangle.

Repeatedly projecting any outside point into the rectangle never increases any distance and therefore never increases the $k$-th smallest distance. At least one optimal point lies inside the enumerated bounds.

Because spread occurs on integer grid cells, only integer coordinates need to be considered. The inclusive ranges include all origin-coordinate boundaries.

**A small example**

For origins $(1,1)$ and $(6,1)$ with $k=2$, candidate $(3,1)$ has distances two and three. Its second-smallest distance is three, so both variants are present on day three. Candidate $(4,1)$ gives three and two and has the same result. No point can make the maximum of the two distances below three because the origins are five grid steps apart.

**Why the enumeration is correct**

For every enumerated point, the sorted distance at index $k-1$ exactly equals its earliest qualifying day. Taking the minimum therefore finds the best point within the bounding rectangle.

The projection argument proves some global optimum is in that rectangle, so restricting the search loses nothing. The returned minimum is consequently the earliest day on which any point contains at least $k$ variants.

The initial `answer = inf` is replaced on the first candidate because the rectangle is nonempty. All computed distances are integers, so the final returned value is an integer despite the floating-point infinity sentinel.

**Why sorting duplicate distances is meaningful**

The input points need not be distinct even though variants are unique. If three variants originate at the same coordinate, their three zero distances occupy three separate positions in the sorted list. For $k=3$, index two is zero and the answer may be day zero. Converting origins or distances to a set would destroy variant identity and produce a wrong order statistic.

Variants can also arrive on the same positive day from different directions. Equal numeric distances remain separate list entries because each is evidence that another unique variant has reached the candidate. Sorting a list rather than a set implements this multiplicity exactly.

## Complexity detail

Let $X=max_x-min_x+1$ and $Y=max_y-min_y+1$ be the numbers of integer coordinates in the bounding rectangle, and let $N$ be the number of variants.

There are $XY$ candidate points. At each, computing distances costs $O(N)$ and sorting them costs $O(N\log N)$. Total time is $O(XYN\log N)$.

The distance collection contains $N$ integers and Python's sort may use $O(N)$ temporary memory. Other state is constant, so auxiliary space is $O(N)$.

Given coordinate bounds from one through 100 and $N\le50$, the explicit rectangle search is practical.

## Alternatives and edge cases

- **Select without full sorting:** A $k$-th-order selection algorithm or size-$k$ heap can find the needed distance in $O(N)$ expected time or $O(N\log k)$ time per point.
- **Binary search the day:** Test whether some point lies within at least $k$ Manhattan diamonds of radius $d$. Designing an efficient multi-diamond overlap test is more complex.
- **Enumerate the infinite grid:** Unnecessary; projecting to the origins' bounding rectangle never worsens any arrival.
- **Coincident origins:** Their zero or equal distances are counted separately because variants are unique even at the same point.
- **Answer day zero:** If at least $k$ variants share one origin, that point already contains them on day zero and the method finds zero.
- **$k=2$:** The objective is the second-smallest distance, not necessarily the maximum distance to all origins.
- **$k=N$:** The order statistic becomes the maximum distance, so the method minimizes the day all variants arrive.
- **Candidate at an origin:** That variant contributes distance zero and can count among the first $k$.
- **Tied distances:** Sorting retains duplicate distance values, correctly representing distinct variants arriving together.
- **Multiple optimal points:** Only the minimum day is returned, so the algorithm need not record their coordinates.
- **Rectangle with one coordinate:** If all origins share an $x$ or $y$ coordinate, one loop dimension has length one and the same projection proof applies.
- **Integer days:** Manhattan distances are integral, matching the required minimum integer number of days.
