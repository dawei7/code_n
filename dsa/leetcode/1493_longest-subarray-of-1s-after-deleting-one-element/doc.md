# Longest Subarray of 1's After Deleting One Element

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1493 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/) |

## Problem Description
### Goal

Given a binary array `nums`, delete exactly one element from it. After that deletion, inspect the remaining array for contiguous subarrays containing only `1` values.

Return the greatest possible length of such an all-ones subarray. The deleted element may be either `0` or `1`; in particular, an input containing only ones must still lose one element. If no `1` remains in a useful run, return `0`.

### Function Contract
**Inputs**

Let $N$ be the length of `nums`.

- `nums`: a binary list with $1 \le N \le 10^5$.
- Every entry is either `0` or `1`.

**Return value**

Return the maximum number of consecutive ones obtainable after deleting exactly one array element.

### Examples
**Example 1**

- Input: `nums = [1,1,0,1]`
- Output: `3`
- Explanation: Deleting the zero joins the runs `[1,1]` and `[1]`.

**Example 2**

- Input: `nums = [0,1,1,1,0,1,1,0,1]`
- Output: `5`
- Explanation: Deleting the zero between the three-one and two-one runs creates five consecutive ones.

**Example 3**

- Input: `nums = [1,1,1]`
- Output: `2`
- Explanation: A deletion is mandatory, so one of the three ones must be removed.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reframe one deletion as a window with at most one zero**

Any all-ones result after one deletion comes from a contiguous interval of the original array containing at most one zero. If the interval contains one zero, deleting it joins the ones on both sides. If it contains no zero, deleting any one inside the interval shortens its all-ones run by one.

Conversely, every original interval with at most one zero can produce an all-ones segment after one deletion. This equivalence turns the problem into finding the longest window with at most one zero, while remembering that the answer contributed by a window is one less than its original length.

**Maintain the legal window with two pointers**

Keep a left boundary `left` and a count `zeros` for the current window. Move `right` from left to right, adding the new value to the window and increasing `zeros` when that value is zero.

If the count becomes two, advance `left` until the older zero has left the window. Decrement `zeros` exactly when the departing value is zero. After this shrinking step, the current interval always contains at most one zero.

**Encode the mandatory deletion directly in the length**

The inclusive window length is `right - left + 1`. Exactly one element must be deleted, so its achievable all-ones length is `right - left`. Update the best answer with that quantity for every valid window.

This single formula handles both cases. With one zero, it removes that zero. With no zeros, it accounts for deleting one of the ones. For a one-element input, `right - left` is zero, which correctly reflects that the only element must be deleted.

**Why no optimal result is missed**

Consider an optimal post-deletion all-ones subarray and the corresponding interval before deletion. That original interval contains at most the deleted element as a zero; any additional zero would remain and break the result. When the scan reaches the interval's right endpoint, the sliding-window invariant retains a legal suffix with at most one zero that is at least as long as this candidate interval unless an earlier second zero forces a later left boundary.

The algorithm evaluates every maximal legal window ending at every `right`. Since removing elements from the left cannot create a longer interval ending at the same position, its recorded `right - left` dominates every other legal candidate with that endpoint. Taking the maximum therefore recovers the global optimum.

**Why each index moves only once**

The right pointer advances exactly $N$ times. The left pointer never moves backward and advances at most $N$ times in total, even though it appears inside a loop. This monotonic movement is what makes the sliding window linear rather than quadratic.

#### Complexity detail

Each element enters the window once and leaves it at most once, so total time is $O(N)$. The algorithm stores two indices, a zero count, and the best length, giving $O(1)$ auxiliary space.

The benchmark uses repeated two-one runs separated by zeros. A correct implementation that tries every deletion and rescans the remaining array performs $O(N^2)$ work, completes all tiers, and is rejected by scaling.

#### Alternatives and edge cases

- **Dynamic programming by adjacent runs:** track the current run of ones and the previous run separated by one zero; combining them yields the same $O(N)$ time and $O(1)$ space.
- **Prefix and suffix run arrays:** precompute consecutive-one counts on both sides of every index, then evaluate deleting each position. This is $O(N)$ time but uses $O(N)$ space.
- **Try every deletion:** remove or skip each index and rescan for the longest run. It is correct but takes $O(N^2)$ time.
- **Window length without subtracting one:** solves an at-most-one-deletion variant and incorrectly returns $N$ for an all-ones array.
- **Single one:** mandatory deletion leaves an empty array, so the answer is `0`.
- **Single zero:** deletion also leaves an empty array, so the answer is `0`.
- **All ones:** return $N-1$, not $N$.
- **All zeros:** no deletion can create a one, so return `0`.
- **Zero at an endpoint:** deleting it can preserve the entire adjacent run of ones.
- **Multiple separated zeros:** the left pointer must move past the older zero whenever a second enters.
- **Alternating values:** deleting one interior zero can join at most the neighboring one runs.
- **Deletion outside the chosen run:** when a legal window contains no zero, the length-minus-one rule still enforces that some array element is deleted.

</details>
