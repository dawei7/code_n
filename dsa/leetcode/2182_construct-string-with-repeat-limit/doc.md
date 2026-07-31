# Construct String With Repeat Limit

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2182 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Greedy, Heap (Priority Queue), Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/construct-string-with-repeat-limit/) |

## Problem Description

### Goal

Rearrange some or all characters from a lowercase string `s` to form a new
string. No letter may occur more than `repeatLimit` times consecutively.
Characters may be discarded when using them would violate that restriction;
using every supplied character is not required.

Among all strings satisfying the limit, return the lexicographically largest.
At the first differing position, the string containing the later alphabetic
letter is larger. If one string is a prefix of the other, the longer string is
larger.

### Function Contract

**Inputs**

- `s`: a string of lowercase English letters.
- `repeatLimit`: the maximum permitted length of any same-letter run.

The inputs satisfy
$1\le\texttt{repeatLimit}\le\lvert\texttt{s}\rvert\le10^5$.

**Return value**

Return the lexicographically largest string obtainable from the available
characters without exceeding the consecutive-repeat limit.

### Examples

**Example 1**

- Input: `s = "cczazcc"`, `repeatLimit = 3`
- Output: `"zzcccac"`

**Example 2**

- Input: `s = "aababab"`, `repeatLimit = 2`
- Output: `"bbabaa"`
- Explanation: one `a` remains unused because no smaller separator exists
  after the final allowed run.

**Example 3**

- Input: `s = "aaaaa"`, `repeatLimit = 2`
- Output: `"aa"`
