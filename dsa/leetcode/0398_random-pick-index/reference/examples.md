## Examples

**Example 1**

- Input: `operations = ["Solution","pick","pick","pick"], arguments = [[[1,2,3,3,3]],[3],[1],[3]]`
- Output: `[null,4,0,2]`
- Explanation: For target `3`, indices `2`, `3`, and `4` are equally likely; the displayed calls return `4` and later `2`. Target `1` occurs only at index `0`, so that call must return `0`.
