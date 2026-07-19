# Find the Kth Largest Integer in the Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1985 |
| Difficulty | Medium |
| Topics | Array, String, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/) |

## Problem Description
### Goal
The array `nums` contains non-negative integers represented as decimal strings.
Each representation contains only digits and has no leading zero, except that
the integer zero itself is written as `"0"`. Values may contain far more digits
than ordinary fixed-width integer types can store.

Order all entries by their numeric values from largest to smallest and return
the string occupying one-based rank `k`. Equal numeric strings remain separate
entries: if the maximum occurs twice, those copies occupy ranks one and two
rather than being deduplicated.

### Function Contract
**Inputs**

- `nums`: a list of $N$ valid decimal integer strings, where
  $1 \le N \le 10^4$ and every string has length from $1$ through $100$.
- `k`: the requested one-based descending rank, where $1 \le k \le N$.
- Let $L$ be the maximum string length in `nums`.

**Return value**

- The original string representing the `k`th largest numeric value, counting
  duplicate entries separately.

### Examples
**Example 1**

- Input: `nums = ["3", "6", "7", "10"], k = 4`
- Output: `"3"`

**Example 2**

- Input: `nums = ["2", "21", "12", "1"], k = 3`
- Output: `"2"`

**Example 3**

- Input: `nums = ["0", "0"], k = 2`
- Output: `"0"`

Both zero entries occupy their own rank.
