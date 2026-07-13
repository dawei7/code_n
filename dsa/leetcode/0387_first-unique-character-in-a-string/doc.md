# First Unique Character in a String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 387 |
| Difficulty | Easy |
| Topics | Hash Table, String, Queue, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/first-unique-character-in-a-string/) |

## Problem Description
### Goal
Given a string of lowercase English letters, find the earliest character occurrence whose total frequency across the entire string is exactly one. A character cannot qualify merely because it has not appeared earlier if another occurrence appears later.

Return the zero-based index of the first unique character. If every character repeats, return `-1`. Repeated characters may be separated by many positions and still disqualify one another. The task returns an index rather than the character itself, and among several unique characters only the leftmost position is accepted.

### Function Contract
**Inputs**

- `s`: a string of lowercase English letters

**Return value**

- Return the zero-based index of the first character with total frequency one, or `-1` when no such character exists.

### Examples
**Example 1**

- Input: `s = "leetcode"`
- Output: `0`

**Example 2**

- Input: `s = "loveleetcode"`
- Output: `2`

**Example 3**

- Input: `s = "aabb"`
- Output: `-1`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Frequency is a whole-string property**

Whether a position is unique cannot be decided from its prefix alone because the same character may reappear later. First scan the complete string and count each lowercase letter in a fixed array of 26 entries.

**Use the original order only after counts are known**

Scan `s` again from left to right. The first position whose counter equals one is unique globally, and left-to-right inspection makes it the earliest such position. If the scan ends without finding one, every character occurs at least twice and the answer is `-1`.

**Why two passes are sufficient**

The first pass records the exact multiplicity of every possible character. The second tests positions in increasing index order against those final multiplicities. Returning at the first count of one therefore satisfies both requirements—global uniqueness and minimum index—while no omitted earlier position could be unique.

#### Complexity detail

For a string of length `n`, the two scans take $O(n)$ time. The frequency array always has 26 entries, so its space usage is $O(1)$.

#### Alternatives and edge cases

- **Hash-map counts:** has the same linear time and works for an unrestricted alphabet, using space proportional to the number of distinct characters.
- **Queue of candidate indices:** supports streaming updates but adds storage that is unnecessary when the full string is already available.
- **Call a counting operation at every position:** can repeatedly scan the string and take $O(n^2)$ time.
- A one-character string returns index zero.
- If every character is repeated, return `-1`.
- The first unique character may appear only at the last index.
- Later duplicates can invalidate characters that looked unique in an early prefix.

</details>
