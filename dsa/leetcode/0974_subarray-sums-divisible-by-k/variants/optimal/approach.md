## General

**Replace subarray sums with differences of prefix sums**

Let prefix sum through index `j` be `P[j]`, with an empty prefix sum zero before the array.

Sum of subarray after earlier prefix `i` through `j` is `P[j] - P[i]`. This difference is divisible by `k` exactly when both prefix sums have the same remainder modulo `k`.

The algorithm counts earlier prefixes by remainder while scanning once.

**State variables**

`s` is current prefix remainder, not the full potentially large sum.

`cnt[r]` is the number of prefixes seen so far whose remainder is `r`.

`ans` is the number of qualifying nonempty subarrays found.

The Counter begins with `{0: 1}`. This represents the empty prefix before index zero.

**Why the empty prefix matters**

If a prefix from array start through current position is itself divisible by `k`, its remainder is zero.

Pairing it with the initial empty prefix creates that entire prefix as a valid subarray. Without initial zero count, all valid subarrays starting at index zero would be missed.

**Process one value**

For each `x`:

`s = (s + x) % k`.

This gives current prefix remainder. If `cnt[s] = c`, there are `c` earlier prefixes with the same remainder.

Each earlier prefix defines one distinct subarray ending at the current index whose sum is divisible by `k`. Therefore:

`ans += cnt[s]`.

Only afterward does `cnt[s] += 1` record the current prefix for future endpoints.

**Why update order prevents an empty subarray**

If current prefix were inserted before counting, it would match itself and add an empty subarray after the current position.

Counting earlier occurrences first ensures every chosen start prefix is strictly earlier than the current end prefix, so every counted subarray contains at least one element.


Write `P[j] = q1*k + r` and `P[i] = q2*k + r` when remainders match.

Their difference is `(q1 - q2)k`, divisible by `k`.

Conversely, if `P[j] - P[i]` is divisible by `k`, both values are congruent modulo `k` and therefore share a normalized remainder.

**Negative values**

Input elements may be negative. Python's `% k` for positive `k` produces a remainder from zero through `k - 1`.

Congruent positive and negative sums normalize to the same key, so the Counter logic remains correct without extra adjustment.

**Trace**

For `[4, 5, 0]` with `k = 5`:

- Initial remainder zero has count one.
- After four, remainder four has no prior match, then count four becomes one.
- After five, remainder remains four. One earlier match adds subarray `[5]`.
- After zero, remainder remains four. Two earlier matches add `[0]` and `[5, 0]`.

Continuing the full example similarly reaches seven.

**Why counts, not just seen remainders**

Several earlier prefixes can share one remainder, and each creates a different start position.

A set would reveal that at least one valid subarray exists but could not count all of them. Counter multiplicity is essential.


Before each element, Counter stores exactly all earlier prefix remainders. Equal-remainder equivalence proves `cnt[s]` is exactly the number of valid subarrays ending here.

Adding that count and then storing the current prefix preserves the invariant. Summing over every endpoint yields every qualifying subarray exactly once.

**Combinatorial view**

If one remainder occurs `c` times among prefixes, any pair of those prefix positions defines a divisible subarray. That class contributes `c(c - 1)/2`.

The online method computes the same total incrementally: successive occurrences add zero, one, two, and so on earlier matches.

**Why each subarray appears once**

A subarray has one unique prefix before its start and one at its end. It is counted exactly when the ending prefix is processed and paired with the earlier one.

No other endpoint iteration can represent that same start-end pair.

**Why full prefix sums are unnecessary**

Only congruence modulo `k` affects divisibility. Reducing after every addition preserves all future equal-remainder relationships while bounding `s` between zero and `k - 1`.

The actual sum may be negative or large without changing this logic.

## Complexity detail

Let `N` be array length.

Each element performs expected constant-time Counter operations, so time is `O(N)`. The editorial may write `O(N + K)` for an initialized remainder array; Counter initialization here is constant.

At most `k` different normalized remainders exist, so auxiliary space is `O(k)`, also bounded by `O(N)` prefixes encountered.

## Alternatives and edge cases

- **Check every subarray:** Prefix sums reduce sum lookup but still leave `O(N^2)` pairs.
- **Fixed array of `k` counts:** Avoid hash overhead and gives the same logic.
- **Set of remainders:** Cannot count multiple starts.
- **Single divisible element:** Matches an earlier equal remainder and is counted.
- **Zero element:** Preserves remainder and creates valid subarrays for every prior same remainder.
- **Negative numbers:** Python normalization keeps keys consistent.
- **Whole prefix divisible:** Initial zero entry counts it.
- **Update before query:** Would incorrectly count an empty subarray.
- **All prefix remainders equal:** Each new endpoint adds all earlier prefixes.
- **Nonempty requirement:** Enforced by count-before-increment order.
