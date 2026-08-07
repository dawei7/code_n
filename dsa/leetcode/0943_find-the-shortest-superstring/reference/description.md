### 1. Description

Given an array of strings `words`, return *the smallest string that contains each string in* `words` *as a substring*. If there are multiple valid strings of the smallest length, return **any of them**.

You may assume that no string in `words` is a substring of another string in `words`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $words = ["alex","loves","leetcode"]$
- **Output:** `"alexlovesleetcode"`
- **Explanation:** All permutations of "alex","loves","leetcode" would also be accepted.
#### Example 2

- **Input:** $words = ["catg","ctaagt","gcta","ttca","atgcatc"]$
- **Output:** `"gctaagttcatgcatc"`

### 4. Constraints

- $1 \le \text{words.length} \le 12$

- $1 \le \text{words}[i].length \le 20$

- $\text{words}[i]$ consists of lowercase English letters.

- All the strings of `words` are **unique**.