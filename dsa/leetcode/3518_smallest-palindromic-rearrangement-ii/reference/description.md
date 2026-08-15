### 1. Description

You are given a **palindromic** string `s` and an integer `k`.

Return the **k-th** **lexicographically smallest** palindromic permutation of `s`. If there are fewer than `k` distinct palindromic permutations, return an empty string.

### 2. Function Contract

**Inputs**

- `s`: Input parameter (`str`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `str`.

### 3. Note

Different rearrangements that yield the same palindromic string are considered identical and are counted once.

### 4. Examples

#### Example 1

- **Input:** s = "abba", k = 2

- **Output:** "baab"

- **Explanation:** 

- The two distinct palindromic rearrangements of `"abba"` are `"abba"` and `"baab"`.

- Lexicographically, `"abba"` comes before `"baab"`. Since $k = 2$, the output is `"baab"`.

#### Example 2

- **Input:** s = "aa", k = 2

- **Output:** ""

- **Explanation:** 

- There is only one palindromic rearrangement: `"aa"`.

- The output is an empty string since $k = 2$ exceeds the number of possible rearrangements.

#### Example 3

- **Input:** s = "bacab", k = 1

- **Output:** "abcba"

- **Explanation:** 

- The two distinct palindromic rearrangements of `"bacab"` are `"abcba"` and `"bacab"`.

- Lexicographically, `"abcba"` comes before `"bacab"`. Since $k = 1$, the output is `"abcba"`.

### 5. Constraints

- $1 \le \text{s.length} \le 10^{4}$

- `s` consists of lowercase English letters.

- `s` is guaranteed to be palindromic.

- $1 \le k \le 10^{6}$
