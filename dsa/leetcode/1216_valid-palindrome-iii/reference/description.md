## Description

Given a string `s` and an integer `k`, return `true` if `s` is a `k`**-palindrome**.

A string is `k`**-palindrome** if it can be transformed into a palindrome by removing at most `k` characters from it.
### Function Contract

**Inputs**

- `s`: The string to test.
- `k`: The maximum number of characters that may be removed.

Let $n = \lvert\texttt{s}\rvert$. Removing characters retains a subsequence of `s`; the retained characters cannot be reordered.

**Return value**

Return `true` if some palindromic subsequence of `s` has length at least $n-k$. Otherwise, return `false`.

### Examples
#### Example 1

- **Input:** `s = "abcdeca", k = 2`
- **Output:** `true`
- **Explanation:** Remove 'b' and 'e' characters.
#### Example 2

- **Input:** `s = "abbababa", k = 1`
- **Output:** `true`
### Constraints

- $1 \le \text{s.length} \le 1000$

- `s` consists of only lowercase English letters.

- $1 \le k \le \text{s.length}$