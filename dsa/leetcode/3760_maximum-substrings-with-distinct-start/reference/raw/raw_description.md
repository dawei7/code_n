## Description

You are given a string `s` consisting of lowercase English letters.

Return an integer denoting the **maximum** number of <span data-keyword="substring-nonempty">substrings</span> you can split `s` into such that each **substring** starts with a **distinct** character (i.e., no two substrings start with the same character).

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "abab"</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

	- Split `"abab"` into `"a"` and `"bab"`.

	- Each substring starts with a distinct character i.e `'a'` and `'b'`. Thus, the answer is 2.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "abcd"</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

	- Split `"abcd"` into `"a"`, `"b"`, `"c"`, and `"d"`.

	- Each substring starts with a distinct character. Thus, the answer is 4.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "aaaa"</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

	- All characters in `"aaaa"` are `'a'`.

	- Only one substring can start with `'a'`. Thus, the answer is 1.

</div>

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` consists of lowercase English letters.
