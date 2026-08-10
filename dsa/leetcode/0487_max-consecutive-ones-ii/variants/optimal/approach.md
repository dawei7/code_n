## General

Flipping at most one zero is equivalent to selecting the longest contiguous subarray containing at most one zero. Every one in that subarray already has the desired value, and its single zero, if present, can be flipped. The solution uses a sliding window, but it applies a compact “non-shrinking” form that differs subtly from the more familiar loop that always contracts until the window is valid.

`l` is the left boundary of the maintained candidate window. The `for` loop supplies the right boundary implicitly by processing one new value at a time. `cnt` counts zeros in the current window. Because every array value is binary, `x ^ 1` converts the value into a zero indicator:

- if `x == 0`, then `0 ^ 1 == 1`;
- if `x == 1`, then `1 ^ 1 == 0`.

Thus `cnt += x ^ 1` increments exactly when the new rightmost value is zero.

**Grow only when growth can produce a new record.** If the new window has at most one zero, it is valid and `l` stays fixed. Since the right boundary moved one step while the left boundary did not, the window length grows by one. That longer valid window becomes the new best length automatically.

If `cnt > 1`, the newly extended window is invalid. The code removes the old leftmost value from the zero count with `cnt -= nums[l] ^ 1` and advances `l` by one. The right boundary also just advanced by one, so the candidate window's length does not grow. This is the central optimization: an invalid attempted extension cannot establish a larger valid answer, so the algorithm preserves the previous record length instead of shrinking repeatedly and storing a separate maximum.

The window may still contain more than one zero after moving `l` once. That is intentional. Suppose the departing value was a one; `cnt` remains too large. On the next iteration, the right side advances and the left side advances again because the window is still invalid. Its length remains unchanged while the left boundary moves toward the older zero. Once enough old elements leave for `cnt <= 1`, the candidate is valid again and can resume growing.

This creates a useful invariant after every processed position:

- the maintained window length equals the largest valid length discovered so far;
- if the maintained window is currently valid, it is a valid witness of that length;
- if it is temporarily invalid, its length is still the previous best, and the algorithm will not increase that length until validity is restored.

The third point explains why an invalid final window is not a problem. Its length was first achieved earlier by a valid window. Invalid iterations only slide a window of that established length; they never increase the claimed answer.

For `nums = [1, 0, 1, 1, 0]`, the first four values contain one zero, so the candidate grows to length four. Adding the last zero makes `cnt = 2`. The code removes the contribution of the old leftmost `1`, which leaves `cnt` at two, and increments `l`. The final maintained window is still temporarily invalid, but its length remains four—the valid record already achieved by `[1, 0, 1, 1]`. Returning four is correct.

Consider a longer continuation such as `[1, 0, 1, 1, 0, 1, 1]`. After the second zero arrives, successive iterations slide the fixed-size candidate until the first zero exits. At that point the window again contains only one zero. A later one can then let it grow if a longer valid segment exists. No possible record is skipped: before a length can increase, the corresponding expanded window must be valid.

**Why the final expression is `len(nums) - l`.** After all `n` values have been processed, the implicit right boundary is `n - 1`. The maintained window length is

`(n - 1) - l + 1 = n - l`.

By the invariant, that length equals the maximum valid window length seen anywhere. The solution therefore needs neither an explicit right index nor an `ans` variable.

The flip is optional. An all-one window has zero zeros and is valid, so arrays with no zeros return their full length. An all-zero array can keep at most one element in a valid window; the non-shrinking mechanism establishes length one on the first value and slides that record across later zeros.

Correctness can be viewed through the record length. A valid extension increases the record by one and supplies a witness. An invalid extension cannot justify a larger answer, so shifting `l` preserves the old record. The algorithm never lowers that record and never raises it without a valid window. Hence the final maintained length is exactly the largest subarray containing at most one zero, which is exactly the largest consecutive-one run obtainable with at most one flip.

## Complexity detail

Let $n$ be the array length. The loop reads every element once. The left boundary only moves forward and advances at most $n$ times. Each iteration performs constant-time arithmetic and indexing, so total time is $O(n)$.

The algorithm stores only `l`, `cnt`, and the current loop value. It modifies neither the array nor any collection proportional to its length, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Standard shrinking sliding window:** Use explicit left and right indices, contract in a `while zero_count > 1` loop, and update a separate maximum. It is also $O(n)$ and may be easier initially, while this source uses the non-shrinking record-length form.
- **Brute-force every subarray:** Counting zeros in all possible ranges costs at least $O(n^2)$ time and repeats work across heavily overlapping windows.
- **Track the previous zero index:** When a second zero arrives, move the left boundary directly after the earlier zero. This also gives $O(n)$ time and is especially useful for a stream because only the recent zero position is needed.
- **All ones:** `cnt` remains zero, `l` remains zero, and the full array length is returned; no flip is required.
- **All zeros:** The best answer is one. Every zero after the first prevents growth and advances `l`.
- **Single element:** Both `[1]` and `[0]` return one, because a zero may be flipped and a one already forms a valid run.
- **Temporarily invalid window:** `cnt` is not guaranteed to be at most one after every iteration. That is deliberate in this non-shrinking formulation and must not be mistaken for a broken standard-window invariant.
- **Infinite-stream follow-up:** The exact code indexes `nums[l]`, so it assumes stored random access. A streaming version can remember the last zero's position and derive the current valid length without retaining the full history.
- **Binary values are required:** The XOR indicator depends on each value being exactly zero or one. For general values, use an explicit comparison such as `int(x == 0)`.
