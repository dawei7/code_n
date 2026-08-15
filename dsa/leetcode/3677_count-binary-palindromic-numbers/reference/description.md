### 1. Description

You are given a **non-negative** integer `n`.

A **non-negative** integer is called **binary-palindromic** if its binary representation (written without leading zeros) reads the same forward and backward.

Return the number of integers `k` such that $0 \le k \le n$ and the binary representation of `k` is a palindrome.

### 2. Function Contract

**Inputs**

- `n`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Note

The number 0 is considered binary-palindromic, and its representation is `"0"`.

### 4. Examples

#### Example 1

- **Input:** n = 9

- **Output:** 6

- **Explanation:** The integers `k` in the range `[0, 9]` whose binary representations are palindromes are:

- `0 → "0"`

- `1 → "1"`

- `3 → "11"`

- `5 → "101"`

- `7 → "111"`

- `9 → "1001"`

All other values in `[0, 9]` have non-palindromic binary forms. Therefore, the count is 6.

#### Example 2

- **Input:** n = 0

- **Output:** 1

- **Explanation:** Since `"0"` is a palindrome, the count is 1.

### 5. Constraints

- $0 \le n \le 10^{15}$
