### 1. Description

Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and **may** press a key for too long, resulting in a character being typed **multiple** times.

You are given a string `word`, which represents the **final** output displayed on Alice's screen. You are also given a **positive** integer `k`.

Return the total number of *possible* original strings that Alice *might* have intended to type, if she was trying to type a string of size **at least** `k`.

Since the answer may be very large, return it **modulo** $10^{9} + 7$.

### 2. Function Contract

**Inputs**

- `word`: Input parameter (`str`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** word = "aabbccdd", k = 7

- **Output:** 5

- **Explanation:** The possible strings are: `"aabbccdd"`, `"aabbccd"`, `"aabbcdd"`, `"aabccdd"`, and `"abbccdd"`.

#### Example 2

- **Input:** word = "aabbccdd", k = 8

- **Output:** 1

- **Explanation:** The only possible string is `"aabbccdd"`.

#### Example 3

- **Input:** word = "aaabbb", k = 3

- **Output:** 8

### 4. Constraints

- $1 \le \text{word.length} \le 5 * 10^{5}$

- `word` consists only of lowercase English letters.

- $1 \le k \le 2000$
