## Examples

**Example 1**

- Input: `operations = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"], arguments = [[], [-2], [0], [-3], [], [], [], []]`
- Output: `[null, null, null, null, -3, null, 0, -2]`
- Explanation:
  1. `MinStack()` creates the empty stack.
  2. `push(-2)`, `push(0)`, and `push(-3)` add those values in order.
  3. `getMin()` returns `-3`.
  4. `pop()` removes `-3` from the top.
  5. `top()` returns `0`.
  6. `getMin()` now returns `-2`.
