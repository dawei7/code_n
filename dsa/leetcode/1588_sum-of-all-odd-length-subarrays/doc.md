# Sum of All Odd Length Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1588 |
| Difficulty | Easy |
| Topics | Array, Math, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-all-odd-length-subarrays/) |

## Problem Description
### Goal

Given an array of positive integers, consider every contiguous subarray whose length is odd. This includes every one-element subarray, every valid three-element subarray, and so on through the largest odd length that fits.

Compute each such subarray's sum, then return the total across all of them. Overlapping subarrays are distinct and must each contribute. A subarray is contiguous; non-adjacent subsequences do not count.

### Function Contract
**Inputs**

- `arr`: An array of $N$ positive integers, where $1 \le N \le 100$ and $1 \le \texttt{arr[i]} \le 1000$.

**Return value**

Return the sum of the sums of all odd-length contiguous subarrays of `arr`.

### Examples
**Example 1**

- Input: `arr = [1,4,2,5,3]`
- Output: `58`

**Example 2**

- Input: `arr = [1,2]`
- Output: `3`

**Example 3**

- Input: `arr = [10,11,12]`
- Output: `66`

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reverse the summation by counting each element's appearances**

Instead of generating subarrays and repeatedly adding their elements, determine how many odd-length subarrays contain each `arr[index]`. Add the element multiplied by that count. Every subarray sum is the sum of its elements, so exchanging these two finite summations preserves the total.

For index `i`, a containing subarray chooses its left endpoint from the $i+1$ positions at or before `i` and its right endpoint from the $N-i$ positions at or after `i`. Therefore

$$
C_i=(i+1)(N-i)
$$

subarrays contain this element.

**Select the odd-length half**

The subarray length is odd exactly when the left and right extensions from `i` have the same parity. Across the rectangular set of endpoint choices, the two parity classes alternate, so exactly half the choices have odd length when $C_i$ is even, and the odd class has one extra choice when $C_i$ is odd. Thus the number of odd-length containing subarrays is

$$
O_i=\left\lceil\frac{C_i}{2}\right\rceil
=\left\lfloor\frac{C_i+1}{2}\right\rfloor.
$$

Add `arr[i] * ((C_i + 1) // 2)` for every index. Each odd-length subarray contributes each of its elements once through that element's containing-subarray count, while even-length subarrays contribute nothing, proving that the accumulated total is exactly the requested sum.

#### Complexity detail

The algorithm visits each of the $N$ indices once and performs constant arithmetic, for $O(N)$ time. It keeps only the length, current contribution values, and total, using $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Prefix sums by odd length:** build prefix sums and query every odd-length interval in constant time. There are $O(N^2)$ such intervals, so total time remains $O(N^2)$ with $O(N)$ space.
- **Running sum for every start:** extend each subarray and add the running sum whenever its length is odd. It uses $O(1)$ extra space but takes $O(N^2)$ time.
- **Parity-state dynamic programming:** maintain the sums and counts of odd- and even-length subarrays ending at the previous index. Extending them gives an independent $O(N)$-time, $O(1)$-space solution.
- **Single element:** the only subarray has odd length, so return that element.
- **Even array length:** the full array is excluded, but shorter odd-length subarrays still count.
- **Overlapping intervals:** each valid choice of endpoints is a separate subarray and contributes independently.
- **Maximum values:** the result combines many occurrences, so fixed-width implementations should use an integer type large enough for the total.

</details>
