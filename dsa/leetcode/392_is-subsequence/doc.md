# Is Subsequence

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 392 |
| Difficulty | Easy |
| Topics | Two Pointers, String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/is-subsequence/) |

## Problem Description
### Goal
Given strings `s` and `t`, decide whether `s` is a subsequence of `t`. You may delete any number of characters from `t`, but the characters retained to form `s` must keep their original relative order.

Return `True` when every character of `s` can be matched from left to right within `t`, not necessarily at adjacent positions. Repeated characters require separate later occurrences, and the matching indices cannot move backward. The empty string is a subsequence of every string, while a nonempty `s` cannot be a subsequence of an empty or too-short `t`.

### Function Contract
**Inputs**

- `s`: the candidate subsequence
- `t`: the source string whose relative character order must be preserved

**Return value**

- Return `True` when every character of `s` can be matched in order within `t`; otherwise return `False`.

### Examples
**Example 1**

- Input: `s = "abc", t = "ahbgdc"`
- Output: `True`

**Example 2**

- Input: `s = "axc", t = "ahbgdc"`
- Output: `False`

**Example 3**

- Input: `s = "", t = "anything"`
- Output: `True`

### Required Complexity

- **Time:** $O(|t|)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Track only the next required character**

Maintain an index `matched` into `s`, initially zero. Scan `t` from left to right. Whenever the current source character equals `s[matched]`, advance `matched`; otherwise discard that source character.

**Greedily take the earliest possible match**

Matching a required character at its earliest available position cannot hurt a later requirement: it leaves at least as much of `t` unconsumed as choosing any later equal character would. Thus no backtracking or alternative match positions need to be stored.

**Why reaching the end of the candidate is decisive**

Every advancement pairs the next character of `s` with a strictly later position in `t`, preserving order. If `matched = len(s)`, those pairs witness that `s` is a subsequence. If the source scan ends earlier, the unmatched suffix has no remaining source positions and no valid embedding exists.

#### Complexity detail

Each character of `t` is inspected once, for $O(|t|)$ time; at most $| s |$ successful pointer advances occur within that scan. The pointer uses $O(1)$ space.

#### Alternatives and edge cases

- **Iterator membership idiom:** consumes `t` monotonically for each required character and has the same linear bound.
- **Longest-common-subsequence dynamic programming:** is correct but uses $O(|s||t|)$ time for a Boolean question that needs no table.
- **Preprocess positions in `t`:** stores each character's sorted indices and answers many different subsequence queries efficiently with binary search.
- The empty string is a subsequence of every string, including another empty string.
- A nonempty `s` cannot be a subsequence of an empty `t`.
- Repeated characters must match distinct source positions in increasing order.
- Equal strings are subsequences without any deletions.

</details>
