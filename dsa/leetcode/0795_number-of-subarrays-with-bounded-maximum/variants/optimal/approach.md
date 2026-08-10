## General

**Replace a two-sided maximum condition with two prefix conditions**

A subarray is valid when:

$$
left \le \max(\text{subarray}) \le right.
$$

Directly maintaining the maximum of every possible subarray would be expensive. Instead, define `f(x)` as the number of nonempty contiguous subarrays whose every element is at most `x`. Equivalently, it counts subarrays whose maximum is at most `x`.

Then:

- `f(right)` counts subarrays with maximum no greater than `right`;
- `f(left - 1)` counts the subset whose maximum is strictly below `left`, because array values are integers.

Subtracting removes exactly the too-small maxima:

$$
\text{answer}=f(right)-f(left-1).
$$

Any subarray containing a value above `right` appears in neither count. Any maximum inside the inclusive interval appears only in the first. Any maximum below `left` appears in both and cancels.

**Count subarrays with maximum at most one threshold**

For a fixed threshold `x`, a subarray qualifies if and only if all its elements are at most `x`. Values greater than `x` act as barriers: no qualifying subarray may cross one.

Variable `t` stores the length of the current consecutive suffix consisting entirely of values at most `x`.

For each value `v`:

- if `v > x`, set `t = 0` because the current position breaks every qualifying suffix;
- otherwise increment `t`, extending every previous qualifying suffix and creating the one-element suffix `[v]`.

The exact assignment is:

`t = 0 if v > x else t + 1`.

**Why `t` is also the number of valid subarrays ending here**

Suppose the last `t` positions all contain values at most `x`. A subarray ending at the current position may start at any of those `t` positions, and every such choice stays entirely within the valid suffix.

Starting earlier would cross either the array boundary or the most recent value greater than `x`, so no additional valid ending subarray exists.

Therefore exactly `t` qualifying subarrays end at the current index. Adding `t` to `cnt` counts them.

Every nonempty subarray has exactly one ending index, so summing these per-index contributions counts each qualifying subarray once.

**Trace one threshold**

Use `nums = [2,1,4,3]` and threshold `x = 3`.

- At value two, `t = 1`. One valid subarray ends here: `[2]`.
- At value one, `t = 2`. The valid endings are `[1]` and `[2,1]`.
- At value four, `t = 0` because four exceeds the threshold.
- At value three, `t = 1`. Only `[3]` ends here without crossing four.

The sum is `1 + 2 + 0 + 1 = 4`. These are all subarrays with maximum at most three.

**Apply the lower threshold**

For the same array and `left = 2`, call `f(left - 1) = f(1)`.

Only the one-element subarray `[1]` has maximum at most one, so this count is one. The difference `4 - 1 = 3` leaves `[2]`, `[2,1]`, and `[3]`, exactly the subarrays whose maximum is between two and three.

**The suffix invariant**

After processing index `i` for threshold `x`:

- `t` is the length of the longest suffix ending at `i` whose values are all at most `x`;
- `cnt` is the number of qualifying subarrays whose ending index is at most `i`.

If `nums[i] > x`, no qualifying suffix can include it, so zero is correct. Otherwise the prior longest suffix extends by one and no longer suffix can be valid, establishing the new `t`.

Adding that new `t` adds exactly all qualifying subarrays ending at `i` while leaving earlier endings already counted. The invariant holds by induction.

**Why subtraction is exact**

Partition all subarrays into three disjoint categories by maximum:

1. maximum less than `left`;
2. maximum in `[left, right]`;
3. maximum greater than `right`.

`f(right)` counts categories one and two. `f(left - 1)` counts exactly category one. Their difference is category two.

No inclusion-exclusion complication remains because the “maximum at most” sets are nested: every subarray counted by the smaller threshold is also counted by the larger one.

**Why integer boundaries matter**

The values and bounds are integers. “Maximum less than `left`” is therefore identical to “maximum at most `left - 1`.”

Using `f(left)` instead would wrongly remove subarrays whose maximum equals the allowed lower endpoint. The minus one preserves the inclusive range.

**No overflow logic is needed in Python**

The statement guarantees the result fits a 32-bit integer. Python integers would grow safely even without that guarantee. Intermediate `f(right)` and `f(left-1)` count at most $\frac{n(n+1)}{2}$ subarrays and are handled directly.

## Complexity detail

Let $n$ be the length of `nums`. Helper `f` scans the array once in $O(n)$ time. It is called twice, so total time is $O(2n)=O(n)$.

Each scan stores only `cnt`, `t`, the threshold, and the current value. The input is not modified and no prefix array is built, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Single-pass last-valid-index method:** Track the most recent element above `right` and the most recent element inside the allowed range. It also reaches $O(n)$ time but has a less immediately reusable counting proof.

- **Monotonic deque for every ending index:** It can maintain window maxima, but here no fixed window length exists and threshold subtraction is simpler.

- **Enumerate all subarrays:** Updating a running maximum for each start still costs $O(n^2)$ time.

- **`left = 0`:** The second threshold is `-1`. Since values are nonnegative, `f(-1)=0`, which is correct.

- **Element above `right`:** It resets both relevant suffix counts and separates independent segments.

- **Element below `left`:** It extends `f(right)` and `f(left-1)` equally unless joined with an allowed-range maximum, so subtraction handles it naturally.

- **Element equal to a boundary:** Equality is included because `f` accepts `v <= x`.

- **All values too small:** Both helper counts are equal and the result is zero.

- **All values in range:** Every nonempty subarray is valid, producing $\frac{n(n+1)}{2}$.
