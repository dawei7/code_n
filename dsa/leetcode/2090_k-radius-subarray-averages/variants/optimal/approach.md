## General

**View every valid average as one fixed-size window**

A center index `c` has a valid k-radius average only when the array contains indices `c - k` through `c + k`. Every valid window therefore has the same length

$$
W=2k+1.
$$

Computing each window sum from scratch would repeat most additions because neighboring windows overlap in all but two positions. The exact solution maintains a rolling sum `s` while moving one right endpoint `i` from left to right.

The answer list begins as `[-1] * n`. This is already correct for all centers lacking enough elements on either side. The loop overwrites only positions for which a complete window has become available.

**Grow the first complete window**

At every iteration, the current value `x` is added to `s`. Before `i` reaches `2 * k`, fewer than $2k+1$ elements have been seen, so no complete window exists and the code leaves the answer untouched.

When `i == 2 * k`, `s` contains indices 0 through `2 * k`, exactly the first window of size $W$. Its center is index `k`, which equals `i - k`. The source stores

`ans[i - k] = s // (k * 2 + 1)`.

The integer division implements the required truncated average. Since all `nums[i]` are nonnegative, Python's floor division `//` has the same result as truncation toward zero.

**Slide by removing the outgoing left endpoint**

After recording a complete window, the code executes

`s -= nums[i - k * 2]`.

At right endpoint `i`, the current window begins at `i - 2 * k`. Subtracting that element after using the sum prepares `s` for the next iteration.

When `i + 1` arrives, its value is added. The sum then represents indices

$$
(i-2k)+1\ \text{ through }\ i+1,
$$

which is the next window shifted right by one.

The subtraction occurs after the average is calculated because the outgoing value still belongs to the current window. Removing it first would make the sum one element too short.

**Match the right endpoint to the correct center**

A window ending at `i` and having radius `k` starts at `i - 2k`. Its center lies `k` positions left of the right endpoint:

`center = i - k`.

This explains the assignment index `ans[i - k]`. The first valid center is `k`, and the last complete window ends at `n - 1`, giving final center `n - 1 - k`. All indices before `k` and after `n - 1 - k` correctly retain `-1`.

For `nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]` and `k = 3`, the first complete right endpoint is `i = 6`. The sum is 37, the center is 3, and `37 // 7 = 5` is written at `ans[3]`. After removing `nums[0]` and adding `nums[7]` on the next iteration, the rolling sum becomes the window centered at 4.

**Why `k = 0` works without a special case**

When `k = 0`, the window size is one and `i >= 0` is true on every iteration. After adding `nums[i]`, the code assigns `ans[i] = s // 1`, then subtracts `nums[i]`. The rolling sum returns to zero before the next element.

Thus every answer equals its single centered value. The generic logic handles radius zero correctly without an early return.

**Why oversized radii leave all answers as `-1`**

If $2k+1>n$, no index has enough values on both sides. The loop condition `i >= 2 * k` never becomes true for any `i <= n - 1`. The algorithm may accumulate the total input sum in `s`, but it never writes an average. The initialized all-`-1` answer is returned, exactly as required.

**Why the rolling invariant proves correctness**

Whenever `i >= 2k` immediately after adding `nums[i]`, `s` equals the sum from `i-2k` through `i`. This is true for the first complete window because nothing has yet been removed except elements preceding its left boundary, of which there are none.

After recording a window, the algorithm removes its leftmost value. Adding the next element establishes the invariant for the next right endpoint. By induction, every stored average uses exactly its required $2k+1$ values.

Every valid center corresponds to one such right endpoint, and invalid centers are never overwritten. Therefore the entire returned array is correct.

## Complexity detail

Let $n$ be the length of `nums`.

The loop visits each element once. Each iteration performs constant-time arithmetic and at most one answer assignment and one subtraction. Total time complexity is $O(n)$.

The required output list uses $O(n)$ space. Excluding that returned array, the algorithm stores only `n`, `s`, `i`, and `x`, so auxiliary space complexity is $O(1)$.

The rolling sum can be as large as $(2k+1)$ times the maximum input value. Python integers handle that automatically; fixed-width implementations should choose a type wide enough for the maximum window sum.

## Alternatives and edge cases

- **Recompute each window sum:** Summing $2k+1$ values for every center costs $O(nk)$ in the worst case. The rolling update reuses overlap and stays linear.
- **Prefix sums:** A prefix array answers each range sum in $O(1)$ after $O(n)$ preprocessing, but uses $O(n)$ extra space. The sliding sum achieves the same time with $O(1)$ auxiliary state.
- **Return the input for `k = 0`:** That optimization is possible, but it returns the same list object. The exact generic path creates and returns a separate answer list while remaining linear.
- **Window larger than the array:** No assignment occurs and every output remains `-1`.
- **Window exactly the array length:** Only center `k` is valid, and the loop writes exactly one average when `i = n - 1`.
- **Subtracting too early:** The leftmost element belongs to the average just computed. It must be removed only afterward.
- **Wrong center index:** The current `i` is the right endpoint, not the center. The correct destination is `i - k`.
- **Radius zero:** Every single element is its own average, and the rolling sum resets after each iteration.
- **Nonnegative inputs:** `//` matches truncation toward zero because window sums cannot be negative. With negative sums, Python floor division would need special handling to match the stated truncation rule.
- **Boundary outputs:** Exactly the first `k` and last `k` positions remain `-1` when a full window fits somewhere.
- **No input mutation:** The loop reads `nums` and writes only to the new `ans` list.
- **Large accumulated value:** Use a wide numeric type outside Python to avoid overflow before division.
