### 1. Description

You are given a **binary** string `s` and an integer `k`.

You are also given a 2D integer array `queries`, where $\text{queries}[i] = [l_{i}, r_{i}]$.

A **binary string** satisfies the **k-constraint** if **either** of the following conditions holds:

- The number of `0`'s in the string is at most `k`.

- The number of `1`'s in the string is at most `k`.

Return an integer array `answer`, where $\text{answer}[i]$ is the number of substrings of $s[l_{i}..r_{i}]$ that satisfy the **k-constraint**.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** s = "0001111", k = 2, queries = [[0,6]]

**Output:** [26]

**Explanation:**

For the query `[0, 6]`, all substrings of $s[0..6] = "0001111"$ satisfy the k-constraint except for the substrings $s[0..5] = "000111"$ and $s[0..6] = "0001111"$.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "010101", k = 1, queries = [[0,5],[1,4],[2,3]]

**Output:** [15,9,3]

**Explanation:**

The substrings of `s` with a length greater than 3 do not satisfy the k-constraint.

</div>

### 4. Constraints

- $1 \le \text{s.length} \le 10^{5}$

- $s[i]$ is either `'0'` or `'1'`.

- $1 \le k \le \text{s.length}$

- $1 \le \text{queries.length} \le 10^{5}$

- $\text{queries}[i] = [l_{i}, r_{i}]$

- $0 \le l_{i} \le r_{i} < \text{s.length}$

- All queries are distinct.