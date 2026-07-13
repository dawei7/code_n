# Restore IP Addresses

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 93 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/restore-ip-addresses/) |

## Problem Description
### Goal
You are given a string containing only decimal digits. Restore IPv4 punctuation by inserting exactly three dots without deleting, reordering, or changing any digit, thereby creating four nonempty segments.

Each segment must represent an integer from `0` through `255` and cannot contain a leading zero unless it is exactly `"0"`. Return every valid restored address, in any order, with no duplicates. If the string length or digit values cannot support four legal segments, return an empty list.

### Function Contract
**Inputs**

- `s`: a string containing only decimal digits

**Return value**

All valid restored addresses in any order.

### Examples
**Example 1**

- Input: `s = "25525511135"`
- Output: `["255.255.11.135","255.255.111.35"]`

**Example 2**

- Input: `s = "0000"`
- Output: `["0.0.0.0"]`

**Example 3**

- Input: `s = "101023"`
- Output: five valid addresses

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Each recursion level chooses one IPv4 segment boundary**

Backtrack from the current string index with a path of completed segments. The next segment can contain one, two, or three digits. Accumulate its numeric value incrementally and stop once it exceeds `255`, since adding another digit can only increase it.

If the segment begins with `0`, allow the one-character segment `"0"` and stop before trying a longer length. This rejects noncanonical forms such as `"00"` and `"01"` without rejecting zero itself.

**Remaining digits must fit the remaining segment count**

If `r = 4 - len(path)` segments remain, the unconsumed suffix must contain at least `r` digits and at most `3r`. Fewer digits cannot give every segment one character; more digits cannot fit under the three-character limit. Reject either state before parsing candidates.

Emit only when four segments have been chosen and the index is exactly at the string end. Reaching four segments early or consuming all digits with fewer than four segments is not a valid address.

**The path represents the source prefix without losing digits**

The path contains valid canonical segments whose concatenated digit text equals exactly `s[:index]`. Every recursive branch chooses a different next boundary, and popping after recursion restores the parent prefix. No branch reorders, inserts, or discards a source digit.

**Trace leading-zero pruning**

For `010010`, the first segment must be `0`. Subsequent valid choices produce `0.10.0.10` and `0.100.1.0`; choices such as `01` are rejected by the leading-zero rule.

**Segment boundaries are the complete address search space**

Every emitted path contains four segments, each satisfying the length, leading-zero, and numeric-range rules, and consumes the entire source. It therefore spells a valid restored address.

Conversely, any valid restoration chooses three boundaries that divide the source into four lengths from one through three. The search enumerates those segment lengths, and its checks accept every segment that belongs to the valid address. Different boundary sequences produce different dotted strings, so all restorations appear once.

#### Complexity detail

IPv4 fixes four segments of at most three digits, so at most $3^{4}$ bounded branches and constant-size paths are explored; under the public contract this is $O(1)$ time and auxiliary space. Returned strings are also bounded in count and length.

#### Alternatives and edge cases

- **Enumerate three dot indices:** is also bounded and correct but has less direct segment-level pruning.
- **Regular expressions:** can validate a finished address but do not naturally generate all partitions.
- **Parse arbitrary-length prefixes:** wastes work because IPv4 segments can never exceed three digits.
- Strings shorter than four or longer than twelve digits fail immediately through the remaining-length bound.
- Output order is unrestricted. Converting a candidate segment to an integer must not erase its original leading-zero evidence before validation.

</details>
