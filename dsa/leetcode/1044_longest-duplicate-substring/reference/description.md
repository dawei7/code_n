## Description

Given a string `s`, consider all *duplicated substrings*: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.

Return **any** duplicated substring that has the longest possible length. If `s` does not have a duplicated substring, the answer is `""`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** `s = "banana"`
- **Output:** `"ana"`
#### Example 2

- **Input:** `s = "abcd"`
- **Output:** `""`
### Constraints

- $2 \le \text{s.length} \le 3 * 10^{4}$

- `s` consists of lowercase English letters.