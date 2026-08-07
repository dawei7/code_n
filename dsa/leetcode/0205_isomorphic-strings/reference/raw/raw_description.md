## Description

Given two strings `s` and `t`, *determine if they are isomorphic*.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "egg", t = "add"</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

The strings `s` and `t` can be made identical by:

	- Mapping `'e'` to `'a'`.

	- Mapping `'g'` to `'d'`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "f11", t = "b23"</span>

**Output:** <span class="example-io">false</span>

**Explanation:**

The strings `s` and `t` can not be made identical as `'1'` needs to be mapped to both `'2'` and `'3'`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "paper", t = "title"</span>

**Output:** <span class="example-io">true</span>

</div>

**Constraints:**

	- `1 <= s.length <= 5 * 10^4`

	- `t.length == s.length`

	- `s` and `t` consist of any valid ascii character.
