### 1. Description

Given a list of strings `dict` where all the strings are of the same length.

Return `true` if there are 2 strings that only differ by 1 character in the same index, otherwise return `false`.

### 2. Function Contract

**Inputs**

- `dict`: A list of $q$ distinct lowercase strings, each of uniform length $\ell$ ($1 \le q \le 10^5$, $1 \le \ell \le 20$, total characters $\le 10^5$).

**Return value**

Return `true` if there exist two strings in `dict` with Hamming distance exactly 1; otherwise return `false`.

### 3. Examples

#### Example 1

- **Input:** $dict = ["abcd","acbd", "aacd"]$
- **Output:** `true`
- **Explanation:** Strings "a**b**cd" and "a**a**cd" differ only by one character in the index 1.
#### Example 2

- **Input:** $dict = ["ab","cd","yz"]$
- **Output:** `false`
#### Example 3

- **Input:** $dict = ["abcd","cccc","abyd","abab"]$
- **Output:** `true`

### 4. Constraints

- The number of characters in $dict \le 10^{5}$

- $\text{dict}[i].length = \text{dict}[j].length$

- $\text{dict}[i]$ should be unique.

- $\text{dict}[i]$ contains only lowercase English letters.