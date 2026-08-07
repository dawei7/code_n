### 1. Description

You are given a string `s` consisting of lowercase English letters.

Your task is to find the **maximum** difference $diff = freq(a_{1}) - freq(a_{2})$ between the frequency of characters $a_{1}$ and $a_{2}$ in the string such that:

- $a_{1}$ has an **odd frequency** in the string.

- $a_{2}$ has an **even frequency** in the string.

Return this **maximum** difference.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** s = "aaaaabbc"

**Output:** 3

**Explanation:**

- The character `'a'` has an **odd frequency** of `5`, and `'b'` has an **even frequency** of `2`.

- The maximum difference is $5 - 2 = 3$.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "abcabcab"

**Output:** 1

**Explanation:**

- The character `'a'` has an **odd frequency** of `3`, and `'c'` has an **even frequency** of 2.

- The maximum difference is $3 - 2 = 1$.

</div>

### 4. Constraints

- $3 \le \text{s.length} \le 100$

- `s` consists only of lowercase English letters.

- `s` contains at least one character with an odd frequency and one with an even frequency.