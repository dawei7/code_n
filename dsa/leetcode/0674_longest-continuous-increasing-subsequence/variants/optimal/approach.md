## General

**Continuity reduces the state to the current run**

Because the requested sequence must be a contiguous subarray, the only way to extend an increasing run ending at one position is to include the immediately next element.

There is no need to compare against every earlier index as in the general longest increasing subsequence problem. One adjacent comparison tells us whether the current run continues or a new run begins.

The exact solution maintains:

- `cnt`: the length of the strictly increasing contiguous run ending at the current processed element;
- `ans`: the largest such length seen anywhere so far.

Both begin at one because the input is nonempty and any single element is an increasing subarray of length one.

**Understand the shifted enumeration**

The loop is:

`for i, x in enumerate(nums[1:])`.

The slice begins with original index one. Therefore:

- loop `i = 0` has `x = nums[1]` and compares it with `nums[0]`;
- loop `i = 1` has `x = nums[2]` and compares it with `nums[1]`;
- in general, `x = nums[i + 1]` while `nums[i]` is its immediate predecessor.

This offset is easy to misread. The comparison `nums[i] < x` is exactly the adjacent original-array comparison.

**Extend on a strict increase**

If `nums[i] < x`, the new value is strictly greater than the previous one. Appending it preserves the current continuous increasing run, so increment `cnt`.

The new run length may be the largest seen, so update:

`ans = max(ans, cnt)`.

**Reset at a boundary**

If `nums[i] >= x`, the previous run cannot include `x`:

- equality violates strict increase;
- a decrease also violates it.

The element `x` starts a new one-element run, so set `cnt = 1`.

There is no need to update `ans` in the reset branch because `ans` was initialized to at least one and every run that grew beyond one updated it during growth.

**A walkthrough**

For `[1, 3, 5, 4, 7]`:

- three exceeds one, so `cnt = 2` and `ans = 2`;
- five exceeds three, so `cnt = 3` and `ans = 3`;
- four does not exceed five, so reset `cnt = 1`;
- seven exceeds four, so `cnt = 2` while `ans` remains three.

The result is three, representing `[1, 3, 5]`.

The noncontinuous sequence `[1, 3, 5, 7]` is irrelevant because selecting seven would skip the intervening four.

**The run invariant**

After processing through original index `p`:

- `cnt` equals the length of the longest strictly increasing subarray that must end at `p`;
- `ans` equals the maximum increasing-run length ending at any index from zero through `p`.

Initially, at index zero, both are one.

For the next index, if the adjacent comparison increases, the only run ending there extends the previous ending run by one. If it fails, no multi-element increasing run can cross that boundary, so the best ending run has length one. Updating the maximum in the extension case preserves the second statement.

By induction, after the final element, `ans` is the required longest continuous increasing length.

**Why no starting index is required**

The problem asks only for length. Resetting `cnt` to one implicitly moves the start to the current element. Storing an explicit anchor would produce the same lengths as `current_index - anchor + 1` but is unnecessary for this implementation.

**Why every candidate run is considered**

Every maximal strictly increasing subarray starts either at index zero or immediately after an adjacent comparison that fails. The reset rule starts a run at exactly those boundaries, and the increment rule measures it until the next boundary. Thus every maximal run contributes its full length to `ans`.

Shorter subarrays contained inside a maximal run cannot beat the maximal run, so they need no separate enumeration.

## Complexity detail

Let `N` be the array length.

The loop performs one constant-time comparison for each adjacent pair, so running time is `O(N)`.

The sliding-run algorithm itself uses only `ans`, `cnt`, `i`, and `x`, which is `O(1)` working state.

However, the exact Python source materializes `nums[1:]` before enumeration. That slice copies `N - 1` references and uses `O(N)` temporary auxiliary space. Therefore, the manifest's `O(1)` space describes the intended scan, not the literal slicing implementation. Iterating `i` from one through `N - 1` directly would preserve the logic and make the actual auxiliary bound constant.

## Alternatives and edge cases

- **Index loop without slicing:** Iterate `for i in range(1, len(nums))` and compare `nums[i - 1] < nums[i]`. This retains `O(N)` time and achieves literal `O(1)` extra space.

- **Anchor-based sliding window:** Store the start index of the current increasing run and reset it after every failed comparison. Compute each length from indices.

- **Dynamic-programming array:** Store the increasing-run length ending at every index. It is correct but wastes `O(N)` space because only the previous length is needed.

- **General LIS algorithm:** It permits skipped elements and would answer a different problem. Continuity is the key simplifying constraint.

- **One element:** The slice is empty, the loop does not run, and the initialized answer one is returned.

- **All equal values:** Every comparison fails under strict inequality, so every run length is one.

- **Strictly decreasing array:** Each element starts a new run and the answer remains one.

- **Strictly increasing array:** `cnt` reaches `N` and so does `ans`.

- **Multiple runs tied for maximum:** Only their common maximum length matters; no count or endpoint is requested.

- **Negative values:** Ordinary numeric comparison handles them without special cases.

- **Equality:** Non-decreasing is not sufficient. Equal adjacent values must reset the run.

- **Temporary slice:** It leaves the original array unchanged but incurs linear memory. Direct indexing is preferable when the stated constant-space bound must be literal.

- **Empty array:** The source guarantees at least one element. The exact initialization would return one for an empty list, so it relies on that contract.
