## Description

You are given the `root` of a **binary tree**, where each node contains an integer value.

A **valid path** in the tree is a sequence of **connected** nodes such that:

	- The path can start and end at **any node** in the tree.

	- The path does **not** need to pass through the root.

	- All node values along the path are **distinct**.

Return an integer denoting the **maximum** possible sum of node values among all valid paths.

**Example 1:**

<div class="example-block">

![](images/screenshot-2026-01-29-at-12940am.png)

**Input:** <span class="example-io">root = [2,2,1]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

	- The path `2 → 2` is invalid because the value 2 is not distinct.

	- The maximum-sum valid path is `2 → 1`, with a sum = `2 + 1 = 3`.

</div>

**Example 2:**

<div class="example-block">

![](images/screenshot-2026-01-29-at-15149am.png)

**Input:** <span class="example-io">root = [1,-2,5,null,null,3,5]</span>

**Output:** <span class="example-io">9</span>

**Explanation:**

	- The path `3 → 5 → 5` is invalid due to duplicate value 5.

	- The maximum-sum valid path is `1 → 5 → 3`, with a sum = `1 + 5 + 3 = 9`.

</div>

**Example 3:**

![](images/screenshot-2026-01-29-at-15555am.png)

​​​​​​​

<div class="example-block">
**Input:** <span class="example-io">root = [4,6,6,null,null,null,9]</span>

**Output:** <span class="example-io">19</span>

**Explanation:**

	- The path `6 → 4 → 6 → 9` is invalid because the value 6 appears more than once.

	- The maximum-sum valid path is `4 → 6 → 9`, with a sum = `4 + 6 + 9 = 19`.

</div>

**Constraints:**

	- The number of nodes in the tree is in the range `[1, 1000]`.

	- `-1000 <= Node.val <= 1000​​​​​​​`
