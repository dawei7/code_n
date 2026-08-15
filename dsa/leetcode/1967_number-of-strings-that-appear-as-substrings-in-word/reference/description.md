### 1. Description

Given an array of strings `patterns` and a string `word`, return *the **number** of strings in *`patterns`* that exist as a **substring** in *`word`.

A **substring** is a contiguous sequence of characters within a string.

### 2. Function Contract

**Inputs**

- `patterns`: Input parameter (`List[str]`).
- `word`: Input parameter (`str`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $patterns = ["a","abc","bc","d"], word = "abc"$
- **Output:** `3`
- **Explanation:** 
- "a" appears as a substring in "<u>a</u>bc".
- "abc" appears as a substring in "<u>abc</u>".
- "bc" appears as a substring in "a<u>bc</u>".
- "d" does not appear as a substring in "abc".
3 of the strings in patterns appear as a substring in word.

#### Example 2

- **Input:** $patterns = ["a","b","c"], word = "aaaaabbbbb"$
- **Output:** `2`
- **Explanation:** 
- "a" appears as a substring in "a<u>a</u>aaabbbbb".
- "b" appears as a substring in "aaaaabbbb<u>b</u>".
- "c" does not appear as a substring in "aaaaabbbbb".
2 of the strings in patterns appear as a substring in word.

#### Example 3

- **Input:** $patterns = ["a","a","a"], word = "ab"$
- **Output:** `3`
- **Explanation:** Each of the patterns appears as a substring in word "<u>a</u>b".

### 4. Constraints

- $1 \le \text{patterns.length} \le 100$

- $1 \le \text{patterns}[i].length \le 100$

- $1 \le \text{word.length} \le 100$

- $\text{patterns}[i]$ and `word` consist of lowercase English letters.
