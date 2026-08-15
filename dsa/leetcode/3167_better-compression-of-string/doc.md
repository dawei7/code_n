# Better Compression of String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3167 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/better-compression-of-string/) |

## Problem Description

### Goal

A string `compressed` describes character frequencies as consecutive groups. Each group contains one lowercase English letter followed by its positive decimal frequency. The same letter may occur in several different groups, and a frequency may contain multiple digits. For example, `"a3b1a1c2"` represents three `a` characters, one `b`, one more `a`, and two `c` characters.

Create a better compression in which every letter with a nonzero total frequency appears exactly once. Its count must be the sum of that letter's counts across all input groups, and the output groups must be ordered alphabetically by letter. Reordering the groups is explicitly allowed.

### Function Contract

**Inputs**

- `compressed`: A valid compressed string containing lowercase English letters and decimal digits.

Let $n = \lvert\texttt{compressed}\rvert$. The constraints satisfy $1 \le n \le 6\cdot10^4$. Every letter is followed by a frequency from $1$ through $10^4$, written without leading zeroes.

**Return value**

- The normalized compression containing one alphabetically ordered group for every letter present in the input.

### Examples

#### Example 1

- **Input:** `compressed = "a3c9b2c1"`
- **Output:** `"a3b2c10"`

The two `c` groups contribute $9+1=10$ copies in total.

#### Example 2

- **Input:** `compressed = "c2b3a1"`
- **Output:** `"a1b3c2"`

The groups already have unique letters, but they are reordered alphabetically.

#### Example 3

- **Input:** `compressed = "a2b4c1"`
- **Output:** `"a2b4c1"`

This input already satisfies both requirements of the better compression.
