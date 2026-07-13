# Max Stack

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 716 |
| Difficulty | Hard |
| Topics | Linked List, Stack, Design, Doubly-Linked List, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/max-stack/) |

## Problem Description
### Goal
Design a maximum stack that supports ordinary last-in-first-out behavior and efficient maximum-value operations. Implement `push(x)`, `pop()`, and `top()` together with `peekMax()`, which reads the largest stored value, and `popMax()`, which removes and returns it.

When the maximum value occurs more than once, `popMax()` must remove the occurrence closest to the top of the stack. Only removal operations modify the sequence; reading the top or maximum leaves it unchanged, and all remaining elements keep their relative stack order after a maximum is removed.

### Function Contract
**Inputs**

- `operations`: ordered calls named `push` with one integer argument or `pop`, `top`, `peekMax`, and `popMax` with no arguments

**Return value**

- A list containing the result of every non-`push` call in operation order

### Examples
**Example 1**

- Input: `operations = [["push",5],["push",1],["push",5],["top"],["popMax"],["top"],["peekMax"],["pop"],["top"]]`
- Output: `[5,5,1,5,1,5]`

**Example 2**

- Input: `operations = [["push",7],["push",7],["push",3],["peekMax"],["popMax"],["top"],["pop"],["top"]]`
- Output: `[7,7,3,3,7]`

**Example 3**

- Input: `operations = [["push",-2],["push",-5],["push",-2],["popMax"],["peekMax"],["top"]]`
- Output: `[-2,-2,-5]`

### Required Complexity

- **Time:** $O(q \log q)$
- **Space:** $O(q)$

<details>
<summary>Approach</summary>

#### General

**Preserve stack order with a doubly linked list**

Store each pushed value in a node between permanent head and tail sentinels. The node immediately before the tail is always the stack top. A node can also be unlinked from the middle in constant time, which is essential when `popMax` selects a value below the top.

**Give every occurrence a sequence number**

Assign increasing identifiers to pushes and place `(-value, -identifier)` in a min-heap. Negating the value makes the heap root a maximum. For equal values, the larger identifier was pushed later and is closer to the top, so its more-negative identifier wins the heap tie exactly as required.

**Connect the two views by identifier**

Map each active identifier to its linked-list node. `popMax` cleans obsolete heap roots, removes the current root, finds its node through the map, and unlinks that node. Ordinary `pop` unlinks the tail node and deletes its identifier from the map; its heap entry can remain until it reaches the root.

**Why lazy heap deletion is safe**

An identifier is active precisely while its linked-list node remains in the stack. Heap cleanup discards only identifiers absent from the active map, so it cannot remove a live occurrence. After cleanup, the root has the greatest live value and, among equal values, the greatest live identifier. Thus `peekMax` reports the correct maximum and `popMax` removes its topmost occurrence, while the linked list continues to answer `top` and `pop` in stack order.

#### Complexity detail

`top` and ordinary `pop` take $O(1)$ time. A push performs one heap insertion, while `peekMax` and `popMax` perform amortized $O(\log q)$ heap work. Every stale entry is inserted and discarded at most once, so `q` operations take $O(q \log q)$ total time. The linked nodes, active map, and heap use $O(q)$ space.

#### Alternatives and edge cases

- **Balanced ordered map plus linked nodes:** map each value to its nodes in stack order; it supports worst-case logarithmic maximum updates, but Python has no built-in balanced ordered map.
- **Two stacks with temporary removal:** maintain a parallel maximum stack and move elements aside during `popMax`; the operation is correct but may take $O(n)$ time.
- **Plain list with a maximum scan:** ordinary stack calls are simple, but every `peekMax` or `popMax` can scan all stored values and make a long sequence quadratic.
- Equal maximum values must be distinguished by push order so `popMax` removes the one closest to the top.
- Negative values require ordinary numeric ordering; the least-negative value is the maximum.
- Heap entries left by ordinary pops are harmless only when every maximum read cleans stale roots first.
- Removing the only element must reconnect the two sentinels and leave both views logically empty.

</details>
