### 1. Description

Given the strings `s1` and `s2` of size `n` and the string `evil`, return *the number of **good** strings*.

A **good** string has size `n`, it is alphabetically greater than or equal to `s1`, it is alphabetically smaller than or equal to `s2`, and it does not contain the string `evil` as a substring. Since the answer can be a huge number, return this **modulo** $10^{9} + 7$.

### 2. Function Contract

**Inputs**

- `n`: Input parameter (`int`).
- `s1`: Input parameter (`str`).
- `s2`: Input parameter (`str`).
- `evil`: Input parameter (`str`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $n = 2, s1 = "aa", s2 = "da", evil = "b"$
- **Output:** `51`
- **Explanation:** There are 25 good strings starting with 'a': "aa","ac","ad",...,"az". Then there are 25 good strings starting with 'c': "ca","cc","cd",...,"cz" and finally there is one good string starting with 'd': "da".

#### Example 2

- **Input:** $n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet"$
- **Output:** `0`
- **Explanation:** All strings greater than or equal to s1 and smaller than or equal to s2 start with the prefix "leet", therefore, there is not any good string.

#### Example 3

- **Input:** $n = 2, s1 = "gx", s2 = "gz", evil = "x"$
- **Output:** `2`

### 4. Constraints

- $\text{s1.length} = n$

- $\text{s2.length} = n$

- $s1 \le s2$

- $1 \le n \le 500$

- $1 \le \text{evil.length} \le 50$

- All strings consist of lowercase English letters.
