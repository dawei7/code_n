# Implement Stack using Queues

| | |
|---|---|
| **ID** | `queue_02` |
| **Category** | queue |
| **Complexity (required)** | $O(N)$ Push, $O(1)$ Pop |
| **Difficulty** | 3/10 |
| **Interview relevance** | 6/10 |
| **LeetCode Equivalent** | [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/) |

## Problem statement

Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (`push`, `top`, `pop`, and `empty`).

You must use only standard operations of a queue, which means only `push to back`, `peek/pop from front`, `size`, and `is empty` operations are valid.

**Input:** A sequence of stack operations.
**Output:** The results of `top` and `pop` operations.

**Example:**
```text
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top();   // return 2
myStack.pop();   // return 2
myStack.empty(); // return False
```

## When to use it

- An interview exercise testing data structure rotation.
- Not practically useful in production software (unlike building Queues from Stacks, which has functional programming use-cases).

## Approach

A Queue is **FIFO** (First-In, First-Out).
A Stack is **LIFO** (Last-In, First-Out).

To make a queue act like a stack, the most recently pushed element must somehow magically end up at the *front* of the queue so it can be popped first.
Unlike stacks which perfectly reverse order when poured into each other, pouring a queue into another queue maintains the exact same order!

**The 1-Queue Rotation Trick:**
When we push a new element `x` into a queue, it goes to the absolute back.
If we want it at the front, we can simply measure the current size of the queue `s`, push `x` to the back, and then **dequeue and re-enqueue** the front element `s` times!
This rotates the entire queue like a conveyor belt, pulling the newly added element all the way to the front.

This completely eliminates the need for two queues! We can build it with just one.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for queue_02: Implement Stack using Queues.

Implement a LIFO stack using only FIFO queues
"""


def solve(operations, n):
    """Implement LIFO stack using one FIFO queue."""
    from collections import deque
    q = deque()
    results = []
    for op in operations:
        name = op[0]
        if name == "push":
            q.append(op[1])
            # Rotate: dequeue and re-enqueue (len(q) - 1) times
            # so the new element ends up at the front.
            for _ in range(len(q) - 1):
                q.append(q.popleft())
        elif name == "pop":
            if q:
                q.popleft()
        elif name == "top":
            if q:
                results.append(q[0])
        elif name == "empty":
            pass
    return results
```

</details>

## Walk-through

1. `push(1)`: 
   - `s = 0`.
   - Append `1`. Queue: `[1]`.
   - Rotate `0` times. Queue: `[1]`.
2. `push(2)`:
   - `s = 1`.
   - Append `2`. Queue: `[1, 2]`.
   - Rotate `1` time. Pop `1`, append `1`. Queue: `[2, 1]`.
3. `push(3)`:
   - `s = 2`.
   - Append `3`. Queue: `[2, 1, 3]`.
   - Rotate `2` times:
     - Pop `2`, append `2`. Queue: `[1, 3, 2]`.
     - Pop `1`, append `1`. Queue: `[3, 2, 1]`.
4. `pop()`:
   - Pop front. Returns `3`. Queue: `[2, 1]`.
5. `pop()`:
   - Pop front. Returns `2`. Queue: `[1]`.

All elements came out in the exact order `3, 2, 1`. LIFO! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ Push | $O(N)$ |
| **Average** | $O(N)$ Push | $O(N)$ |
| **Worst** | $O(N)$ Push | $O(N)$ |

- **Push:** $O(N)$ strictly. Every time we push an element, we must physically rotate all N previously existing elements.
- **Pop / Top:** $O(1)$ strictly. Because the heavy lifting is done during push, the newest element is always sitting patiently at the front of the queue.
Space complexity is $O(N)$ for the queue.

## Variants & optimizations

- **Two Queues ($O(N)$ Pop):** The "official" naive solution is to use `q1` and `q2`. To `push`, simply enqueue to `q1` in $O(1)$. To `pop`, dequeue N-1 elements from `q1` to `q2`, pop and return the final remaining element in `q1`, and then swap the references of `q1` and `q2`. This makes `push` $O(1)$ and `pop` $O(N)$.
- **Why is 1-Queue better?** Because the 1-Queue approach uses the exact same Time Complexity but literally half the memory allocation and avoids managing dual pointers.

## Real-world applications

- **Conveyor Belt Scheduling:** Structuring round-robin CPU schedulers to dynamically boost the priority of an incoming thread by manually fast-forwarding the execution ring buffer.

## Related algorithms in cOde(n)

- **[queue_01 - Implement Queue using Stacks](queue_01_implement-queue-using-stacks.md)** — The inverse problem, which brilliantly achieves amortized $O(1)$ time for all operations.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
