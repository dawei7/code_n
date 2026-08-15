### 1. Description

You are given a string array `words` and a string `s`, where $\text{words}[i]$ and `s` comprise only of **lowercase English letters**.

Return *the **number of strings** in* `words` *that are a **prefix** of* `s`.

A **prefix** of a string is a substring that occurs at the beginning of the string. A **substring** is a contiguous sequence of characters within a string.

### 2. Function Contract

**Inputs**

- `words`: Input parameter (`List[str]`).
- `s`: Input parameter (`str`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $words = ["a","b","c","ab","bc","abc"], s = "abc"$
- **Output:** `3`
- **Explanation:** The strings in words which are a prefix of s = "abc" are:
"a", "ab", and "abc".
Thus the number of strings in words which are a prefix of s is 3.

#### Example 2

- **Input:** $words = ["a","a"], s = "aa"$
- **Output:** `2`
- **Explanation:** 
**Both of the strings are a prefix of s.
Note that the same string can occur multiple times in words, and it should be counted each time.

### 4. Constraints

- $1 \le \text{words.length} \le 1000$

- $1 \le \text{words}[i].length, \text{s.length} \le 10$

- $\text{words}[i]$ and `s` consist of lowercase English letters **only**.
