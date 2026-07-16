# Maximum Length of Subarray With Positive Product

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1567 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/) |

## Problem Description
### Goal

Given an integer array `nums`, choose a contiguous, nonempty subarray whose element product is positive. The numerical product itself may be very large; only whether its sign is positive matters.

A zero makes the product zero and therefore cannot belong to a qualifying subarray. Negative values reverse the sign, so a zero-free subarray has a positive product exactly when it contains an even number of negative values. Return the greatest possible length of such a subarray, or `0` when none exists.

### Function Contract
**Inputs**

- `nums`: An integer array of length $N$, where $1 \le N \le 10^5$ and $-10^9 \le \texttt{nums[i]} \le 10^9$.

**Return value**

Return the maximum length of a contiguous subarray whose product is strictly positive. Return `0` if every nonempty subarray has a zero or negative product.

### Examples
**Example 1**

- Input: `nums = [1,-2,-3,4]`
- Output: `4`

**Example 2**

- Input: `nums = [0,1,-2,-3,-4]`
- Output: `3`

**Example 3**

- Input: `nums = [-1,-2,-3,0,1]`
- Output: `2`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Keep the best two signs ending at the current position**

For each processed value, maintain `positive_length`, the longest positive-product subarray ending at that value, and `negative_length`, the longest negative-product subarray ending there. A zero resets both lengths because no nonzero-product subarray can cross it.

When the current value is positive, it preserves an existing product's sign. Extend the positive state by one. Extend the negative state only if a negative state already existed; otherwise no negative-product subarray can end here.

**Swap sign roles at a negative value**

A negative value reverses the product sign. The new positive state exists only by extending the previous negative state, while the new negative state comes from extending the previous positive state or starting with the current negative value alone. Both updates must use the old state, so assign them together.

After each value, compare `positive_length` with the global maximum. The two states cover every subarray ending at the current position by sign, and retain the longest one of each sign. Their transitions consider exactly the possible effects of zero, a positive value, or a negative value. Induction over the array therefore proves that every optimal positive-product subarray is represented when its final element is processed.

#### Complexity detail

Each of the $N$ values causes a constant number of sign checks and state updates, so the total time is $O(N)$.

The algorithm stores two ending lengths and one global maximum, giving $O(1)$ auxiliary space. It never forms the potentially enormous numerical product.

#### Alternatives and edge cases

- **Zero-delimited parity analysis:** split the array at zeros. A segment with an even number of negatives is wholly valid; for an odd count, discard the prefix through the first negative or the suffix from the last negative. This is also $O(N)$.
- **Enumerate every subarray:** extend a running product from every start index. It is correct but requires $O(N^2)$ time.
- **Store full DP arrays:** record the positive and negative ending lengths for every index. This preserves the recurrence but uses unnecessary $O(N)$ space.
- **Zeros:** no qualifying subarray can cross a zero, and an array containing only zeros returns `0`.
- **One negative value:** by itself its product is negative, so it contributes no positive length.
- **Even negative count:** an entire zero-free segment has positive product and may be the optimum.
- **Odd negative count:** removing through the first negative or from the last negative is sufficient to make the remaining negative count even.
- **Magnitude and overflow:** only zero and sign matter; multiplying values is unnecessary and can overflow fixed-width types.
- **Positive singleton:** any single positive value is a qualifying length-one subarray.

</details>
