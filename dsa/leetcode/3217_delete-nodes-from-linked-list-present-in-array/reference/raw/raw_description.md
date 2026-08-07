## Description

You are given an array of integers `nums` and the `head` of a linked list. Return the `head` of the modified linked list after **removing** all nodes from the linked list that have a value that exists in `nums`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3], head = [1,2,3,4,5]</span>

**Output:** <span class="example-io">[4,5]</span>

**Explanation:**

**

![](images/linkedlistexample0.png)

**

Remove the nodes with values 1, 2, and 3.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1], head = [1,2,1,2,1,2]</span>

**Output:** <span class="example-io">[2,2,2]</span>

**Explanation:**

![](images/linkedlistexample1.png)

Remove the nodes with value 1.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5], head = [1,2,3,4]</span>

**Output:** <span class="example-io">[1,2,3,4]</span>

**Explanation:**

**

![](images/linkedlistexample2.png)

**

No node has value 5.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`

	- All elements in `nums` are unique.

	- The number of nodes in the given list is in the range `[1, 10^5]`.

	- `1 <= Node.val <= 10^5`

	- The input is generated such that there is at least one node in the linked list that has a value not present in `nums`.
