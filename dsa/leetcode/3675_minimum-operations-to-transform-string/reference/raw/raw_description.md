## Description

You are given a string `s` consisting only of lowercase English letters.

You can perform the following operation any number of times (including zero):

	- Choose any character `c` in the string and replace **every** occurrence of `c` with the **next** lowercase letter in the English alphabet.

Return the **minimum** number of operations required to transform `s` into a string consisting of **only** `'a'` characters.

**Note: **Consider the alphabet as circular, thus `'a'` comes after `'z'`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "yz"</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

	- Change `'y'` to `'z'` to get `"zz"`.

	- Change `'z'` to `'a'` to get `"aa"`.

	- Thus, the answer is 2.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "a"</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

	- The string `"a"` only consists of `'a'`​​​​​​​ characters. Thus, the answer is 0.

</div>

**Constraints:**

	- `1 <= s.length <= 5 * 10^5`

	- `s` consists only of lowercase English letters.
