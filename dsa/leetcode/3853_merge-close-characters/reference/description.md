### 1. Description

You are given a string `s` consisting of lowercase English letters and an integer `k`.

Two **equal** characters in the **current** string `s` are considered **close** if the distance between their indices is **at most** `k`.

When two characters are **close**, the right one merges into the left. Merges happen **one at a time**, and after each merge, the string updates until no more merges are possible.

Return the resulting string after performing all possible merges.

### 2. Function Contract

**Inputs**

- `s`: A nonempty string containing only lowercase English letters.
- `k`: The maximum allowed distance between the current indices of two equal characters that may merge.

At any stage, a pair of indices $i<j$ is eligible exactly when $s[i] = s[j]$ and

$j-i\le\texttt{k}.$

The chosen eligible pair minimizes $i$ first and $j$ second. Its right character at index $j$ is deleted, its left character at index $i$ remains, and all later indices are recomputed in the shortened string before selecting another pair.

**Return value**

Return the stable string in which no equal characters have current-index distance at most `k`.

### 3. Note

: If multiple merges are possible, always merge the pair with the **smallest left** index. If multiple pairs share the smallest left index, choose the pair with the **smallest right** index.

### 4. Examples

#### Example 1

<div class="example-block">
**Input:** s = "abca", k = 3

**Output:** "abc"

**Explanation:**

- **​​​​​​​**Characters `'a'` at indices $i = 0$ and $i = 3$ are close as $3 - 0 = 3 \le k$.

- Merge them into the left `'a'` and `s = "abc"`.

- No other equal characters are close, so no further merges occur.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "aabca", k = 2

**Output:** "abca"

**Explanation:**

- Characters `'a'` at indices $i = 0$ and $i = 1$ are close as $1 - 0 = 1 \le k$.

- Merge them into the left `'a'` and `s = "abca"`.

- Now the remaining `'a'` characters at indices $i = 0$ and $i = 3$ are not close as `k < 3`, so no further merges occur.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "yybyzybz", k = 2

**Output:** "ybzybz"

**Explanation:**

- Characters `'y'` at indices $i = 0$ and $i = 1$ are close as $1 - 0 = 1 \le k$.

- Merge them into the left `'y'` and `s = "ybyzybz"`.

- Now the characters `'y'` at indices $i = 0$ and $i = 2$ are close as $2 - 0 = 2 \le k$.

- Merge them into the left `'y'` and `s = "ybzybz"`.

- No other equal characters are close, so no further merges occur.

</div>

### 5. Constraints

- $1 \le \text{s.length} \le 100$

- $1 \le k \le \text{s.length}$

- `s` consists of lowercase English letters.