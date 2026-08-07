## Description

Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and **may** press a key for too long, resulting in a character being typed **multiple** times.

Although Alice tried to focus on her typing, she is aware that she may still have done this **at most** *once*.

You are given a string `word`, which represents the **final** output displayed on Alice's screen.

Return the total number of *possible* original strings that Alice *might* have intended to type.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">word = "abbcccc"</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

The possible strings are: `"abbcccc"`, `"abbccc"`, `"abbcc"`, `"abbc"`, and `"abcccc"`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">word = "abcd"</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

The only possible string is `"abcd"`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">word = "aaaa"</span>

**Output:** <span class="example-io">4</span>

</div>

**Constraints:**

	- `1 <= word.length <= 100`

	- `word` consists only of lowercase English letters.
