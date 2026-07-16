# Maximum Number of Non-Overlapping Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1520 |
| Difficulty | Hard |
| Topics | Hash Table, String, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/) |

## Problem Description
### Goal

Choose a collection of nonempty, pairwise non-overlapping substrings from a lowercase string `s`. Whenever a selected substring contains a character, it must contain every occurrence of that character in the entire source string; a substring cannot capture only some copies of one of its letters.

First maximize how many substrings are selected. Among collections attaining that maximum count, minimize the sum of their lengths. The minimum-total-length optimum is guaranteed to be unique, although its substrings may be returned in any order.

### Function Contract
**Inputs**

- `s`: A lowercase English string of length $n$, where $1 \leq n \leq 10^5$.

**Return value**

Return the unique minimum-total-length collection among all maximum-cardinality collections of valid, disjoint substrings. The app-local implementation returns them in left-to-right source order.

### Examples
**Example 1**

- Input: `s = "adefaddaccc"`
- Output: `["e", "f", "ccc"]`
- Explanation: Selecting `e` and `f` separately is better than the combined `ef`, and the independent `ccc` interval adds a third substring.

**Example 2**

- Input: `s = "abbaccd"`
- Output: `["bb", "cc", "d"]`
- Explanation: `abba` is valid, but replacing it with `bb` preserves three selected substrings while reducing total length.

**Example 3**

- Input: `s = "abcd"`
- Output: `["a", "b", "c", "d"]`
- Explanation: Every character occurs once, so each single-character substring is independently valid.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Derive the smallest interval for each possible start**

Record the first and last occurrence of every letter. A minimal valid substring can start only at the first occurrence of its initial letter; starting later would omit that earlier occurrence.

For such a start `left`, initialize `right` to the letter's last occurrence and scan the current interval. Every encountered letter requires its own last occurrence to be included, so extend `right` as needed. If an encountered letter first appears before `left`, this start can never form a valid interval: including all copies would require moving the left boundary, so discard it. Otherwise the scan ends at the smallest valid interval beginning at `left`.

Although intervals may expand, there are at most 26 candidate starts. Each expansion scans at most $n$ positions, so the fixed lowercase alphabet keeps total work linear in $n$.

**Select intervals by earliest finishing boundary**

Process candidate starts from left to right. If a valid interval begins after the last selected interval, append it. If it overlaps the most recently selected interval, replace that interval with the new one.

The new overlapping candidate ends no later than the previous selection: otherwise its start would lie inside the already closed previous interval and its required first occurrences would invalidate it. Replacing therefore never reduces the number of intervals that can be chosen later, while it shortens the current choice or leaves its length minimal. This is the usual earliest-finish interval-scheduling exchange argument.

Every appended interval increases the cardinality, and every overlap replacement preserves cardinality while choosing the tighter finishing interval. The final collection consequently has maximum count and, among those collections, minimum total length.

#### Complexity detail

The first/last-occurrence pass is $O(n)$. At most 26 candidate starts each scan no more than $n$ positions; because 26 is a fixed alphabet size, closure expansion is $O(n)$. Greedy selection is absorbed in the same scan.

The two 26-entry boundary arrays use constant auxiliary space. The returned substrings occupy output space, which is excluded from the $O(1)$ auxiliary bound.

#### Alternatives and edge cases

- **Generate and sort all valid intervals:** this can recover the same interval-scheduling solution, but enumerating arbitrary substrings costs at least quadratic time.
- **Dynamic programming over positions:** possible after deriving valid intervals, but earliest-finish greedy already proves both objectives and uses less state.
- **Take every letter's raw first-to-last span:** spans may contain another letter whose occurrences extend outside them; closure expansion is mandatory.
- **One character:** the entire one-character string is the only and optimal answer.
- **All characters equal:** every valid substring containing that character must be the whole string.
- **All characters distinct:** each character is its own optimal substring.
- **Nested intervals:** the smaller valid interval replaces an overlapping larger one, preserving count and minimizing length.
- **Return order:** the source accepts any order, while left-to-right order gives deterministic local judging.

</details>
