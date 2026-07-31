# Remove Adjacent Almost-Equal Characters

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2957 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/remove-adjacent-almost-equal-characters/) |

## Problem Description
### Goal
You are given a 0-indexed lowercase English string `word`. Two characters are
almost-equal when they are identical or occupy adjacent positions in the
alphabet. Equivalently, their alphabet codes differ by at most one; the
alphabet does not wrap from `a` to `z`.

In one operation, choose any index and replace its character with any lowercase
English letter. Make changes so that no neighboring pair in the final string is
almost-equal. Return the minimum number of operations needed; the resulting
string itself is not required.

### Function Contract
**Inputs**

- `word`: the lowercase English string to modify conceptually

Let $N=\lvert\texttt{word}\rvert$. The contract guarantees $1\le N\le100$.

**Return value**

The minimum number of single-position character replacements needed to make
every adjacent pair differ by at least two alphabet positions.

### Examples
**Example 1**

- Input: `word = "aaaaa"`
- Output: `2`
- Explanation: Changing the second and fourth characters to `c` produces `acaca`, whose adjacent pairs are all safe.

**Example 2**

- Input: `word = "abddez"`
- Output: `2`
- Explanation: Two replacements suffice to break the conflict at the beginning and the equal middle pair without creating new conflicts.

**Example 3**

- Input: `word = "zyxyxyz"`
- Output: `3`
- Explanation: Three carefully placed replacements remove every equal or alphabet-adjacent neighboring pair.
