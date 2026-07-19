# Maximum Number of Vowels in a Substring of Given Length

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1456 |
| Difficulty | Medium |
| Topics | String, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/) |

## Problem Description
### Goal

Given a lowercase English string `s` and an integer `k`, consider every
substring whose length is exactly `k`. A substring is a contiguous sequence of
characters, so its positions must be adjacent in the original string; letters
cannot be skipped or rearranged.

The English vowels for this problem are exactly `a`, `e`, `i`, `o`, and `u`.
Count how many of those vowels occur in each length-$k$ substring and return
the largest count. Repeated vowels count separately, and the answer may range
from $0$ when no eligible window contains a vowel to $k$ when some whole
window consists of vowels.

### Function Contract
**Inputs**

- `s`: a string of $n$ lowercase English letters, where
  $1 \le n \le 10^5$.
- `k`: the required substring length, where $1 \le k \le n$.

**Return value**

Return an integer equal to the maximum number of characters from
`{"a", "e", "i", "o", "u"}` in any contiguous substring of `s` having
exactly length `k`.

### Examples
**Example 1**

- Input: `s = "abciiidef", k = 3`
- Output: `3`
- Explanation: The window `"iii"` contains three vowels, which is the largest
  possible count for a length-$3$ window.

**Example 2**

- Input: `s = "aeiou", k = 2`
- Output: `2`
- Explanation: Every adjacent pair consists only of vowels.

**Example 3**

- Input: `s = "leetcode", k = 3`
- Output: `2`
- Explanation: Windows such as `"lee"`, `"eet"`, and `"ode"` each contain
  two vowels.
