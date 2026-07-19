# Sequential Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1291 |
| Difficulty | Medium |
| Topics | Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/sequential-digits/) |

## Problem Description
### Goal
An integer has sequential digits exactly when every digit after the first is one greater than the digit immediately before it. For example, 1234 qualifies, while 1245 and 321 do not.

Given inclusive integer bounds `low` and `high`, return every sequential-digit integer in the closed range $[\texttt{low},\texttt{high}]$. The returned list must be sorted in ascending numeric order.

### Function Contract
**Inputs**

- `low` and `high`: integers satisfying $10 \le \texttt{low} \le \texttt{high} \le 10^9$.

**Return value**

A sorted list containing exactly the integers between the bounds, inclusive, whose adjacent decimal digits increase by one.

### Examples
**Example 1**

- Input: `low = 100`, `high = 300`
- Output: `[123,234]`

**Example 2**

- Input: `low = 1000`, `high = 13000`
- Output: `[1234,2345,3456,4567,5678,6789,12345]`

**Example 3**

- Input: `low = 90`, `high = 100`
- Output: `[]`
