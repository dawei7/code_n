## Description

You are given a string `s`.

A string `t` is called **good** if all characters of `t` occur the same number of times.

You can perform the following operations **any number of times**:

	- Delete a character from `s`.

	- Insert a character in `s`.

	- Change a character in `s` to its next letter in the alphabet.

**Note** that you cannot change `'z'` to `'a'` using the third operation.

Return* *the **minimum** number of operations required to make `s` **good**.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "acab"</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

We can make `s` good by deleting one occurrence of character `'a'`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "wddw"</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

We do not need to perform any operations since `s` is initially good.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "aaabc"</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

We can make `s` good by applying these operations:

	- Change one occurrence of `'a'` to `'b'`

	- Insert one occurrence of `'c'` into `s`

</div>

**Constraints:**

	- `3 <= s.length <= 2 * 10^4`

	- `s` contains only lowercase English letters.
