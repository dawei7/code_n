### 1. Description

You are given two strings `word1` and `word2`.

A string `x` is called **valid** if `x` can be rearranged to have `word2` as a prefix.

Return the total number of **valid** substrings of `word1`.

### 2. Function Contract

**Inputs**

- `word1`: Input parameter (`str`).
- `word2`: Input parameter (`str`).

**Return value**

- Returns `int`.

### 3. Note

that the memory limits in this problem are **smaller** than usual, so you **must** implement a solution with a *linear* runtime complexity.

### 4. Examples

#### Example 1

- **Input:** word1 = "bcca", word2 = "abc"

- **Output:** 1

- **Explanation:** The only valid substring is `"bcca"` which can be rearranged to `"abcc"` having `"abc"` as a prefix.

#### Example 2

- **Input:** word1 = "abcabc", word2 = "abc"

- **Output:** 10

- **Explanation:** All the substrings except substrings of size 1 and size 2 are valid.

#### Example 3

- **Input:** word1 = "abcabc", word2 = "aaabc"

- **Output:** 0

### 5. Constraints

- $1 \le \text{word1.length} \le 10^{6}$

- $1 \le \text{word2.length} \le 10^{4}$

- `word1` and `word2` consist only of lowercase English letters.
