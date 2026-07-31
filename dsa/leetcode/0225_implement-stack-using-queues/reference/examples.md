## Examples

**Example 1**

- Input: `["MyStack","push","push","top","pop","empty"], [[],[1],[2],[],[],[]]`
- Output: `[null,null,null,2,2,false]`
- Explanation: After pushing `1` and then `2`, the LIFO top is `2`; `pop()` removes that same value, and the remaining stack is not empty.

| Call | Result |
|---|---:|
| `MyStack()` | `null` |
| `push(1)` | `null` |
| `push(2)` | `null` |
| `top()` | `2` |
| `pop()` | `2` |
| `empty()` | `false` |
