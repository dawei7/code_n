### 1. Description

Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

### 2. Function Contract

**Inputs**

- `x`: The signed 32-bit integer to examine.

**Return value**

Return `True` if `x` is palindromic; otherwise return `False`.

### 3. Examples

#### Example 1

- **Input:** $x = 121$
- **Output:** `true`
- **Explanation:** 121 reads as 121 from left to right and from right to left.

#### Example 2

- **Input:** $x = -121$
- **Output:** `false`
- **Explanation:** From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

#### Example 3

- **Input:** $x = 10$
- **Output:** `false`
- **Explanation:** Reads 01 from right to left. Therefore it is not a palindrome.

### 4. Constraints

- $-2^{31} \le x \le 2^{31} - 1$

**Follow up:** Could you solve it without converting the integer to a string?
