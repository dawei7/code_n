### 1. Description

You are given a string `word` that consists of digits and lowercase English letters.

You will replace every non-digit character with a space. For example, `"a123bc34d8ef34"` will become `" 123  34 8  34"`. Notice that you are left with some integers that are separated by at least one space: `"123"`, `"34"`, `"8"`, and `"34"`.

Return *the number of **different** integers after performing the replacement operations on *`word`.

Two integers are considered different if their decimal representations **without any leading zeros** are different.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $word = "a<u>123</u>bc<u>34</u>d<u>8</u>ef<u>34</u>"$
- **Output:** `3`
- **Explanation:** The three different integers are "123", "34", and "8". Notice that "34" is only counted once.
#### Example 2

- **Input:** $word = "leet<u>1234</u>code<u>234</u>"$
- **Output:** `2`
#### Example 3

- **Input:** $word = "a<u>1</u>b<u>01</u>c<u>001</u>"$
- **Output:** `1`
- **Explanation:** The three integers "1", "01", and "001" all represent the same integer because
the leading zeros are ignored when comparing their decimal values.

### 4. Constraints

- $1 \le \text{word.length} \le 1000$

- `word` consists of digits and lowercase English letters.