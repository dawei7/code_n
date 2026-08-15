### 1. Description

You are given a string `s` of length `n` consisting of lowercase English letters.

Return the smallest index `i` such that $s[i] = s[n - i - 1]$.

If no such index exists, return -1.

### 2. Function Contract

**Inputs**

- `s`: A non-empty string of lowercase English letters.

Let $n=\lvert\texttt{s}\rvert$. The mirror of an index $i$ is $m(i)=n-i-1$, so valid indices are tested against pairs $s[i]$ and `s[m(i)]`.

**Return value**

Return the minimum index $i$ for which $s[i] = s[n - i - 1]$. Return `-1` when no such index exists.

### 3. Examples

#### Example 1

- **Input:** s = "abcacbd"

- **Output:** 1

- **Explanation:** At index $i = 1$, $s[1]$ and $s[5]$ are both `'b'`.

No smaller index satisfies the condition, so the answer is 1.

#### Example 2

- **Input:** s = "abc"

- **Output:** 1

- **Explanation:** ​​​​​​​At index $i = 1$, the two compared positions coincide, so both characters are `'b'`.

No smaller index satisfies the condition, so the answer is 1.

#### Example 3

- **Input:** s = "abcdab"

- **Output:** -1

- **Explanation:** ​​​​​​​For every index `i`, the characters at positions `i` and $n - i - 1$ are different.

Therefore, no valid index exists, so the answer is -1.

### 4. Constraints

- $1 \le n = \text{s.length} \le 100$

- `s` consists of lowercase English letters.
