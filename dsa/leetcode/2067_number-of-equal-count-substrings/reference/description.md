## Description

You are given a **0-indexed** string `s` consisting of only lowercase English letters, and an integer `count`. A **substring** of `s` is said to be an **equal count substring** if, for each **unique** letter in the substring, it appears exactly `count` times in the substring.

Return *the number of **equal count substrings** in *`s`.

A **substring** is a contiguous non-empty sequence of characters within a string.
### Function Contract

- Refer to method signature.

### Examples

#### Example 1

- **Input:** `s = "aaabcbbcc", count = 3`
- **Output:** `3`
- **Explanation:**
The substring that starts at index 0 and ends at index 2 is "aaa".
The letter 'a' in the substring appears exactly 3 times.
The substring that starts at index 3 and ends at index 8 is "bcbbcc".
The letters 'b' and 'c' in the substring appear exactly 3 times.
The substring that starts at index 0 and ends at index 8 is "aaabcbbcc".
The letters 'a', 'b', and 'c' in the substring appear exactly 3 times.
#### Example 2

- **Input:** `s = "abcd", count = 2`
- **Output:** `0`
- **Explanation:**
The number of times each letter appears in s is less than count.
Therefore, no substrings in s are equal count substrings, so return 0.
#### Example 3

- **Input:** `s = "a", count = 5`
- **Output:** `0`
- **Explanation:**
The number of times each letter appears in s is less than count.
Therefore, no substrings in s are equal count substrings, so return 0
### Constraints

- $1 \le \text{s.length} \le 3 * 10^{4}$

- $1 \le count \le 3 * 10^{4}$

- `s` consists only of lowercase English letters.