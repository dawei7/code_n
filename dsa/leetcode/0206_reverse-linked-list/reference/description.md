## Description

Given the `head` of a singly linked list, reverse the list, and return *the reversed list*.
### Function Contract

**Inputs**

- `head`: The head of a singly linked list, or `null` for an empty list.

**Return value**

Return the head whose traversal visits all original nodes in reverse order.

### Examples
#### Example 1

![](images/rev1ex1.jpg)

- **Input:** $head = [1,2,3,4,5]$
- **Output:** `[5,4,3,2,1]`
#### Example 2

![](images/rev1ex2.jpg)

- **Input:** $head = [1,2]$
- **Output:** `[2,1]`
#### Example 3

- **Input:** $head = []$
- **Output:** `[]`
### Constraints

- The number of nodes in the list is the range `[0, 5000]`.

- $-5000 \le \text{Node.val} \le 5000$

**Follow up:** A linked list can be reversed either iteratively or recursively. Could you implement both?