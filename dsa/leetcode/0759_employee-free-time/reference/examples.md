## Examples

**Example 1**

- Input: `schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]`
- Output: `[[3,4]]`
- Explanation: There are three employees. Their common free intervals are conceptually `[-inf,1]`, `[3,4]`, and `[10,inf]`; the two intervals containing infinity are excluded because the result must be finite.

**Example 2**

- Input: `schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]`
- Output: `[[5,6],[7,9]]`
