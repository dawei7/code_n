## Examples

**Example 1**

- Input: `dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]`
- Output: `7`
- Explanation: With initial health `7`, an optimal route is right, right, down, down.

```text
start -2 -> -3 ->  3
                   |
      -5    -10    1
                   |
      10     30 -> -5 princess
```

**Example 2**

- Input: `dungeon = [[0]]`
- Output: `1`
