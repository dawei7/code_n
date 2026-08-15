### 1. Description

Given a string `s` and an array of strings `words`, return *the number of* $\text{words}[i]$ *that is a subsequence of* `s`.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- For example, `"ace"` is a subsequence of `"abcde"`.

### 2. Function Contract

**Inputs**

- `s`: Input parameter (`str`).
- `words`: Input parameter (`List[str]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** `s = "abcde", words = ["a","bb","acd","ace"]`
- **Output:** `3`
- **Explanation:** There are three strings in words that are a subsequence of s: "a", "acd", "ace".

#### Example 2

- **Input:** `s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]`
- **Output:** `2`

### 4. Constraints

- $1 \le \text{s.length} \le 5 * 10^{4}$

- $1 \le \text{words.length} \le 5000$

- $1 \le \text{words}[i].length \le 50$

- `s` and $\text{words}[i]$ consist of only lowercase English letters.
