## Description

You are given a string array `words`.

Find the **maximum distance** between two **distinct** indices `i` and `j` such that:

	- `words[i] != words[j]`, and

	- the distance is defined as `j - i + 1`.

Return the maximum distance among all such pairs. If no valid pair exists, return 0.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">words = ["leetcode","leetcode","codeforces"]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

In this example, `words[0]` and `words[2]` are not equal, and they have the maximum distance `2 - 0 + 1 = 3`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">words = ["a","b","c","a","a"]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

In this example `words[1]` and `words[4]` have the largest distance of `4 - 1 + 1 = 4`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">words = ["z","z","z"]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

In this example all the words are equal, thus the answer is 0.

</div>

**Constraints:**

	- `1 <= words.length <= 100`

	- `1 <= words[i].length <= 10`

	- `words[i]` consists of lowercase English letters.
