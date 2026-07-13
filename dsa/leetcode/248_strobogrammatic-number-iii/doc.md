# Strobogrammatic Number III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 248 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Recursion |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/strobogrammatic-number-iii/) |

## Problem Description
### Goal
Given decimal strings `low` and `high` representing an inclusive nonnegative range without unnecessary leading zeroes, count the integers whose written digits remain unchanged after a 180-degree rotation. Valid mirrored digits use `0`, `1`, `6`, `8`, and `9` in their compatible pairings.

Return the number of strobogrammatic numerals `x` satisfying `low <= x <= high`, including either boundary when valid. Generated multi-digit forms may not begin with zero, while the single numeral `0` is allowed when inside the range. Compare potentially long bounds by numeric-string length and order rather than converting them unsafely to fixed-width integers.

### Function Contract
**Inputs**

- `low`: the inclusive lower bound without leading zeros
- `high`: the inclusive upper bound without leading zeros

**Return value**

The number of strobogrammatic integers `x` satisfying `low <= x <= high`.

### Examples
**Example 1**

- Input: `low = "50", high = "100"`
- Output: `3`

**Example 2**

- Input: `low = "0", high = "0"`
- Output: `1`

**Example 3**

- Input: `low = "0", high = "10"`
- Output: `3`

### Required Complexity

- **Time:** $O(d \cdot 5^{d/2})$
- **Space:** $O(d)$

<details>
<summary>Approach</summary>

#### General

**Generate only rotationally valid structures**

For every length from `len(low)` through `len(high)`, recursively place compatible digit pairs from outside inward. The middle of an odd length can be only $0$, $1$, or $8$.

**Length handles most bounds; lexical order handles ties**

Reject a leading zero for multi-digit candidates. At complete candidates, compare lexicographically only against a bound having the same length; equal-length decimal strings preserve numeric order.

Candidates shorter than `low` or longer than `high` are never generated. For an interior length, every valid candidate is automatically inside the numeric range. Only the two boundary lengths need comparison, avoiding integer conversion even when the bounds exceed native numeric types.

**Outer-to-inner pairs give each valid number one construction path**

Every recursive partial assignment contains only mirrored pairs that rotate into one another, so each completed candidate is strobogrammatic. Conversely, every strobogrammatic number uniquely determines those outer-to-inner pairs and its optional middle digit, giving it one construction path. The leading-zero, length, and inclusive boundary checks retain that candidate exactly when it represents a number in `[low, high]`.

#### Complexity detail

For maximum bound length $d$, the search explores $O(5^{d/2})$ pair assignments. Constructing or comparing a completed candidate costs $O(d)$, so a direct string-building implementation takes $O(d \cdot 5^{d/2})$ time in the worst case. Depth-first construction uses $O(d)$ working space; retaining generated strings instead of counting immediately would add output-sized storage.

#### Alternatives and edge cases

- **Scan every integer in the range:** depends on numeric magnitude rather than digit length.
- Single-value ranges, zero, and bounds with different lengths require inclusive handling.

</details>
