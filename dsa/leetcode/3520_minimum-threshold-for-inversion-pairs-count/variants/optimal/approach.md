## General

**Turn the requested minimum into a monotone decision problem**

For a fixed threshold `x`, define `C(x)` as the number of pairs `(i,j)` satisfying:

- `i < j`;
- `nums[i] > nums[j]`;
- `nums[i] - nums[j] <= x`.

If a pair qualifies for threshold `x`, it also qualifies for every larger threshold because its difference does not change. Therefore `C(x)` is non-decreasing as `x` grows.

The question asks for the smallest integer `x` with `C(x) >= k`. This is exactly a first-true binary search, provided the algorithm can evaluate `C(x)` efficiently.

All inversion differences are positive integers because `nums[i] > nums[j]`. Thus, if an answer exists, it is at least one. The largest possible difference between any two array values is:

`R = max(nums) - min(nums)`.

At threshold `R`, every inversion pair satisfies the difference condition. If fewer than `k` pairs exist even then, no threshold can work and the source returns `-1`.

**Count qualifying inversions by scanning right endpoints**

Fix a threshold `x` and scan `nums` from left to right. When the current value `v = nums[j]` is processed, every value already inserted into the data structure comes from an index `i < j`. The index-order condition is therefore automatic.

For the earlier value `u = nums[i]` to form a qualifying pair with `v`, it must satisfy:

`u > v`

and

`u - v <= x`, equivalently `u <= v + x`.

Together, the desired earlier values lie in the half-open/closed numerical interval:

`v < u <= v + x`.

So the checker needs a dynamic multiset of earlier values that can answer how many lie in this interval.

**Coordinate-compress the values**

Array values may reach `10^9`, so a frequency array indexed directly by value would be wasteful. The source builds:

`values = sorted(set(nums))`.

Each distinct input value now has a dense rank from zero through `size - 1`. A Fenwick tree stores how many already-scanned occurrences have each rank. Duplicate array values share a rank, and their frequency accumulates in the same Fenwick position.

Compression is valid because the checker uses only value order and inclusive boundaries, both preserved by sorted ranks.

**Translate interval boundaries with binary search**

`bisect_right(values, bound)` returns the number of distinct compressed values less than or equal to `bound`. The Fenwick helper `prefix_sum(t)` returns the number of inserted occurrences whose one-based rank is at most `t`. Passing the bisect result directly therefore counts earlier values at most the bound.

For current `v`, the source adds:

`prefix_sum(bisect_right(values, v + x)) - prefix_sum(bisect_right(values, v))`.

The first prefix counts earlier values `u <= v + x`. The second removes all `u <= v`. Their difference counts exactly `v < u <= v + x`.

Using `bisect_right(values, v)` rather than a boundary below `v` is essential: equal values are not inversions and must be excluded.

After counting pairs ending at the current index, the source inserts `v`. `bisect_left(values, v) + 1` gives its one-based Fenwick rank. Inserting afterward, rather than before the query, prevents the current index from pairing with itself and maintains the “earlier indices only” invariant.

**Fenwick tree operations**

The local `tree` begins with zeros on every call to `count_pairs`. A prefix query repeatedly removes the lowest set bit from its index, accumulating counts for disjoint rank ranges. An insertion repeatedly adds the lowest set bit, updating every Fenwick node whose range contains that rank.

Both operations take logarithmic time in the number of distinct values. The tree stores occurrence counts rather than booleans, so repeated earlier values contribute separately, as required for distinct index pairs.

The checker returns early once `pairs >= k`. Binary search needs only the truth of this comparison, not an exact count above `k`. This can save substantial work for large thresholds while preserving the decision result.

**Establish that an answer exists before searching**

The source first evaluates `count_pairs(R)`. Every inversion difference is at most `max(nums)-min(nums)=R`, so this count equals the total number of ordinary inversions.

If it is below `k`, increasing the threshold cannot introduce any new pair: all possible value differences are already allowed. Returning `-1` is therefore correct.

If at least `k` inversions exist, an answer lies in `[1,R]`. Notice that `R` must then be at least one; when all values are equal, there are no inversions and the impossibility check returns before binary search begins.

**Binary-search the first sufficient threshold**

