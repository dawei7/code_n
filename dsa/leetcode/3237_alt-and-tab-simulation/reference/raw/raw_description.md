## Description

There are `n` windows open numbered from `1` to `n`, we want to simulate using alt + tab to navigate between the windows.

You are given an array `windows` which contains the initial order of the windows (the first element is at the top and the last one is at the bottom).

You are also given an array `queries` where for each query, the window `queries[i]` is brought to the top.

Return the final state of the array `windows`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">windows = [1,2,3], queries = [3,3,2]</span>

**Output:** <span class="example-io">[2,3,1]</span>

**Explanation:**

Here is the window array after each query:

	- Initial order: `[1,2,3]`

	- After the first query: `[<u>**3**</u>,1,2]`

	- After the second query: `[<u>**3**</u>,1,2]`

	- After the last query: `[<u>**2**</u>,3,1]`

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">windows = [1,4,2,3], queries = [4,1,3]</span>

**Output:** <span class="example-io">[3,1,4,2]</span>

**Explanation:**

Here is the window array after each query:

	- Initial order: `[1,4,2,3]`

	- After the first query: `[<u>**4**</u>,1,2,3]`

	- After the second query: `[<u>**1**</u>,4,2,3]`

	- After the last query: `[<u>**3**</u>,1,4,2]`

</div>

**Constraints:**

	- `1 <= n == windows.length <= 10^5`

	- `windows` is a permutation of `[1, n]`.

	- `1 <= queries.length <= 10^5`

	- `1 <= queries[i] <= n`
