## Description

You are given two strings `s` and `t` such that every character occurs at most once in `s` and `t` is a permutation of `s`.

The **permutation difference** between `s` and `t` is defined as the **sum** of the absolute difference between the index of the occurrence of each character in `s` and the index of the occurrence of the same character in `t`.

Return the **permutation difference** between `s` and `t`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "abc", t = "bac"</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

For `s = "abc"` and `t = "bac"`, the permutation difference of `s` and `t` is equal to the sum of:

	- The absolute difference between the index of the occurrence of `"a"` in `s` and the index of the occurrence of `"a"` in `t`.

	- The absolute difference between the index of the occurrence of `"b"` in `s` and the index of the occurrence of `"b"` in `t`.

	- The absolute difference between the index of the occurrence of `"c"` in `s` and the index of the occurrence of `"c"` in `t`.

That is, the permutation difference between `s` and `t` is equal to `|0 - 1| + |1 - 0| + |2 - 2| = 2`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "abcde", t = "edbac"</span>

**Output:** <span class="example-io">12</span>

**Explanation:** The permutation difference between `s` and `t` is equal to `|0 - 3| + |1 - 2| + |2 - 4| + |3 - 1| + |4 - 0| = 12`.

</div>

**Constraints:**

	- `1 <= s.length <= 26`

	- Each character occurs at most once in `s`.

	- `t` is a permutation of `s`.

	- `s` consists only of lowercase English letters.
