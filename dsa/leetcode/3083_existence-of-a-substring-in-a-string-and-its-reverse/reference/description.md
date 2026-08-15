### 1. Description

Given a** **string `s`, find any substring of length `2` which is also present in the reverse of `s`.

Return `true`* if such a substring exists, and *`false`* otherwise.*

### 2. Function Contract

**Inputs**

- `s`: Input parameter (`str`).

**Return value**

- Returns `bool`.

### 3. Examples

#### Example 1

- **Input:** s = "leetcode"

- **Output:** true

- **Explanation:** Substring `"ee"` is of length `2` which is also present in $reverse(s) = "edocteel"$.

#### Example 2

- **Input:** s = "abcba"

- **Output:** true

- **Explanation:** All of the substrings of length `2` `"ab"`, `"bc"`, `"cb"`, `"ba"` are also present in $reverse(s) = "abcba"$.

#### Example 3

- **Input:** s = "abcd"

- **Output:** false

- **Explanation:** There is no substring of length `2` in `s`, which is also present in the reverse of `s`.

### 4. Constraints

- $1 \le \text{s.length} \le 100$

- `s` consists only of lowercase English letters.
