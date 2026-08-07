## Description

You are given a **binary** string `s` and an integer `k`.

You are also given a 2D integer array `queries`, where `queries[i] = [l_i, r_i]`.

A **binary string** satisfies the **k-constraint** if **either** of the following conditions holds:

	- The number of `0`'s in the string is at most `k`.

	- The number of `1`'s in the string is at most `k`.

Return an integer array `answer`, where `answer[i]` is the number of <span data-keyword="substring-nonempty">substrings</span> of `s[l_i..r_i]` that satisfy the **k-constraint**.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "0001111", k = 2, queries = [[0,6]]</span>

**Output:** <span class="example-io">[26]</span>

**Explanation:**

For the query `[0, 6]`, all substrings of `s[0..6] = "0001111"` satisfy the k-constraint except for the substrings `s[0..5] = "000111"` and `s[0..6] = "0001111"`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "010101", k = 1, queries = [[0,5],[1,4],[2,3]]</span>

**Output:** <span class="example-io">[15,9,3]</span>

**Explanation:**

The substrings of `s` with a length greater than 3 do not satisfy the k-constraint.

</div>

**Constraints:**

	- `1 <= s.length <= 10^5`

	- `s[i]` is either `'0'` or `'1'`.

	- `1 <= k <= s.length`

	- `1 <= queries.length <= 10^5`

	- `queries[i] == [l_i, r_i]`

	- `0 <= l_i <= r_i < s.length`

	- All queries are distinct.
