# Minimum Operations to Make Character Frequencies Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3389 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Hash Table, String, Dynamic Programming, Counting, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-character-frequencies-equal/) |

## Problem Description

### Goal

A string is good when every character that occurs in it has the same frequency. Characters absent from the string do not need to share that positive frequency.

Starting from `s`, one operation may delete any character, insert any lowercase English character, or change one character to the next letter of the alphabet. The last operation follows alphabet order only: for example, `'c'` may become `'d'`, but `'z'` cannot wrap around to `'a'`.

Apply any number of these operations and return the minimum number needed to obtain a good string. Character order does not constrain the result; only the 26 frequencies and the one-way transitions between adjacent letters matter.

### Function Contract

**Inputs**

- `s`: A string of lowercase English letters.

The length satisfies $3 \le \lvert s \rvert \le 2 \times 10^4$.

**Return value**

Return the minimum number of allowed operations required to make the string good.

### Examples

**Example 1**

- Input: `s = "acab"`
- Output: `1`
- Explanation: Deleting one `'a'` leaves every remaining character with frequency 1.

**Example 2**

- Input: `s = "wddw"`
- Output: `0`
- Explanation: Both present characters already occur twice.

**Example 3**

- Input: `s = "aaabc"`
- Output: `2`
- Explanation: Change one `'a'` to `'b'`, then insert one `'c'`; all three frequencies become 2.
