## Examples

**Example 1**

- Input: `length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]`
- Output: `[-2,0,3,5,3]`

The source illustration applies the three inclusive updates from top to bottom:

```text
initial                [ 0, 0, 0, 0, 0]
add  2 to indices 1..3 [ 0, 2, 2, 2, 0]
add  3 to indices 2..4 [ 0, 2, 5, 5, 3]
add -2 to indices 0..2 [-2, 0, 3, 5, 3]
```

**Example 2**

- Input: `length = 10, updates = [[2,4,6],[5,6,8],[1,9,-4]]`
- Output: `[0,-4,2,2,2,4,4,-4,-4,-4]`
