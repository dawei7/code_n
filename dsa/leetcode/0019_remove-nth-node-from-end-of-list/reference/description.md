### 1. Description

Given the `head` of a linked list, remove the $n^{\text{th}}$ node from the end of the list and return its head.

### 2. Function Contract

**Inputs**

- `head`: The linked-list values in head-to-tail order.
- `n`: The one-based position of the node when counted from the tail.

Let $sz$ be the number of nodes in `head`.

**Return value**

Return the head of the linked list after removing its $n$th node from the end.

### 3. Examples

#### Example 1

![](images/remove_ex1.jpg)

- **Input:** $head = [1,2,3,4,5], n = 2$
- **Output:** `[1,2,3,5]`

#### Example 2

- **Input:** $head = [1], n = 1$
- **Output:** `[]`

#### Example 3

- **Input:** $head = [1,2], n = 1$
- **Output:** `[1]`

### 4. Constraints

- The number of nodes in the list is `sz`.

- $1 \le sz \le 30$

- $0 \le \text{Node.val} \le 100$

- $1 \le n \le sz$

**Follow up:** Could you do this in one pass?
