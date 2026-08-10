## General

**Count the union of inclusive integer intervals.** Each car covers every integer point from `start` through `end`, including both endpoints. A point covered by several cars must still be counted only once.

The coordinate range is fixed at one through one hundred, so the exact solution uses a difference array rather than sorting and merging intervals.

**Represent range additions at two boundaries.** Array `d` has length 102, providing indices zero through 101. For interval `[start, end]`:

- `d[start] += 1` begins one additional unit of coverage.
- `d[end + 1] -= 1` ends that coverage immediately after the inclusive endpoint.

The index `end + 1` is why position 101 must exist when `end = 100`.

**Recover coverage with a prefix sum.** `accumulate(d)` yields the running sum of difference entries. At coordinate $p$, this running value equals the number of input intervals satisfying

$$
\texttt{start}\le p\le\texttt{end}.
$$

Every interval adds one starting at its left boundary and removes that one after its right boundary, so its contribution is active at exactly the intended coordinates.

**Convert positive coverage into one counted point.** The generator `s > 0 for s in accumulate(d)` produces true when at least one car covers that coordinate and false otherwise. Python sums Booleans as one and zero, so overlap is counted once regardless of how large `s` becomes.

Coordinates zero and 101 are also scanned because the entire difference array is accumulated. Coordinate zero has zero coverage since starts are at least one. At 101, every interval ending at 100 has just been removed, so coverage is again zero. These sentinel positions do not change the answer.
After applying all boundary updates, prefix sum through position $p$ equals the number of intervals whose start update has occurred but whose after-end removal has not. That is exactly the number covering $p$ inclusively. The final Boolean sum counts precisely the positions with nonzero coverage, which is the required interval union cardinality.

**Why subtracting at `end` would be wrong.** An update `d[end] -= 1` would deactivate coverage before evaluating the endpoint itself, treating intervals as half-open. The problem's intervals are inclusive, so the removal belongs at `end + 1`.

**Why a set is not necessary.** One could insert every integer point from every interval into a set, but the difference array aggregates an entire interval with two updates. The fixed coordinate universe makes its later full scan constant-sized.

**No mutation of input intervals.** The code reads each pair and updates only the new difference array.

**Space is constant because the domain is fixed.** The array length 102 does not depend on the number of cars. If coordinate limits were unbounded, this direct allocation would not be constant and interval sorting would be preferable.

**A boundary-update trace.** For interval `[3, 6]`, the algorithm adds one at index three and subtracts one at index seven. Prefix coverage is zero through point two, positive at points three, four, five, and six, and returns to zero at seven. Adding interval `[5, 8]` raises coverage again at five and removes its contribution at nine. Points five and six then have coverage two, but `s > 0` still contributes only one for each.

**Why counts rather than Booleans are stored in the difference array.** Overlapping intervals may start and end at different locations. A numeric active count lets one interval end while another remains active. If boundary updates merely toggled a Boolean, ending one car could incorrectly mark a point uncovered even though another car still spans it.

## Complexity detail

Let $n$ be the number of car intervals and $C=102$ the fixed difference-array length. Applying two updates per interval takes $O(n)$ time. Accumulating and summing across `d` takes $O(C)$ time.

Total time is $O(n+C)$, which simplifies to $O(n)$ because $C$ is fixed by the constraints.

The difference array uses $O(C)=O(1)$ auxiliary space under the fixed coordinate bound. `accumulate` is lazy and retains only running state; the Boolean generator is also lazy.

In a generalized coordinate range up to $M$, the same implementation would use $O(n+M)$ time and $O(M)$ space rather than constant space.

## Alternatives and edge cases

- **Set of covered points:** Add every integer in each inclusive range. With endpoints at most 100 this is simple, but it performs work proportional to total interval lengths.
- **Sort and merge intervals:** This handles huge coordinates in $O(n\log n)$ time and computes integer union lengths with inclusive endpoint adjustments.
- **Boolean coverage array:** Mark every point in each interval. It is easy but uses one update per covered coordinate instead of two per interval.
- **Single-point car:** When start equals end, the start update and removal at the next coordinate cover exactly one point.
- **Overlapping cars:** Prefix coverage may exceed one, but the positivity test counts the coordinate only once.
- **Adjacent intervals:** Intervals ending at three and starting at four cover distinct consecutive points; difference updates handle them without a gap.
- **Duplicate intervals:** They increase coverage counts but not the Boolean union count.
- **Endpoint one:** The sentinel coordinate zero remains uncovered.
- **Endpoint one hundred:** Array index 101 safely receives the removal update.
- **Inclusive semantics:** The `end + 1` boundary is essential.
- **Fixed-domain assumption:** Constant space relies on the documented maximum coordinate of one hundred.
