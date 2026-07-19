# Check if an Original String Exists Given Two Encoded Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2060 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/) |

## Problem Description

### Goal

To encode a lowercase original string, split it into nonempty substrings, optionally replace any chosen substring by the decimal representation of its length, and concatenate all resulting pieces. A run of digits in the encoding may therefore represent one length or several adjacent lengths; for example, `"123"` can arise from lengths $123$, $1+23$, $12+3$, or $1+2+3$.

Given two such encoded strings, determine whether at least one lowercase original string could produce both. Each input contains letters and digits `1` through `9`, has length at most $40$, and contains no digit run longer than three characters.

### Function Contract

**Inputs**

- `s1`, `s2`: nonempty encoded strings of lengths $n_1$ and $n_2$, each at most $40$, containing lowercase letters and digits `1` through `9`; consecutive digit runs have length at most three.

Let $B$ be the number of distinct unmatched-length balances reachable for one pair of input positions.

**Return value**

- Return `true` when some lowercase string can be encoded as both `s1` and `s2`; otherwise return `false`.

### Examples

**Example 1**

- Input: `s1 = "internationalization", s2 = "i18n"`
- Output: `true`
- Explanation: The middle eighteen letters may be replaced by their length.

**Example 2**

- Input: `s1 = "l123e", s2 = "44"`
- Output: `true`
- Explanation: Both may encode `"leetcode"` using different substring partitions.

**Example 3**

- Input: `s1 = "a5b", s2 = "c5b"`
- Output: `false`
- Explanation: Their first required literal letters disagree.
