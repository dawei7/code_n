# Design Circular Deque

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 641 |
| Difficulty | Medium |
| Topics | Array, Linked List, Design, Queue |
| Official Link | [LeetCode](https://leetcode.com/problems/design-circular-deque/) |

## Problem Description
### Goal
Design a circular double-ended queue, or deque, with maximum size `k`. Its storage wraps from the final slot to the first so positions freed at either end can be reused without shifting the remaining values.

Implement `insertFront`, `insertLast`, `deleteFront`, `deleteLast`, `getFront`, `getRear`, `isEmpty`, and `isFull`. Insertions and deletions return whether they succeed, endpoint queries return `-1` when the deque is empty, and a failed operation leaves the data structure unchanged. Each operation should run in constant time without using a built-in deque implementation.

### Function Contract
**Inputs**

- `operations`: a sequence beginning with `MyCircularDeque`, followed by deque method calls
- `arguments`: the matching constructor capacity, inserted values, or empty method arguments
- `insertFront(value)` / `insertLast(value)`: add at the chosen end and report success
- `deleteFront()` / `deleteLast()`: remove at the chosen end and report success
- `getFront()` / `getRear()`: return the endpoint value, or `-1` when empty
- `isEmpty()` / `isFull()`: report the current state

**Return value**

- The operation trace returns null for construction and the documented result for every later call
- Failed insertions or deletions leave the deque unchanged

### Examples
**Example 1**

- Input: construct capacity `3`; insert `1` and `2` at the rear, `3` at the front, then try another front insertion
- Output: the first three insertions succeed, the fourth fails, and the rear remains `2`

**Example 2**

- Input: construct capacity `1`, insert `7` at the front, then query both ends
- Output: both endpoint queries return `7`

**Example 3**

- Input: fill a deque, delete its front, and insert a new rear value
- Output: the freed circular slot is reused successfully
