# Process String with Special Operations II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3614 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/process-string-with-special-operations-ii/) |

## Problem Description
### Goal

Process `s` from left to right while conceptually building a result string. Lowercase English letters append themselves. The special character `*` removes the last result character when one exists, `#` duplicates the current result and appends the copy, and `%` reverses the result.

After every input character has been applied in order, return the character at zero-based index `k` in the final result. If `k` is not a valid final index, return `'.'`. The conceptual result can be vastly longer than the input, so the required character must be found without constructing that complete string.

### Function Contract

**Inputs**

- `s`: A string of lowercase English letters and the special characters `*`, `#`, and `%`.
- `k`: The zero-based index requested from the final conceptual result.

The constraints are $1 \le \lvert\texttt{s}\rvert \le 10^5$ and $0 \le k \le 10^{15}$. The final conceptual result length does not exceed $10^{15}$.

**Return value**

Return the final result's character at index `k`, or `'.'` when `k` lies outside the result.

### Examples

**Example 1**

- Input: `s = "a#b%*", k = 1`
- Output: `"a"`
- Explanation: The final result is `"ba"`, whose character at index 1 is `a`.

**Example 2**

- Input: `s = "cd%#*#", k = 3`
- Output: `"d"`
- Explanation: Processing produces `"dcddcd"`; index 3 contains `d`.

**Example 3**

- Input: `s = "z*#", k = 0`
- Output: `"."`
- Explanation: The final result is empty, so index 0 is out of bounds.
