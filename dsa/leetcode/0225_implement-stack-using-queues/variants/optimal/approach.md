## General
**Rotate each new value to the queue front**

Enqueue the new value at the back, then repeat a front-to-back queue move once for every older value. The new value finishes at the front, followed by all previous values in their existing order.

Once the queue is arranged this way, `pop` removes the front, `top` reads the front, and `empty` checks whether the queue contains anything.

**Queue order is exactly stack removal order**

Suppose the queue currently runs from newest to oldest. Enqueuing a value temporarily places it last. Rotating precisely the older entries moves each of them behind the new value without changing their relative order. The queue therefore again runs from newest to oldest.

Because that order is the exact LIFO removal order, reading or removing the queue front implements the corresponding stack operation.

## Complexity detail
Push costs $O(n)$ and other operations $O(1)$; storage is $O(n)$. Across a command stream, worst-case total time is quadratic in pushes.

## Alternatives and edge cases
- **Two queues:** can make either push or pop costly.
- **Use a list as a stack:** violates the queue-only design constraint.
- **Skip rotation:** yields FIFO behavior.
- The specification calls `pop` and `top` only when the structure is nonempty. After the last element is removed, later pushes start a valid new stack state.
