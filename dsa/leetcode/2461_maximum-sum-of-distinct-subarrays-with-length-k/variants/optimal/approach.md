## General

**Maintain exactly one length-$k$ window**

Neighboring length-$k$ subarrays overlap in $k-1$ positions. Recomputing each sum and distinctness check from scratch would repeat almost all work. A sliding window updates only the value entering and the value leaving.

The map `cnt` stores frequencies inside the current window, and `s` stores its sum. The first window is `nums[:k]`. If `len(cnt) == k`, all $k$ values are distinct and `ans` starts at its sum; otherwise `ans` starts at zero, matching the required fallback.

**Why dictionary size tests distinctness**

A window contains exactly $k$ elements. Its frequency map has one key per distinct value. Therefore it contains all distinct elements if and only if the number of keys is $k$.

Keys whose frequency falls to zero must be removed. Leaving a zero-count key in `cnt` would make `len(cnt)` overstate the number of values currently present.

**Slide one position**

For new right index `i`, `nums[i]` enters and `nums[i-k]` leaves:

- Increment the entering value's frequency.
- Decrement the leaving value's frequency.
- Remove the leaving key if its count becomes zero.
- Update the sum by adding the entrant and subtracting the departure.

After these operations, `cnt` and `s` describe exactly `nums[i-k+1:i+1]`.

If the map has $k$ keys, the window qualifies and `ans=max(ans,s)` retains the greatest qualifying sum seen so far. Positive input values mean every valid sum is positive, so zero remains an unambiguous sentinel when no window qualifies.

The update order remains correct even when the entering and leaving values are identical. The code increments that key and then decrements it, leaving the same positive frequency. The zero-removal condition does not fire, and adding then subtracting the same numeric value leaves `s` unchanged. This is exactly right because the window's multiset has not changed even though its positions shifted.

**Trace the example**

For `nums=[1,5,4,2,9,9,9]` and $k=3$, the first window has keys 1, 5, and 4 with sum 10. Sliding produces:

- `[5,4,2]` with sum 11 and three keys;
- `[4,2,9]` with sum 15 and three keys;
- `[2,9,9]` with only two keys, so it is ignored;
- `[9,9,9]` with one key, also ignored.

The maximum remains 15.

**What remains true for every sliding window**

Before evaluating each window, `s` equals the sum of its $k$ elements and `cnt[x]` equals the number of occurrences of `x` in it, with no zero-frequency keys. Initialization establishes this for the first window, and the entering/leaving updates preserve it for the next.

The key-count test is therefore equivalent to the distinctness requirement. Every length-$k$ subarray appears once as the window, so taking the maximum of precisely the qualifying sums returns the requested result. If none qualifies, no update replaces the initialized zero.

There are exactly `len(nums)-k+1` windows. Initialization evaluates the one ending at index `k-1`. Each later loop index `i` evaluates the unique window ending at `i`. Thus no window is skipped between the initial slice and the sliding loop, and no endpoint is processed twice.

**Initial slicing details**

The exact source calls `nums[:k]` twice, once for `Counter` and once for `sum`. Each call creates a temporary list of $k$ references. This is still $O(k)$ space and linear initialization time, though a single saved slice or direct loop could avoid duplicate copying.

## Complexity detail

Initialization costs $O(k)$. The sliding loop performs $n-k$ expected constant-time hash-map updates, removals, and arithmetic operations. Total expected time is $O(n)$.

The frequency map contains at most $k$ keys. Initial slices contain $k$ references temporarily, and the scalar state is constant. Peak auxiliary space is $O(k)$.

The sum can reach $k\cdot10^5$, at most $10^{10}$, so fixed-width implementations should use 64-bit arithmetic. Python integers handle it.

## Alternatives and edge cases

- **Last-seen indices:** Track the most recent position of each value and a duplicate-free left boundary. Because the required length is fixed, a frequency map is more direct.
- **Rebuild a set per window:** This costs $O(k)$ for each of $O(n)$ windows, leading to $O(nk)$ time.
- **Sorted multiset:** It can detect duplicates but adds $O(\log k)$ updates without helping the sum calculation.
- **$k=1$:** Every one-element window is distinct, so the answer is the maximum array value.
- **$k=n$:** Only the full array is tested.
- **All values equal with $k>1$:** No window has $k$ keys and zero is returned.
- **Leaving value equals entering value:** Increment and decrement cancel in frequency, and the sum remains correct.
- **Zero-count removal:** It is necessary for dictionary size to equal the number of currently distinct values.
- **Positive values:** They make zero a safe no-solution result even though zero is also an arithmetic sum sentinel.
- **Input preservation:** Slices and counters are new objects; `nums` is never modified.
