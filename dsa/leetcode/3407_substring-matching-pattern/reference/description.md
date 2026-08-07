### 1. Description

You are given a string `s` and a pattern string `p`, where `p` contains **exactly one** `'*'` character.

The `'*'` in `p` can be replaced with any sequence of zero or more characters.

Return `true` if `p` can be made a substring of `s`, and `false` otherwise.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** s = "leetcode", p = "ee*e"

**Output:** true

**Explanation:**

By replacing the `'*'` with `"tcod"`, the substring `"eetcode"` matches the pattern.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "car", p = "c*v"

**Output:** false

**Explanation:**

There is no substring matching the pattern.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "luck", p = "u*"

**Output:** true

**Explanation:**

The substrings `"u"`, `"uc"`, and `"uck"` match the pattern.

</div>

### 4. Constraints

- $1 \le \text{s.length} \le 50$

- $1 \le \text{p.length} \le 50$

- `s` contains only lowercase English letters.

- `p` contains only lowercase English letters and exactly one `'*'`