# Largest Number After Mutating Substring

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1946 |
| Difficulty | Medium |
| Topics | Array, String, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-number-after-mutating-substring/) |

## Problem Description
### Goal
The string `num` represents a nonnegative integer using decimal digits. A
length-10 array `change` defines a replacement for every digit: digit `d` maps
to `change[d]`.

You may choose at most one substring, meaning one contiguous sequence of
positions, and replace every digit in that substring according to the mapping.
You may also leave `num` unchanged. Return the string representing the largest
integer obtainable under those rules.

### Function Contract
**Inputs**

- `num`: a string of $N$ decimal digits, where
  $1 \le N \le 10^5$.
- `change`: an array of exactly 10 integers; `change[d]` is between 0 and 9
  for each original digit `d`.

**Return value**

- The numerically largest length-$N$ digit string obtainable by mutating zero
  or one contiguous substring of `num`.

### Examples
**Example 1**

- Input: `num = "132", change = [9, 8, 5, 0, 3, 6, 4, 2, 6, 8]`
- Output: `"832"`

**Example 2**

- Input: `num = "021", change = [9, 4, 3, 5, 7, 2, 1, 9, 0, 6]`
- Output: `"934"`

**Example 3**

- Input: `num = "5", change = [1, 4, 7, 5, 3, 2, 5, 6, 9, 4]`
- Output: `"5"`

### Required Complexity
- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Start at the earliest strict improvement**

Equal-length decimal strings are ordered by their first differing digit.
Therefore the optimal mutation must begin at the earliest position whose
replacement is strictly larger than its original digit. Starting earlier on
only equal replacements changes nothing, while starting at a harmful
replacement would make the result smaller before any later benefit could
matter.

Scan from left to right without mutating until such a strict improvement
appears. Replace that digit and mark the substring as started.

**Extend through every non-harmful replacement**

After the substring starts, continue across replacements that are greater than
or equal to their original digits. A greater replacement improves the result;
an equal replacement keeps the value unchanged and preserves contiguity so a
later beneficial digit can still be included.

Stop permanently at the first replacement that is smaller than its original
digit. Including it would create the earliest harmful difference after the
already fixed prefix, making the number smaller than ending the substring just
before it. Because only one substring may be mutated, no later position can be
changed after this stop.

These choices maximize the earliest position at which any candidate can differ
from `num`, then maximize every following position until mutation would become
harmful. Lexicographic and numeric order coincide for equal-length digit
strings, so the constructed result is globally largest.

#### Complexity detail

The scan examines each of the $N$ digits at most once, and joining the mutable
digit list is another linear pass, for $O(N)$ time. The mutable result contains
$N$ characters, so the auxiliary space is $O(N)$.

#### Alternatives and edge cases

- **Enumerate every substring:** Apply the mapping to every possible interval
  and retain the largest result. This is exhaustive but requires at least
  $O(N^2)$ candidates and substantially more copying.
- **Mutate every locally improved digit:** Changing disjoint beneficial
  positions violates the single-substring rule when a harmful digit separates
  them.
- Equal replacements before the first improvement may be skipped without
  changing the result.
- Equal replacements after mutation starts must not end the substring because
  later improvements may still be reachable.
- If no replacement is strictly larger, choosing no substring is optimal.
- A harmful replacement before mutation starts is simply skipped; a later
  position may still begin the chosen substring.
- Leading zeroes are ordinary positions and remain part of the returned
  length-$N$ string.

</details>
