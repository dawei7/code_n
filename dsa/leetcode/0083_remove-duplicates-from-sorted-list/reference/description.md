## Description

Given the `head` of a sorted linked list, *delete all duplicates such that each element appears only once*. Return *the linked list **sorted** as well*.
### Function Contract

**Inputs**

- `head`: The first node of an ascending linked list, or `null` for an empty list.

**Return value**

Return the head of the sorted list with one retained node for each distinct value.

### Examples

#### Example 1

![](images/list1.jpg)

- **Input:** $head = [1,1,2]$
- **Output:** `[1,2]`
#### Example 2

![](images/list2.jpg)

- **Input:** $head = [1,1,2,3,3]$
- **Output:** `[1,2,3]`
### Constraints

- The number of nodes in the list is in the range `[0, 300]`.

- $-100 \le \text{Node.val} \le 100$

- The list is guaranteed to be **sorted** in ascending order.