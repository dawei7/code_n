## Description

You are given a **0-indexed** string `text` and another **0-indexed** string `pattern` of length `2`, both of which consist of only lowercase English letters.

You can add **either** $\text{pattern}[0]$ **or** $\text{pattern}[1]$ anywhere in `text` **exactly once**. Note that the character can be added even at the beginning or at the end of `text`.

Return *the **maximum** number of times* `pattern` *can occur as a **subsequence** of the modified *`text`.

A **subsequence** is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** $text = "abdcdbc", pattern = "ac"$
- **Output:** `4`
- **Explanation:**
If we add pattern[0] = 'a' in between text[1] and text[2], we get "ab<u>**a**</u>dcdbc". Now, the number of times "ac" occurs as a subsequence is 4.
Some other strings which have 4 subsequences "ac" after adding a character to text are "<u>**a**</u>abdcdbc" and "abd<u>**a**</u>cdbc".
However, strings such as "abdc<u>**a**</u>dbc", "abd<u>**c**</u>cdbc", and "abdcdbc<u>**c**</u>", although obtainable, have only 3 subsequences "ac" and are thus suboptimal.
It can be shown that it is not possible to get more than 4 subsequences "ac" by adding only one character.
#### Example 2

- **Input:** $text = "aabb", pattern = "ab"$
- **Output:** `6`
- **Explanation:**
Some of the strings which can be obtained from text and have 6 subsequences "ab" are "<u>**a**</u>aabb", "aa<u>**a**</u>bb", and "aab<u>**b**</u>b".
### Constraints

- $1 \le \text{text.length} \le 10^{5}$

- $\text{pattern.length} = 2$

- `text` and `pattern` consist only of lowercase English letters.