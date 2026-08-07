## Description

You are given a string `source` of size `n`, a string `pattern` that is a <span data-keyword="subsequence-string">subsequence</span> of `source`, and a **sorted** integer array `targetIndices` that contains **distinct** numbers in the range `[0, n - 1]`.

We define an **operation** as removing a character at an index `idx` from `source` such that:

	- `idx` is an element of `targetIndices`.

	- `pattern` remains a <span data-keyword="subsequence-string">subsequence</span> of `source` after removing the character.

Performing an operation **does not** change the indices of the other characters in `source`. For example, if you remove `'c'` from `"acb"`, the character at index 2 would still be `'b'`.

Return the **maximum** number of *operations* that can be performed.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">source = "abbaa", pattern = "aba", </span>targetIndices<span class="example-io"> = [0,1,2]</span>

**Output:** 1

**Explanation:**

We can't remove `source[0]` but we can do either of these two operations:

	- Remove `source[1]`, so that `source` becomes `"a_baa"`.

	- Remove `source[2]`, so that `source` becomes `"ab_aa"`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">source = "bcda", pattern = "d", </span>targetIndices<span class="example-io"> = [0,3]</span>

**Output:** 2

**Explanation:**

We can remove `source[0]` and `source[3]` in two operations.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">source = "dda", pattern = "dda", </span>targetIndices<span class="example-io"> = [0,1,2]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

We can't remove any character from `source`.

</div>

**Example 4:**

<div class="example-block">
**Input:** <span class="example-io">source = </span>"yeyeykyded"<span class="example-io">, pattern = </span>"yeyyd"<span class="example-io">, </span>targetIndices<span class="example-io"> = </span>[0,2,3,4]

**Output:** 2

**Explanation:**

We can remove `source[2]` and `source[3]` in two operations.

</div>

**Constraints:**

	- `1 <= n == source.length <= 3 * 10^3`

	- `1 <= pattern.length <= n`

	- `1 <= targetIndices.length <= n`

	- `targetIndices` is sorted in ascending order.

	- The input is generated such that `targetIndices` contains distinct elements in the range `[0, n - 1]`.

	- `source` and `pattern` consist only of lowercase English letters.

	- The input is generated such that `pattern` appears as a subsequence in `source`.
