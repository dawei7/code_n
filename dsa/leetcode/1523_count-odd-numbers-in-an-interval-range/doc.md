# Count Odd Numbers in an Interval Range

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1523 |
| Difficulty | Easy |
| Topics | Math |
| Official Link | [LeetCode](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/) |

## Problem Description
### Goal

Two non-negative integers `low` and `high` define an inclusive interval. Count how many integers in that interval are odd, including either endpoint whenever it is odd.

The interval may be very wide—its upper endpoint can reach one billion—so the result should be derived from endpoint arithmetic rather than by inspecting every contained integer. Return only the count; the odd values themselves do not need to be listed.

### Function Contract
**Inputs**

- `low`: The inclusive lower endpoint.
- `high`: The inclusive upper endpoint.
- The source guarantees $0 \leq \texttt{low} \leq \texttt{high} \leq 10^9$.

**Return value**

Return the number of odd integers $x$ satisfying $\texttt{low} \leq x \leq \texttt{high}$.

### Examples
**Example 1**

- Input: `low = 3, high = 7`
- Output: `3`
- Explanation: The qualifying values are 3, 5, and 7.

**Example 2**

- Input: `low = 8, high = 10`
- Output: `1`
- Explanation: Only 9 is odd.

**Example 3**

- Input: `low = 4, high = 4`
- Output: `0`
