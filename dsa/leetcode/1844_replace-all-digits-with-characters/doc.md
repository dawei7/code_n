# Replace All Digits with Characters

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/replace-all-digits-with-characters/) |
| Frontend ID | 1844 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

The input `s` alternates by index: every even position contains a lowercase English letter, and every odd position contains a decimal digit. Define `shift(c, x)` as the letter found $x$ alphabet positions after letter `c`; a shift of zero returns `c` itself.

Replace each digit at odd index $i$ with `shift(s[i - 1], s[i])`, using the immediately preceding original letter. All requested shifts are guaranteed to stay at or before `'z'`. Return the resulting all-letter string without changing its length or its even-indexed characters.

### Function Contract

**Inputs**

- `s`: a string containing lowercase English letters at even indices and digits at odd indices.
- $1 \le \lvert\texttt{s}\rvert \le 100$.
- Every requested alphabet shift stays within `'a'` through `'z'`.
- Let $n=\lvert\texttt{s}\rvert$.

**Return value**

- Preserve every even-indexed letter.
- At each odd index $i$, replace digit `s[i]` with the character whose code is `ord(s[i - 1]) + int(s[i])`.
- Return the transformed string of length $n$.

### Examples

**Example 1**

- Input: `s = "a1c1e1"`
- Output: `"abcdef"`

The three shifts are `'a' + 1 = 'b'`, `'c' + 1 = 'd'`, and `'e' + 1 = 'f'`.

**Example 2**

- Input: `s = "a1b2c3d4e"`
- Output: `"abbdcfdhe"`

Each digit uses the letter directly to its left; the final `'e'` has no following digit and stays unchanged.

**Example 3**

- Input: `s = "x0"`
- Output: `"xx"`

A zero shift reproduces the preceding letter.
