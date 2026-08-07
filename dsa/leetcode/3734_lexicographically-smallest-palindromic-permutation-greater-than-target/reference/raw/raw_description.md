## Description

You are given two strings `s` and `target`, each of length `n`, consisting of lowercase English letters.

Return the **<span data-keyword="lexicographically-smaller-string">lexicographically smallest</span> string** that is **both** a **<span data-keyword="palindrome-string">palindromic</span> <span data-keyword="permutation">permutation</span>** of `s` and **strictly** greater than `target`. If no such permutation exists, return an empty string.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "baba", target = "abba"</span>

**Output:** <span class="example-io">"baab"</span>

**Explanation:**

	- The palindromic permutations of `s` (in lexicographical order) are `"abba"` and `"baab"`.

	- The lexicographically smallest permutation that is strictly greater than `target` is `"baab"`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "baba", target = "bbaa"</span>

**Output:** <span class="example-io">""</span>

**Explanation:**

	- The palindromic permutations of `s` (in lexicographical order) are `"abba"` and `"baab"`.

	- None of them is lexicographically strictly greater than `target`. Therefore, the answer is `""`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "abc", target = "abb"</span>

**Output:** <span class="example-io">""</span>

**Explanation:**

`s` has no palindromic permutations. Therefore, the answer is `""`.

</div>

**Example 4:**

<div class="example-block">
**Input:** <span class="example-io">s = "aac", target = "abb"</span>

**Output:** <span class="example-io">"aca"</span>

**Explanation:**

	- The only palindromic permutation of `s` is `"aca"`.

	- `"aca"` is strictly greater than `target`. Therefore, the answer is `"aca"`.

</div>

**Constraints:**

	- `1 <= n == s.length == target.length <= 300`

	- `s` and `target` consist of only lowercase English letters.
