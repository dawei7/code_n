# Naming a Company

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2306 |
| Difficulty | Hard |
| Topics | Array, Hash Table, String, Bit Manipulation, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/naming-a-company/) |

## Problem Description
### Goal
`ideas` contains distinct lowercase names available during a company-naming
process. Choose two different entries, call them idea A and idea B, and
exchange their first letters.

The ordered selection is valid only when both newly formed names are absent
from the original `ideas`. When valid, their concatenation in A-then-B order,
separated by a space, is a distinct company name. Return the number of
distinct valid company names. Reversing a valid selection changes the order
and therefore counts separately.

### Function Contract
**Inputs**

- `ideas`: An array of $n$ unique strings containing only lowercase English
  letters.

The contract guarantees $2\le n\le5\cdot10^4$ and each string has length from
1 through 10.

**Return value**

The number of ordered pairs of distinct ideas whose first-letter swap produces
two names not present in the original array.

### Examples
**Example 1**

- Input: `ideas = ["coffee", "donuts", "time", "toffee"]`
- Output: `6`
- Explanation: Three unordered selections work, including `coffee` with
  `donuts`; each orientation produces a different ordered company name.

**Example 2**

- Input: `ideas = ["lack", "back"]`
- Output: `0`
- Explanation: Swapping the initials recreates the two existing names.
