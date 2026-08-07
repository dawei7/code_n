## Description

You are given a string `word` and an integer `k`.

A substring `s` of `word` is **complete** if:

- Each character in `s` occurs **exactly** `k` times.

- The difference between two adjacent characters is **at most** `2`. That is, for any two adjacent characters `c1` and `c2` in `s`, the absolute difference in their positions in the alphabet is **at most** `2`.

Return *the number of **complete **substrings of* `word`.

A **substring** is a **non-empty** contiguous sequence of characters in a string.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** $word = "igigee", k = 2$
- **Output:** `3`
- **Explanation:** The complete substrings where each character appears exactly twice and the difference between adjacent characters is at most 2 are: <u>**igig**</u>ee, igig<u>**ee**</u>, <u>**igigee**</u>.
#### Example 2

- **Input:** $word = "aaabbbccc", k = 3$
- **Output:** `6`
- **Explanation:** The complete substrings where each character appears exactly three times and the difference between adjacent characters is at most 2 are: **<u>aaa</u>**bbbccc, aaa<u>**bbb**</u>ccc, aaabbb<u>**ccc**</u>, **<u>aaabbb</u>**ccc, aaa<u>**bbbccc**</u>, <u>**aaabbbccc**</u>.
### Constraints

- $1 \le \text{word.length} \le 10^{5}$

- `word` consists only of lowercase English letters.

- $1 \le k \le \text{word.length}$