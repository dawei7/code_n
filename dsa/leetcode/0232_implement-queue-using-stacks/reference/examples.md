## Examples

**Example 1**

- Input: `["MyQueue","push","push","peek","pop","empty"], [[],[1],[2],[],[],[]]`
- Output: `[null,null,null,1,1,false]`
- Explanation: Pushing `1` and then `2` produces the queue `[1,2]`, with `1` at the front. Both `peek()` and the following `pop()` return `1`; afterward `[2]` remains, so `empty()` is `false`.

| Call | Queue after call | Result |
|---|---|---:|
| `MyQueue()` | `[]` | `null` |
| `push(1)` | `[1]` | `null` |
| `push(2)` | `[1,2]` | `null` |
| `peek()` | `[1,2]` | `1` |
| `pop()` | `[2]` | `1` |
| `empty()` | `[2]` | `false` |
