## Examples

**Example 1**

- Input: `matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`
- Output: `[[7, 4, 1], [8, 5, 2], [9, 6, 3]]`

The independently rendered matrix view shows the same clockwise transformation:

```text
1 2 3       7 4 1
4 5 6  -->  8 5 2
7 8 9       9 6 3
```

**Example 2**

- Input: `matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]`
- Output: `[[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]`

The same input and output can be compared spatially as follows:

```text
 5  1  9 11        15 13  2  5
 2  4  8 10        14  3  4  1
13  3  6  7  -->   12  6  8  9
15 14 12 16        16  7 10 11
```
