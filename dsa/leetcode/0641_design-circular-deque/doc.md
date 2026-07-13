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

### Required Complexity

- **Time:** $O(Q)$
- **Space:** $O(k)$

<details>
<summary>Approach</summary>

#### General

**Represent the occupied circular segment**

Allocate exactly `k` array slots. Track `front`, the index of the first live value, and `size`, the number of live values. Empty means `size = 0`, while full means `size = k`, so wrapped indices never make those states ambiguous.

**Derive both insertion positions**

For a front insertion, decrement `front` modulo `k` and write there. The next rear insertion belongs at `(front + size) % k`, immediately after the current occupied segment. Increment `size` only after a successful insertion.

**Delete by moving boundaries**

Deleting the front advances `front` modulo `k`; deleting the rear only decrements `size`. Existing values outside the live segment need not be erased. When nonempty, the rear value is at `(front + size - 1) % k`.

**Why both endpoint orders remain correct**

The live deque is always `size` consecutive circular positions beginning at `front`. Front operations extend or shrink that segment at its first position, while rear operations extend or shrink its other boundary. Each successful operation preserves this representation, so the derived endpoint indices always identify the logical first and last values.

#### Complexity detail

Every one of the `Q` method calls performs a constant number of state checks, modular arithmetic operations, or array accesses, giving $O(Q)$ total time and $O(1)$ time per call. The fixed backing array uses $O(k)$ space.

#### Alternatives and edge cases

- **Doubly linked list with head and tail:** supports every operation in $O(1)$ time and tracks capacity with a count, but allocates nodes individually.
- **Singly linked list without a tail:** front operations remain constant-time, but rear insertion or deletion requires traversal and can make a trace quadratic.
- **Dynamic language deque:** provides the operations directly, but the exercise requires implementing the bounded behavior and failure conditions.
- Capacity one must distinguish empty and full even though front and rear refer to the same slot.
- Insertion on a full deque returns false without overwriting an endpoint.
- Deletion on an empty deque returns false, and endpoint queries return `-1`.
- Repeated deletions and insertions must wrap indices and reuse freed slots.

</details>
