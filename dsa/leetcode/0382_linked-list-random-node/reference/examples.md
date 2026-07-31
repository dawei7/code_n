## Examples

**Example 1**

- Input: `operations = ["Solution","getRandom","getRandom","getRandom","getRandom","getRandom"], arguments = [[[1,2,3]],[],[],[],[],[]]`
- Output: `[null,1,3,2,2,3]`
- Explanation: Construct the selector from `1 -> 2 -> 3`. The displayed calls produce `1`, `3`, `2`, `2`, and `3`, but every call may independently return any of the three values with probability $1/3$.

The source illustration shows the initialized linked list:

```text
(1) -> (2) -> (3)
```
