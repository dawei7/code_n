## Description

You are given a string `s` of length `n` and an integer array `cost` of the same length, where `cost[i]` is the cost to **delete** the `i^th` character of `s`.

You may delete any number of characters from `s` (possibly none), such that the resulting string is **non-empty** and consists of **equal** characters.

Return an integer denoting the **minimum** total deletion cost required.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "aabaac", cost = [1,2,3,4,1,10]</span>

**Output:** <span class="example-io">11</span>

**Explanation:**

Deleting the characters at indices 0, 1, 2, 3, 4 results in the string `"c"`, which consists of equal characters, and the total cost is `cost[0] + cost[1] + cost[2] + cost[3] + cost[4] = 1 + 2 + 3 + 4 + 1 = 11`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "abc", cost = [10,5,8]</span>

**Output:** <span class="example-io">13</span>

**Explanation:**

Deleting the characters at indices 1 and 2 results in the string `"a"`, which consists of equal characters, and the total cost is `cost[1] + cost[2] = 5 + 8 = 13`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "zzzzz", cost = [67,67,67,67,67]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

All characters in `s` are equal, so the deletion cost is 0.

</div>

**Constraints:**

	- `n == s.length == cost.length`

	- `1 <= n <= 10^5`

	- `1 <= cost[i] <= 10^9`

	- `s` consists of lowercase English letters.
