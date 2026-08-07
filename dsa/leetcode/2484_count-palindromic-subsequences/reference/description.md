## Description

Given a string of digits `s`, return *the number of **palindromic subsequences** of* `s`* having length *`5`. Since the answer may be very large, return it **modulo** $10^{9} + 7$.

**Note:**

- A string is **palindromic** if it reads the same forward and backward.

- A **subsequence** is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

- **Input:** `s = "103301"`
- **Output:** `2`
- **Explanation:**
There are 6 possible subsequences of length 5: "10330","10331","10301","10301","13301","03301".
Two of them (both equal to "10301") are palindromic.
#### Example 2

- **Input:** `s = "0000000"`
- **Output:** `21`
- **Explanation:** All 21 subsequences are "00000", which is palindromic.
#### Example 3

- **Input:** `s = "9999900000"`
- **Output:** `2`
- **Explanation:** The only two palindromic subsequences are "99999" and "00000".
### Constraints

- $1 \le \text{s.length} \le 10^{4}$

- `s` consists of digits.