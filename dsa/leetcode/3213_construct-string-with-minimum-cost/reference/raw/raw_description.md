## Description

You are given a string `target`, an array of strings `words`, and an integer array `costs`, both arrays of the same length.

Imagine an empty string `s`.

You can perform the following operation any number of times (including **zero**):

	- Choose an index `i` in the range `[0, words.length - 1]`.

	- Append `words[i]` to `s`.

	- The cost of operation is `costs[i]`.

Return the **minimum** cost to make `s` equal to `target`. If it's not possible, return `-1`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">target = "abcdef", words = ["abdef","abc","d","def","ef"], costs = [100,1,1,10,5]</span>

**Output:** <span class="example-io">7</span>

**Explanation:**

The minimum cost can be achieved by performing the following operations:

	- Select index 1 and append `"abc"` to `s` at a cost of 1, resulting in `s = "abc"`.

	- Select index 2 and append `"d"` to `s` at a cost of 1, resulting in `s = "abcd"`.

	- Select index 4 and append `"ef"` to `s` at a cost of 5, resulting in `s = "abcdef"`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">target = "aaaa", words = ["z","zz","zzz"], costs = [1,10,100]</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

It is impossible to make `s` equal to `target`, so we return -1.

</div>

**Constraints:**

	- `1 <= target.length <= 5 * 10^4`

	- `1 <= words.length == costs.length <= 5 * 10^4`

	- `1 <= words[i].length <= target.length`

	- The total sum of `words[i].length` is less than or equal to `5 * 10^4`.

	- `target` and `words[i]` consist only of lowercase English letters.

	- `1 <= costs[i] <= 10^4`
