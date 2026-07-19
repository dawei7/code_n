# Minimum Length of String After Deleting Similar Ends

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1750 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/) |

## Problem Description

### Goal

You are given a string `s` containing only `a`, `b`, and `c`. In one operation, choose a nonempty prefix whose characters are all equal and a nonempty suffix whose characters are all equal. The two chosen parts must contain the same character and must not overlap at any index.

Delete both chosen parts simultaneously. You may repeat this operation any number of times, including zero. Return the minimum length that can remain. Prefix and suffix lengths are chosen independently, so equal boundary runs do not need to have the same size, but neither side may consume a character also selected by the other.

### Function Contract

**Inputs**

- `s`: a nonempty string over the alphabet `{a, b, c}`, with $1 \le \lvert s\rvert \le 10^5$.

Let $n=\lvert s\rvert$.

**Return value**

- Return the smallest possible length after repeatedly deleting legal equal-character prefix and suffix pairs.

### Examples

**Example 1**

- Input: `s = "ca"`
- Output: `2`
- Explanation: The endpoint characters differ, so no operation is available.

**Example 2**

- Input: `s = "cabaabac"`
- Output: `0`
- Explanation: Successive matching boundary runs can remove `c`, then `a`, then `b`, and finally the remaining `a` characters.

**Example 3**

- Input: `s = "aabccabba"`
- Output: `3`
- Explanation: Removing the outer `a` runs and then the outer `b` runs leaves `"cca"`, whose endpoints differ.
