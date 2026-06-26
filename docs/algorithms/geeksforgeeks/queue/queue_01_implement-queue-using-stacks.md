# Implement Queue using Stacks

| | |
|---|---|
| **ID** | `queue_01` |
| **Category** | queue |
| **Complexity (required)** | Amortized $O(1)$ Push/Pop |
| **Difficulty** | 3/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) |

## Problem statement

Implement a first-in-first-out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (`push`, `peek`, `pop`, and `empty`).

You must use only standard operations of a stack, which means only `push to top`, `peek/pop from top`, `size`, and `is empty` operations are valid.

**Input:** A sequence of queue operations.
**Output:** The results of `peek` and `pop` operations.

**Example:**
```text
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek();  // return 1
myQueue.pop();   // return 1, queue is [2]
myQueue.empty(); // return false
```

## When to use it

- An essential interview warm-up testing data structure fundamental inversion.
- Used practically in functional programming languages (like Haskell) where purely immutable linked lists operate exactly like LIFO stacks, requiring two stacks to simulate a mutable FIFO queue.

## Approach

A Stack is **LIFO** (Last-In, First-Out).
A Queue is **FIFO** (First-In, First-Out).

To flip LIFO into FIFO, we need to reverse the order of the elements.
If you pop everything out of one stack and push it directly into another stack, the order perfectly reverses!

We use two stacks:
1. `push_stack`: We blindly push all incoming elements here. This is extremely fast $O(1)$.
2. `pop_stack`: We exclusively pop elements from here. Since they were poured from the `push_stack`, they are reversed, meaning the oldest element is beautifully sitting at the very top, exactly like a Queue!

**The Golden Rule:**
- **Push:** Always push onto `push_stack`.
- **Pop / Peek:** Check if `pop_stack` is empty.
  - If it is empty, we must pour *all* current elements from `push_stack` into `pop_stack` one by one. This physically reverses their order.
  - If it is NOT empty, we simply return the top element of `pop_stack`. We **do not** pour elements back and forth. We only pour when `pop_stack` is completely drained.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for queue_01: Implement Queue using Stacks.

Implement a FIFO queue using only two LIFO stacks.
"""


def solve(operations, n):
    """Implement FIFO queue with two LIFO stacks."""
    inbox = []
    outbox = []
    results = []
    for op in operations:
        name = op[0]
        if name == "push":
            inbox.append(op[1])
        elif name == "pop":
            if not outbox:
                while inbox:
                    outbox.append(inbox.pop())
            if outbox:
                outbox.pop()
        elif name == "peek":
            if not outbox:
                while inbox:
                    outbox.append(inbox.pop())
            if outbox:
                results.append(outbox[-1])
        elif name == "empty":
            pass
    return results
```

</details>

## Walk-through

1. `push(1)`: `push_stack = [1]`, `pop_stack = []`.
2. `push(2)`: `push_stack = [1, 2]`, `pop_stack = []`.
3. `push(3)`: `push_stack = [1, 2, 3]`, `pop_stack = []`.
4. `pop()`: 
   - `pop_stack` is empty. Transfer!
   - Pop 3, push 3. Pop 2, push 2. Pop 1, push 1.
   - `push_stack = []`, `pop_stack = [3, 2, 1]`.
   - Pop from `pop_stack`: Returns `1`. `pop_stack = [3, 2]`.
5. `push(4)`: `push_stack = [4]`, `pop_stack = [3, 2]`. *(Notice we don't transfer!)*
6. `pop()`:
   - `pop_stack` is NOT empty. Do not transfer.
   - Pop from `pop_stack`: Returns `2`. `pop_stack = [3]`.
7. `pop()`:
   - Pop from `pop_stack`: Returns `3`. `pop_stack = []`.
8. `pop()`:
   - `pop_stack` is empty. Transfer!
   - `push_stack = []`, `pop_stack = [4]`.
   - Pop from `pop_stack`: Returns `4`. `pop_stack = []`.

All elements came out in the exact order `1, 2, 3, 4`. FIFO! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(N)$ |
| **Average** | Amortized $O(1)$ | $O(N)$ |
| **Worst** | $O(N)$ (single operation) | $O(N)$ |

- **Push:** Strictly $O(1)$.
- **Pop/Peek:** Amortized $O(1)$. Although a single `pop` might trigger a transfer of N elements taking $O(N)$ time, that element will only ever be transferred *exactly once* during its entire lifecycle. Thus, across N operations, the total time spent transferring is $O(N)$, averaging out to $O(1)$ per operation.
Space complexity is $O(N)$ to hold the elements.

## Variants & optimizations

- **Strict $O(1)$ Pop, $O(N)$ Push:** You can reverse the design. Whenever you `push`, you pour everything from `queue_stack` to an `auxiliary_stack`, push the new element to the bottom of `queue_stack`, and then pour everything back. This makes `pop` strictly $O(1)$ but `push` strictly $O(N)$. The amortized design is vastly superior.

## Real-world applications

- **Functional Programming Queues:** Purely functional languages like Clojure use this exact "Two-List" structure to implement persistent immutable queues efficiently.

## Related algorithms in cOde(n)

- **[queue_02 - Implement Stack using Queues](queue_02_implement-stack-using-queues.md)** — The inverse problem.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
