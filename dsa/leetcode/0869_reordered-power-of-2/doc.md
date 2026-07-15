# Reordered Power of 2

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 869 |
| Difficulty | Medium |
| Topics | Hash Table, Math, Sorting, Counting, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/reordered-power-of-2/) |

## Problem Description
### Goal
Given a positive integer `n`, rearrange all of its decimal digits in any order, including their original order. Every digit must be used exactly once, and the resulting decimal representation may not begin with `0`.

Return `true` if at least one permitted ordering forms a power of two, and return `false` otherwise. A valid target has the form $2^e$ for some nonnegative integer exponent $e$; the task asks only whether such an ordering exists, not which ordering produces it.

### Function Contract
**Inputs**

- `n`: a positive integer where $1 \leq n \leq 10^9$.

Let $d$ be the number of decimal digits in `n`, so $1 \leq d \leq 10$.

**Return value**

Return `true` exactly when the digits of `n` can be reordered, without a leading zero, to equal a power of two.

### Examples
**Example 1**

- Input: `n = 1`
- Output: `true`

The original ordering is $2^0$.

**Example 2**

- Input: `n = 10`
- Output: `false`

Neither `10` nor the only other ordering `01` is a valid power-of-two representation.

**Example 3**

- Input: `n = 46`
- Output: `true`

Reordering the digits produces `64`, which is $2^6$.

### Required Complexity
- **Time:** $O(d)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**A digit multiset determines reorderability**

Represent an integer by a ten-entry signature whose entry for digit `x` is the number of times `x` occurs. Two positive integers can be reordered into one another exactly when these signatures match: equality is necessary because reordering preserves every count, and it is sufficient because the source digits can be placed in the target's order.

A power of two's ordinary decimal representation never begins with zero. Therefore matching its signature automatically proves that a valid nonzero-leading ordering exists, even when `n` contains zeros; there is no need to test leading-zero permutations separately.

**Compare against the bounded power signatures**

The input has at most ten digits. Powers from $2^0$ through $2^{33}$ cover every power of two with at most ten decimal digits that could share its signature. Precompute their ten-count signatures once, compute the signature of `n`, and test set membership.

If a match exists, arranging the digits exactly like that power gives a valid result. If none exists, every same-digit-count power has been considered, so no allowed reordering can succeed.

#### Complexity detail

Building the signature processes the $d$ digits of `n` once, giving $O(d)$ time. The power-signature set has a fixed 34 entries under the stated bound, and each signature has exactly ten counters; per-call and fixed precomputed storage are therefore $O(1)$.

#### Alternatives and edge cases

- **Enumerate unique digit permutations:** It is correct and can skip leading zero, but up to $d!$ orderings make it factorial in the worst case.
- **Sort decimal digits:** Comparing the sorted digit string with every bounded power is concise, though sorting costs $O(d\log d)$ rather than counting in one pass.
- **Test only the original integer:** The original order is allowed but is not the only one; `46` succeeds through `64`.
- **Leading zeros:** An ordering such as `01` is invalid, but signature equality with an actual power always supplies a valid ordering.
- **Repeated digits:** Counts preserve multiplicity, so no duplicate permutation handling is needed.
- **`n = 1`:** It is already $2^0$ and returns `true`.
- **Ten-digit input bound:** Only `1000000000` occurs at that length within the domain, and its signature matches none of the bounded powers.

</details>
