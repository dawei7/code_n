## Examples

**Example 1**

- Input: `matrix = [[9,9,4],[6,6,8],[2,1,1]]`
- Output: `4`
- Explanation: One longest increasing path follows the values `[1,2,6,9]`.

```text
 9   9   4
 ^
 6   6   8
 ^
 2 <-1   1
```

**Example 2**

- Input: `matrix = [[3,4,5],[3,2,6],[2,2,1]]`
- Output: `4`
- Explanation: The values `[3,4,5,6]` form a longest increasing path. A diagonal move cannot be used.

```text
 3 ->4 ->5
         |
 3   2   v
 2   2   6
```

**Example 3**

- Input: `matrix = [[1]]`
- Output: `1`
