## Description

You are given a string `s` and an integer `k`.

Define a function `distance(s_1, s_2)` between two strings `s_1` and `s_2` of the same length `n` as:

	- The** sum** of the **minimum distance** between `s_1[i]` and `s_2[i]` when the characters from `'a'` to `'z'` are placed in a **cyclic** order, for all `i` in the range `[0, n - 1]`.

For example, `distance("ab", "cd") == 4`, and `distance("a", "z") == 1`.

You can **change** any letter of `s` to **any** other lowercase English letter, **any** number of times.

Return a string denoting the **<span data-keyword="lexicographically-smaller-string">lexicographically smallest</span>** string `t` you can get after some changes, such that `distance(s, t) <= k`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "zbbz", k = 3</span>

**Output:** <span class="example-io">"aaaz"</span>

**Explanation:**

Change `s` to `"aaaz"`. The distance between `"zbbz"` and `"aaaz"` is equal to `k = 3`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "xaxcd", k = 4</span>

**Output:** <span class="example-io">"aawcd"</span>

**Explanation:**

The distance between "xaxcd" and "aawcd" is equal to k = 4.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "lol", k = 0</span>

**Output:** <span class="example-io">"lol"</span>

**Explanation:**

It's impossible to change any character as `k = 0`.

</div>

**Constraints:**

	- `1 <= s.length <= 100`

	- `0 <= k <= 2000`

	- `s` consists only of lowercase English letters.
