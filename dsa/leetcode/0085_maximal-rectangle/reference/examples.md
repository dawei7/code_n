## Examples

**Example 1**

- Input: `matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]`
- Output: `6`
- Explanation: The independent diagram brackets the largest all-`1` rectangle, which has two rows and three columns and therefore area `6`.

```text
1 0  1   0   0
1 0 [1] [1] [1]
1 1 [1] [1] [1]
1 0  0   1   0
```

**Example 2**

- Input: `matrix = [["0"]]`
- Output: `0`

**Example 3**

- Input: `matrix = [["1"]]`
- Output: `1`
