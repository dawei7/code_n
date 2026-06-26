# Reverse Linked List

| | |
|---|---|
| **ID** | `linked_list_01` |
| **Category** | linked_list |
| **Complexity (required)** | $O(N)$ Time, $O(1)$ Space |
| **Difficulty** | 2/10 |
| **Interview relevance** | 10/10 |
| **LeetCode Equivalent** | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) |

## Problem statement

Given the `head` of a singly linked list, reverse the list, and return the reversed list.

**Input:** A singly linked list Node `head`.
**Output:** A singly linked list Node representing the new head.

**Example 1:**
`head = [1, 2, 3, 4, 5]`
Output: `[5, 4, 3, 2, 1]`.

## When to use it

- The absolute most fundamental Linked List operation. Almost every advanced Linked List algorithm (like checking for palindromes or reversing sub-segments) relies entirely on your ability to confidently reverse pointers in-place.

## Approach

**Iterative Approach (Three Pointers):**
To reverse a singly linked list, we must change every single node's `next` pointer to point backwards to its previous node.
Since it's a singly linked list, a node doesn't know who its previous node is. We must maintain a `prev` pointer manually!
If we change `curr.next = prev`, we instantly sever the connection to the rest of the list! To prevent losing the rest of the list, we must temporarily save `curr.next` in a `next_node` pointer *before* we overwrite it.

1. Initialize `prev = None` and `curr = head`.
2. While `curr` is not `None`:
   - Save the next node: `next_node = curr.next`.
   - Reverse the pointer: `curr.next = prev`.
   - Shift `prev` forward: `prev = curr`.
   - Shift `curr` forward: `curr = next_node`.
3. When the loop ends, `curr` is `None`, and `prev` points to the last node we processed, which is the new `head`!

**Recursive Approach:**
We can recursively traverse to the very end of the list. The last node becomes the new head. As the recursion unwinds, for a given `node`, we command its next node to point back at it: `node.next.next = node`, and then sever the forward pointer `node.next = None`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for linked_list_01: Reverse Linked List.

Iterative in-place reversal. Walk the list with prev, cur,
nxt pointers; on each step, flip cur.next to prev, then
advance. O(n) time, O(1) space. Return the new parallel
``(values, next)`` representation.
"""


def solve(values, next, head, n):
    if n == 0 or head == -1:
        return values, next, -1
    new_next = list(next)
    prev = -1
    cur = head
    new_head = -1
    while cur != -1:
        nxt_node = new_next[cur]
        new_next[cur] = prev
        new_head = cur
        prev = cur
        cur = nxt_node
    return list(values), new_next, new_head
```

</details>

## Walk-through

*(Iterative)*
`List: 1 -> 2 -> 3 -> None`.
`prev = None`, `curr = Node(1)`.

**Iteration 1:**
- `next_node = Node(2)`.
- `curr.next = prev` (Node 1 points to `None`).
- `prev = Node(1)`.
- `curr = Node(2)`.
*(List is now: 1 -> None, and 2 -> 3 -> None)*

**Iteration 2:**
- `next_node = Node(3)`.
- `curr.next = prev` (Node 2 points to Node 1).
- `prev = Node(2)`.
- `curr = Node(3)`.
*(List is now: 2 -> 1 -> None, and 3 -> None)*

**Iteration 3:**
- `next_node = None`.
- `curr.next = prev` (Node 3 points to Node 2).
- `prev = Node(3)`.
- `curr = None`.
*(List is now: 3 -> 2 -> 1 -> None)*

Loop ends (`curr` is None). Return `prev` (Node 3). ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(1)$ |
| **Average** | $O(N)$ | $O(1)$ |
| **Worst** | $O(N)$ | $O(1)$ |

The iterative approach traverses the list exactly once, taking $O(N)$ time, and uses three auxiliary pointers, taking $O(1)$ space.
The recursive approach takes $O(N)$ time but uses $O(N)$ space due to the recursive call stack. The iterative approach is almost always preferred in interviews.

## Variants & optimizations

- **Reverse Sub-segment (Reverse Linked List II):** Reverse only the nodes from position `m` to `n`. You traverse to position `m`, use the exact same iterative reversing logic for `n - m` steps, and then carefully stitch the "head" and "tail" of the reversed segment back into the main list.
- **Reverse in Blocks of K:** See `linked_list_05`.

## Real-world applications

- **Undo Operations:** Reversing a chronological sequence of state changes stored in a singly linked list to rollback operations.

## Related algorithms in cOde(n)

- **[linked_list_05 - Reverse in Groups of K](ll_05_reverse-in-groups-of-k.md)** — The ultimate test of your pointer manipulation mastery.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
