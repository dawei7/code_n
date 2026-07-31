# Maximum Value of an Ordered Triplet II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2874 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Maximum Value of an Ordered Triplet II](https://leetcode.com/problems/maximum-value-of-an-ordered-triplet-ii/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums`. For three indices satisfying $i < j < k$, define their ordered-triplet value as

$$
(\texttt{nums[i]} - \texttt{nums[j]}) \cdot \texttt{nums[k]}.
$$

The indices must be distinct and appear in their original left-to-right order; the values stored at those indices do not need to be distinct. Depending on the chosen positions, the product may be positive, zero, or negative.

Return the maximum value among all ordered triplets. If every triplet value is negative, return $0$ instead.

### Function Contract

**Inputs**

- `nums`: A list of positive integers containing at least three elements.

Let $n = \lvert\texttt{nums}\rvert$. The constraints are $3 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^6$.

**Return value**

- The largest ordered-triplet value for indices $i < j < k$, clamped to a minimum of $0$.

### Examples

**Example 1**

- Input: `nums = [12,6,1,2,7]`
- Output: `77`
- Explanation: Indices $(0,2,4)$ give $(12 - 1) \cdot 7 = 77$.

**Example 2**

- Input: `nums = [1,10,3,4,19]`
- Output: `133`
- Explanation: Indices $(1,2,4)$ give $(10 - 3) \cdot 19 = 133$.

**Example 3**

- Input: `nums = [1,2,3]`
- Output: `0`
- Explanation: The only triplet has value $(1 - 2) \cdot 3 = -3$, so the required nonnegative result is zero.
