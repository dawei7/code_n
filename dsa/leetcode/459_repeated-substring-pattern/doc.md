# Repeated Substring Pattern

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 459 |
| Difficulty | Easy |
| Topics | String, String Matching |
| Official Link | [LeetCode](https://leetcode.com/problems/repeated-substring-pattern/) |

## Problem Description
### Goal
Given a nonempty string `s`, determine whether it can be constructed by repeating one of its proper nonempty prefixes. Every repetition must use the identical substring, concatenated without gaps, overlaps, or leftover characters.

Return `True` when some shorter unit repeated an integer number of times at least two equals the complete string, and `False` otherwise. The unit length must divide `len(s)` exactly. Repeated characters alone are insufficient if no common block tiles the entire string, while a one-character string cannot use a shorter nonempty unit.

### Function Contract
**Inputs**

- `s`: a nonempty string

**Return value**

- `True` when some proper prefix repeated an integer number of times equals `s`; otherwise `False`

### Examples
**Example 1**

- Input: `s = "abab"`
- Output: `True`

**Example 2**

- Input: `s = "aba"`
- Output: `False`

**Example 3**

- Input: `s = "abcabcabcabc"`
- Output: `True`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Measure reusable prefix structure**

Build the KMP prefix table. At position `i`, the table stores the length of the longest proper prefix of `s[:i + 1]` that is also its suffix. On a mismatch, fall back through previously computed borders instead of restarting comparisons, so every character contributes amortized constant work.

**Derive the only possible shortest period**

Let `border` be the final prefix-table value. If the string repeats a block, removing one copy from the front leaves a suffix equal to a prefix, and the candidate block length is `period = n - border`. Conversely, a border of that length means characters align across a shift of `period` positions.

**Require the period to tile the whole string**

Alignment alone is not enough: the candidate period must divide `n`. Therefore repetition exists exactly when `border > 0` and `n % period = 0`. Under those conditions, the prefix-table alignment propagates through each full block, making every block equal to the first; without divisibility, a partial final block prevents a valid tiling.

#### Complexity detail

KMP fallback moves through already computed border lengths, so the table is built in $O(n)$ time. The prefix array uses $O(n)$ space.

#### Alternatives and edge cases

- **Doubled-string search:** `s` appears inside `(s + s)[1:-1]` exactly when it has a nontrivial rotation, giving linear-time behavior with a linear-time matcher.
- **Z-function:** a position whose match reaches the end and divides `n` identifies a repeating period in $O(n)$ time.
- **Try every candidate length:** repeatedly comparing a candidate against the full string can take $O(n^2)$ time.
- **One character:** has no shorter nonempty block and returns `False`.
- **All equal characters:** any one-character block repeats when length is at least two.
- **Border without divisibility:** a matching prefix and suffix does not imply repetition unless its derived period tiles the full length.
- **Overlapping borders:** use the longest final border; KMP fallback has already encoded all shorter alternatives.

</details>
