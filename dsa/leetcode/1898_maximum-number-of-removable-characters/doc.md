# Maximum Number of Removable Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1898 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, String, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Maximum Number of Removable Characters](https://leetcode.com/problems/maximum-number-of-removable-characters/) |

## Problem Description

### Goal

You receive strings `s` and `p`, where `p` is already a subsequence of `s`. You also receive `removable`, a list of distinct indices into the original string. For a chosen integer $k$, remove the characters at the first $k$ indices of this list. The indices always refer to their positions in the original `s`; deleting one character does not renumber the others.

Choose as many leading entries of `removable` as possible while ensuring that `p` remains a subsequence of the characters left in their original relative order. Return that maximum prefix length $k$, which may be zero or the entire length of `removable`.

### Function Contract

**Inputs**

- `s`: a lowercase English string of length $n$.
- `p`: a nonempty lowercase English string that is a subsequence of `s`.
- `removable`: an array of $r$ distinct zero-based indices of `s`, in removal order.
- The constraints satisfy $1 \le \lvert p \rvert \le n \le 10^5$ and $0 \le r < n$.

**Return value**

Return the greatest integer $k$ with $0 \le k \le r$ such that deleting the characters at `removable[0]` through `removable[k - 1]` leaves `p` as a subsequence.

### Examples

**Example 1**

- Input: `s = "abcacb", p = "ab", removable = [3, 1, 0]`
- Output: `2`
- Explanation: Removing original indices `3` and `1` leaves `"accb"`, which still contains `"ab"` as a subsequence. Removing index `0` as well destroys that subsequence.

**Example 2**

- Input: `s = "abcbddddd", p = "abcd", removable = [3, 2, 1, 4, 5, 6]`
- Output: `1`
- Explanation: After the first removal, `"abcddddd"` still contains `"abcd"`. The next removal makes that impossible.

**Example 3**

- Input: `s = "abcab", p = "abc", removable = [0, 1, 2, 3, 4]`
- Output: `0`
- Explanation: Removing original index `0` immediately eliminates every possible `"abc"` subsequence.
