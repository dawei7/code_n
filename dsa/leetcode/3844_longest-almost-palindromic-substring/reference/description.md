## Description

You are given a string `s` consisting of lowercase English letters.

A substring is **almost-palindromic** if it becomes a palindrome after removing **exactly** one character from it.

Return an integer denoting the length of the **longest** **almost-palindromic** substring in `s`.
### Function Contract

**Inputs**

- `s`: The lowercase English string in which a contiguous substring is chosen.

For substring boundaries $0\le l\le r<\lvert\texttt{s}\rvert$, the candidate is $s[l:r + 1]$. It is almost-palindromic exactly when there is an index $k$ with $l\le k\le r$ such that

$\texttt{s}[l:k]\mathbin{+}\texttt{s}[k+1:r+1]$

is a palindrome. This expression deletes one character, $s[k]$, while preserving the order of every other character.

**Return value**

Return the maximum value of $r-l+1$ over all almost-palindromic substrings. Since $\lvert\texttt{s}\rvert\ge2$, an answer of at least `2` always exists: deleting either character from any length-two substring leaves a one-character palindrome.

### Examples

#### Example 1

<div class="example-block">
**Input:** s = "abca"

**Output:** 4

**Explanation:**

Choose the substring `"<u>**abca**</u>"`.

- Remove `"ab<u>**c**</u>a"`.

- The string becomes `"aba"`, which is a palindrome.

- Therefore, `"abca"` is almost-palindromic.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "abba"

**Output:** 4

**Explanation:**

Choose the substring `"<u>**abba**</u>"`.

- Remove `"a<u>**b**</u>ba"`.

- The string becomes `"aba"`, which is a palindrome.

- Therefore, `"abba"` is almost-palindromic.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "zzabba"

**Output:** 5

**Explanation:**

Choose the substring `"z<u>**zabba**</u>"`.

- Remove `"<u>**z**</u>abba"`.

- The string becomes `"abba"`, which is a palindrome.

- Therefore, `"zabba"` is almost-palindromic.

</div>
### Constraints

- $2 \le \text{s.length} \le 2500$

- `s` consists of only lowercase English letters.