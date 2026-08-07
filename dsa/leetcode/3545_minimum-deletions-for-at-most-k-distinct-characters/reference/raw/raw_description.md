## Description

You are given a string `s` consisting of lowercase English letters, and an integer `k`.

Your task is to delete some (possibly none) of the characters in the string so that the number of **distinct** characters in the resulting string is **at most** `k`.

Return the **minimum** number of deletions required to achieve this.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "abc", k = 2</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

	- `s` has three distinct characters: `'a'`, `'b'` and `'c'`, each with a frequency of 1.

	- Since we can have at most `k = 2` distinct characters, remove all occurrences of any one character from the string.

	- For example, removing all occurrences of `'c'` results in at most `k` distinct characters. Thus, the answer is 1.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "aabb", k = 2</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

	- `s` has two distinct characters (`'a'` and `'b'`) with frequencies of 2 and 2, respectively.

	- Since we can have at most `k = 2` distinct characters, no deletions are required. Thus, the answer is 0.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "yyyzz", k = 1</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

	- `s` has two distinct characters (`'y'` and `'z'`) with frequencies of 3 and 2, respectively.

	- Since we can have at most `k = 1` distinct character, remove all occurrences of any one character from the string.

	- Removing all `'z'` results in at most `k` distinct characters. Thus, the answer is 2.

</div>

**Constraints:**

	- `1 <= s.length <= 16`

	- `1 <= k <= 16`

	- `s` consists only of lowercase English letters.
