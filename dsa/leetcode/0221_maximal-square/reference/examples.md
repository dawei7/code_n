## Examples

**Example 1**

```text
1 0 1 0 0
1 0 [1 1] 1
1 1 [1 1] 1    highlighted square: side 2, area 4
1 0  0 1  0
```

- Input: `matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]`
- Output: `4`

**Example 2**

```text
0 1
1 0    largest all-one square: one cell
```

- Input: `matrix = [["0","1"],["1","0"]]`
- Output: `1`

**Example 3**

- Input: `matrix = [["0"]]`
- Output: `0`
