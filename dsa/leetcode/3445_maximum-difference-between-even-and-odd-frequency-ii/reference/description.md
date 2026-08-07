### 1. Description

You are given a string `s` and an integer `k`. Your task is to find the **maximum** difference between the frequency of **two** characters, $\text{freq}[a] - \text{freq}[b]$, in a substring `subs` of `s`, such that:

- `subs` has a size of **at least** `k`.

- Character `a` has an *odd frequency* in `subs`.

- Character `b` has a **non-zero** *even frequency* in `subs`.

Return the **maximum** difference.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Note

that `subs` can contain more than 2 **distinct** characters.

### 4. Examples

#### Example 1

<div class="example-block">
**Input:** s = "12233", k = 4

**Output:** -1

**Explanation:**

For the substring `"12233"`, the frequency of `'1'` is 1 and the frequency of `'3'` is 2. The difference is $1 - 2 = -1$.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "1122211", k = 3

**Output:** 1

**Explanation:**

For the substring `"11222"`, the frequency of `'2'` is 3 and the frequency of `'1'` is 2. The difference is $3 - 2 = 1$.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "110", k = 3

**Output:** -1

</div>

### 5. Constraints

- $3 \le \text{s.length} \le 3 * 10^{4}$

- `s` consists only of digits `'0'` to `'4'`.

- The input is generated that at least one substring has a character with an even frequency and a character with an odd frequency.

- $1 \le k \le \text{s.length}$