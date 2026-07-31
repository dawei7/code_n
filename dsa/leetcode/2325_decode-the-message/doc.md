# Decode the Message

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2325 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/decode-the-message/) |

## Problem Description

### Goal

The strings `key` and `message` describe a substitution cipher. Read `key`
from left to right and retain only the first occurrence of each lowercase
English letter. The problem guarantees that this first-occurrence sequence
eventually contains all 26 letters.

Align the first retained letter with `a`, the second with `b`, and so on
through `z`. Decode every letter of `message` using that mapping while
preserving each space exactly as a space. Return the resulting plaintext
string; repeated letters or spaces in `key` do not create new table entries.

### Function Contract

**Inputs**

- `key`: A string of length from 26 through 2000 containing lowercase English
  letters and spaces. Every lowercase letter occurs at least once.
- `message`: A nonempty string of at most 2000 lowercase English letters and
  spaces.

**Return value**

The decoded message obtained from the first-occurrence substitution table,
with spaces unchanged.

### Examples

**Example 1**

- Input: `key = "the quick brown fox jumps over the lazy dog"`,
  `message = "vkbs bs t suepuv"`
- Output: `"this is a secret"`
- Explanation: The distinct letters encountered in `key` begin `t`, `h`, `e`,
  so those cipher letters decode to `a`, `b`, and `c`, respectively.

**Example 2**

- Input: `key = "eljuxhpwnyrdgtqkviszcfmabo"`,
  `message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"`
- Output: `"the five boxing wizards jump quickly"`
- Explanation: Since the key has no repeated letters, its order directly
  defines all 26 substitutions.

**Example 3**

- Input: `key = "abcdefghijklmnopqrstuvwxyz"`, `message = "stay curious"`
- Output: `"stay curious"`
- Explanation: Alphabetical key order creates the identity substitution.
