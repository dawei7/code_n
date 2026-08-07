## Description

You are given a **0-indexed** array of **unique** strings `words`.

A **palindrome pair** is a pair of integers `(i, j)` such that:

- $0 \le i, j < \text{words.length}$,

- $i \neq j$, and

- $\text{words}[i] + \text{words}[j]$ (the concatenation of the two strings) is a palindrome.

Return *an array of all the **palindrome pairs** of *`words`.

You must write an algorithm with $O(sum of \text{words}[i].length)$ runtime complexity.
### Function Contract

**Inputs**

- `words`: A zero-indexed array of distinct lowercase strings; a string may be empty.

**Return value**

Return all ordered index pairs `[i,j]` with distinct indices whose corresponding concatenation is a palindrome.

### Examples
#### Example 1

- **Input:** $words = ["abcd","dcba","lls","s","sssll"]$
- **Output:** `[[0,1],[1,0],[3,2],[2,4]]`
- **Explanation:** The palindromes are ["abcddcba","dcbaabcd","slls","llssssll"]
#### Example 2

- **Input:** $words = ["bat","tab","cat"]$
- **Output:** `[[0,1],[1,0]]`
- **Explanation:** The palindromes are ["battab","tabbat"]
#### Example 3

- **Input:** $words = ["a",""]$
- **Output:** `[[0,1],[1,0]]`
- **Explanation:** The palindromes are ["a","a"]
### Constraints

- $1 \le \text{words.length} \le 5000$

- $0 \le \text{words}[i].length \le 300$

- $\text{words}[i]$ consists of lowercase English letters.