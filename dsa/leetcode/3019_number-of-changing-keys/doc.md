# Number of Changing Keys

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3019 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-changing-keys/) |

## Problem Description

### Goal

A user types a nonempty string `s` consisting of uppercase and lowercase English letters. A key change occurs whenever the physical letter key used for one character differs from the key used for the immediately preceding character.

Letter case does not identify a different key: typing `a` after `A`, or `A` after `a`, does not count as a change. Modifier keys such as Shift and Caps Lock are ignored.

Return the number of adjacent transitions that require changing to a different letter key. The first character establishes the initial key and does not itself count as a change.

### Function Contract

**Inputs**

- `s`: A nonempty string containing only uppercase and lowercase English letters.

The source constraints guarantee $1 \le \lvert\texttt{s}\rvert \le 100$.

**Return value**

- The number of case-insensitive key changes between adjacent characters.

### Examples

#### Example 1

- **Input:** `s = "aAbBcC"`
- **Output:** `2`
- **Explanation:** Case-only transitions keep the same key; the changes are from `a` to `b` and from `b` to `c`.

#### Example 2

- **Input:** `s = "AaAaAaaA"`
- **Output:** `0`
- **Explanation:** Every character uses the `a` key regardless of case.

#### Example 3

- **Input:** `s = "abBA"`
- **Output:** `2`
- **Explanation:** Ignoring case gives `"abba"`, with changes at `a -> b` and `b -> a`.
