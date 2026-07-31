# House Robber IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2560 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [House Robber IV](https://leetcode.com/problems/house-robber-iv/) |

## Problem Description

### Goal

Several houses stand consecutively along a street, and `nums[i]` is the amount of money stored in house $i$. A robber may choose multiple houses, but refuses to rob two adjacent houses. The robber's capability is the largest amount taken from any single chosen house.

Given the minimum required number of houses `k`, consider every valid way to rob at least `k` non-adjacent houses. Return the smallest capability attainable by any such choice. The constraints guarantee that selecting at least `k` non-adjacent houses is possible.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive house values, where $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.
- `k`: The minimum number of houses to rob, where $1 \le k \le \lceil n/2 \rceil$.

**Return value**

- The minimum possible value of the largest robbed house among all selections of at least `k` pairwise non-adjacent houses.

### Examples

**Example 1**

- Input: `nums = [2, 3, 5, 9], k = 2`
- Output: `5`
- Explanation: Robbing indices `0` and `2` gives capability `5`; every other valid two-house choice has capability at least `9`.

**Example 2**

- Input: `nums = [2, 7, 9, 3, 1], k = 2`
- Output: `2`
- Explanation: The endpoint houses at indices `0` and `4` are non-adjacent and have maximum value `2`.

**Example 3**

- Input: `nums = [2, 7, 9, 3, 1], k = 3`
- Output: `9`
- Explanation: Selecting three non-adjacent houses forces indices `0`, `2`, and `4`, whose maximum value is `9`.
