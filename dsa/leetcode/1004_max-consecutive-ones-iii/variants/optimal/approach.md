## General

**Reframe flips as a zero budget inside a subarray**

Any chosen consecutive segment can be turned entirely into ones if and only if it contains at most `k` zeros. Ones already need no work, and each zero consumes one permitted flip.

The task is therefore:

> find the maximum length of a contiguous window containing at most `k` zeros.

A sliding window works because extending the right side can only keep or increase the zero count, while removing values from the left can only keep or decrease it.

**Count zeros with a bit expression**

For a binary value `x`:

- `0 ^ 1 = 1`;
- `1 ^ 1 = 0`.

Thus `x ^ 1` is an indicator that contributes one exactly when `x` is zero. The update

`cnt += x ^ 1`

adds the new rightmost element's zero contribution without an explicit branch.

Variable `l` is the current left boundary, while the for-loop advances the implicit right boundary one position per iteration.

**The exact implementation uses a non-shrinking window**

A conventional sliding window would use a `while cnt > k` loop to restore validity fully and would record a separate maximum length.

This solution uses only:

`if cnt > k:`

and moves `l` forward exactly one position when the zero budget is exceeded. This means the represented suffix can temporarily remain invalid after the shift. That is intentional.

The key idea is that the maintained window length never decreases:

- If adding `x` does not exceed the budget, `l` stays fixed while the right endpoint advances, so the window grows by one.
- If the budget is exceeded, the right endpoint advances by one and `l` also advances by one, so the window length stays unchanged.

The algorithm lets the current span grow only when that longer span is valid. During invalid periods, it slides a fixed-length span rightward until enough old zeros leave.

**Update the zero count when the left edge leaves**

When `cnt > k`, the code executes:

`cnt -= nums[l] ^ 1`

before incrementing `l`. If the departing value is zero, its contribution is removed; if it is one, the count stays unchanged.

If a one leaves, `cnt` may remain above `k`. On later iterations, the same fixed window length continues sliding. It cannot grow while `cnt > k` because each such iteration also advances `l`.

Eventually, either a zero leaves and restores validity or the scan ends. No invalid longer window is ever accepted as a new maximum.

**Why no explicit maximum variable is needed**

Let the current maintained length after processing right endpoint `r` be `r - l + 1`.

This length increases only on an iteration where the newly extended window has at most `k` zeros. Therefore, every increase establishes a real valid window of the new length.

When the current suffix is invalid, its length remains equal to the best valid length reached earlier; it does not increase. The method is remembering the best length through the size of its non-shrinking span rather than through a separate `ans` variable.

After the final element, `r = len(nums) - 1`, so the maintained length is

`len(nums) - l`,

which is exactly what the method returns.

**Trace a temporarily invalid window**

Suppose the current best valid length is five. A new zero makes `cnt = k + 1`. The algorithm adds that element on the right and removes one element on the left, keeping length five.

If the removed element is a one, the span still has too many zeros. On the next input element, the algorithm again moves both boundaries, still keeping length five. Once an old zero leaves, the span becomes valid again. A later extension may then grow to six and establish a new best.

A standard implementation would shrink several times immediately; this implementation distributes those left shifts across later right iterations. Both preserve the same maximum.

**Trace the role of `k = 0`**

With no flips allowed, every zero makes `cnt > 0`. The left pointer advances on every iteration during which the maintained span still contains a zero. The span can grow only while it consists entirely of ones.

The returned length is therefore the longest original run of consecutive ones, with no special-case code.

**Why the returned length is optimal**

Every time the maintained length grows, the window is valid, so the returned maximum-sized length is achievable.

Now consider any valid window ending at the current or an earlier position. The non-shrinking algorithm never reduces its remembered length; on invalid extensions it shifts rather than shrinks. If a longer valid window becomes possible, an iteration with `cnt <= k` leaves `l` in place and increases the remembered length.

Thus no valid length larger than the maintained span can pass unnoticed. At the end, `len(nums) - l` is both achievable at some earlier or current window and at least as large as every valid window length, proving optimality.

**No array values are actually flipped**

The problem asks for the maximum possible length, not the modified array. Counting zeros is enough to know how many flips a window would require. The method leaves `nums` unchanged and never chooses specific mutation operations.

## Complexity detail

Let `N` be the array length.

The for-loop reads every value once. Pointer `l` advances at most once per iteration and never moves backward. Every operation is constant time, so total time is `O(N)`.

Only `l`, `cnt`, the current value, and loop state are stored. Auxiliary space is `O(1)`.

Any solution must inspect the input in the worst case, so the linear time bound is asymptotically optimal.

## Alternatives and edge cases

- **Standard valid-window form:** Use `while zero_count > k` to restore validity fully and update `ans = max(ans, right - left + 1)`. It is easier to recognize but uses an extra result variable.
- **Prefix sums plus binary search:** A zero prefix sum can test any window, and each start can binary-search its longest valid end. This costs `O(N \log N)` rather than linear time.
- **Store zero positions:** Keep indices of zeros in a queue and move the left boundary past the oldest when more than `k` occur. It is also linear but uses up to `O(k)` space.
- **All ones:** `cnt` stays zero, `l` remains zero, and the full length is returned.
- **All zeros:** The answer is `min(k, N)`; the window grows until the budget is full and then slides without growing.
- **`k = 0`:** The method finds the longest existing run of ones.
- **`k >= number of zeros`:** No shift is needed and the entire array is valid.
- **Temporary invalidity:** It is safe only because window length is prevented from increasing while over budget. A conventional algorithm that records the current window each time would need full shrinking.
- **Binary-input requirement:** The `x ^ 1` indicator relies on `x` being exactly zero or one.
- **Input preservation:** Flips are conceptual; the array is never modified.
