# Merge Two Sorted Linked Lists

| | |
|---|---|
| **ID** | `linked_list_03` |
| **Category** | linked_list |
| **Complexity (required)** | $O(N + M)$ Time, $O(1)$ Space |
| **Difficulty** | 2/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) |

## Problem statement

You are given the heads of two sorted linked lists `list1` and `list2`.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists (do not create new nodes, just rewire the existing pointers).
Return the head of the merged linked list.

**Input:** Two singly linked list Nodes `list1` and `list2`.
**Output:** A singly linked list Node representing the merged head.

**Example:**
`list1 = [1, 2, 4]`, `list2 = [1, 3, 4]`
Output: `[1, 1, 2, 3, 4, 4]`.

## When to use it

- To understand the "Dummy Head" paradigm, which is arguably the most important design pattern for avoiding edge-case crashes in Linked List manipulation.
- It is the core subroutine required to implement Merge Sort on a Linked List.

## Approach

We need to iterate through both lists simultaneously. At each step, we compare the current nodes of both lists, pick the smaller one, append it to our merged list, and advance the pointer of the list we picked from.

**The "Dummy Node" Pattern:**
When building a new linked list, the hardest part is dealing with the very first node (the `head`). If the list is initially empty, we have to write special `if not head: head = node` logic.
To avoid this completely, we create a fake `dummy` node (e.g., `Node(-1)`).
We use a `tail` pointer starting at `dummy`.
We can blindly append nodes using `tail.next = picked_node` without ever worrying about `None` exceptions!
At the very end, we just return `dummy.next` to return the real list, entirely ignoring the fake dummy node.

1. Initialize `dummy = Node(-1)` and `tail = dummy`.
2. While `list1` and `list2` are both not `None`:
   - If `list1.val <= list2.val`:
     - `tail.next = list1`
     - `list1 = list1.next`
   - Else:
     - `tail.next = list2`
     - `list2 = list2.next`
   - `tail = tail.next`
3. If one list exhausts before the other, the remaining elements in the other list are already sorted! We can just append the entire remaining chunk in one $O(1)$ operation: `tail.next = list1 if list1 else list2`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for linked_list_03: Merge Two Sorted Lists.

Two-pointer walk. On each step, attach the smaller of the two
heads to the merged tail and advance that head. Append the
remaining tail of the non-empty list. Return the merged
``(values, next)`` representation.
"""


def solve(values1, next1, head1, values2, next2, head2, n1, n2):
    if n1 == 0:
        merged = list(values2)
    elif n2 == 0:
        merged = list(values1)
    else:
        merged = []
        i, j = head1, head2
        while i != -1 and j != -1:
            if values1[i] <= values2[j]:
                merged.append(values1[i])
                i = next1[i]
            else:
                merged.append(values2[j])
                j = next2[j]
        while i != -1:
            merged.append(values1[i])
            i = next1[i]
        while j != -1:
            merged.append(values2[j])
            j = next2[j]
    n = len(merged)
    merged_nxt = [k + 1 for k in range(n - 1)] + [-1]
    return merged, merged_nxt
```

</details>

## Walk-through

`L1: 1 -> 3`, `L2: 2 -> 4`.
`dummy = Node(-1)`, `tail = dummy`.

1. `L1 (1) < L2 (2)`.
   - `tail.next = Node(1)`. `tail` moves to `Node(1)`.
   - `L1` moves to `Node(3)`.
2. `L1 (3) > L2 (2)`.
   - `tail.next = Node(2)`. `tail` moves to `Node(2)`.
   - `L2` moves to `Node(4)`.
3. `L1 (3) < L2 (4)`.
   - `tail.next = Node(3)`. `tail` moves to `Node(3)`.
   - `L1` moves to `None`.
4. Loop terminates because `L1` is `None`.
5. Attach leftovers: `L1` is `None`, so `tail.next = L2 (Node(4))`.

Merged List: `-1 -> 1 -> 2 -> 3 -> 4`.
Return `dummy.next`: `1 -> 2 -> 3 -> 4`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N + M)$ | $O(1)$ |
| **Average** | $O(N + M)$ | $O(1)$ |
| **Worst** | $O(N + M)$ | $O(1)$ |

We traverse each node in both lists exactly once. Time complexity is strictly $O(N + M)$.
Since we are only rewiring existing pointers and not creating any new nodes (except the single $O(1)$ dummy node), the space complexity is strictly $O(1)$.

## Variants & optimizations

- **Merge K Sorted Lists:** You are given K sorted linked lists. You can solve this by merging them pairwise (Divide and Conquer, $O(N log K)$), or by throwing all K heads into a Min-Heap. The Min-Heap approach instantly gives you the absolute smallest node among all K lists. You pop the smallest, append it to your dummy tail, and push that node's `next` back into the heap! Also runs in $O(N log K)$ but is often easier to implement.

## Real-world applications

- **External Merge Sort:** When sorting datasets that are too massive to fit in RAM (like 100GB databases), chunks are sorted and saved to disk. A pointer is assigned to the start of each file chunk, and they are merged exactly like this to produce the final sorted output without exceeding RAM constraints.

## Related algorithms in cOde(n)

- **[heap_04 - Merge K Sorted Lists](../heap/heap_04_merge-k-sorted-lists.md)** — The multi-list generalization using Priority Queues.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
