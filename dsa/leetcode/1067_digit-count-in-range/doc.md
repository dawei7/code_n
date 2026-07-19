# Digit Count in Range

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1067 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Math, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/digit-count-in-range/) |

## Problem Description

### Goal

Given one decimal digit `d` and two positive integers `low` and `high`, inspect the ordinary decimal representations of every integer in the inclusive range from `low` through `high`.

Return the total number of times digit `d` occurs across all those representations. Count every position separately when a number contains the digit more than once, and do not treat omitted leading zeros as written digits.

### Function Contract

**Inputs**

- `d`: an integer digit satisfying $0 \le d \le 9$.
- `low` and `high`: inclusive bounds satisfying $1 \le \texttt{low} \le \texttt{high} \le 2 \cdot 10^8$.
- Let $H=\texttt{high}$.

**Return value**

- The number of occurrences of `d` in all decimal representations from `low` through `high`.

### Examples

**Example 1**

- Input: `d = 1, low = 1, high = 13`
- Output: `6`
- Explanation: The digit appears in `1`, `10`, twice in `11`, `12`, and `13`.

**Example 2**

- Input: `d = 3, low = 100, high = 250`
- Output: `35`

**Example 3**

- Input: `d = 0, low = 1, high = 10`
- Output: `1`
- Explanation: Only the ones position of `10` contributes a written zero.
