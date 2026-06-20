# Reverse Nodes in k-Group

| | |
|---|---|
| **ID** | `linked_list_05` |
| **Category** | linked_list |
| **Complexity (required)** | $O(N)$ Time, $O(1)$ Space |
| **Difficulty** | 8/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) |

## Problem statement

Given the `head` of a linked list, reverse the nodes of the list `k` at a time, and return the modified list.
`k` is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of `k` then left-out nodes at the end should remain as they are.

You may not alter the values in the list's nodes, only nodes themselves may be changed. You must solve it in $O(1)$ extra memory space.

**Input:** A singly linked list Node `head` and an integer `k`.
**Output:** A singly linked list Node representing the modified head.

**Example 1:**
`head = [1, 2, 3, 4, 5]`, `k = 2`
Output: `[2, 1, 4, 3, 5]`. (1 and 2 swap, 3 and 4 swap, 5 is left alone).

**Example 2:**
`head = [1, 2, 3, 4, 5]`, `k = 3`
Output: `[3, 2, 1, 4, 5]`. (1, 2, and 3 reverse, 4 and 5 are left alone).

## When to use it

- To prove absolute mastery over Linked List pointer manipulation. This is one of the most conceptually dense pointer problems you can face in an interview.

## Approach

This problem combines the **Dummy Node** pattern with the **In-Place Reversal** pattern.

We process the list in chunks of size `k`.
For each chunk:
1. Verify if there are actually `k` nodes remaining. If not, we are done! Break the loop.
2. If there are `k` nodes, we mark the start and end of this chunk.
3. We perform standard $O(1)$ pointer reversal (from `linked_list_01`) *strictly* on this chunk.
4. **The Hard Part (Stitching):** After reversing a chunk, the original "start" of the chunk is now the "tail" of the reversed chunk! And the original "end" of the chunk is now the new "head"! We must manually stitch the previous chunk's tail to this new head, and stitch our new tail to the upcoming unreversed segment.

**The Pointers Needed:**
- `dummy`: To handle the absolute head of the list cleanly.
- `prev_group_tail`: Points to the node immediately preceding the current chunk. We need this to attach the reversed chunk back to the main list.
- `kth`: A runner to find the end of the current chunk.
- `prev`, `curr`, `next_node`: The standard trio for reversing.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for linked_list_05: Reverse in Groups of K.

Walk the list in chunks of k; reverse each chunk. The trick is
to thread the previous chunk's tail to the current chunk's
new head. Return (new_values, new_next, new_head).
"""


def solve(values, next, head, k, n):
    if n == 0 or head == -1 or k <= 1:
        return list(values), list(next), head
    new_next = list(next)
    prev_tail_new = -1
    cur = head
    new_head = -1
    while cur != -1:
        chunk = []
        c = cur
        for _ in range(k):
            if c == -1:
                break
            chunk.append(c)
            c = new_next[c]
        if len(chunk) < k:
            if prev_tail_new != -1:
                new_next[prev_tail_new] = chunk[0]
            break
        for i in range(len(chunk) - 1, 0, -1):
            new_next[chunk[i]] = chunk[i - 1]
        new_next[chunk[0]] = c
        if prev_tail_new != -1:
            new_next[prev_tail_new] = chunk[-1]
        else:
            new_head = chunk[-1]
        prev_tail_new = chunk[0]
        cur = c
    if new_head == -1:
        new_head = head
    return list(values), new_next, new_head
```

</details>

## Walk-through

`head = [1, 2, 3]`, `k = 2`.
`dummy -> 1 -> 2 -> 3`. `prev_group_tail = dummy`.

**Group 1:**
- `get_kth_node(dummy, 2)` returns `Node(2)`.
- `kth` is not None. `next_group_head = Node(3)`.
- Reversal Setup: `prev = Node(3)`, `curr = Node(1)`.
- Reversal Loop (until `curr == Node(3)`):
  - `curr = 1`: `next_node = 2`. `1.next = 3`. `prev = 1`. `curr = 2`.
  - `curr = 2`: `next_node = 3`. `2.next = 1`. `prev = 2`. `curr = 3`.
- Loop ends. Reversed group: `2 -> 1 -> 3`.
- Stitching:
  - `tmp = dummy.next` (which is `Node(1)`).
  - `dummy.next = prev` (which is `Node(2)`).
  - `prev_group_tail = tmp` (moves to `Node(1)`).
List is now: `dummy -> 2 -> 1 -> 3`.

**Group 2:**
- `get_kth_node(Node(1), 2)` returns `None` (only 1 node left).
- Break loop!

Return `dummy.next`: `[2, 1, 3]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(1)$ |
| **Average** | $O(N)$ | $O(1)$ |
| **Worst** | $O(N)$ | $O(1)$ |

We traverse the list once to find the `kth` nodes, and a second time to perform the actual pointer reversals. This means we process each node exactly twice. The time complexity is strictly $O(N)$.
Space complexity is strictly $O(1)$ as we only maintain a fixed set of pointers regardless of the list or chunk size.

## Variants & optimizations

- **Recursive $O(N)$ Space:** You can easily solve this recursively by grabbing the first `k` nodes, passing the remainder of the list to the recursive function, and taking the returned head and attaching it to your reversed chunk. However, LeetCode strictly prohibits this in the problem description, enforcing $O(1)$ space.

## Real-world applications

- **Network Packet Reassembly:** When receiving chunked stream data over UDP, packets might arrive in reverse block orders that need continuous chunked re-stitching before being passed to the application layer.

## Related algorithms in cOde(n)

- **[linked_list_01 - Reverse Linked List](ll_01_reverse-linked-list.md)** — The absolute prerequisite to this algorithm.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
