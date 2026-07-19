# K Radius Subarray Averages

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2090 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/k-radius-subarray-averages/) |

## Problem Description

### Goal

You are given a zero-indexed integer array `nums` and a nonnegative radius `k`. For an index $i$, its $k$-radius subarray contains every element from index $i-k$ through $i+k$, inclusive, and therefore has length $2k+1$.

If that complete window fits inside `nums`, assign index $i$ the window's arithmetic mean using integer division that discards the fractional part. If fewer than $k$ elements exist on either side of $i$, assign `-1` instead. Return all $n$ assigned values in an array of the same length as `nums`.

### Function Contract

**Inputs**

- `nums`: an array of $n$ nonnegative integers, where $1 \le n \le 10^5$.
- `k`: an integer radius with $0 \le k \le 10^5$.
- Every element of `nums` is between $0$ and $10^5$.

Let the window length be

$$
W = 2k + 1.
$$

**Return value**

Return an array `avgs` of length $n$. For each valid center $i$,

$$
\texttt{avgs}[i]
= \left\lfloor
\frac{\sum_{j=i-k}^{i+k}\texttt{nums}[j]}{W}
\right\rfloor,
$$

and every other entry is `-1`.

### Examples

**Example 1**

- Input: `nums = [7, 4, 3, 9, 1, 8, 5, 2, 6]`, `k = 3`
- Output: `[-1, -1, -1, 5, 4, 4, -1, -1, -1]`
- Explanation: Only centers `3`, `4`, and `5` have complete windows of length `7`.

**Example 2**

- Input: `nums = [100000]`, `k = 0`
- Output: `[100000]`

**Example 3**

- Input: `nums = [8]`, `k = 100000`
- Output: `[-1]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Separating invalid centers from complete windows**

Initialize the length-$n$ result with `-1`. A complete window exists only when $W \le n$; otherwise this initialized result is final. When a window does fit, valid centers range from `k` through `n - k - 1`, while the untouched prefix and suffix correctly remain `-1`.

**Reusing almost the entire previous sum**

Compute the first window sum for indices `0` through `2 * k` and write its integer average at center `k`. Advancing the center by one removes exactly the old leftmost element and adds exactly the new rightmost element:

`window_sum += nums[center + k] - nums[center - k - 1]`.

Thus each subsequent average is obtained in constant time rather than summing all $W$ elements again.

**Why every result entry is correct**

Before writing a center, `window_sum` equals the sum of precisely its inclusive radius-$k$ interval. Integer division by the fixed positive length $W$ gives the required truncated average. Every valid center is visited once, and no invalid center overwrites its initial `-1`.

#### Complexity detail

The first sum and all sliding updates together inspect $O(n)$ elements, so the time is $O(n)$. Beyond the required output array, the algorithm stores only the window length and running sum, giving $O(1)$ auxiliary space. The returned array itself uses $O(n)$ space.

#### Alternatives and edge cases

- **Recompute every window:** Summing all $W$ values independently at each valid center is simple but takes $O(nW)$ time in the worst case.
- **Prefix sums:** A prefix-sum array also obtains each window sum in constant time, with $O(n)$ time overall but $O(n)$ additional space.
- **Convolution:** A box filter expresses the same operation but adds machinery unnecessary for one-dimensional integer windows.
- When `k` is zero, each one-element average equals the original value.
- When $W=n$, exactly one center receives the average of the entire array.
- When $W>n$, every result entry remains `-1`.
- Input values are nonnegative, so truncation toward zero agrees with the floor notation used above.

</details>
