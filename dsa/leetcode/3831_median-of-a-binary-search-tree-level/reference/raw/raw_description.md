## Description

You are given the `root` of a **Binary Search Tree (BST)** and an integer `level`.

The root node is at level 0. Each level represents the distance from the root.

Return the **median value** of all node values present at the given `level`. If the level does not exist or contains no nodes, return -1.

The **median** is defined as the middle element after sorting the values at that level in **non-decreasing** order. If the number of values at that level is even, return the **upper** median (the larger of the two middle elements after sorting).

**Example 1:**

![](images/screenshot-2026-01-27-at-20801pm.png)

<div class="example-block">
**Input:** <span class="example-io">root = [4,null,5,null,7], level = 2</span>

**Output:** <span class="example-io">7</span>

**Explanation:**

The nodes at `level = 2` are `[7]`. The median value is 7.

</div>

**Example 2:**

![](images/screenshot-2026-01-27-at-20926pm.png)

<div class="example-block">
**Input:** <span class="example-io">root = [6,3,8], level = 1</span>

**Output:** <span class="example-io">8</span>

**Explanation:**

The nodes at `level = 1` are `[3, 8]`. There are two possible median values, so the larger one 8 is the answer.

</div>

**Example 3:**

**​​​​​​​​​​​​​​**

![](images/screenshot-2026-01-27-at-21001pm.png)

<div class="example-block">
**Input:** <span class="example-io">root = [2,1], level = 2</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

There is no node present at `level = 2`​​​​​​​, so the answer is -1.

</div>

**Constraints:**

	- The number of nodes in the tree is in the range `[1, 2 * 10^5]`.

	- `1 <= Node.val <= 10^6`

	- `0 <= level <= 2 * 10^​​​​​​​5`
