# Implement Stack using Queues

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 225 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Stack, Design, Queue |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/implement-stack-using-queues/) |

## Problem Description
### Goal
Implement a last-in, first-out stack while using only queue-style storage operations. `push(x)` adds an integer to the top, `pop()` removes and returns the most recently pushed remaining value, and `top()` returns that value without removing it.

`empty()` reports whether the stack contains no values. Process every command against one persistent stack state and return results in operation order, with pushes producing no value. Calls to `pop` and `top` are made only when the stack is nonempty. The internal implementation may use queue operations such as enqueue, dequeue, size, and front inspection, but must not substitute a native stack abstraction.

### Function Contract
**Inputs**

- `operations`: app commands `push value`, `pop`, `top`, and `empty`

**Return value**

Results from non-push operations in command order.

### Examples
**Example 1**

- Push 1, push 2, top, pop, empty
- Output: `[2,2,False]`

**Example 2**

- Query a newly created stack
- Output: `True`

**Example 3**

- Pop the only value, then push another
- Output follows independent LIFO states

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Rotate each new value to the queue front**

Enqueue the new value at the back, then repeat a front-to-back queue move once for every older value. The new value finishes at the front, followed by all previous values in their existing order.

Once the queue is arranged this way, `pop` removes the front, `top` reads the front, and `empty` checks whether the queue contains anything.

**Queue order is exactly stack removal order**

Suppose the queue currently runs from newest to oldest. Enqueuing a value temporarily places it last. Rotating precisely the older entries moves each of them behind the new value without changing their relative order. The queue therefore again runs from newest to oldest.

Because that order is the exact LIFO removal order, reading or removing the queue front implements the corresponding stack operation.

#### Complexity detail

Push costs $O(n)$ and other operations $O(1)$; storage is $O(n)$. Across a command stream, worst-case total time is quadratic in pushes.

#### Alternatives and edge cases

- **Two queues:** can make either push or pop costly.
- **Use a list as a stack:** violates the queue-only design constraint.
- **Skip rotation:** yields FIFO behavior.
- The specification calls `pop` and `top` only when the structure is nonempty. After the last element is removed, later pushes start a valid new stack state.

</details>