The loop maintains the invariant that some sufficient threshold exists at or below `high`, while every threshold below `low` is insufficient.

At `middle = (low + high) // 2`:

- if `count_pairs(middle) >= k`, `middle` is sufficient, but a smaller answer may exist, so set `high = middle`;
- otherwise `middle` and every smaller threshold are insufficient by monotonicity, so set `low = middle + 1`.

When `low == high`, the interval contains one value. The invariant makes it sufficient and excludes every smaller value, so the source returns the minimum threshold.

**Why the count checker is exact**

Consider any qualifying pair `(i,j)`. When the scan reaches `j`, occurrence `nums[i]` has already been inserted. Its value lies in `(nums[j], nums[j]+x]`, so the prefix difference counts it once. Conversely, every occurrence counted by that difference was inserted by an earlier index and satisfies both strict inversion and threshold inequalities, so it represents a valid pair.

Each pair has one unique right endpoint and is considered during exactly that iteration. Thus `count_pairs(x)` is exact until an allowed early return at `k`, and its boolean result is always exact. Combined with monotonic binary search, this proves the returned threshold or `-1` result.

## Complexity detail

Let `n = len(nums)`, `m` be the number of distinct values, and `R = max(nums)-min(nums)`. Sorting the distinct values costs `O(n \log n)` time in the worst case and uses `O(n)` space.

One `count_pairs` call allocates a Fenwick array of `m + 1` entries. For each of at most `n` scanned values, it performs two binary searches, two Fenwick prefix queries, and one Fenwick update. Each costs `O(\log m)`, so a full check is `O(n \log m)` time and `O(m)` temporary space.

The existence check uses one call. Binary search performs `O(\log R)` further calls when `R > 0`. Total time is:

`O(n \log n + n \log m \log R)`,

which simplifies to the manifest bound `O(n \log n \log R)`. More commonly it is written `O(n \log n \log R)` with preprocessing absorbed. Early termination can improve practical time but not the worst-case bound.

The compressed values and Fenwick tree use `O(n)` auxiliary space. A new tree is created for each checker call, but calls are sequential, so their memory is reused rather than multiplied by `\log R`.

## Alternatives and edge cases

- **Enumerate all index pairs:** Computing every inversion difference and sorting it would make the answer the `k`-th smallest difference, but `O(n^2)` pairs are too many for `n = 10^4`.
- **Merge-sort inversion counting alone:** It counts all inversions efficiently but does not directly restrict their value differences to at most a trial threshold. The Fenwick interval query handles both conditions.
- **Balanced ordered multiset:** An order-statistics tree could count earlier values in the required range without coordinate compression. Python lacks one in the standard library, while a compressed Fenwick tree is direct.
- **Binary search the list of distinct observed differences:** Constructing that list itself may require quadratic work. Searching the numeric range costs only `O(log R)` checks.
- **Insert before querying:** That would include the current occurrence in prefix counts. Although equality subtraction happens to remove it here, maintaining the earlier-only invariant by querying first is clearer and robust.
- **Use values greater than or equal to v:** Equal values are not inversions. The lower prefix through `v` must be subtracted.
- **Threshold zero:** Strict integer inversions have difference at least one, so no pair qualifies. Since `k >= 1`, a valid answer never needs zero.
- **No inversions:** The maximum-threshold check returns fewer than `k` and the result is `-1`.
- **k exceeds total inversions:** The same existence check detects this even though `k` may be much larger than `n(n-1)/2`.
- **All values equal:** `R = 0`, but the source returns `-1` before initializing `low = 1` can create an invalid search interval.
- **Duplicate values:** Fenwick frequencies count occurrences separately, while the strict lower boundary prevents equal-valued pairs from being counted.
- **Negative delta is irrelevant:** Input values are positive and threshold is searched as a nonnegative difference; only relative ordering matters.
- **Very large values:** Compression prevents space from depending on `10^9`, and Python safely computes `v + threshold`.
- **Early checker return:** Returning any count at least `k` is sufficient because callers ask only whether the threshold passes.
- **Minimum boundary:** The lower-bound binary search keeps a sufficient `high` and finishes at the first sufficient integer, not merely any working threshold.
