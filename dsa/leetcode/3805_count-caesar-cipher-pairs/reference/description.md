### 1. Description

You are given an array `words` of `n` strings. Each string has length `m` and contains only lowercase English letters.

Two strings `s` and `t` are **similar** if we can apply the following operation any number of times (possibly zero times) so that `s` and `t` become **equal**.

- Choose either `s` or `t`.

- Replace **every** letter in the chosen string with the next letter in the alphabet cyclically. The next letter after `'z'` is `'a'`.

Count the number of pairs of indices `(i, j)` such that:

- `i < j`

- $\text{words}[i]$ and $\text{words}[j]$ are **similar**.

Return an integer denoting the number of such pairs.

### 2. Function Contract

**Inputs**

- `words`: A nonempty array of equal-length lowercase English strings.

Let $n=\lvert\texttt{words}\rvert$, let $m$ be the common word length, and define the total number of input characters as

$S = \sum_{w \in \texttt{words}} \lvert w \rvert = nm.$

Each pair is determined by two distinct indices with the smaller index first. Equal string values at different indices remain distinct elements and may form a valid pair. A cyclic shift advances every character in one selected string by the same amount modulo 26.

**Return value**

Return an integer equal to the number of index pairs whose two strings can be made equal by uniform cyclic shifts.

### 3. Examples

#### Example 1

- **Input:** words = ["fusion","layout"]

- **Output:** 1

- **Explanation:** $\text{words}[0] = "fusion"$ and $\text{words}[1] = "layout"$ are similar because we can apply the operation to `"fusion"` 6 times. The string `"fusion"` changes as follows.

- `"fusion"`

- `"gvtjpo"`

- `"hwukqp"`

- `"ixvlrq"`

- `"jywmsr"`

- `"kzxnts"`

- `"layout"`

#### Example 2

- **Input:** words = ["ab","aa","za","aa"]

- **Output:** 2

- **Explanation:** $\text{words}[0] = "ab"$ and $\text{words}[2] = "za"$ are similar. $\text{words}[1] = "aa"$ and $\text{words}[3] = "aa"$ are similar.

### 4. Constraints

- $1 \le n = \text{words.length} \le 10^{5}$

- $1 \le m = \text{words}[i].length \le 10^{5}$

- $1 \le n * m \le 10^{5}$

- $\text{words}[i]$ consists only of lowercase English letters.
