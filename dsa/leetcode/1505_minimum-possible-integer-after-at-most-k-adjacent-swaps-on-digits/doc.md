# Minimum Possible Integer After at Most K Adjacent Swaps On Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1505 |
| Difficulty | Hard |
| Topics | String, Greedy, Binary Indexed Tree, Segment Tree |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/) |

## Problem Description
### Goal

The string `num` contains the decimal digits of a very large integer. One operation swaps two adjacent digits, and at most `k` such operations may be performed. Moving a digit left across $s$ digits consumes exactly $s$ adjacent swaps; all crossed digits shift one position right.

Return the lexicographically smallest digit string reachable within the budget, which is also the minimum numerical representation at the fixed input length. The result may begin with zero even though the input never does. Every digit occurrence must remain present, and fewer than `k` swaps may be used when additional operations cannot improve the result.

### Function Contract
**Inputs**

Let $n=\lvert\texttt{num}\rvert$.

- `num`: a string of decimal digits with $1\le n\le3\cdot10^4$ and no leading zero.
- `k`: the maximum number of adjacent swaps, with $1\le k\le10^9$.

**Return value**

Return the lexicographically smallest length-$n$ string obtainable by at most `k` adjacent swaps. Leading zeroes in the result are retained.

### Examples
**Example 1**

- Input: `num = "4321", k = 4`
- Output: `"1342"`
- Explanation: Bringing `1` to the front costs three swaps; the remaining swap brings `3` before `4`.

**Example 2**

- Input: `num = "100", k = 1`
- Output: `"010"`
- Explanation: The first zero moves left once. A leading zero is valid in the returned string.

**Example 3**

- Input: `num = "36789", k = 1000`
- Output: `"36789"`
- Explanation: The digits are already minimal, so spending swaps is unnecessary.
