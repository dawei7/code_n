# Check if All Characters Have Equal Number of Occurrences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1941 |
| Difficulty | Easy |
| Topics | Hash Table, String, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/) |

## Problem Description
### Goal
You are given a string `s` containing only lowercase English letters. The
number of occurrences of a character is the number of positions in `s` that
contain that character. Characters that do not appear in the string are not
part of the comparison.

Determine whether all distinct characters present in `s` occur equally often.
Return `true` when their positive occurrence counts are identical, and return
`false` as soon as at least two present characters have different counts.

### Function Contract
**Inputs**

- `s`: a string of lowercase English letters with length $N$, where
  $1 \le N \le 1000$.

**Return value**

- `true` if every distinct character appearing in `s` has the same positive
  occurrence count; otherwise, `false`.

### Examples
**Example 1**

- Input: `s = "abacbc"`
- Output: `true`
- Explanation: `a`, `b`, and `c` each occur twice.

**Example 2**

- Input: `s = "aaabb"`
- Output: `false`
- Explanation: `a` occurs three times while `b` occurs twice.

**Example 3**

- Input: `s = "abcd"`
- Output: `true`
- Explanation: Every present character occurs once.

### Required Complexity
- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Build the occurrence profile**

Allocate 26 counters, one for each lowercase English letter. Scan `s` once and
increment the counter selected by each character. The fixed alphabet gives
direct access to every occurrence count without storing the characters
themselves.

**Compare only characters that appear**

Because $N \ge 1$, at least one counter is positive. Use the first positive
counter as the required frequency, then inspect all 26 counters. A zero counter
represents a character absent from `s` and is irrelevant; every positive
counter must equal the required frequency.

If the comparison succeeds, every appearing character has the same count. If
it fails, the required frequency and the unequal positive counter identify two
appearing characters with different counts. These two directions establish
that the returned Boolean exactly matches the contract.

#### Complexity detail

The scan performs $N$ constant-time counter updates. Inspecting the 26 counters
adds a fixed amount of work, so the total time is $O(N)$. The counter array has
exactly 26 entries regardless of $N$, which is $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Hash-map counting:** A dictionary or `Counter` can store only characters
  that appear and makes the final comparison concise, but it uses space
  proportional to the number of distinct characters in a generalized
  alphabet.
- **Repeated full-string counting:** Calling a full-string count for each
  possible lowercase letter remains $O(N)$ under this fixed 26-letter
  alphabet, but it scans the same input repeatedly and has a larger constant
  factor.
- A one-character string is valid because its sole present character sets the
  only positive frequency.
- A string containing just one distinct character is valid regardless of how
  many times that character repeats.
- If all characters are distinct, every positive count is one, so the result
  is `true`.
- Zero counters must be ignored; absent letters do not need to match the
  positive occurrence count.

</details>
