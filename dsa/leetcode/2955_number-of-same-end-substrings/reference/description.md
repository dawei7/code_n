## Description

You are given a **0-indexed** string `s`, and a 2D array of integers `queries`, where $\text{queries}[i] = [l_{i}, r_{i}]$ indicates a substring of `s` starting from the index $l_{i}$ and ending at the index $r_{i}$ (both **inclusive**), i.e. $s[l_{i}..r_{i}]$.

Return *an array *`ans`* where* $\text{ans}[i]$ *is the number of **same-end** substrings of* $\text{queries}[i]$.

A **0-indexed** string `t` of length `n` is called **same-end** if it has the same character at both of its ends, i.e., $t[0] = t[n - 1]$.

A **substring** is a contiguous non-empty sequence of characters within a string.
### Function Contract

- Refer to method signature.

### Examples
#### Example 1

- **Input:** `s = "abcaab", queries = [[0,0],[1,4],[2,5],[0,5]]`
- **Output:** `[1,5,5,10]`
- **Explanation:** Here is the same-end substrings of each query:
1^st query: s[0..0] is "a" which has 1 same-end substring: "**<u>a</u>**".
2^nd query: s[1..4] is "bcaa" which has 5 same-end substrings: "**<u>b</u>**caa", "b**<u>c</u>**aa", "bc**<u>a</u>**a", "bca**<u>a</u>**", "bc**<u>aa</u>**".
3^rd query: s[2..5] is "caab" which has 5 same-end substrings: "**<u>c</u>**aab", "c**<u>a</u>**ab", "ca**<u>a</u>**b", "caa**<u>b</u>**", "c**<u>aa</u>**b".
4^th query: s[0..5] is "abcaab" which has 10 same-end substrings: "**<u>a</u>**bcaab", "a**<u>b</u>**caab", "ab**<u>c</u>**aab", "abc**<u>a</u>**ab", "abca**<u>a</u>**b", "abcaa**<u>b</u>**", "abc**<u>aa</u>**b", "**<u>abca</u>**ab", "**<u>abcaa</u>**b", "a**<u>bcaab</u>**".
#### Example 2

- **Input:** `s = "abcd", queries = [[0,3]]`
- **Output:** `[4]`
- **Explanation:** The only query is s[0..3] which is "abcd". It has 4 same-end substrings: "**<u>a</u>**bcd", "a**<u>b</u>**cd", "ab**<u>c</u>**d", "abc**<u>d</u>**".
### Constraints

- $2 \le \text{s.length} \le 3 * 10^{4}$

- `s` consists only of lowercase English letters.

- $1 \le \text{queries.length} \le 3 * 10^{4}$

- $\text{queries}[i] = [l_{i}, r_{i}]$

- $0 \le l_{i} \le r_{i} < \text{s.length}$