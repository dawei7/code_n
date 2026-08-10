## General

**Ask whether one proposed portion size is possible**

Suppose every child should receive exactly `x` candies. A pile containing `c` candies can be divided into `c // x` complete subpiles of size `x`. Any remainder smaller than `x` cannot serve another child, and it cannot be combined with a remainder from another pile.

Therefore, the total number of children that can receive `x` candies is

$$
\sum_{c \in \texttt{candies}} \left\lfloor \frac{c}{x} \right\rfloor.
$$

The proposal is feasible exactly when this sum is at least `k`. If it exceeds `k`, the extra complete portions may simply go unused.

This calculation respects both important rules. Division creates multiple child portions from one pile, while summing counts portions rather than candy remainders, so no child receives a merged portion from different original piles.

**Feasibility changes monotonically**

If portion size `x` is feasible, every smaller positive size is also feasible. Reducing the requested amount cannot reduce `c // x` for any pile. Conversely, if `x` is infeasible, every larger size is infeasible because each pile can serve no more children.

The candidate answers therefore have the ordered shape

`feasible, feasible, ..., feasible, infeasible, ..., infeasible`.

The goal is the last feasible value, which is the standard “binary search on the answer” pattern.

**Choose safe search bounds**

The code initializes `l = 0` and `r = max(candies)`. Zero represents the answer when even one candy per child is impossible. No child can receive more than the largest original pile because one child's portion must come entirely from one pile, so the maximum pile is a valid upper bound.

The search never evaluates division by zero. While `l < r`, the upper midpoint

`mid = (l + r + 1) >> 1`

is strictly greater than `l`. Since `l` is at least zero, `mid` is at least one whenever an iteration occurs. Right-shifting by one is integer division by two for these nonnegative integers.

**Keep the last feasible value**

For each midpoint, the exact feasibility test is

`sum(x // mid for x in candies) >= k`.

If it is true, `mid` itself might be the answer, and larger values may also work. The code assigns `l = mid`, preserving `mid` while discarding all smaller candidates as unnecessary.

If it is false, monotonicity proves `mid` and every larger value are impossible, so `r = mid - 1` safely removes them.

The upper midpoint is essential when the feasible branch keeps `mid` as the new lower bound. With a lower midpoint, an interval of two consecutive values could repeatedly choose the lower value and fail to shrink. The `+ 1` before halving guarantees progress.

**Why termination returns the maximum**

Throughout the search, no candidate larger than `r` can be feasible, and `l` is a feasible lower-bound answer under the convention that zero is always available. A true test raises the lower bound only to a proven feasible midpoint. A false test lowers the upper bound below a proven infeasible midpoint.

Each iteration strictly shortens the integer interval. Eventually `l == r`. At that point the surviving value is feasible, and every larger original candidate has been proven infeasible or excluded by the initial upper bound. It is exactly the largest feasible portion size.

For `candies = [5, 8, 6]` and `k = 3`, size five yields `1 + 1 + 1 = 3` portions and is feasible. Size six yields `0 + 1 + 1 = 2` and is not. The boundary is therefore five.

For `candies = [2, 5]` and `k = 11`, even size one creates only seven portions. Every positive size is infeasible, so the interval collapses to zero.

**Why total candy count alone is insufficient**

A condition such as `sum(candies) >= k * x` is necessary but not sufficient because leftovers cannot be merged. With piles `[2, 2]` and size three, the total is four but neither pile can produce a three-candy portion. Summing floor divisions correctly returns zero.

**Exact data flow**

The generator expression produces each pile's quotient one at a time for `sum`, so no list of quotients is stored. The input list is never modified. Because every original pile is positive and the list is nonempty, `max(candies)` is valid and at least one.

The method does not stop the feasibility sum early after reaching `k`; it scans all piles on each iteration. An early exit could improve constants but would not change the asymptotic bound.

## Complexity detail

Let `n = len(candies)` and `V = max(candies)`. The initial `max` costs `O(n)` time. Binary search performs `O(\log V)` iterations, and each iteration scans all `n` piles to sum their quotients. Total time is `O(n \log V)`, with the initial linear pass dominated by that bound.

The method stores a constant number of integers. The generator used by `sum` is lazy and does not materialize `n` values, so auxiliary space is `O(1)`.

The child count `k` can be as large as `10^{12}`, and quotient totals can also be large. Python integers handle them safely. Fixed-width implementations should use a sufficiently wide integer type.

## Alternatives and edge cases

- **Try sizes from largest downward:** This eventually finds the answer but can test up to `V` sizes, each requiring an `O(n)` scan, for `O(nV)` time.
- **Search by total candies only:** Dividing `sum(candies)` by `k` ignores the no-merging rule and can claim portions that no single pile can supply.
- **Physically split piles:** Constructing subpiles for every candidate wastes memory and work. Integer division already gives the exact number of complete portions.
- **Binary search with lower midpoint:** If the feasible branch sets `l = mid`, a lower midpoint can make a two-value interval stall. The exact upper midpoint prevents that.
- **More portions than children:** Feasibility needs at least `k`, not exactly `k`. Extra portions or piles may remain unused.
- **Total candies below `k`:** No positive allocation works and the search returns zero.
- **One child:** The child can receive the entire largest pile, so the answer is `max(candies)`.
- **One pile:** The answer is `candies[0] // k` because all child portions must be cut from that pile.
- **Remainders:** Leftover candies smaller than the candidate size are discarded separately for each pile and never combined.
- **Candidate zero:** It is a boundary sentinel and is never passed to division.
- **Large `k`:** The method searches portion size, not child count, so the iteration count remains logarithmic in `V`.
- **Input preservation:** Only quotient calculations are performed; no pile is changed.
