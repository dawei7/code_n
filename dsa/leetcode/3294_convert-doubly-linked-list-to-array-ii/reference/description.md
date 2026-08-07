## Description

You are given an **arbitrary** `node` from a **doubly linked list**, which contains nodes that have a next pointer and a previous pointer.

Return an integer array which contains the elements of the linked list **in order**.
### Function Contract

- Refer to method signature.

### Examples

#### Example 1

<div class="example-block">
**Input:** head = [1,2,3,4,5], node = 5

**Output:** [1,2,3,4,5]

</div>
#### Example 2

<div class="example-block">
**Input:** head = [4,5,6,7,8], node = 8

**Output:** [4,5,6,7,8]

</div>
### Constraints

- The number of nodes in the given list is in the range `[1, 500]`.

- $1 \le \text{Node.val} \le 1000$

- All nodes have unique `Node.val`.