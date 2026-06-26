# Min Stack

| | |
|---|---|
| **ID** | `stack_05` |
| **Category** | stack |
| **Complexity (required)** | $O(1)$ for all operations |
| **Difficulty** | 3/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Min Stack](https://leetcode.com/problems/min-stack/) |

## Problem statement

Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element in constant time.

Implement the `MinStack` class:
- `MinStack()` initializes the stack object.
- `void push(int val)` pushes the element `val` onto the stack.
- `void pop()` removes the element on the top of the stack.
- `int top()` gets the top element of the stack.
- `int getMin()` retrieves the minimum element in the stack.

You must implement a solution with $O(1)$ time complexity for each function.

**Input:** A sequence of stack operations.
**Output:** The results of `top` and `getMin` operations.

**Example:**
```text
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
```

## When to use it

- To maintain a rolling history of aggregated states (like `min` or `max`) alongside raw data, guaranteeing $O(1)$ rollback when data is removed.

## Approach

A standard stack gives us $O(1)$ `push`, `pop`, and `top`. However, finding the minimum element requires an $O(N)$ scan.
If we use a single integer variable `current_min` to track the minimum, it works perfectly for `push` operations. BUT, if we `pop` the element that happens to be the `current_min`, we have absolutely no idea what the *second* smallest element was! We would have to rescan the whole stack.

**The Solution: Two Stacks (or Tuples)**
We can maintain two parallel stacks:
1. `main_stack`: Stores the actual values.
2. `min_stack`: Stores the minimum value *at the exact moment* the corresponding element was pushed to the `main_stack`.

Whenever we push a new value `x`, the new minimum is simply `min(x, min_stack.top())`. We push this new minimum onto the `min_stack`.
When we pop from the `main_stack`, we simultaneously pop from the `min_stack`. This instantly "rolls back" time, restoring the `min_stack` to whatever the minimum was before `x` was pushed!

Alternatively, you can just use one stack that stores a tuple: `(val, current_min_at_this_level)`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for stack_05: Min Stack.

Two parallel stacks: one for values, one for the running minimum.
push, pop, top, get_min are all O(1).
"""


def solve(ops, n):
    stack = []
    mins = []
    out = []
    for op in ops:
        cmd = op[0]
        if cmd == "push":
            v = op[1]
            stack.append(v)
            if not mins or v <= mins[-1]:
                mins.append(v)
        elif cmd == "pop":
            if not stack:
                out.append(-1)
            else:
                v = stack.pop()
                if mins and v == mins[-1]:
                    mins.pop()
                out.append(v)
        elif cmd == "get_min":
            out.append(mins[-1] if mins else -1)
    return out
```

</details>

## Walk-through

1. `push(-2)`: Stack empty. Push `(-2, -2)`.
2. `push(0)`: `min(0, -2) = -2`. Push `(0, -2)`. Stack: `[(-2, -2), (0, -2)]`.
3. `push(-3)`: `min(-3, -2) = -3`. Push `(-3, -3)`. Stack: `[(-2, -2), (0, -2), (-3, -3)]`.
4. `getMin()`: Look at top tuple `(-3, -3)`. Return `1st index` -> `-3`.
5. `pop()`: Pop `(-3, -3)`. Stack: `[(-2, -2), (0, -2)]`.
6. `top()`: Look at top tuple `(0, -2)`. Return `0th index` -> `0`.
7. `getMin()`: Look at top tuple `(0, -2)`. Return `1st index` -> `-2`.

All operations took $O(1)$! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(1)$ | $O(N)$ |
| **Average** | $O(1)$ | $O(N)$ |
| **Worst** | $O(1)$ | $O(N)$ |

Every single operation strictly accesses the end of the array, requiring $O(1)$ time.
The space complexity is $O(N)$ because we are storing two values (or two parallel stacks) for every N elements pushed.

## Variants & optimizations

- **Space Optimization (Difference Storage):** You can technically achieve $O(1)$ space (excluding the mandatory $O(N)$ to hold the values). Instead of storing tuples, you store an encoded difference: `val - current_min`. If the difference is negative, it means a new minimum was found, and the `current_min` variable is updated. When popping a negative difference, you can mathematically reconstruct the previous minimum! This trick is beautiful but rarely expected in interviews.

## Real-world applications

- **Undo/Redo States:** Text editors track the history of the document state using stacks. If a specific metric (like character count or document hash) needs to be instantly queryable for any past state, attaching the metric to the state tuple ensures $O(1)$ rollbacks.

## Related algorithms in cOde(n)

- **[queue_01 - Implement Queue using Stacks](../queue/queue_01_implement-queue-using-stacks.md)** — Another fundamental data-structure design problem using stacks.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
