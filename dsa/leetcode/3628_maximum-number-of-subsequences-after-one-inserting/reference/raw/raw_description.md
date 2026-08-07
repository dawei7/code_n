## Description

You are given a string `s` consisting of uppercase English letters.

You are allowed to insert **at most one** uppercase English letter at **any** position (including the beginning or end) of the string.

Return the **maximum** number of `"LCT"` <span data-keyword="subsequence-string-nonempty">subsequences</span> that can be formed in the resulting string after **at most one insertion**.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "LMCT"</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

We can insert a `"L"` at the beginning of the string s to make `"LLMCT"`, which has 2 subsequences, at indices [0, 3, 4] and [1, 3, 4].

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "LCCT"</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

We can insert a `"L"` at the beginning of the string s to make `"LLCCT"`, which has 4 subsequences, at indices [0, 2, 4], [0, 3, 4], [1, 2, 4] and [1, 3, 4].

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "L"</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

Since it is not possible to obtain the subsequence `"LCT"` by inserting a single letter, the result is 0.

</div>

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s` consists of uppercase English letters.
