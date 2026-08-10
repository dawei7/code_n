## General

**Turn a maximum-length question into a feasibility question.** For a proposed positive segment length `L`, a ribbon of length `x` produces exactly `x // L` whole segments of that length; any remainder may be discarded. Summing this quotient over all ribbons tells whether at least `k` segments can be produced. The optimization asks for the largest `L` whose total is at least `k`.

**Feasibility is monotone.** If length `L` is feasible, every smaller positive length is also feasible because each original ribbon yields at least as many shorter pieces. If `L` is infeasible, every larger length is also infeasible. Thus candidate lengths form a prefix of feasible integers followed by infeasible integers. This ordered boundary is exactly what binary search can locate.

**Choose complete search bounds.** `left` starts at zero. Zero is not a legal positive segment length, but it is a useful sentinel answer for the case in which even length one cannot produce `k` pieces. `right = max(ribbons)` is a valid upper bound because no produced piece can be longer than the longest original ribbon. The input is nonempty, so `max` is always defined.

The loop invariant is that the true answer lies in closed interval `[left, right]`. Initially this includes every possible positive answer plus zero. Updates never discard the maximum feasible length.

**Use the upper middle.** The midpoint is

`mid = (left + right + 1) >> 1`,

which is integer floor division of `left + right + 1` by two. This rounds upward. When only two candidates remain, such as `left = 3` and `right = 4`, it chooses four. If four is feasible, assigning `left = mid` makes progress to equality. A lower midpoint would choose three and could repeat forever after the same feasible update.

Whenever `left < right`, the upper midpoint is at least one because `right` is positive or the loop would already be finished. Therefore `x // mid` never divides by zero, even though zero is allowed as the sentinel lower bound.

**Count pieces for the candidate.** The generator `x // mid for x in ribbons` computes each ribbon's contribution, and `sum` produces `cnt`. If `cnt >= k`, `mid` is feasible, so the maximum feasible value is at least `mid` and the code keeps the upper half with `left = mid`. Otherwise, `mid` and every larger length are infeasible, so `right = mid - 1` keeps only the lower half.

**Trace `[9, 7, 5]` with three required pieces.** Length five produces `1 + 1 + 1 = 3` pieces and is feasible. Length six produces `1 + 1 + 0 = 2` and is infeasible. Monotonicity then tells us every length above five fails and every positive length below five succeeds. Binary search converges to five without testing every length sequentially.

**Why “at least” is important.** A candidate producing more than `k` pieces is still feasible because unwanted pieces or leftover material can be discarded. Requiring exactly `k` could destroy monotonicity and reject a perfectly usable length. The source correctly tests `cnt >= k`.

**Why the final bound is the answer.** On a feasible midpoint, the lower bound moves up to that midpoint; on an infeasible midpoint, the upper bound moves below it. The interval shrinks every iteration because of upper-mid rounding. When `left == right`, the invariant leaves only one possible boundary value. If positive length one was infeasible, repeated failures drive both bounds to zero; otherwise they meet at the largest feasible positive length.

**No cutting simulation is necessary.** Integer division already counts how many equal whole pieces can be extracted independently from each ribbon. Their remainders cannot be combined across ribbons, and the quotient does not combine them. This exactly models the cutting rules with constant state per ribbon.

## Complexity detail

Let $N$ be the number of ribbons and $M$ the maximum ribbon length. Binary search performs $O(\log M)$ iterations. The exact source's `sum` scans all $N$ ribbons in every iteration, even if the count reaches `k` early. Total time is therefore $O(N\log M)$.

The generator expression is lazy and holds only the current ribbon contribution. Beyond input storage, the method uses a fixed number of integers, so auxiliary space is $O(1)$, matching the manifest.

The sum of contributions can be large: with $N=10^5$, ribbon lengths $10^5$, and candidate one, it reaches $10^{10}$. Python integers handle this. A fixed-width implementation should use a 64-bit count, or stop counting once `k` is reached.

## Alternatives and edge cases

- **Early-stop feasibility helper:** Accumulate pieces and return true as soon as the total reaches `k`. This keeps the same worst-case complexity but can save work for small candidate lengths. The exact generator always completes the scan.
- **Linear search over lengths:** Testing every value up to $M$ costs $O(NM)$ and ignores monotonicity, which is too slow at the constraints.
- **Sort ribbons first:** Sorting is unnecessary because each feasibility count is an independent quotient sum. It adds $O(N\log N)$ work without helping the binary-search predicate.
- **Impossible even at length one:** All available unit pieces total less than `k`, so every positive candidate fails and the algorithm returns sentinel zero.
- **Exactly enough pieces:** Equality `cnt == k` satisfies `>=` and correctly marks the length feasible.
- **One ribbon:** Binary search finds the largest length `L` with `ribbon // L >= k`, equivalent to `floor(ribbon / k)` when positive.
- **Discarded remainders:** `x // mid` intentionally ignores `x % mid`. Remainders from different ribbons cannot be joined and may be discarded.
- **Very large `k`:** The count and comparison remain valid, and zero is returned when unit segments are insufficient.
- **Division by zero:** Although `left` can be zero, upper-mid selection guarantees `mid >= 1` whenever the loop body runs. The code never evaluates a zero-length predicate.
