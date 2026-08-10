## General

**Sorting exposes safe decisions at both extremes**

The method first executes `nums.sort()`, arranging values in nondecreasing order. It then places `l` at the smallest remaining value and `r` at the largest. Every unused candidate lies between them.

At each step, the sum `s = nums[l] + nums[r]` determines whether an endpoint can participate in any valid remaining pair. This lets the algorithm either form a pair or permanently discard one impossible endpoint.

**When the sum is exactly `k`**

If `s == k`, the two endpoint values form a legal operation. The source increments `ans` and moves both pointers inward, consuming each element exactly once.

Using this pair is safe. The smallest value needs a complement equal to `k - nums[l]`, and the largest endpoint has exactly that value. Pairing them cannot deprive some other value of a uniquely better match: values are interchangeable by numeric value, and removing one valid pair leaves the same pairing problem on the middle multiset. Thus an optimal solution exists that includes this endpoint pair.

**When the sum is too small**

If `s < k`, even pairing `nums[l]` with the largest remaining value is insufficient. Every other possible partner is at most `nums[r]`, so

$$
\texttt{nums[l]} + \text{any remaining partner} < k.
$$

The left endpoint can never belong to a valid pair. Incrementing `l` discards it without reducing the maximum achievable operation count.

Moving `r` instead would be unjustified: the largest value might pair successfully with a larger left-side value.

**When the sum is too large**

If `s > k`, even pairing `nums[r]` with the smallest remaining value is excessive. Every other possible partner is at least `nums[l]`, so all sums involving the right endpoint are greater than `k`. Decrementing `r` safely discards that largest value.

Moving `l` would only increase the partner and make the sum still larger.

**A trace**

For `nums = [1, 2, 3, 4]` and `k = 5`, sorting leaves the order unchanged. The first endpoints sum to five, so `1` and `4` form one operation. The remaining endpoints `2` and `3` also sum to five, producing two operations total.

For `[3, 1, 3, 4, 3]` with `k = 6`, sorting gives `[1, 3, 3, 3, 4]`. Endpoints one and four sum to five, so one is discarded. The next endpoints three and four sum to seven, so four is discarded. Two threes then form one pair, leaving one unpaired three.

**Why the greedy pointer walk is optimal**

Consider the current sorted interval. If its endpoint sum is below `k`, the smallest endpoint is provably unusable; if above, the largest is provably unusable. Removing an unusable value cannot change the optimum.

If the sum equals `k`, one operation is immediately achievable with the endpoints. After removing them, any collection of disjoint valid pairs in the middle can be added. Conversely, no solution can use either endpoint more than once, and pairing these matching extremes is at least as good as leaving them unused or pairing equal-valued substitutes. The optimum is therefore one plus the optimum of the middle interval.

Each loop step applies one of these optimality-preserving reductions. When pointers meet or cross, fewer than two unused elements remain and no operation is possible. `ans` is consequently the maximum number of disjoint sum-`k` pairs.

**Element identity versus value**

Sorting changes positions, but the problem does not ask for original indices or operation order. Elements with equal values are interchangeable. The only constraints are their values and one-use rule, both preserved by sorting and pointer consumption.

## Complexity detail

Let `n` be the length of `nums`. Python’s in-place list sort takes $O(n\log n)$ time in the worst case. The two-pointer loop moves at least one pointer on every iteration, so it performs at most `n - 1` iterations and costs $O(n)$ time. Total time is $O(n\log n)$.

The exact implementation therefore does not match the manifest’s $O(n)$ time, which would describe the single-pass hash-count approach. Python’s Timsort can use $O(n)$ temporary memory in the worst case, while the pointer variables themselves use $O(1)$. The exact auxiliary-space bound is thus $O(n)$ worst case.

`nums.sort()` mutates the caller’s list. No separate sorted copy is created.

## Alternatives and edge cases

- **Single-pass frequency map:** For each value, consume one previously seen complement if available; otherwise store the value. This gives expected $O(n)$ time and $O(n)$ space and matches the manifest.
- **Two-pass counter:** Count every value, then consume counts for complements carefully, especially when `value == k-value`. It is also expected linear time but can be easier to double-count incorrectly.
- **Brute-force pairing:** Trying every pair and marking used elements takes $O(n^2)$ time.
- **`l == r`:** One remaining element cannot pair with itself because an operation requires two array elements, so the strict loop condition stops.
- **Duplicate complements:** Each successful equality moves both pointers, consuming exactly one copy from each side.
- **Self-complement value `k/2`:** Pairs are formed from two distinct occurrences as pointers converge; an odd leftover occurrence remains unused.
- **All sums too small:** The left pointer repeatedly advances because each current smallest value is impossible even with the maximum.
- **All sums too large:** The right pointer repeatedly retreats because each current maximum is impossible even with the minimum.
- **Values greater than `k`:** Since inputs are positive, such a value cannot have a positive complement and will be discarded from the right.
- **No valid pair:** `ans` remains zero.
- **Input mutation:** If preserving the original order matters to a caller, use `sorted(nums)` instead, at the cost of an explicit $O(n)$ copy.
- **Sorting-space nuance:** Calling the algorithm “constant space” based only on `l`, `r`, and `ans` ignores the language runtime’s sorting workspace.
