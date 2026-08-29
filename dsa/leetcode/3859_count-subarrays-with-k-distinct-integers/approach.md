## General

**Separate “exactly” with a difference of two monotone counts**

For a subarray, let `D` be its number of distinct values and let `Q` be the number of those values whose frequency is at least `m`. The desired subarrays satisfy

$$
D=k\quad\text{and}\quad Q=k.
$$

The equality `Q=k` then means every one of the `k` distinct values meets the threshold.

Counting this exact condition directly with one sliding window is difficult. When the left endpoint moves, a value may disappear completely or merely fall below frequency `m`, and there can be several categories of invalid windows. The source defines a helper `f(lim)` that counts the monotone condition

$$
D\ge\texttt{lim}\quad\text{and}\quad Q\ge k.
$$

It returns

`f(k) - f(k + 1)`.

Every subarray counted by `f(k+1)` is also counted by `f(k)`. Their difference contains subarrays with `D\ge k` and `Q\ge k` but not `D\ge k+1`. Therefore `D=k`. Since `Q` cannot exceed `D`, `Q\ge k` becomes `Q=k`. This is exactly the original requirement.

**Maintain both distinct and qualified counts**

Inside `f`, `cnt[x]` is the frequency of `x` in the active window `nums[l:right+1]`. The number of keys in the counter, `len(cnt)`, is `D`.

The scalar `t` stores `Q`, the number of values whose current frequency is at least `m`. When the right endpoint adds `x`, its count rises by one. Only the transition from `m-1` to `m` changes whether it is qualified, so the source increments `t` exactly when `cnt[x] == m`.

When the left endpoint removes `y`, its count falls by one. Only the transition from `m` to `m-1` loses qualification, so the source decrements `t` exactly when the new count equals `m-1`. If the count reaches zero, it removes the key from `cnt` so that `len(cnt)` remains the exact distinct-value count.

Counts above `m` do not repeatedly change `t`. A value occurring `m+3` times is still one qualified distinct value, not four.

**Why the shrinking loop counts starts**

For a fixed right endpoint, consider the property

$$
\lvert\texttt{cnt}\rvert\ge\texttt{lim}
\quad\text{and}\quad
t\ge k.
$$

If a window has this property, extending it to the left can only add occurrences and possibly add distinct values. Neither `D` nor `Q` can decrease, so every earlier starting position also has the property. Conversely, once repeatedly removing left elements makes the property false, removing still more elements cannot restore it.

The helper exploits this monotonicity. While the active window satisfies the property, it removes `nums[l]` and increments `l`. When the loop stops, `[l,right]` is the first failing window. Exactly the starts

$$
0,1,\ldots,l-1
$$

produce valid windows ending at this right endpoint. There are `l` such starts, so `ans += l`.

The pointer never moves backward. When a new right element is appended, previously removed prefixes remain valid starts if the enlarged window satisfies the property, and the loop may discover additional valid starts. This standard “shrink past validity” form differs from windows that preserve validity inside the active interval: here the active interval is deliberately left at the first invalid start so that its index directly equals the number of valid starts.

**State invariant for one helper pass**

After processing a right endpoint and completing the while loop:

- `cnt` contains exactly the frequencies in `nums[l:right+1]`;
- `t` equals the number of counter values at least `m`;
- the active window fails `D\ge lim` and `Q\ge k`;
- every start smaller than `l` forms a window ending at `right` that satisfies the property; and
- `ans` contains the total number of satisfying subarrays ending at or before `right`.

Adding the next element updates the exact frequencies and may make the active window valid again. Each loop removal preserves the first two statements, and monotonicity establishes the next two. Adding `l` accounts for precisely the new right endpoint. Induction proves that `f(lim)` returns the intended count.

**Walk through the first example**

For `nums=[1,2,1,2,2]`, `k=2`, and `m=2`, `f(2)` begins recognizing windows only after both one and two have frequency at least two. At right endpoint three, window `[0,3]` qualifies. Removing its first one makes that value occur only once, so `t` falls and the loop stops at `l=1`. Exactly one start, zero, works for that right endpoint.

