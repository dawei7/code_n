### 1. Description

You are given a string `s` and a pattern string `p`, where `p` contains **exactly two** `'*'` characters.

The `'*'` in `p` matches any sequence of zero or more characters.

Return the length of the **shortest** substring in `s` that matches `p`. If there is no such substring, return -1.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Note

The empty substring is considered valid.

### 4. Examples

#### Example 1

<div class="example-block">
**Input:** s = "abaacbaecebce", p = "ba*c*ce"

**Output:** 8

**Explanation:**

The shortest matching substring of `p` in `s` is `"<u>**ba**</u>e<u>**c**</u>eb<u>**ce**</u>"`.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "baccbaadbc", p = "cc*baa*adb"

**Output:** -1

**Explanation:**

There is no matching substring in `s`.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "a", p = "**"

**Output:** 0

**Explanation:**

The empty substring is the shortest matching substring.

</div>
#### Example 4

<div class="example-block">
**Input:** s = "madlogic", p = "*adlogi*"

**Output:** 6

**Explanation:**

The shortest matching substring of `p` in `s` is `"**<u>adlogi</u>**"`.

</div>

### 5. Constraints

- $1 \le \text{s.length} \le 10^{5}$

- $2 \le \text{p.length} \le 10^{5}$

- `s` contains only lowercase English letters.

- `p` contains only lowercase English letters and exactly two `'*'`.