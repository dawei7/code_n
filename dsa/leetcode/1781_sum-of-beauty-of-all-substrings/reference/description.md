## Description

The **beauty** of a string is the difference in frequencies between the most frequent and least frequent characters.

- For example, the beauty of `"abaacc"` is $3 - 1 = 2$.

Given a string `s`, return *the sum of **beauty** of all of its substrings.*
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** `s = "aabcb"`
- **Output:** `5`
- **Explanation:** The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
#### Example 2

- **Input:** `s = "aabcbaa"`
- **Output:** `17`
### Constraints

- $1 \le \text{s.length} \le ^ 500$

- `s` consists of only lowercase English letters.