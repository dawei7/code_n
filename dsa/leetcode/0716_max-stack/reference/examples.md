## Examples

**Example 1**

- Input: `["MaxStack","push","push","push","top","popMax","top","peekMax","pop","top"], [[],[5],[1],[5],[],[],[],[],[],[]]`
- Output: `[null,null,null,null,5,5,1,5,1,5]`
- Explanation:
  1. Construct `stk` as an empty `MaxStack`.
  2. `stk.push(5)` changes the stack to `[5]`; its top and maximum are both `5`.
  3. `stk.push(1)` changes the stack to `[5,1]`; its top is `1`, while its maximum remains `5`.
  4. `stk.push(5)` changes the stack to `[5,1,5]`; the top is `5`, which is also the top-most maximum.
  5. `stk.top()` returns `5` and leaves `[5,1,5]` unchanged.
  6. `stk.popMax()` returns and removes the top-most `5`, leaving `[5,1]`; the top is now `1`, while the maximum is `5`.
  7. `stk.top()` returns `1` and leaves `[5,1]` unchanged.
  8. `stk.peekMax()` returns `5` and leaves `[5,1]` unchanged.
  9. `stk.pop()` returns and removes `1`, leaving `[5]`; its top and maximum are now both `5`.
  10. `stk.top()` returns `5` and leaves `[5]` unchanged.

For the app-adapted input `operations = [["push",5],["push",1],["push",5],["top"],["popMax"],["top"],["peekMax"],["pop"],["top"]]`, omitting the constructor and `null` results produces `[5,5,1,5,1,5]`.
