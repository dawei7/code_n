## Examples

**Example 1**

- Input: `["Vector2D","next","next","next","hasNext","hasNext","next","hasNext"], [[[[1,2],[3],[4]]],[],[],[],[],[],[],[]]`
- Output: `[null,1,2,3,true,true,4,false]`
- Explanation: Initialize the iterator with `[[1,2],[3],[4]]`. Three `next` calls return `1`, `2`, and `3`. Two consecutive `hasNext` calls both return `true` without advancing. The next call returns `4`, after which `hasNext` returns `false`.
