## Description

Given a string `s`, return *the length of the longest **substring** that contains at most **two distinct characters***.
### Function Contract

**Inputs**

- `s`: A string consisting of English letters ($1 \le \text{s.length} \le 10^5$).

**Return value**

Return an integer representing the maximum length of a contiguous substring containing at most two distinct characters.

### Examples
#### Example 1

- **Input:** `s = "eceba"`
- **Output:** `3`
- **Explanation:** The substring is "ece" which its length is 3.
#### Example 2

- **Input:** `s = "ccaabbb"`
- **Output:** `5`
- **Explanation:** The substring is "aabbb" which its length is 5.
### Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` consists of English letters.