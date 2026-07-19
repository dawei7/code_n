# Encode String with Shortest Length

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 471 |
| Difficulty | Hard |
| Topics | String, Dynamic Programming |
| Official Link | [LeetCode](https://leetcode.com/problems/encode-string-with-shortest-length/) |

## Problem Description
### Goal
Given a nonempty lowercase string, represent repeated consecutive text with notation `count[encoded_block]`, meaning the decoded block repeated `count` times. Encoded blocks may themselves contain shorter nested encodings, and literal text may be combined with encoded regions.

Return an equivalent representation with the minimum character length among all valid choices. Leave a region literal when encoding it is not strictly shorter, and preserve the exact decoded string. Repetition must tile a region completely; similar prefixes with leftover characters need separate treatment. When several shortest encodings exist, any valid minimum-length form is acceptable under the semantic contract.

### Function Contract
**Inputs**

- `s`: a lowercase string

**Return value**

- A shortest string that decodes to `s`; leave text unencoded whenever an encoding is not strictly shorter

### Examples
**Example 1**

- Input: `s = "aaa"`
- Output: `"aaa"`

**Example 2**

- Input: `s = "aaaaa"`
- Output: `"5[a]"`

**Example 3**

- Input: `s = "aabcaabcd"`
- Output: `"2[aabc]d"`
