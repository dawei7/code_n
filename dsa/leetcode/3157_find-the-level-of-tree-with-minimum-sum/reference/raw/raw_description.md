## Description

Given the root of a binary tree `root` where each node has a value, return the level of the tree that has the **minimum** sum of values among all the levels (in case of a tie, return the **lowest** level).

**Note** that the root of the tree is at level 1 and the level of any other node is its distance from the root + 1.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">root = [50,6,2,30,80,7]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

![](images/image_2024-05-17_16-15-46.png)

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">root = [36,17,10,null,null,24]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

![](images/image_2024-05-17_16-14-18.png)

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">root = [5,null,5,null,5]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

![](images/image_2024-05-19_19-07-20.png)

</div>

**Constraints:**

	- The number of nodes in the tree is in the range `[1, 10^5]`.

	- `1 <= Node.val <= 10^9`