At right endpoint four, the extra two restores or preserves enough frequency for the appropriate shrink behavior, and another qualifying start is counted. `f(3)` counts no window here because the array has only two distinct values. The difference is two, matching the example.

When `m=1`, every present distinct value is automatically qualified, so `t=len(cnt)`. The helper difference reduces to the familiar exact-`k`-distinct sliding-window idea, while the same code continues to support higher frequency thresholds.

**What the subtraction removes**

A subarray can have at least `k` values meeting the threshold while also containing extra distinct values that occur fewer than `m` times. Such a window is counted by `f(k)` even though it is not a valid answer. It also has at least `k+1` distinct values and is counted by `f(k+1)`, so subtraction removes it.

A subarray with more than `k` qualified values is likewise counted by both helpers because it necessarily has more than `k` distinct values. A subarray with exactly `k` distinct values but even one underqualified value has `Q<k` and is counted by neither. Only the target category remains.

## Complexity detail

In one call to `f`, every element enters the counter once as the right endpoint advances. The left pointer removes each array position at most once. Expected constant-time `Counter` operations make each helper `O(N)` time. Calling it for `k` and `k+1` doubles only the constant, so total time is `O(N)`, matching the manifest.

The exact source does not generally use `O(K)` space. The counter holds every distinct value in the current active window, including values whose frequency is below `m`. If `m>1` and the array contains many unique values, `t` stays zero, the while loop never shrinks, and the counter grows to `N` keys even when `k` is small. Thus peak auxiliary space is `O(U)`, where `U` is the number of distinct values in `nums`, and `O(N)` in the worst case. The value bound also gives `O(\min(N,10^5))`. The manifest's `O(K)` space is accurate for special cases such as `m=1`, when shrinking bounds the active distinct count, but not for the general protected source.

The answer can be as large as `N(N+1)/2`. Python integers store it safely; fixed-width implementations should use a 64-bit result.

## Alternatives and edge cases

- **Enumerate all subarrays:** Extending every start and recounting frequencies takes at least `O(N^2)` time. The two monotone helper passes reuse frequency information and move each endpoint only forward.
- **Use only an exact-distinct window:** Knowing there are exactly `k` keys does not ensure every count is at least `m`. The qualified counter `t` is a separate required dimension.
- **Traditional `atMost(k)-atMost(k-1)`:** That identity handles exact distinct count, but the “every present value has frequency at least `m`” condition is not monotone under ordinary at-most windows. The source instead subtracts two at-least conditions that share `Q\ge k`.
- **Recompute qualified values by scanning the counter:** This can add `O(U)` work per endpoint. Updating `t` only at threshold crossings keeps each window move constant time.
- **Increment `t` whenever a count exceeds `m`:** This would count occurrences rather than qualified distinct values. Increment only when the count becomes exactly `m`.
- **Forget to remove zero-count keys:** Then `len(cnt)` would include absent values and corrupt the distinct count. The source pops a key as soon as its frequency reaches zero.
- **`m=1`:** Every present value qualifies at its first occurrence, and it loses qualification when removed to zero. The threshold-update conditions still work because `m-1=0`.
- **`k=1`:** Count constant-value subarrays in which that one value occurs at least `m` times. Extra singleton or low-frequency values are removed correctly by the `f(2)` subtraction.
- **Impossible length:** Any answer subarray needs at least `k\cdot m` elements. If this exceeds `N`, the result is zero. The source discovers this naturally without an early check.
- **Many low-frequency distinct values:** They demonstrate why space may reach `O(N)`. They remain in `cnt` even though they do not contribute to `t`.
- **Large multiplicities:** Counts above `m` remain qualified until removals lower them to `m-1`. No special handling is needed.
- **Counter dependency:** The exact solution requires `collections.Counter` to be available in its execution environment.
