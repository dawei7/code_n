# Find Middle of Linked List

| | |
|---|---|
| **ID** | `linked_list_04` |
| **Category** | linked_list |
| **Complexity (required)** | $O(N)$ Time, $O(1)$ Space |
| **Difficulty** | 1/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/) |

## Problem statement

Given the `head` of a singly linked list, return the middle node of the linked list.
If there are two middle nodes (i.e., the length is even), return the **second** middle node.

**Input:** A singly linked list Node `head`.
**Output:** A singly linked list Node representing the middle.

**Example 1 (Odd):**
`head = [1, 2, 3, 4, 5]`
Output: `Node(3)`.

**Example 2 (Even):**
`head = [1, 2, 3, 4, 5, 6]`
Output: `Node(4)`. (The two middles are 3 and 4, we return the second one).

## When to use it

- As a helper subroutine to cleanly split a linked list in half for Divide and Conquer algorithms (like Merge Sort for Linked Lists) or Palindrome checking.
- Further cements the **Fast and Slow Pointer** paradigm.

## Approach

A naive approach takes two passes:
1. Traverse the whole list to count the total nodes N.
2. Traverse again and stop at N / 2.
This requires $O(1.5 N)$ iterations.

We can achieve it in exactly one pass (0.5 N iterations) using **Fast and Slow Pointers**.

1. Initialize two pointers: `slow` and `fast`, both pointing to `head`.
2. Move `slow` by 1 step, and `fast` by 2 steps.
3. Because `fast` is moving twice as quickly, by the time `fast` reaches the end of the list, `slow` will mathematically be at exactly the halfway point!

*Edge Case Handling:*
If the list is `[1, 2]`:
- Initial: `slow=1`, `fast=1`.
- Step 1: `slow=2`, `fast=None`.
- Loop terminates. `slow` is on `2` (the second middle node). Perfect!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for linked_list_04: Find Middle of Linked List.

Slow and fast pointers: slow moves 1 step, fast moves 2. When
fast hits the end, slow is at the middle. Return (new_values,
new_next, new_head) with the list unchanged structurally
(only the head is set to the middle index).
"""


def solve(values, next, head, n):
    if n == 0 or head == -1:
        return list(values), list(next), -1
    slow = head
    fast = head
    while fast != -1 and next[fast] != -1:
        slow = next[slow]
        fast = next[next[fast]]
    return list(values), list(next), slow
```

</details>

## Walk-through

*(Odd Length)*
`List: 1 -> 2 -> 3 -> 4 -> 5`
- Start: `S=1, F=1`.
- Iteration 1: `S=2, F=3`.
- Iteration 2: `S=3, F=5`.
- Iteration 3: `F.next` is `None`. Loop terminates.
Return `S` (`Node(3)`). ✓

*(Even Length)*
`List: 1 -> 2 -> 3 -> 4`
- Start: `S=1, F=1`.
- Iteration 1: `S=2, F=3`.
- Iteration 2: `S=3, F=None`.
- Iteration 3: `F` is `None`. Loop terminates.
Return `S` (`Node(3)`). ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(1)$ |
| **Average** | $O(N)$ | $O(1)$ |
| **Worst** | $O(N)$ | $O(1)$ |

The fast pointer traverses N nodes, taking N/2 iterations. Time complexity is strictly $O(N)$.
Only two pointers are instantiated regardless of list size. Space complexity is $O(1)$.

## Variants & optimizations

- **First Middle Node:** If the problem asks for the *first* middle node in an even-length list (e.g. returning `3` instead of `4` for `[1, 2, 3, 4, 5, 6]`), you simply initialize the fast pointer one step ahead! `slow = head, fast = head.next`.
- **Palindrome Linked List:** Use this exact algorithm to find the middle. Then, use `linked_list_01` to reverse the second half of the list in-place. Finally, use two pointers (one at the head, one at the middle) to step through and check if the values match. You can check for palindromes in $O(N)$ time and $O(1)$ space!

## Real-world applications

- **Network Routing:** In gossip protocols, halving the transmission distance recursively requires identifying topological midpoints efficiently without mapping the entire network state.

## Related algorithms in cOde(n)

- **[linked_list_02 - Detect Cycle](ll_02_detect-cycle-in-linked-list.md)** — The other core use-case for Fast/Slow pointers.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
