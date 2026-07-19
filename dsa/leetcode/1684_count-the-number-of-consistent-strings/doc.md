# Count the Number of Consistent Strings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1684 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Bit Manipulation, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-the-number-of-consistent-strings/) |

## Problem Description
### Goal

The string `allowed` contains distinct lowercase English letters and defines which characters may appear in a consistent string. A word is consistent only if every one of its characters occurs in `allowed`; repeated uses of an allowed character remain valid, and a single character outside the set makes the whole word inconsistent.

Inspect each string in `words` independently and return how many of them are consistent. The answer counts array entries rather than distinct word values, so equal words at different positions each contribute when they satisfy the rule.

### Function Contract
**Inputs**

- `allowed`: a nonempty string of distinct lowercase English letters
- `words`: a nonempty list of nonempty lowercase English strings

Let

$$
S = \lvert \texttt{allowed} \rvert + \sum_{w \in \texttt{words}} \lvert w \rvert.
$$

**Return value**

The number of entries in `words` whose every character belongs to `allowed`.

### Examples
**Example 1**

- Input: `allowed = "ab", words = ["ad", "bd", "aaab", "baa", "badab"]`
- Output: `2`

Only `"aaab"` and `"baa"` use no letter outside `"ab"`.

**Example 2**

- Input: `allowed = "abc", words = ["a", "b", "c", "ab", "ac", "bc", "abc"]`
- Output: `7`

Every word is consistent.

**Example 3**

- Input: `allowed = "cad", words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]`
- Output: `4`

The consistent entries are `"cc"`, `"acd"`, `"ac"`, and `"d"`.
