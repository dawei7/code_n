## General

**Recognize weighted interval scheduling.** Every offer covers an inclusive interval of houses and supplies a profit. Two accepted offers are compatible exactly when their intervals do not share a house. The task is to choose a maximum-profit set of nonoverlapping intervals; houses not covered by an accepted offer are irrelevant.

The exact solution sorts offers by their ending house and applies the classic weighted interval scheduling recurrence.

**Sort by inclusive end position.** `offers.sort(key=lambda x: x[1])` places earlier-finishing offers first. It also mutates the caller's list order. After sorting, any offer compatible before the current offer must occur in an earlier part of the list, which makes a one-dimensional prefix DP possible.

The list `g = [x[1] for x in offers]` stores sorted end positions for binary search.

**Define the dynamic-programming prefix.** With offers numbered one through $m$ after sorting, `f[i]` is the maximum profit obtainable from the first $i$ offers. `f[0] = 0` represents selecting nothing.

For current one-based offer `i` with start `s` and profit `v`, an optimum over the first $i$ offers has two exhaustive possibilities:

- Skip the current offer, retaining `f[i - 1]`.
- Take it, add `v` to the best solution using only offers whose end is strictly less than `s`.

Strictness is necessary because both interval endpoints are inclusive. An earlier offer ending at `s` would also sell house `s` and would overlap.

**Locate all compatible predecessors.** `j = bisect_left(g, s)` returns the first sorted end position that is at least `s`. Therefore, exactly the first `j` offers have end positions below `s` and are compatible candidates.

Although the binary search uses the full `g` list rather than passing `hi=i-1`, the result cannot include a later offer. The current offer's end is at least its start `s`, and sorted order ensures every later end is at least the current end. Thus every end below `s` lies before the current offer, and `j \le i-1`.

The take profit is `f[j] + v`. The recurrence

`f[i] = max(f[i - 1], f[j] + v)`

chooses the better of skip and take.

**Why `f[j]` can be combined safely.** Every offer represented in `f[j]` ends before `s` because it lies within the first `j` sorted offers. Those offers are mutually nonoverlapping by the DP's definition. Adding the current offer therefore preserves compatibility.

Conversely, if an optimal solution takes the current offer, every other accepted offer must end before `s` and hence belongs to that compatible prefix. Its prior profit cannot exceed `f[j]`. This proves the take branch captures the best solution containing the current offer.

**Inductive correctness.** The base prefix has profit zero. Assume all earlier `f` values are optimal. Any optimal selection among the first $i$ sorted offers either excludes offer $i$, bounded and achieved by `f[i-1]`, or includes it, bounded and achieved by `f[j]+v`. Taking their maximum therefore makes `f[i]` optimal. By induction, `f[-1]` is the maximum profit over every offer.

**House count `n` is not used.** The interval endpoints are already validated to lie within zero through $n-1$. Once that guarantee holds, profit depends only on interactions between offers, not on unoffered houses. The exact DP therefore never allocates a length-$n$ array.

**The exact algorithm differs from the manifest.** The manifest describes grouping offers by ending house and advancing a DP over all $n$ house prefixes in $O(n+m)$ time. This source sorts $m$ offers, binary-searches for each predecessor, and uses an offer-prefix DP. Its actual time is $O(m\log m)$ and its space is $O(m)$.

The offer-based version can be better when $n$ is much larger than the number of offers, while the grouped house DP avoids sorting when the bounded house range is convenient.

## Complexity detail

Let $m$ be `len(offers)`. Sorting takes $O(m\log m)$ time. Building `g` is $O(m)$. The loop performs one binary search over $m$ end positions for each offer, taking $O(m\log m)$ total. The overall time is $O(m\log m)$.

Arrays `f` and `g` each contain $O(m)$ values. Python's sort can use $O(m)$ temporary storage. Total auxiliary space is $O(m)$.

The manifest's $O(n+m)$ time and space refer to a different house-indexed DP. Parameter `n` does not appear in the exact computation after validation, so it should not be inserted into this source's complexity merely because it is part of the signature.

Profits may accumulate across many offers, but Python integers prevent overflow.

## Alternatives and edge cases

- **House-prefix grouped DP:** Group every offer by its end house. At each house position, carry forward the previous best and test offers ending there using the DP value before their start. This gives $O(n+m)$ time and $O(n+m)$ storage and matches the manifest.
- **Top-down memoization:** Sort offers by start, then recursively skip or take and binary-search the next compatible start. It has the same $O(m\log m)$ time but uses recursion.
- **Quadratic interval DP:** Scan all earlier offers for every current one. It is $O(m^2)$ and too slow at $10^5$ offers.
- **Inclusive endpoints:** Compatibility requires earlier end strictly less than current start; `bisect_left` enforces this.
- **Offers touching at a house:** Intervals ending and starting at the same index overlap and cannot both be accepted.
- **Identical intervals:** The recurrence can choose at most one; it naturally favors the greater profit through the maximum.
- **Equal end positions:** Their relative sort order does not affect correctness because each prefix recurrence can skip lower-profit choices and compatible predecessor search excludes ends at the current start.
- **Leave houses unsold:** The skip branch permits any gaps and rejects unprofitable combinations, although all individual profits are positive.
- **No compatible predecessor:** `j = 0` and taking the offer yields `v` alone.
- **Current offer dominated:** If `f[i-1]` is at least `f[j]+v`, the offer is skipped.
- **Input mutation:** Sorting changes offer order. Make a copy first if the caller needs original ordering.
- **Unused `n`:** This is intentional for offer-indexed weighted scheduling, not an omitted boundary check.
