## General

**Search the answer value instead of constructing every pair**

For `n` numbers there are `n(n - 1) / 2` index pairs. Building every absolute difference and sorting those differences would materialize a quadratic collection. The exact solution avoids that collection by binary-searching the distance value.

After sorting `nums`, the distance of a pair with earlier index `j` and later index `i` is simply `nums[i] - nums[j]`, because the later value is never smaller. Possible distances range from `0` through

`W = nums[-1] - nums[0]`.

The central question becomes: for a proposed distance `dist`, how many pairs have distance at most `dist`? If that count is at least `k`, then the kth-smallest distance is no greater than `dist`. If the count is less than `k`, the desired distance must be larger.

**How `count(dist)` counts qualifying pairs**

The helper considers every sorted position `i` as the right endpoint of a pair. Its value is stored as `b = nums[i]`. A prior value `nums[j]` forms a qualifying pair precisely when

`b - nums[j] <= dist`,

which is equivalent to

`nums[j] >= b - dist`.

The helper sets `a = b - dist` and calls `bisect_left(nums, a, 0, i)`. This returns the first index `j` in the already-sorted prefix `nums[0:i]` whose value is at least `a`. Therefore all prior indices from `j` through `i - 1` qualify, and there are exactly `i - j` of them.

Summing `i - j` across every right endpoint counts each unordered index pair exactly once. A pair is counted when its larger index is used as `i`, and it cannot be counted under any other right endpoint.

Duplicates are handled naturally. If `b` has earlier equal copies and `dist = 0`, the threshold is `b` itself. The left binary search locates the first equal copy, so all equal earlier values contribute zero-distance pairs.

**Why the counting function is monotone**

If a pair has distance at most `d`, it also has distance at most any larger value. Consequently, `count(d)` never decreases as `d` grows.

This monotonicity creates a boundary in the distance domain:

- Before the boundary, fewer than `k` pairs qualify.
- At the boundary and afterward, at least `k` pairs qualify.

The first distance at which the count reaches `k` is exactly the kth element of the sorted multiset of pair distances. “Multiset” matters because different index pairs with the same distance occupy separate ranks, and the helper counts them separately.

**What the outer `bisect_left` call means**

The return statement uses `bisect_left(range(W), k, key=count)`. With a key function, Python’s binary search applies `count` to candidate values from the range and finds the first position whose keyed value is at least `k`.

The range contains `0, 1, ..., W - 1`. Its indices equal its values, so the insertion position returned by `bisect_left` is itself the candidate distance.

At first glance, excluding `W` may look like an off-by-one error. It is not. If the kth distance is smaller than `W`, the search finds that value inside the range. If even `count(W - 1) < k`, every range element belongs before `k` under the key comparison, so the insertion position is `len(range(W)) = W`. That returned position is the omitted maximum distance, which is the correct answer.

If `W = 0`, every number is equal. The range is empty, and `bisect_left` returns insertion position `0`, again the correct distance.

**A small example**

For `nums = [1, 3, 1]`, sorting produces `[1, 1, 3]`. The pair-distance multiset is `[0, 2, 2]`.

For `dist = 0`:

- The first `1` has no prior partner.
- The second `1` finds the first `1` as its lower bound and contributes one pair.
- The `3` finds no prior value at least `3` in the prefix and contributes zero.

Thus `count(0) = 1`. For `dist = 1` the count is still one, while for `dist = 2` all three pairs qualify. If `k = 1`, the first count reaching one is distance zero. If `k = 2` or `3`, the first count reaching that rank is distance two.

**Why sorting is indispensable**

The threshold calculation only becomes useful because the prefix is ordered. Sorting guarantees both that `nums[i] - nums[j]` is nonnegative for `j < i` and that all values meeting `nums[j] >= b - dist` occupy one contiguous suffix of the prefix. Binary search can then locate the beginning of that suffix.

**Why the returned boundary is correct**

The helper exactly counts all pairs with distance no greater than its argument. The count is monotone, and the kth-smallest distance is precisely the least threshold containing at least `k` pairs. The outer binary search returns that least threshold, including the maximum-distance boundary case through its insertion position. Therefore the returned integer is exactly the kth-smallest pair distance.

## Complexity detail

Let `n` be the number of values and `W = max(nums) - min(nums)` after sorting.

Sorting costs `O(n log n)` time. One call to `count(dist)` loops over all `n` positions. For each position it performs `bisect_left` on a prefix, which costs `O(log n)` time. A complete count therefore costs `O(n log n)`.

The outer binary search needs `O(log(W + 1))` count evaluations. The exact implementation consequently takes

`O(n log n + n log n log(W + 1))`

time. This literal bound is important: the commonly cited `O(n log n + n log W)` bound assumes that each count is computed with a linear two-pointer window. The exact helper shown here performs a separate binary search for each right endpoint, so it has an additional `log n` factor.

Python’s in-place list sort may use `O(n)` temporary memory in the worst case. Apart from the sorting workspace, the helper stores only counters and scalar values, and `range(W)` is a lazy range object rather than a list of `W` integers. The auxiliary-space bound is therefore `O(n)` under Python’s sorting behavior, with `O(1)` explicit algorithmic state after sorting.

## Alternatives and edge cases

- **Two-pointer counting inside the answer search:** For each right endpoint, move one shared left pointer forward until the distance is at most the candidate. Both pointers move only forward, making one count `O(n)`. Combined with value binary search, this yields `O(n log n + n log(W + 1))` time and is the standard refinement that meets the tighter manifest-style bound.

- **Generate and sort every distance:** This is conceptually simple but creates `O(n^2)` distances and then spends `O(n^2 log n)` time sorting them. It becomes impractical as `n` grows.

- **Heap-based pair generation:** A heap can produce distances in increasing order from sorted data without storing all pairs at once. It can be useful when `k` is very small, but its indexing logic is more involved and its running time depends directly on `k`.

- **Binary-search the count boundary, not pair indices:** Searching positions in the original array cannot order all pair distances. The monotone object is the number of qualifying pairs as a function of a proposed distance.

- **Duplicate values:** Distances of zero may occur many times. Because pairs are defined by indices, every distinct pair of equal positions counts separately; the threshold helper does exactly that.

- **Maximum answer `W`:** The outer range excludes `W` as an element, but its insertion position can equal `W`. Returning that position deliberately handles the maximum-distance answer.

- **All values equal:** Then `W = 0`, the searched range is empty, and the result is zero. No special branch is needed.

- **Mutation of the input:** `nums.sort()` changes the caller-provided list order. This is harmless for the problem result, but it is observable if the surrounding program expected the original ordering to remain intact.

- **Large numeric spread:** The algorithm does not allocate memory proportional to `W` because `range` is lazy. The spread affects only the logarithmic number of outer probes.
