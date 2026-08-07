### 1. Description

You are given a string `s`, which contains stars `*`.

In one operation, you can:

- Choose a star in `s`.

- Remove the closest **non-star** character to its **left**, as well as remove the star itself.

Return *the string after **all** stars have been removed*.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Note

- The input will be generated such that the operation is always possible.

- It can be shown that the resulting string will always be unique.

### 4. Examples

#### Example 1

- **Input:** `s = "leet**cod*e"`
- **Output:** `"lecoe"`
- **Explanation:** Performing the removals from left to right:
- The closest character to the 1^st star is 't' in "lee**<u>t</u>****cod*e". s becomes "lee*cod*e".
- The closest character to the 2^nd star is 'e' in "le**<u>e</u>***cod*e". s becomes "lecod*e".
- The closest character to the 3^rd star is 'd' in "leco**<u>d</u>***e". s becomes "lecoe".
There are no more stars, so we return "lecoe".
#### Example 2

- **Input:** `s = "erase*****"`
- **Output:** `""`
- **Explanation:** The entire string is removed, so we return an empty string.

### 5. Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` consists of lowercase English letters and stars `*`.

- The operation above can be performed on `s`.