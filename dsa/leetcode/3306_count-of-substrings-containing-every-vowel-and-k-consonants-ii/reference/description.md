## Description

You are given a string `word` and a **non-negative** integer `k`.

Return the total number of substrings of `word` that contain every vowel (`'a'`, `'e'`, `'i'`, `'o'`, and `'u'`) **at least** once and **exactly** `k` consonants.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** word = "aeioqq", k = 1

**Output:** 0

**Explanation:**

There is no substring with every vowel.

</div>
#### Example 2

<div class="example-block">
**Input:** word = "aeiou", k = 0

**Output:** 1

**Explanation:**

The only substring with every vowel and zero consonants is `word[0..4]`, which is `"aeiou"`.

</div>
#### Example 3

<div class="example-block">
**Input:** word = "ieaouqqieaouqq", k = 1

**Output:** 3

**Explanation:**

The substrings with every vowel and one consonant are:

- `word[0..5]`, which is `"ieaouq"`.

- `word[6..11]`, which is `"qieaou"`.

- `word[7..12]`, which is `"ieaouq"`.

</div>
### Constraints

- $5 \le \text{word.length} \le 2 * 10^{5}$

- `word` consists only of lowercase English letters.

- $0 \le k \le \text{word.length} - 5$