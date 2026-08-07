## Description

Given a digit string `s`, return *the number of **unique substrings **of *`s`* where every digit appears the same number of times.*
### Function Contract

- Refer to method signature.

### Examples

#### Example 1

- **Input:** `s = "1212"`
- **Output:** `5`
- **Explanation:** The substrings that meet the requirements are "1", "2", "12", "21", "1212".
Note that although the substring "12" appears twice, it is only counted once.
#### Example 2

- **Input:** `s = "12321"`
- **Output:** `9`
- **Explanation:** The substrings that meet the requirements are "1", "2", "3", "12", "23", "32", "21", "123", "321".
### Constraints

- $1 \le \text{s.length} \le 1000$

- `s` consists of digits.