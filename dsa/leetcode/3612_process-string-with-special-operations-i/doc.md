# Process String with Special Operations I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3612 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/process-string-with-special-operations-i/) |

## Problem Description

### Goal

Process the input string `s` from left to right while building a separate result. Every lowercase English letter is appended to the result. The three special characters modify whatever has already been built and are not themselves included in the output.

When the current character is `*`, remove the result's last character if one exists. When it is `#`, duplicate the entire current result and append that copy. When it is `%`, reverse the current result. Apply each operation immediately in input order and return the final result after every character has been processed.

### Function Contract

**Inputs**

- `s`: A string containing only lowercase English letters and the special characters `*`, `#`, and `%`.

The constraint is $1 \le \lvert\texttt{s}\rvert \le 20$.

**Return value**

Return the string remaining after all letters and special operations have been applied from left to right.

### Examples

#### Example 1

- **Input:** `s = "a#b%*"`
- **Output:** `"ba"`
- **Explanation:** The intermediate results are `"a"`, `"aa"`, `"aab"`, `"baa"`, and finally `"ba"`.

#### Example 2

- **Input:** `s = "z*#"`
- **Output:** `""`
- **Explanation:** Removing `z` empties the result, and duplicating an empty result changes nothing.

#### Example 3

- **Input:** `s = "ab%#"`
- **Output:** `"baba"`
- **Explanation:** Reversal produces `"ba"`, then duplication appends another `"ba"`.
