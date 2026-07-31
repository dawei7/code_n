# Count the Number of Fair Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2563 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [count-the-number-of-fair-pairs](https://leetcode.com/problems/count-the-number-of-fair-pairs/) |

## Problem Description

### Goal

An integer array `nums` and two integers `lower` and `upper` define an inclusive range of allowed pair sums. A pair is identified by two different array positions, so equal values at different indices still form distinct pairs.

Count the index pairs $(i, j)$ for which $0 \le i < j < n$ and the sum of the selected values lies between the two bounds, inclusive:

$$
\texttt{lower} \le \texttt{nums[i]} + \texttt{nums[j]} \le \texttt{upper}.
$$

Return the total number of such fair pairs. The array may contain negative values and duplicates, and the answer counts positions rather than unique value combinations.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $1 \le n \le 10^5$ and $-10^9 \le \texttt{nums[i]} \le 10^9$.
- `lower`: The inclusive lower bound for a fair pair sum, with $-10^9 \le \texttt{lower} \le 10^9$.
- `upper`: The inclusive upper bound for a fair pair sum, with $\texttt{lower} \le \texttt{upper} \le 10^9$.

**Return value**

- The number of index pairs $(i, j)$ satisfying $0 \le i < j < n$ and the inclusive sum bounds.

### Examples

**Example 1**

- Input: `nums = [0, 1, 7, 4, 4, 5], lower = 3, upper = 6`
- Output: `6`
- Explanation: The six fair index pairs have sums in the inclusive range from $3$ through $6$.

**Example 2**

- Input: `nums = [1, 7, 9, 2, 5], lower = 11, upper = 11`
- Output: `1`
- Explanation: Only the values `9` and `2` form a pair whose sum is exactly $11$.

**Example 3**

- Input: `nums = [-2, 0, 2], lower = 0, upper = 0`
- Output: `1`
- Explanation: Only the pair containing `-2` and `2` has a sum of zero.
