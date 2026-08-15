### 1. Description

You are given a string `s`. You can convert `s` to a palindrome by adding characters in front of it.

Return *the shortest palindrome you can find by performing this transformation*.

### 2. Function Contract

**Inputs**

- `s`: The lowercase string that must remain intact as the result's suffix.

**Return value**

Return the shortest palindrome formed solely by prepending characters to `s`.

### 3. Examples

#### Example 1

- **Input:** `s = "aacecaaa"`
- **Output:** `"aaacecaaa"`

#### Example 2

- **Input:** `s = "abcd"`
- **Output:** `"dcbabcd"`

### 4. Constraints

- $0 \le \text{s.length} \le 5 * 10^{4}$

- `s` consists of lowercase English letters only.
