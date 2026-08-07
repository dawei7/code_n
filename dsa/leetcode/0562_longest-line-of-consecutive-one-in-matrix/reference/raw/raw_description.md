## Description

Given an `m x n` binary matrix `mat`, return *the length of the longest line of consecutive one in the matrix*.

The line could be horizontal, vertical, diagonal, or anti-diagonal.

**Example 1:**

![](images/long1-grid.jpg)

```
**Input:** mat = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
**Output:** 3
```

**Example 2:**

![](images/long2-grid.jpg)

```
**Input:** mat = [[1,1,1,1],[0,1,1,0],[0,0,0,1]]
**Output:** 4
```

**Constraints:**

	- `m == mat.length`

	- `n == mat[i].length`

	- `1 <= m, n <= 10^4`

	- `1 <= m * n <= 10^4`

	- `mat[i][j]` is either `0` or `1`.
