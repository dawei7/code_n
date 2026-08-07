## Description

You are given two strings, `source` and `target`.

You are also given a 2D string array `rules`, where `rules[i] = [pattern_i, replacement_i]`, and an integer array `costs`, where `costs[i]` is the base cost of applying `rules[i]`. Both arrays have the same length. Additionally, `pattern_i` and `replacement_i` have the same length.

You may apply **any** rule **any** number of times. Each rule application works as follows:

	- Choose an index `l` such that the range of positions from `l` to `l + pattern_i.length - 1` exists in the current string and **none** of these positions has been used in a previous rule application.

	- For each index `j`, the character `pattern_i[j]` must either be **equal** to the current character at position `l + j`, or be `'*'`.

	- Replace the characters in this range with `replacement_i`. The replacement is used **exactly** as given and does not contain wildcards.

	- The cost of this rule application is `costs[i]` **plus** the number of `'*'` characters in `pattern_i`.

	- Once a character position has been used in a rule application, it **cannot** be used in any **later** rule application.

Since every `pattern_i` and `replacement_i` have the same length, character positions are preserved after every rule application.

Return the **minimum** total cost required to transform `source` into `target`. If it is impossible, return -1.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">source = "hello", target = "world", rules = [["he","wo"],["llo","rld"]], costs = [3,4]</span>

**Output:** <span class="example-io">7</span>

**Explanation:**

	- Apply `rules[0]` to replace `"he"` with `"wo"` at cost 3, so the string becomes `"wollo"`.

	- Apply `rules[1]` to replace `"llo"` with `"rld"` at cost 4, so the string becomes `"world"`.

	- The total cost is `3 + 4 = 7`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">source = "cat", target = "dog", rules = [["c*t","dog"]], costs = [2]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

	- Apply `rules[0]` to replace `"cat"` with `"dog"`. The wildcard `'*'` matches `'a'`, adding 1 to the base cost 2.

	- The total cost is `2 + 1 = 3`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">source = "test", target = "next", rules = [["*e*t","next"]], costs = [4]</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

	- Apply `rules[0]` to replace `"test"` with `"next"`. The first wildcard matches `'t'` and the second wildcard matches `'s'`, adding 2 to the base cost 4.

	- The total cost is `4 + 2 = 6`.

</div>

**Example 4:**

<div class="example-block">
**Input:** <span class="example-io">source = "ab", target = "bc", rules = [["a*","bd"]], costs = [9]</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

No sequence of rule applications can transform `source` into `target`, so the answer is -1.

</div>

**Constraints:**

	- `1 <= source.length == target.length <= 5000`

	- `source` and `target` consist of lowercase English letters.

	- `1 <= rules.length == costs.length <= 200`

	- `rules[i] = [pattern_i, replacement_i]`

	- `1 <= pattern_i.length == replacement_i.length <= 20`

	- `pattern_i` contains at least one lowercase English letter and at most 5 `'*'` characters.

	- `replacement_i` contains only lowercase English letters.

	- `1 <= costs[i] <= 1000`
