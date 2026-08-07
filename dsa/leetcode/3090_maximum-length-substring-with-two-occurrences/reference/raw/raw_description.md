## Description

Given a string `s`, return the **maximum** length of a <span data-keyword="substring">substring</span> such that it contains *at most two occurrences* of each character.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "bcbbbcba"</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

The following substring has a length of 4 and contains at most two occurrences of each character: `"bcbb<u>bcba</u>"`.</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "aaaa"</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The following substring has a length of 2 and contains at most two occurrences of each character: `"<u>aa</u>aa"`.</div>

**Constraints:**

	- `2 <= s.length <= 100`

	- `s` consists only of lowercase English letters.
