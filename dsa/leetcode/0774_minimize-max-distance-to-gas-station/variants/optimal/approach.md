## General

**Binary-search the answer value**

The new station positions are real numbers, so directly enumerating placements is impossible. Instead, ask a feasibility question for a proposed maximum gap `x`:

Can every original gap be divided into pieces of length at most `x` using no more than `k` new stations?

If a value is feasible, every larger value is also feasible. If it is infeasible, every smaller value is infeasible. This monotonic boundary supports binary search over real values.

**How many stations a single gap needs**

For original adjacent stations at `a` and `b`, let gap `g = b - a`. Adding `q` stations divides it into `q + 1` pieces.

The exact mathematical minimum is

`ceil(g / x) - 1`.

For non-exact ratios, this equals `floor(g / x)`, which the code computes as `int(g / x)`. At a ratio that is exactly an integer, `int(g / x)` is one larger than the mathematical requirement because stations can divide the gap into exactly equal pieces.

The source’s check is therefore conservative at exact floating-point boundaries. It treats those isolated boundary values as infeasible and converges to a value infinitesimally above them. Because the accepted answer tolerance is `10^-6` and the search interval is narrowed to that width, the returned value remains within tolerance.

For instance, when `g = 6` and `x = 2`, the exact requirement is two new stations, producing three pieces of length two. The implementation computes `int(6 / 2) = 3`. For every candidate just larger than two, however, the quotient is just below three and truncates to two. Thus the discrepancy changes only which side owns the single boundary point; it does not create an interval of incorrect answers.

**Sum requirements across independent gaps**

Stations added inside one original gap cannot reduce another gap. The total number required for candidate `x` is the sum over consecutive station pairs.

`check(x)` returns true when the computed count is at most `k`.

Although the problem says add exactly `k` stations, using fewer to meet a candidate is sufficient: any remaining stations can be inserted inside existing gaps and cannot increase the maximum distance.

**Maintain infeasible and feasible boundaries**

The search starts with `left = 0` and `right = 10^8`. Zero is impossible for distinct original stations. The maximum coordinate span is at most `10^8`, so the right endpoint is safely feasible.

At midpoint:

- If `check(mid)` is true, the optimum is no larger, so move `right` down.
- Otherwise the optimum is larger, so move `left` up.

The interval always encloses the feasibility boundary.

**Why the loop stops at `10^-6`**

Each iteration halves the numeric interval. When `right - left <= 10^-6`, both boundaries are within the accepted absolute error of the true optimum.

The exact source returns `left`, the lower boundary. Even though it is nominally infeasible under the maintained convention, its distance from the feasible boundary is at most the tolerance.

**Trace evenly spaced stations**

For stations one unit apart and one new station available per gap overall in a suitable example, testing `x = 0.5` asks for two half-unit pieces in a unit gap. Mathematically one station suffices.

The conservative integer formula may reject exactly 0.5 but accepts values just above it. Binary search still converges within `10^-6` of 0.5.

**Why placement construction is unnecessary**

For a feasible gap, the required number formula proves that equally or suitably spaced stations can divide it into enough pieces. The task asks only for the minimum penalty value, not station coordinates, so the binary search need not construct positions.


The required-station count is monotone nonincreasing as candidate gap `x` grows. Summing per-gap requirements exactly characterizes whether the entire line can achieve that maximum, apart from the source’s conservative exact-ratio boundary behavior.

Binary search maintains the optimum between its bounds and shrinks their distance below the allowed error. Thus the returned floating value satisfies the required accuracy.

Notice that feasibility depends only on the sum of additions. Each gap can be handled independently, and joining the per-gap placements creates a valid placement for the whole road because original station positions are the boundaries between those gaps.

## Complexity detail

Let `n` be the number of existing stations, `R` the initial search width, and `epsilon = 10^-6`. One feasibility check examines `n - 1` gaps in `O(n)` time.

Binary search performs `O(log(R / epsilon))` iterations. Total time is `O(n log(R / epsilon))`.

Only scalar bounds and a streaming sum are stored, giving `O(1)` auxiliary space.

## Alternatives and edge cases

- **Use `ceil(g/x) - 1` explicitly:** This is the mathematically exact station count and avoids conservative exact-multiple behavior.

- **Priority queue splitting:** Repeatedly split the currently worst effective gap. It can work but costs roughly `O((n+k) log n)` and is expensive for `k` up to one million.

- **Binary-search station coordinates:** Placement space is continuous and multidimensional; search the penalty instead.

- **Exact number of additions:** Extra unused stations can always be placed without worsening a feasible penalty.

- **Very large coordinate gaps:** The initial right bound covers the complete allowed axis span.

- **Floating termination:** A fixed tolerance is necessary because an exact real-number equality loop may never finish.

- **Return lower boundary:** Its separation from the true boundary is bounded by the final interval width.
