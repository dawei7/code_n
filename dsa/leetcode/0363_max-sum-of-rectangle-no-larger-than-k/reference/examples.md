## Examples

**Example 1**

- Input: `matrix = [[1,0,1],[0,-2,3]], k = 2`
- Output: `2`
- Explanation: The rectangle `[[0,1],[-2,3]]` has sum `2`, which is the greatest rectangle sum no larger than `k = 2`.

```text
 1 |  0   1 |
 0 | -2   3 |   selected rectangle sum = 0 + 1 - 2 + 3 = 2
```

**Example 2**

- Input: `matrix = [[2,2,-1]], k = 3`
- Output: `3`
