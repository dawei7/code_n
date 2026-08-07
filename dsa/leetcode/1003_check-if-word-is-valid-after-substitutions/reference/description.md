### 1. Description

Given a string `s`, determine if it is **valid**.

A string `s` is **valid** if, starting with an empty string $t = ""$, you can **transform **`t`** into **`s` after performing the following operation **any number of times**:

- Insert string `"abc"` into any position in `t`. More formally, `t` becomes $t_{left} + "abc" + t_{right}$, where $t = t_{left} + t_{right}$. Note that $t_{left}$ and $t_{right}$ may be **empty**.

Return `true` *if *`s`* is a **valid** string, otherwise, return* `false`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `s = "aabcbc"`
- **Output:** `true`
- **Explanation:**
"" -> "<u>abc</u>" -> "a<u>abc</u>bc"
Thus, "aabcbc" is valid.
#### Example 2

- **Input:** `s = "abcabcababcc"`
- **Output:** `true`
- **Explanation:**
"" -> "<u>abc</u>" -> "abc<u>abc</u>" -> "abcabc<u>abc</u>" -> "abcabcab<u>abc</u>c"
Thus, "abcabcababcc" is valid.
#### Example 3

- **Input:** `s = "abccba"`
- **Output:** `false`
- **Explanation:** It is impossible to get "abccba" using the operation.

### 4. Constraints

- $1 \le \text{s.length} \le 2 * 10^{4}$

- `s` consists of letters `'a'`, `'b'`, and `'c'`