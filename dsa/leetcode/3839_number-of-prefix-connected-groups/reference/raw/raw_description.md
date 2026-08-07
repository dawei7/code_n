## Description

You are given an array of strings `words` and an integer `k`.

Two words `a` and `b` at **distinct indices** are **<span data-keyword="string-prefix">prefix</span>-connected** if `a[0..k-1] == b[0..k-1]`.

A **connected group** is a set of words such that each pair of words is prefix-connected.

Return the **number of connected groups** that contain **at least** two words, formed from the given words.

**Note:**

	- Words with length less than `k` cannot join any group and are ignored.

	- Duplicate strings are treated as separate words.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">words = ["apple","apply","banana","bandit"], k = 2</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

Words sharing the same first `k = 2` letters are grouped together:

	- `words[0] = "apple"` and `words[1] = "apply"` share prefix `"ap"`.

	- `words[2] = "banana"` and `words[3] = "bandit"` share prefix `"ba"`.

Thus, there are 2 connected groups, each containing at least two words.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">words = ["car","cat","cartoon"], k = 3</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

Words are evaluated for a prefix of length `k = 3`:

	- `words[0] = "car"` and `words[2] = "cartoon"` share prefix `"car"`.

	- `words[1] = "cat"` does not share a 3-length prefix with any other word.

Thus, there is 1 connected group.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">words = </span>["bat","dog","dog","doggy","bat"]<span class="example-io">, k = 3</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

Words are evaluated for a prefix of length `k = 3`:

	- `words[0] = "bat"` and `words[4] = "bat"` form a group.

	- `words[1] = "dog"`, `words[2] = "dog"` and `words[3] = "doggy"` share prefix `"dog"`.

Thus, there are 2 connected groups, each containing at least two words.

</div>

**Constraints:**

	- `1 <= words.length <= 5000`

	- `1 <= words[i].length <= 100`

	- `1 <= k <= 100`

	- All strings in `words` consist of lowercase English letters.
