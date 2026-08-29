## General

**Separate the required journey into adjacent legs**

The points must be visited in the given order. Therefore the journey consists of a leg from `points[0]` to `points[1]`, then from `points[1]` to `points[2]`, and so on. How one travels between one required pair cannot change the required endpoints of any later leg. The minimum total time is consequently the sum of the minimum times for all adjacent pairs.

Python's `pairwise(points)` produces exactly those adjacent pairs without constructing a separate list. For points `A, B, C`, it yields `(A, B)` and `(B, C)`. The generator expression calculates one distance for each pair, and `sum` adds them.

Passing through a later point early does not alter this decomposition. The statement says such a pass does not count as visiting it. The traveler must still reach each point at its proper place in the sequence, so adjacent required legs remain the correct units.

**Finding the minimum time for one leg**

Suppose two adjacent points differ by

$$
\Delta x=\lvert x_1-x_2\rvert,\qquad
\Delta y=\lvert y_1-y_2\rvert.
$$

One diagonal second can reduce both remaining coordinate differences by one. A horizontal or vertical second reduces only one. It is always beneficial to use diagonal movement while both differences are positive because one second then accomplishes the work of one horizontal and one vertical step together.

The traveler can make $\min(\Delta x,\Delta y)$ diagonal moves toward the destination. After that, the smaller coordinate difference is zero. The larger coordinate still needs

$$
\max(\Delta x,\Delta y)-\min(\Delta x,\Delta y)
$$

straight moves. Total time becomes

$$
\min(\Delta x,\Delta y)+\max(\Delta x,\Delta y)-\min(\Delta x,\Delta y)
=\max(\Delta x,\Delta y).
$$

This quantity is the Chebyshev distance between the points. The exact source computes it as `max(abs(p1[0] - p2[0]), abs(p1[1] - p2[1]))`.

Movement directions are chosen according to the signs of the coordinate differences. If both destination coordinates are larger, diagonal moves go up and right; if one is smaller, they go in the corresponding opposite diagonal direction. Absolute values correctly count required movement regardless of direction.

**Why no route can be faster**

In one second, the rules allow either one straight unit or one diagonal unit. Under all options, the x-coordinate changes by at most one and the y-coordinate changes by at most one. Any path must correct $\Delta x$ units horizontally, so it needs at least $\Delta x$ seconds. It must also correct $\Delta y$ units vertically, so it needs at least $\Delta y$ seconds. Hence every path needs at least $\max(\Delta x,\Delta y)$ seconds.

The diagonal-then-straight construction reaches the destination in exactly that many seconds. It meets the lower bound, so it is optimal. Summing these individually optimal, mandatory legs produces a globally optimal trip.

For `[1,1]` to `[3,4]`, the differences are two and three. Two diagonal steps reach `[3,3]`, and one vertical step reaches `[3,4]`, for a total of three. From `[3,4]` to `[-1,0]`, both differences are four, so four diagonal steps suffice. The sum is seven.

For `[3,2]` to `[-2,2]`, the vertical difference is zero and the horizontal difference is five. No diagonal movement helps; five horizontal steps match the maximum difference.

**Reading the one-expression implementation**

The outer `sum` begins with zero and consumes the generator lazily. Each pair contributes its Chebyshev distance. There is no explicit accumulator variable, but `sum` performs the same accumulation a loop would.

When the input contains one point, `pairwise(points)` yields no pair because there is no next destination. The sum of an empty iterable is zero, correctly indicating that the starting point is already the only required visit.

The function returns an integer because all coordinate differences are integers and every allowed move costs exactly one second. The geometric length $\sqrt 2$ of a diagonal does not mean the time is irrational; the rule explicitly assigns that move a cost of one second.

## Complexity detail

Let $n$ be the number of points. There are $n-1$ adjacent pairs. Each pair requires a constant number of indexing, subtraction, absolute-value, and maximum operations, so the total time is $O(n)$.

This is optimal in the input model because each point can affect the distance to a neighbor and therefore must be inspected.

The generator expression does not build a list of distances. `pairwise` retains only the previous point while advancing through the input, and `sum` retains only its running total. The exact implementation therefore uses $O(1)$ auxiliary space.

The input and integer result are not counted as extra space. Coordinate bounds keep individual differences small, though Python also handles the accumulated integer without overflow.

## Alternatives and edge cases

- **Explicit loop:** Iterate through indices from one to $n-1$ and add each Chebyshev distance. It has identical complexity and may be easier to debug, while the exact generator is more concise.
- **Simulate every second:** Constructing the actual diagonal and straight moves produces the same answer but takes time proportional to total travel distance rather than merely the number of points.
- **Manhattan distance is incorrect:** $\Delta x+\Delta y$ assumes horizontal and vertical work cannot occur together. Diagonal movement makes that an overestimate whenever both differences are positive.
- **Euclidean distance is incorrect:** The objective counts allowed one-second moves, not continuous geometric path length.
- **Single point:** There are no legs, and `sum` returns zero.
- **Repeated consecutive points:** Both coordinate differences are zero, so that leg contributes zero.
- **Purely horizontal or vertical leg:** One difference is zero, making the maximum equal to the required straight distance.
- **Equal coordinate differences:** Every move can be diagonal, so time equals either difference.
- **Negative coordinates:** Absolute differences remove direction and make the same formula valid in every quadrant.
- **Passing a later point early:** It does not count as a visit, so the required adjacent-pair order cannot be shortened by such a crossing.
- **Input order is mandatory:** Reordering points could shorten a traveling-salesperson tour, but it would solve a different problem.
