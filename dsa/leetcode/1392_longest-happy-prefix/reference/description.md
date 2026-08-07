## Description

A string is called a **happy prefix** if it is a **non-empty** prefix which is also a suffix (excluding itself).

Given a string `s`, return *the **longest happy prefix** of* `s`. Return an empty string `""` if no such prefix exists.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** `s = "level"`
- **Output:** `"l"`
- **Explanation:** s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".
#### Example 2

- **Input:** `s = "ababab"`
- **Output:** `"abab"`
- **Explanation:** "abab" is the largest prefix which is also suffix. They can overlap in the original string.
### Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` contains only lowercase English letters.