# Largest Time for Given Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 949 |
| Difficulty | Medium |
| Topics | Array, String, Backtracking, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-time-for-given-digits/) |

## Problem Description

### Goal

An array `arr` contains exactly four decimal digits. Rearrange those four supplied occurrences, using every digit exactly once, to form a time in the 24-hour string format `"HH:MM"`.

A valid hour ranges from `"00"` through `"23"`, and a valid minute ranges from `"00"` through `"59"`. Among all valid arrangements, return the latest time of day; `"00:00"` is the earliest possible time and `"23:59"` is the latest. If the digits cannot form any valid 24-hour time, return the empty string `""`.

### Function Contract

**Inputs**

- `arr`: a list of exactly four integers, each from $0$ through $9$. Repeated digits are allowed.

**Return value**

Return the latest valid time as a zero-padded `"HH:MM"` string, or `""` when no permutation is valid.

### Examples

**Example 1**

- Input: `arr = [1, 2, 3, 4]`
- Output: `"23:41"`

Several arrangements form valid times, and `"23:41"` is the latest among them.

**Example 2**

- Input: `arr = [5, 5, 5, 5]`
- Output: `""`

The only distinct arrangement is `"55:55"`, which is not a valid 24-hour time.

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Enumerate the complete fixed domain.** Generate every permutation of the four digit occurrences. There are only $4! = 24$ index arrangements, so duplicates may cause the same digit sequence to be inspected more than once without affecting the constant bound.

For a permutation `(a, b, c, d)`, compute the hour with `a * 10 + b` and the minute with `c * 10 + d`. Reject the arrangement unless the hour is below $24$ and the minute is below $60$. Convert each valid time to its number of minutes after midnight using `hour * 60 + minute`, and retain the greatest such value.

Every permitted answer uses the four occurrences in some order, so it appears among the enumerated permutations. Every retained candidate satisfies both clock ranges. Taking the maximum minute total therefore selects exactly the latest valid time. If no candidate is retained, return `""`; otherwise split the maximum back into hours and minutes and format both fields with two digits.

#### Complexity detail

The input always has four digits, so at most 24 permutations are evaluated and the work is $O(1)$. The permutation iterator, loop variables, and best minute total use $O(1)$ space because their sizes cannot grow with any input dimension.

#### Alternatives and edge cases

- **Scan times backward:** Test `"23:59"`, `"23:58"`, and so on until the time's digit multiset matches `arr`. This is correct but may inspect nearly all 1440 minutes.
- **Position-by-position backtracking:** Fill the four clock positions while pruning invalid hour and minute prefixes. It remains constant for this input size but requires more boundary logic.
- **Greedy digit placement:** Choosing the largest digit that currently fits each position can require backtracking; an early hour choice may leave no valid minute even though a smaller hour works.
- **Repeated digits:** Permutations are arrangements of occurrences, so equal values must still be used with their full multiplicity.
- **Leading zeros:** Times such as `"07:05"` are valid and must retain both zero-padded fields.
- **Midnight:** Four zeros produce `"00:00"`, not an empty result.
- **No valid hour or minute:** Return exactly `""` rather than a sentinel time.

</details>
