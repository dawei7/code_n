### 1. Description

Let's say a positive integer is a **super-palindrome** if it is a palindrome, and it is also the square of a palindrome.

Given two positive integers `left` and `right` represented as strings, return *the number of **super-palindromes** integers in the inclusive range* `[left, right]`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $left = "4", right = "1000"$
- **Output:** `4`
**Explanation**: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
#### Example 2

- **Input:** $left = "1", right = "2"$
- **Output:** `1`

### 4. Constraints

- $1 \le \text{left.length}, \text{right.length} \le 18$

- `left` and `right` consist of only digits.

- `left` and `right` cannot have leading zeros.

- `left` and `right` represent integers in the range $[1, 10^{18} - 1]$.

- `left` is less than or equal to `right`.