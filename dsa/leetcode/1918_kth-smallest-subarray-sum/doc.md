# Kth Smallest Subarray Sum

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/kth-smallest-subarray-sum/) |
| Frontend ID | 1918 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given an integer array `nums` containing only positive values. Every non-empty contiguous subarray contributes one sum, and equal sums from different subarray positions remain separate entries.

Arrange all $N(N+1)/2$ subarray sums in non-decreasing order and return the value at rank `k`, where ranks are one-based.

The choice concerns values rather than intervals: the function returns only the selected sum, not the subarray that produced it. If several subarrays have the same sum, each occurrence keeps its own place in the ordering.

### Function Contract

**Inputs**

- `nums`: an array of $N$ positive integers, with $1 \le N \le 2 \cdot 10^4$ and $1 \le \texttt{nums[i]} \le 5 \cdot 10^4$.
- `k`: a one-based rank satisfying $1 \le k \le N(N+1)/2$.

**Return value**

- Return the `k`th smallest sum among all non-empty contiguous subarrays of `nums`.

### Examples

**Example 1**

- Input: `nums = [2, 1, 3], k = 4`
- Output: `3`

The sorted subarray sums are `1, 2, 3, 3, 4, 6`, so the fourth value is `3`.

**Example 2**

- Input: `nums = [3, 3, 5, 5], k = 7`
- Output: `10`

The sorted sums are `3, 3, 5, 5, 6, 8, 10, 11, 13, 16`.

### Required Complexity

- **Time:** $O(N \log S)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Turn selection into a monotone counting question**

For a candidate sum limit $x$, count how many non-empty subarrays have sum at most $x$. This count never decreases as $x$ grows. Therefore, the requested answer is the smallest $x$ for which the count reaches at least `k`.

The answer lies between the smallest single element and

$$
S = \sum_{i=0}^{N-1} \texttt{nums[i]},
$$

so binary search can find that first sufficient limit.

**Count qualifying subarrays with one sliding window**

Fix a candidate $x$ and move a right endpoint from left to right. Add the new value to a running window sum. While that sum exceeds $x$, remove values from the left.

Because every array value is positive, once the window sum is at most $x$, every subarray ending at the current right endpoint and starting between `left` and `right` also has sum at most $x$. There are `right - left + 1` such subarrays. Any earlier start would have a larger sum and cannot qualify, so adding this quantity counts exactly all qualifying subarrays ending at that position.

At the end of the binary search, every smaller limit has fewer than `k` qualifying sums, while the returned limit has at least `k`. This is precisely the value occupying rank `k`, including when several different subarrays share that value.

#### Complexity detail

For each tested limit, both sliding-window pointers move forward at most $N$ times, so counting costs $O(N)$. The inclusive search range has width at most $S$, requiring $O(\log S)$ counting passes and $O(N \log S)$ time overall. The algorithm stores only scalar indices, sums, counts, and binary-search bounds, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate and sort every subarray sum:** This direct method materializes $N(N+1)/2$ values, requiring $O(N^2)$ space and at least quadratic work before sorting.
- **Prefix sums plus per-start binary search:** Prefix sums can count valid endpoints in $O(N \log N)$ per candidate, but positivity permits the faster linear sliding-window count.
- **Smallest rank:** The first value is the minimum array element because every longer positive subarray has a strictly larger sum than each of its elements.
- **Largest rank:** Rank $N(N+1)/2$ selects the sum of the entire array.
- **Repeated sums:** Equal numeric sums occupy separate ranks when they come from different subarrays.
- **Single element:** The only legal rank is one, and its answer is that element.

</details>
