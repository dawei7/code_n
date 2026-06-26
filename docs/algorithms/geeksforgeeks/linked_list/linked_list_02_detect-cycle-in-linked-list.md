# Detect Cycle in Linked List

| | |
|---|---|
| **ID** | `linked_list_02` |
| **Category** | linked_list |
| **Complexity (required)** | $O(N)$ Time, $O(1)$ Space |
| **Difficulty** | 3/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Linked List Cycle I & II](https://leetcode.com/problems/linked-list-cycle/) |

## Problem statement

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.
A cycle exists if there is some node in the list that can be reached again by continuously following the `next` pointer.
Return `True` if there is a cycle, otherwise return `False`.
*(Follow-up: If there is a cycle, return the EXACT Node where the cycle begins).*

**Input:** A singly linked list Node `head`.
**Output:** A boolean (or a Node for the follow-up).

**Example:**
`head = [3, 2, 0, -4]`, where `-4` points back to `2`.
Output: `True` (Cycle begins at node `2`).

## When to use it

- To detect infinite loops in pointer-based traversal.
- This is the textbook introduction to **Floyd's Cycle-Finding Algorithm** (also known as the Tortoise and Hare algorithm).

## Approach

A naive solution puts every visited node into a Hash Set. If you ever encounter a node that is already in the set, a cycle exists! This takes $O(N)$ Time and $O(N)$ Space.
We can solve this in $O(1)$ Space using **Two Pointers**: a Slow pointer (Tortoise) and a Fast pointer (Hare).

**Detecting the Cycle:**
1. Both pointers start at the `head`.
2. The slow pointer moves 1 step at a time (`slow = slow.next`).
3. The fast pointer moves 2 steps at a time (`fast = fast.next.next`).
4. If there is NO cycle, the fast pointer will eventually reach the end of the list (`None`).
5. If there IS a cycle, the fast pointer will lap the slow pointer inside the loop. They are mathematically guaranteed to eventually point to the exact same node!

**Finding the Start of the Cycle (The Math Trick):**
If they meet, we know a cycle exists. But where does it start?
Let L be the distance from the head to the cycle start.
Let C be the length of the cycle.
When they meet, the slow pointer has traveled L + x steps (where x is the distance into the cycle).
The fast pointer has traveled L + x + nC steps.
Since the fast pointer moves twice as fast: 2(L + x) = L + x + nC.
Solving for L: L = nC - x.
This means the distance from the head to the cycle start (L) is mathematically identical to the distance from the meeting point to the cycle start!
**Algorithm:** Leave the `slow` pointer at the meeting point. Move the `fast` pointer back to the `head`. Now move BOTH pointers 1 step at a time. The exact node where they collide again is the start of the cycle!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for linked_list_02: Detect Cycle.

Floyd's tortoise and hare: walk with slow and fast pointers
that advance 1 and 2 steps at a time respectively. If they
ever meet, there's a cycle; if fast reaches the end, there
isn't. O(n) time, O(1) space.
"""


def solve(next, head, n):
    if n == 0 or head == -1:
        return False
    slow = head
    fast = head
    while fast != -1 and next[fast] != -1:
        slow = next[slow]
        fast = next[next[fast]]
        if slow == fast:
            return True
    return False
```

</details>

## Walk-through

List: `1 -> 2 -> 3 -> 4 -> 5 -> 6 -> (back to 3)`

**Phase 1 (Detect):**
- Start: `S=1, F=1`.
- Step 1: `S=2, F=3`.
- Step 2: `S=3, F=5`.
- Step 3: `S=4, F=3`. (F wraps from 6 to 3).
- Step 4: `S=5, F=5`.
Collision at `5`! Cycle exists.

**Phase 2 (Find Start):**
- Reset Fast: `S=5, F=1`.
- Move 1 step: `S=6, F=2`.
- Move 1 step: `S=3, F=3`.
Collision at `3`! The cycle begins at Node `3`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(1)$ |
| **Average** | $O(N)$ | $O(1)$ |
| **Worst** | $O(N)$ | $O(1)$ |

The fast pointer will catch the slow pointer in at most N steps. Time complexity is strictly $O(N)$.
Only two pointers are used. Space complexity is $O(1)$.

## Variants & optimizations

- **Find the Duplicate Number ($O(1)$ Space):** Given an array of integers where values are between 1 and N, find the single duplicate number without modifying the array. You can treat the array values as "next pointers" (`next_node = arr[current_node]`). Because multiple numbers point to the duplicate value, it forms a cycle! You can use this exact Linked List algorithm to find the start of the cycle, which IS the duplicate number!

## Real-world applications

- **Deadlock Detection:** Operating Systems monitor resource allocation graphs. If a directed cycle is detected using pointer traversal, a deadlock has occurred.

## Related algorithms in cOde(n)

- **[linked_list_04 - Find Middle of Linked List](ll_04_find-middle-of-linked-list.md)** — The other fundamental application of the Slow/Fast pointer technique.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
