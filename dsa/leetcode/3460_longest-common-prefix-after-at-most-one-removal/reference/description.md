## Description

You are given two strings `s` and `t`.

Return the **length** of the **longest common prefix** between `s` and `t` after removing **at most** one character from `s`.

**Note:** `s` can be left without any removal.
### Function Contract

- Refer to method signature.

### Examples

#### Example 1

<div class="example-block">
**Input:** s = "madxa", t = "madam"

**Output:** 4

**Explanation:**

Removing $s[3]$ from `s` results in `"mada"`, which has a longest common prefix of length 4 with `t`.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "leetcode", t = "eetcode"

**Output:** 7

**Explanation:**

Removing $s[0]$ from `s` results in `"eetcode"`, which matches `t`.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "one", t = "one"

**Output:** 3

**Explanation:**

No removal is needed.

</div>
#### Example 4

<div class="example-block">
**Input:** s = "a", t = "b"

**Output:** 0

**Explanation:**

`s` and `t` cannot have a common prefix.

</div>
### Constraints

- $1 \le \text{s.length} \le 10^{5}$

- $1 \le \text{t.length} \le 10^{5}$

- `s` and `t` contain only lowercase English letters.