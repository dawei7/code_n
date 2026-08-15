# Find the Sequence of Strings Appeared on the Screen

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3324 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-sequence-of-strings-appeared-on-the-screen/) |

## Problem Description

### Goal

Alice starts with an empty screen and a keyboard containing only two keys. The first key appends the character `"a"`. The second key advances the last screen character to the next lowercase English letter, with `"z"` wrapping to `"a"`. The advance key cannot be used while the screen is empty.

Given a nonempty lowercase string `target`, Alice must reach it with the minimum possible number of key presses. Return every nonempty screen string that appears after a press, in chronological order. Each new target position must first be created as `"a"`; because that position starts at the alphabet's first letter, advancing directly to its desired character is the unique shortest route and never needs the wrap from `"z"` to `"a"`.

### Function Contract

**Inputs**

- `target`: A lowercase English string of length $n$, where $1\leq n\leq400$.

**Return value**

Return the complete ordered list of screen states produced by a minimum-length key sequence ending at `target`.

### Examples

#### Example 1

- **Input:** `target = "abc"`
- **Output:** `["a", "aa", "ab", "aba", "abb", "abc"]`
- **Explanation:** Each position appears first as `a`; the second and third positions are advanced once and twice respectively.

#### Example 2

- **Input:** `target = "he"`
- **Output:** `["a", "b", "c", "d", "e", "f", "g", "h", "ha", "hb", "hc", "hd", "he"]`
- **Explanation:** The first position advances from `a` through `h`; the second is then appended and advanced through `e`.
