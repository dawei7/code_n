### 1. Description

A subsequence of a string `s` is considered a **good palindromic subsequence** if:

- It is a subsequence of `s`.

- It is a palindrome (has the same value if reversed).

- It has an **even** length.

- No two consecutive characters are equal, except the two middle ones.

For example, if `s = "abcabcabb"`, then `"abba"` is considered a **good palindromic subsequence**, while `"bcb"` (not even length) and `"bbbb"` (has equal consecutive characters) are not.

Given a string `s`, return *the **length** of the **longest good palindromic subsequence** in *`s`.

### 2. Function Contract

**Inputs**

- `s`: A string of lowercase English letters ($1 \le \text{s.length} \le 250$).

**Return value**

Return an integer representing the maximum length of a good palindromic subsequence of `s`, or `0` if no such subsequence exists.

### 3. Examples

#### Example 1

- **Input:** `s = "bbabab"`
- **Output:** `4`
- **Explanation:** The longest good palindromic subsequence of s is "baab".
#### Example 2

- **Input:** `s = "dcbccacdb"`
- **Output:** `4`
- **Explanation:** The longest good palindromic subsequence of s is "dccd".

### 4. Constraints

- $1 \le \text{s.length} \le 250$

- `s` consists of lowercase English letters.