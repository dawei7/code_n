### 1. Description

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true`* if it is a **palindrome**, or *`false`* otherwise*.

### 2. Function Contract

**Inputs**

- `s`: The printable ASCII string to normalize and test.

**Return value**

Return `true` when the lowercase alphanumeric characters read the same in both directions; otherwise return `false`.

### 3. Examples

#### Example 1

- **Input:** `s = "A man, a plan, a canal: Panama"`
- **Output:** `true`
- **Explanation:** "amanaplanacanalpanama" is a palindrome.
#### Example 2

- **Input:** `s = "race a car"`
- **Output:** `false`
- **Explanation:** "raceacar" is not a palindrome.
#### Example 3

- **Input:** `s = " "`
- **Output:** `true`
- **Explanation:** s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

### 4. Constraints

- $1 \le \text{s.length} \le 2 * 10^{5}$

- `s` consists only of printable ASCII characters.