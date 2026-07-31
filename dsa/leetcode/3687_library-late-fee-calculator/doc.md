# Library Late Fee Calculator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3687 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/library-late-fee-calculator/) |

## Problem Description
### Goal

A library records in `daysLate` how many days late each returned book was. Calculate each book's fee independently from its delay, then return the sum of all fees.

A book returned exactly one day late costs 1. A delay from 2 through 5 days, inclusive, costs twice its number of late days. A delay greater than 5 days costs three times its number of late days. These ranges are separate, so the boundary values 1, 2, 5, and 6 must use their corresponding rules exactly.

### Function Contract

**Inputs**

- `daysLate`: A nonempty list of late-day counts, with $1 \le \lvert\texttt{daysLate}\rvert \le 100$ and $1 \le \texttt{daysLate[i]} \le 100$.

**Return value**

Return the total fee obtained by adding the independently calculated penalty for every book.

### Examples

**Example 1**

- Input: `daysLate = [5, 1, 7]`
- Output: `32`

The fees are `10`, `1`, and `21`.

**Example 2**

- Input: `daysLate = [1, 1]`
- Output: `2`

Each one-day delay contributes 1.

**Example 3**

- Input: `daysLate = [2, 5, 6]`
- Output: `32`

The fees at these important boundaries are `4`, `10`, and `18`.
