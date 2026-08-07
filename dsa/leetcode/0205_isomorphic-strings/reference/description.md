## Description

Given two strings `s` and `t`, *determine if they are isomorphic*.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
### Function Contract

**Inputs**

- `s`: The source string whose characters define the mapping.
- `t`: The target string to compare with the mapped form of `s`.

**Return value**

Return `true` exactly when a consistent one-to-one character mapping transforms `s` into `t`.

### Examples
#### Example 1

<div class="example-block">
**Input:** s = "egg", t = "add"

**Output:** true

**Explanation:**

The strings `s` and `t` can be made identical by:

- Mapping `'e'` to `'a'`.

- Mapping `'g'` to `'d'`.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "f11", t = "b23"

**Output:** false

**Explanation:**

The strings `s` and `t` can not be made identical as `'1'` needs to be mapped to both `'2'` and `'3'`.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "paper", t = "title"

**Output:** true

</div>
### Constraints

- $1 \le \text{s.length} \le 5 * 10^{4}$

- $\text{t.length} = \text{s.length}$

- `s` and `t` consist of any valid ascii character.