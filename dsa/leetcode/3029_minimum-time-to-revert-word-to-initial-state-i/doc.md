# Minimum Time to Revert Word to Initial State I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3029 |
| Difficulty | Medium |
| Topics | String, Rolling Hash, String Matching, Hash Function |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i/) |

## Problem Description
### Goal
You begin with a 0-indexed string `word`. During every second, exactly two operations must be performed: remove the first `k` characters from the current word, then append any `k` characters to its end.

The appended characters do not have to equal the characters just removed. Even when a convenient choice could restore the target, both the removal and the append still occur during that second.

Determine the minimum positive number of seconds after which the current word can equal its initial value.

### Function Contract
Let $N$ be the length of `word`.

**Inputs**

- `word`: A string of $N$ lowercase English letters, where $1 \le N \le 50$.
- `k`: The number of characters removed and appended per second, where $1 \le k \le N$.

**Return value**

Return the minimum integer time greater than zero at which suitable appended characters can make `word` equal its initial state.

### Examples
**Example 1**

- Input: `word = "abacaba", k = 3`
- Output: `2`
- Explanation: After one second, the surviving suffix cannot occupy the matching prefix. After two seconds, the surviving `"a"` does match the initial prefix, and the appended characters can complete the original word.

**Example 2**

- Input: `word = "abacaba", k = 4`
- Output: `1`
- Explanation: Removing `"abac"` leaves `"aba"`, which already equals the initial prefix of length three; appending `"caba"` restores the word.

**Example 3**

- Input: `word = "abcbabcd", k = 2`
- Output: `4`
- Explanation: No earlier surviving suffix matches the corresponding initial prefix. After four seconds all original characters have been removed, so the appended characters can form the initial word.
