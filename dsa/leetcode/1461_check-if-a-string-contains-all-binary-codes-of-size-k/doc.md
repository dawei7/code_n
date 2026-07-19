# Check If a String Contains All Binary Codes of Size K

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1461 |
| Difficulty | Medium |
| Topics | Hash Table, String, Bit Manipulation, Rolling Hash, Hash Function |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/) |

## Problem Description
### Goal

Given a binary string `s` and a positive integer `k`, determine whether
every possible binary code of length exactly `k` occurs somewhere in `s`
as a substring. A substring is contiguous, and occurrences may overlap.

There are $2^k$ different length-$k$ binary strings, ranging from the all-zero
code through the all-one code. Return `true` only when each of those distinct
codes appears at least once; repeated occurrences of one code do not compensate
for another code being absent.

### Function Contract
**Inputs**

- `s`: a string of $n$ characters, each either `"0"` or `"1"`, where
  $1 \le n \le 5\cdot10^5$.
- `k`: the required code length, where $1 \le k \le 20$.

**Return value**

Return `true` if the set of all contiguous length-$k$ substrings of `s`
contains all $2^k$ binary codes; otherwise return `false`.

### Examples
**Example 1**

- Input: `s = "00110110", k = 2`
- Output: `true`
- Explanation: `"00"`, `"01"`, `"10"`, and `"11"` all occur.

**Example 2**

- Input: `s = "0110", k = 1`
- Output: `true`
- Explanation: Both one-bit codes occur.

**Example 3**

- Input: `s = "0110", k = 2`
- Output: `false`
- Explanation: The code `"00"` is absent.
