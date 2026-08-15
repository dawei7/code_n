### 1. Description

Given a string `s` and an integer `k`, return the total number of substrings of `s` where **at least one** character appears **at least** `k` times.

### 2. Function Contract

- Refer to method signature.

### 3. Examples

#### Example 1

- **Input:** s = "abacb", k = 2

- **Output:** 4

- **Explanation:** The valid substrings are:

- "`aba"` (character `'a'` appears 2 times).

- `"abac"` (character `'a'` appears 2 times).

- `"abacb"` (character `'a'` appears 2 times).

- `"bacb"` (character `'b'` appears 2 times).

#### Example 2

- **Input:** s = "abcde", k = 1

- **Output:** 15

- **Explanation:** All substrings are valid because every character appears at least once.

### 4. Constraints

- $1 \le \text{s.length} \le 3 * 10^{5}$

- $1 \le k \le \text{s.length}$

- `s` consists only of lowercase English letters.
