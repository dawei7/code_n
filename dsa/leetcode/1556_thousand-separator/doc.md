# Thousand Separator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1556 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/thousand-separator/) |

## Problem Description
### Goal

You are given a non-negative integer `n`. Write its ordinary base-ten representation, but use a dot (`.`) as the thousands separator.

Starting at the rightmost digit, place a dot between each adjacent group of three digits. The leftmost group may contain one, two, or three digits, and a value with at most three digits has no separator. Return the resulting representation as a string.

### Function Contract
**Inputs**

- `n`: An integer satisfying $0 \le n \le 2^{31} - 1$.
- Let $D$ be the number of decimal digits in `n`, counting `0` as one digit. The source bound guarantees $1 \le D \le 10$.

**Return value**

Return the decimal digits of `n` with a dot before every three-digit group measured from the right. Do not add leading zeros or a leading or trailing dot.

### Examples
**Example 1**

- Input: `n = 987`
- Output: `"987"`

**Example 2**

- Input: `n = 1234`
- Output: `"1.234"`

**Example 3**

- Input: `n = 123456789`
- Output: `"123.456.789"`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Form groups from the direction that defines them**

Convert `n` to its decimal string. Thousands groups are determined from right to left, so repeatedly take the final three characters and append that slice to a list. The last extraction may contain fewer than three characters; it is the leftmost group and is still kept as-is.

These groups are discovered in reverse display order. Reverse their order once and join them with dots. Every non-leftmost group then contains exactly three original digits, and every boundary lies three digits farther left than the preceding boundary. Because slicing never changes the characters inside a group, removing the inserted dots recovers the original decimal representation, which establishes that the returned string has both the correct digits and separator positions.

**Handle zero without a special representation**

The decimal conversion of `0` is the one-character string `"0"`. The same loop extracts it as a single group, so zero naturally returns `"0"` without a separate formatting rule.

#### Complexity detail

For a general $D$-digit value, conversion, grouping, and joining take $O(D)$ time and the produced groups occupy $O(D)$ space. Under this problem's source contract, however, $D \le 10$. Both the work and storage are therefore bounded by constants, giving the required $O(1)$ time and $O(1)$ space.

A `bounded_domain` certificate replaces runtime scaling. Inputs cannot grow beyond ten digits, so timing tiers would measure fixed interpreter and conversion overhead instead of distinguishing meaningful asymptotic classes.

#### Alternatives and edge cases

- **Built-in numeric formatting:** format with comma grouping and replace commas with dots. This is concise, but manual grouping makes the required direction and separator invariant explicit and is portable to environments with different locale rules.
- **Forward scan with a countdown:** compute the first group's width from $D \bmod 3$, then append dots while scanning left to right. This is also correct but needs careful handling when the remainder is zero.
- **Repeated arithmetic division:** extract three-digit numeric chunks with division and remainder. It avoids slicing but must preserve zeros inside groups, such as the middle group in `1000001`.
- **Fewer than four digits:** values from `0` through `999` must contain no dot.
- **Exact transition:** `1000` becomes `"1.000"`; this is the first input requiring a separator.
- **Internal zeros:** each group after the first must retain all three positions, so `1000001` becomes `"1.000.001"`.
- **Upper bound:** `2147483647` has ten digits and must become `"2.147.483.647"`.

</details>
