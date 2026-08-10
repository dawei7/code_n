## General

**Separate unavoidable fixed gaps from gaps containing missing values.** Adjacent non-missing values cannot be changed. Their absolute differences provide an immediate lower bound, recorded as `max_fixed_gap`.

Whenever exactly one member of an adjacent pair is `-1`, the fixed member is a boundary value that some chosen replacement must approach. The first scan records the smallest and largest such values as `min_boundary` and `max_boundary`. Interior fixed values that are never adjacent to a missing block impose no condition on `x` or `y` beyond their already measured fixed-fixed gaps.

If there is no mixed fixed/missing boundary, then the array is either entirely fixed or entirely missing. In the all-fixed case, only `max_fixed_gap` matters. In the all-missing case, choose `x=y` and make every adjacent difference zero. Because all legal fixed values are positive, `max_boundary == 0` safely identifies this no-boundary situation.

**Binary-search a proposed maximum difference.** Let $D$ be a candidate limit. Feasibility is monotone: any assignment whose adjacent differences are at most $D$ also works for every larger limit. The source searches from the unavoidable `max_fixed_gap` to a guaranteed feasible upper bound.

For a fixed $D$, it selects the canonical pair

$$
x=\texttt{min\_boundary}+D,\qquad
y=\texttt{max\_boundary}-D.
$$

The extreme boundary values must each lie within $D$ of at least one chosen replacement. If any pair can satisfy the limit, a lower representative can be moved to the right edge of the smallest boundary's allowed interval, and an upper representative can be moved to the left edge of the largest boundary's allowed interval. These movements do not lose coverage of boundary values between the extremes and move the representatives toward each other, which cannot worsen a required transition between them. Thus it is sufficient to test this canonical pair rather than search over all positive integers.

The names `x` and `y` do not require `x <= y`; the helper checks use them symmetrically. At the chosen upper bound they may meet or cross, which is harmless because the statement permits choosing equal values.

**Classify each missing block by how many fixed endpoints it has.** A run of `-1` values can occur between two fixed values, at one array edge, or across the entire array. The all-missing case was handled early. The other structures are checked independently because fixed values separate their adjacency constraints.

**One missing position between fixed endpoints.** For a gap `a, -1, b`, the single replacement must be entirely `x` or entirely `y`. Its cost with `x` is

$$
\max(\lvert a-x\rvert,\lvert b-x\rvert),
$$

and similarly for `y`. `check_single_gap` takes the smaller of these two costs and compares it with $D$. Using both chosen values is impossible because there is only one missing slot.

**Two or more missing positions between fixed endpoints.** Only the first replacement touches `a`, only the last touches `b`, and any change from `x` to `y` inside the block creates an adjacent cost $\lvert x-y\rvert$. Multiple switches never help: once that transition cost is paid, extra switches add no new endpoint option.

There are exactly four useful patterns:

- all missing positions use `x`;
- all use `y`;
- the block starts with `x` and ends with `y`;
- the block starts with `y` and ends with `x`.

`check_multiple_gap` computes the maximum adjacent cost for each pattern and accepts when the least of the four is at most $D$. A block of length at least two can realize either mixed pattern by placing one value at the first position and the other at the last, with any middle positions grouped on either side of a single transition.

**A missing block at an array edge has one attachment.** Leading missing positions touch only the first fixed value; trailing missing positions touch only the last fixed value. Filling the whole edge block with whichever of `x` or `y` is closer creates no internal difference and is feasible exactly when `check_boundary_gap` succeeds.

**Scan the blocks without storing them.** Inside `feasible`, `gap_length` counts consecutive missing positions and `previous` stores the last fixed value. When a new fixed value arrives after an interior gap, the source selects the one-slot or multiple-slot helper. Fixed values are positive, so zero is a safe sentinel for “no previous fixed value.”

Leading and trailing gaps do not have two fixed endpoints during this scan. The source checks them afterward by finding the first and last non-missing values. Each generator scan is still linear and uses constant storage.

**Choose search bounds.** `low = max_fixed_gap` is mandatory. The value

$$
\left\lceil\frac{\texttt{max\_boundary}-\texttt{min\_boundary}}{2}\right\rceil
$$

is represented by `(difference + 1) // 2` and provides a safe boundary-based upper limit; `high` is the maximum of it and the fixed-gap lower bound. At that scale, the canonical representatives meet or overlap enough to satisfy the extreme spread, while fixed gaps are already covered.

The standard lower-bound binary search tests the midpoint. A feasible midpoint replaces `high`; an infeasible one raises `low` to `mid + 1`. When they meet, every smaller limit has been rejected and the retained limit is feasible.

**Why all adjacency constraints are covered.** Fixed-fixed pairs are bounded by `max_fixed_gap`. Every maximal missing block is checked according to its exact endpoint and length structure, and the four-pattern argument covers every meaningful use of the two global replacements inside a block. The canonical-pair lemma removes the need to try other numeric choices for a fixed $D$. Consequently `feasible(D)` is exact, and monotone binary search returns the minimum achievable maximum difference.

## Complexity detail

Let $n$ be the array length and let $U$ be the numeric search range, at most on the order of $10^9$. The initial boundary scan costs $O(n)$. Each feasibility check scans `nums` once and may additionally scan from each edge to find the first or last fixed value; this remains $O(n)$ total time per check.

Binary search performs $O(\log U)$ checks, giving $O(n\log U)$ time. All helpers store only counters and integer values. The forward/reverse generators are lazy, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Dynamic programming over every replacement:** The numeric choices range up to $10^9$, so direct state enumeration is infeasible.
- **Search arbitrary pairs `(x,y)`:** The extreme-boundary canonical pair collapses a two-dimensional choice into one feasibility test per limit.
- **Only one replacement value:** It can be suboptimal when separated boundary clusters are better served by two values.
- **No missing values:** The result is simply the largest fixed adjacent difference.
- **All values missing:** Choose `x=y` and return zero.
- **One missing value between fixed endpoints:** It cannot use a transition from `x` to `y`; the single-gap helper is essential.
- **Long interior missing block:** It may use both values once, paying `abs(x-y)` between them.
- **Leading missing block:** Only its right fixed neighbor constrains it.
- **Trailing missing block:** Only its left fixed neighbor constrains it.
- **Multiple disjoint gaps:** The same global `x` and `y` must satisfy all of them, so every helper uses the same canonical pair.
- **Existing fixed gap dominates:** Binary search never considers a limit below `max_fixed_gap`.
- **Equal canonical values:** The pair may contain the same positive integer, which the examples and contract allow.
- **Positive-value sentinel:** `previous = 0` is safe only because every non-missing input value is at least one.
- **Gap length exactly two:** Mixed patterns are realizable as `[x,y]` or `[y,x]`.
- **Multiple switches inside a gap:** They add repeated `abs(x-y)` edges without improving either endpoint attachment.
- **Large values:** Python integer subtraction and absolute value avoid overflow.
- **Generated source status:** The local editorial is unavailable; this explanation follows the exact Optimal implementation and its helper formulas rather than a competitive-folder approach.
