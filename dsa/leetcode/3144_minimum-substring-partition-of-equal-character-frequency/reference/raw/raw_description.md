## Description

Given a string `s`, you need to partition it into one or more **balanced** <span data-keyword="substring">substrings</span>. For example, if `s == "ababcc"` then `("abab", "c", "c")`, `("ab", "abc", "c")`, and `("ababcc")` are all valid partitions, but `("a", **"bab"**, "cc")`, `(**"aba"**, "bc", "c")`, and `("ab", **"abcc"**)` are not. The unbalanced substrings are bolded.

Return the **minimum** number of substrings that you can partition `s` into.

**Note:** A **balanced** string is a string where each character in the string occurs the same number of times.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "fabccddg"</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

We can partition the string `s` into 3 substrings in one of the following ways: `("fab, "ccdd", "g")`, or `("fabc", "cd", "dg")`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "abababaccddb"</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

We can partition the string `s` into 2 substrings like so: `("abab", "abaccddb")`.

</div>

**Constraints:**

	- `1 <= s.length <= 1000`

	- `s` consists only of English lowercase letters.
