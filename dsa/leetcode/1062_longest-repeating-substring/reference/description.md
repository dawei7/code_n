## Description

Given a string `s`, return *the length of the longest repeating substrings*. If no repeating substring exists, return `0`.
### Function Contract

**Inputs**

- `s`: a non-empty string containing only lowercase English letters.

Let $N = \lvert s \rvert$. Repetition requires equal contiguous contents at two or more distinct starting positions. Only the length is requested; no particular repeated substring needs to be returned.

**Return value**

- The maximum length of a repeating substring, or `0` when no non-empty substring repeats.

### Examples
#### Example 1

- **Input:** `s = "abcd"`
- **Output:** `0`
- **Explanation:** There is no repeating substring.
#### Example 2

- **Input:** `s = "abbaba"`
- **Output:** `2`
- **Explanation:** The longest repeating substrings are "ab" and "ba", each of which occurs twice.
#### Example 3

- **Input:** `s = "aabcaabdaab"`
- **Output:** `3`
- **Explanation:** The longest repeating substring is "aab", which occurs 3 times.
### Constraints

- $1 \le \text{s.length} \le 2000$

- `s` consists of lowercase English letters.