### 1. Description

You are given a **0-indexed** array of string `words` and two integers `left` and `right`.

A string is called a **vowel string** if it starts with a vowel character and ends with a vowel character where vowel characters are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

Return *the number of vowel strings *$\text{words}[i]$* where *`i`* belongs to the inclusive range *`[left, right]`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $words = ["are","amy","u"], left = 0, right = 2$
- **Output:** `2`
- **Explanation:**
- "are" is a vowel string because it starts with 'a' and ends with 'e'.
- "amy" is not a vowel string because it does not end with a vowel.
- "u" is a vowel string because it starts with 'u' and ends with 'u'.
The number of vowel strings in the mentioned range is 2.
#### Example 2

- **Input:** $words = ["hey","aeo","mu","ooo","artro"], left = 1, right = 4$
- **Output:** `3`
- **Explanation:**
- "aeo" is a vowel string because it starts with 'a' and ends with 'o'.
- "mu" is not a vowel string because it does not start with a vowel.
- "ooo" is a vowel string because it starts with 'o' and ends with 'o'.
- "artro" is a vowel string because it starts with 'a' and ends with 'o'.
The number of vowel strings in the mentioned range is 3.

### 4. Constraints

- $1 \le \text{words.length} \le 1000$

- $1 \le \text{words}[i].length \le 10$

- $\text{words}[i]$ consists of only lowercase English letters.

- $0 \le left \le right < \text{words.length}$