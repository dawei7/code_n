### 1. Description

You are given a string `s`. An **awesome** substring is a non-empty substring of `s` such that we can make any number of swaps in order to make it a palindrome.

Return *the length of the maximum length **awesome substring** of* `s`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `s = "3242415"`
- **Output:** `5`
- **Explanation:** "24241" is the longest awesome substring, we can form the palindrome "24142" with some swaps.
#### Example 2

- **Input:** `s = "12345678"`
- **Output:** `1`
#### Example 3

- **Input:** `s = "213123"`
- **Output:** `6`
- **Explanation:** "213123" is the longest awesome substring, we can form the palindrome "231132" with some swaps.

### 4. Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` consists only of digits.