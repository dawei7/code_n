# Time Needed to Rearrange a Binary String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2380 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/time-needed-to-rearrange-a-binary-string/) |

## Problem Description

### Goal

Given a binary string `s`, repeatedly perform a simultaneous update once per second: every occurrence of `"01"` in the string at the start of that second becomes `"10"`.

Continue until the string contains no `"01"` pair, meaning that every `'1'` appears before every `'0'`. Return the number of seconds required. All eligible pairs in one second are replaced together rather than one after another.

### Function Contract

**Inputs**

- `s`: A binary string with $1 \le \lvert\texttt{s}\rvert \le 1000$.

**Return value**

- Return the number of simultaneous replacement rounds needed until no `"01"` remains.

**Update semantics**

- Each second uses the string state from the beginning of that second to determine all replacements.
- Replacements occur simultaneously, so a character moved during a second cannot move again until the next second.

### Examples

#### Example 1

- **Input:** `s = "0110101"`
- **Output:** `4`
- **Explanation:** The successive strings are `"1011010"`, `"1101100"`, `"1110100"`, and `"1111000"`.

#### Example 2

- **Input:** `s = "11100"`
- **Output:** `0`
- **Explanation:** No `"01"` occurs initially, so the process is already complete.
