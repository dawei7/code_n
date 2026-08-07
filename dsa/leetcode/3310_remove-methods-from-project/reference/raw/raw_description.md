## Description

You are maintaining a project that has `n` methods numbered from `0` to `n - 1`.

You are given two integers `n` and `k`, and a 2D integer array `invocations`, where `invocations[i] = [a_i, b_i]` indicates that method `a_i` invokes method `b_i`.

There is a known bug in method `k`. Method `k`, along with any method invoked by it, either **directly** or **indirectly**, are considered **suspicious** and we aim to remove them.

A group of methods can only be removed if no method **outside** the group invokes any methods **within** it.

Return an array containing all the remaining methods after removing all the **suspicious** methods. You may return the answer in *any order*. If it is not possible to remove **all** the suspicious methods, **none** should be removed.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 4, k = 1, invocations = [[1,2],[0,1],[3,2]]</span>

**Output:** <span class="example-io">[0,1,2,3]</span>

**Explanation:**

![](images/graph-2.png)

Method 2 and method 1 are suspicious, but they are directly invoked by methods 3 and 0, which are not suspicious. We return all elements without removing anything.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 5, k = 0, invocations = [[1,2],[0,2],[0,1],[3,4]]</span>

**Output:** <span class="example-io">[3,4]</span>

**Explanation:**

![](images/graph-3.png)

Methods 0, 1, and 2 are suspicious and they are not directly invoked by any other method. We can remove them.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 3, k = 2, invocations = [[1,2],[0,1],[2,0]]</span>

**Output:** <span class="example-io">[]</span>

**Explanation:**

![](images/graph.png)

All methods are suspicious. We can remove them.

</div>

**Constraints:**

	- `1 <= n <= 10^5`

	- `0 <= k <= n - 1`

	- `0 <= invocations.length <= 2 * 10^5`

	- `invocations[i] == [a_i, b_i]`

	- `0 <= a_i, b_i <= n - 1`

	- `a_i != b_i`

	- `invocations[i] != invocations[j]`
