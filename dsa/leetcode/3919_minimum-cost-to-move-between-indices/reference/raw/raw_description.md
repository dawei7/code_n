## Description

You are given an integer array `nums` where `nums` is **<span data-keyword="strictly-increasing-array">strictly increasing</span>**.

For each index `x`, let `closest(x)` be the **adjacent** index `y` such that `abs(nums[x] - nums[y])` is **minimized**. If both **adjacent** indices exist and give the same difference, choose the **smaller** index.

From any index `x`, you can move in two ways:

	- To any index `y` with cost `abs(nums[x] - nums[y])`, or

	- To `closest(x)` with cost 1.

You are also given a 2D integer array `queries`, where each `queries[i] = [l_i, r_i]`.

For each query, calculate the **minimum total cost** to move from index `l_i` to index `r_i`.

Return an integer array `ans`, where `ans[i]` is the answer for the `i^th` query.

The **absolute difference** between two values `x` and `y` is defined as `abs(x - y)`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [-5,-2,3], queries = [[0,2],[2,0],[1,2]]</span>

**Output:** <span class="example-io">[6,2,5]</span>

**Explanation:**​​​​​​​​​​​​​​​​​​​​

	- The closest indices are `[1, 0, 1]` respectively.

	- For `[0, 2]`, the path `0 → 1 → 2` uses a closest move from index 0 to 1 with cost 1 and a move from index 1 to 2 with cost `|-2 - 3| = 5`, giving total `1 + 5 = 6`.

	- For `[2, 0]`, the path `2 → 1 → 0` uses two closest moves from index 2 to 1 and from index 1 to 0, each with cost 1, giving total 2.

	- For `[1, 2]`, the direct move from index 1 to index 2 has cost `|-2 - 3| = 5`, which is optimal.

Thus, `ans = [6, 2, 5]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [0,2,3,9], queries = [[3,0],[1,2],[2,0]]</span>

**Output:** <span class="example-io">[4,1,3]</span>

**Explanation:**

	- The closest indices are `[1, 2, 1, 2]` respectively.

	- For `[3, 0]`, the path `3 → 2 → 1 → 0` uses closest moves from index 3 to 2 and from 2 to 1, each with cost 1, and a move from 1 to 0 with cost `|2 - 0| = 2`, giving total `1 + 1 + 2 = 4`.

	- For `[1, 2]`, the closest move from index 1 to 2 has cost 1.

	- For `[2, 0]`, the path `2 → 1 → 0` uses a closest move from index 2 to 1 with cost 1 and a move from 1 to 0 with cost `|2 - 0| = 2`, giving total `1 + 2 = 3`.

Thus, `ans = [4, 1, 3]`.

</div>

**Constraints:**

	- `2 <= nums.length <= 10^5`

	- `-10^9 <= nums[i] <= 10^9`

	- `nums` is strictly increasing

	- `1 <= queries.length <= 10^5`

	- `queries[i] = [l_i, r_i]`​​​​​​​

	- `0 <= l_i, r_i < nums.length`
