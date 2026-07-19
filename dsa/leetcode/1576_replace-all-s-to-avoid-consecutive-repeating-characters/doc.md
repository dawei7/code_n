# Replace All ?'s to Avoid Consecutive Repeating Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1576 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/) |

## Problem Description
### Goal

Given a string `s` containing lowercase English letters and `?` placeholders, replace every `?` with a lowercase English letter. The input guarantees that any consecutive equal characters already present can only be placeholders, so fixed letters do not themselves form an unrepairable adjacent repetition.

The completed string must contain no `?` characters and no pair of equal adjacent characters. Letters that were present in the input must remain unchanged; only placeholder positions may be modified.

Return any completed string satisfying these rules. More than one answer may be valid, and the judge accepts every valid completion rather than requiring a particular choice of replacement letters.

### Function Contract
**Inputs**

- `s`: A string of length $N$, where $1 \le N \le 100$, containing only lowercase English letters and `?`.

**Return value**

Return any length-$N$ lowercase string that preserves every fixed input letter, replaces every `?`, and has no equal adjacent characters.

### Examples
**Example 1**

- Input: `s = "?zs"`
- Output: `"azs"`

**Example 2**

- Input: `s = "ubv?w"`
- Output: `"ubvaw"`

**Example 3**

- Input: `s = "j?qg??b"`
- Output: `"jaqgacb"`

The displayed outputs are examples; other valid replacements are also accepted.
