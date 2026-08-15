### 1. Description

You are given a string `word` and a **non-negative** integer `k`.

Return the total number of substrings of `word` that contain every vowel (`'a'`, `'e'`, `'i'`, `'o'`, and `'u'`) **at least** once and **exactly** `k` consonants.

### 2. Function Contract

**Inputs**

- `word`: Input parameter (`str`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** word = "aeioqq", k = 1

- **Output:** 0

- **Explanation:** There is no substring with every vowel.

#### Example 2

- **Input:** word = "aeiou", k = 0

- **Output:** 1

- **Explanation:** The only substring with every vowel and zero consonants is `word[0..4]`, which is `"aeiou"`.

#### Example 3

- **Input:** word = "ieaouqqieaouqq", k = 1

- **Output:** 3

- **Explanation:** The substrings with every vowel and one consonant are:

- `word[0..5]`, which is `"ieaouq"`.

- `word[6..11]`, which is `"qieaou"`.

- `word[7..12]`, which is `"ieaouq"`.

### 4. Constraints

- $5 \le \text{word.length} \le 250$

- `word` consists only of lowercase English letters.

- $0 \le k \le \text{word.length} - 5$
