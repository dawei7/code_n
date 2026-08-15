# Maximum XOR Score Subarray Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3277 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Maximum XOR Score Subarray Queries](https://leetcode.com/problems/maximum-xor-score-subarray-queries/) |

## Problem Description

### Goal

For an array `a`, define its XOR score through a repeated simultaneous reduction. Replace every element except the last by the XOR of it and its right neighbor, then remove the last element. Repeat this operation until one value remains; that final value is the array's score.

An integer array `nums` and several inclusive index ranges are given. For every query `[left, right]`, consider every nonempty subarray contained within `nums[left..right]`, compute each subarray's XOR score under that reduction, and report the largest score. Return the query answers in their original order.

### Function Contract

**Inputs**

- `nums`: A nonempty list of $n$ integers, each between $0$ and $2^{31}-1$.
- `queries`: A nonempty list of inclusive pairs `[left, right]` satisfying $0 \le \textit{left} \le \textit{right} < n$.

The bounds are $1 \le n \le 2000$ and $1 \le q \le 10^5$, where $q$ is the number of queries.

**Return value**

Return a list of $q$ integers whose $i$th entry is the maximum XOR score of any subarray fully contained in the $i$th query range.

### Examples

#### Example 1

- **Input:** `nums = [2, 8, 4, 32, 16, 1], queries = [[0, 2], [1, 4], [0, 5]]`
- **Output:** `[12, 60, 60]`
- **Explanation:** The best scores in the three ranges are produced by `[8, 4]`, `[8, 4, 32, 16]`, and that same four-element subarray, respectively.

#### Example 2

- **Input:** `nums = [0, 7, 3, 2, 8, 5, 1], queries = [[0, 3], [1, 5], [2, 4], [2, 6], [5, 6]]`
- **Output:** `[7, 14, 11, 14, 5]`

#### Example 3

- **Input:** `nums = [5, 3], queries = [[0, 0], [1, 1], [0, 1]]`
- **Output:** `[5, 3, 6]`
- **Explanation:** The two-element array reduces once to `5 XOR 3 = 6`.
