## Description

Given the `head` of a linked list and an integer `val`, remove all the nodes of the linked list that has $\text{Node.val} = val$, and return *the new head*.
### Function Contract

**Inputs**

- `head`: The head of a singly linked list, or `null` for an empty list.
- `val`: The node value that must be removed.

**Return value**

Return the new head after removing every matching node while retaining the other nodes in their original order.

### Examples

#### Example 1

![](images/removelinked-list.jpg)

- **Input:** $head = [1,2,6,3,4,5,6], val = 6$
- **Output:** `[1,2,3,4,5]`
#### Example 2

- **Input:** $head = [], val = 1$
- **Output:** `[]`
#### Example 3

- **Input:** $head = [7,7,7,7], val = 7$
- **Output:** `[]`
### Constraints

- The number of nodes in the list is in the range $[0, 10^{4}]$.

- $1 \le \text{Node.val} \le 50$

- $0 \le val \le 50$