# Maximum Absolute Sum of Any Subarray

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1749 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/) |

## Problem Description

### Goal

You are given an integer array `nums`. For a contiguous subarray, its absolute sum is the absolute value of the ordinary sum of all elements in that subarray: a negative total is negated, while a nonnegative total is unchanged.

Return the maximum absolute sum among all possibly empty contiguous subarrays. The empty subarray has sum zero, so the answer is always nonnegative. A winning subarray may therefore have either a large positive total or a strongly negative total whose magnitude is larger; both directions must be considered.

### Function Contract

**Inputs**

- `nums`: a nonempty list of integers with $1 \le \lvert\texttt{nums}\rvert \le 10^5$ and $-10^4 \le \texttt{nums[i]} \le 10^4$.

Let $n = \lvert\texttt{nums}\rvert$.

**Return value**

- Return the largest value of $\left\lvert\sum_{k=l}^{r}\texttt{nums[k]}\right\rvert$ over all contiguous index ranges, also allowing the empty range with sum zero.

### Examples

**Example 1**

- Input: `nums = [1, -3, 2, 3, -4]`
- Output: `5`
- Explanation: The subarray `[2, 3]` has sum `5`, whose absolute value is `5`.

**Example 2**

- Input: `nums = [2, -5, 1, -4, 3, -2]`
- Output: `8`
- Explanation: The subarray `[-5, 1, -4]` sums to `-8`, giving absolute sum `8`.

**Example 3**

- Input: `nums = [0, 0, 0]`
- Output: `0`
- Explanation: Every subarray, including the empty one, has sum zero.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Express every subarray through two prefix sums**

Start with prefix sum zero before the array. If $P_i$ is the sum of the first $i$ elements, then the sum of a subarray ending before position $j$ and starting at position $i$ is $P_j-P_i$. Thus every candidate is the difference between two prefix sums.

**Use absolute value to remove chronological direction**

For any two prefix sums $a$ and $b$, the relevant magnitude is $\lvert a-b\rvert$, which is unchanged when their order is reversed. Consequently, the largest possible magnitude among all prefix pairs is simply the difference between the greatest prefix sum and the smallest prefix sum. Their positions do not need to be ordered manually: whichever occurs later determines whether the corresponding subarray sum is positive or negative.

**Track only the two extrema**

Scan the array while maintaining the current prefix sum and the smallest and largest prefix sums seen, including the initial zero. At the end, `maximum_prefix - minimum_prefix` is attainable by the subarray between those two prefix positions and dominates every other pairwise difference, so it is exactly the requested answer.

#### Complexity detail

The scan performs constant work for each of the $n$ elements, taking $O(n)$ time. Only the current prefix sum and two extrema are stored, so the auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Two Kadane scans:** Track the maximum and minimum subarray sums and return the larger of their absolute values. This is also $O(n)$ time and $O(1)$ space.
- **Enumerate all subarrays:** Extending a running sum from every start index is correct but requires $O(n^2)$ time.
- **Prefix array plus pair enumeration:** Materializing all prefix sums uses $O(n)$ space and comparing every pair remains quadratic; only the extrema are needed.
- **All positive:** The full array gives the maximum positive sum.
- **All negative:** The full array gives the most negative sum, whose magnitude is returned.
- **All zero:** The answer is zero, matching the permitted empty subarray.
- **Cancellation:** A total array sum near zero does not rule out a large-magnitude interior subarray.
- **Initial prefix:** Including prefix zero is necessary for subarrays that begin at index zero.

</details>
