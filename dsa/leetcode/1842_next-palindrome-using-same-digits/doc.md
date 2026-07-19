# Next Palindrome Using Same Digits

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/next-palindrome-using-same-digits/) |
| Frontend ID | 1842 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You receive `num`, a numeric string that may be too large for ordinary integer types. It is guaranteed to already read identically from left to right and right to left.

Rearrange exactly the same digit occurrences to form another palindrome. Among all such palindromes that are strictly larger than `num`, return the smallest one. If the existing arrangement is already the greatest possible palindromic arrangement of those digits, return the empty string.

### Function Contract

**Inputs**

- `num`: a string of decimal digits representing a palindrome.
- $1 \le \lvert\texttt{num}\rvert \le 10^5$.
- Let $n=\lvert\texttt{num}\rvert$.

**Return value**

- Return the lexicographically smallest palindromic digit string that is strictly larger than `num` and uses every input digit exactly once.
- Return `""` when no larger valid palindrome exists.
- Preserve the input length and, for odd $n$, the unique center position's digit.

### Examples

**Example 1**

- Input: `num = "1221"`
- Output: `"2112"`

The two possible first-half arrangements are `12` and `21`; mirroring the next one produces `2112`.

**Example 2**

- Input: `num = "32123"`
- Output: `""`

The first half `32` is already its greatest permutation, so no larger palindrome can use the same digits.

**Example 3**

- Input: `num = "45544554"`
- Output: `"54455445"`

The first half advances from `4554` to its next permutation, `5445`, and mirroring it gives the result.
