## Description

You are given an `m x n` matrix `grid` consisting of characters and a string `pattern`.

A **horizontal substring** is a contiguous sequence of characters read from left to right. If the end of a row is reached before the substring is complete, it wraps to the first column of the next row and continues as needed. You do **not** wrap from the bottom row back to the top.

A **vertical substring** is a contiguous sequence of characters read from top to bottom. If the bottom of a column is reached before the substring is complete, it wraps to the first row of the next column and continues as needed. You do **not** wrap from the last column back to the first.

Count the number of cells in the matrix that satisfy the following condition:

- The cell must be part of **at least** one horizontal substring and **at least** one vertical substring, where **both** substrings are equal to the given `pattern`.

Return the count of these cells.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

![](images/gridtwosubstringsdrawio.png)

<div class="example-block">
**Input:** grid = [["a","a","c","c"],["b","b","b","c"],["a","a","b","a"],["c","a","a","c"],["a","a","b","a"]], pattern = "abaca"

**Output:** 1

**Explanation:**

The pattern `"abaca"` appears once as a horizontal substring (colored blue) and once as a vertical substring (colored red), intersecting at one cell (colored purple).

</div>
#### Example 2

![](images/gridexample2fixeddrawio.png)

<div class="example-block">
**Input:** grid = [["c","a","a","a"],["a","a","b","a"],["b","b","a","a"],["a","a","b","a"]], pattern = "aba"

**Output:** 4

**Explanation:**

The cells colored above are all part of at least one horizontal and one vertical substring matching the pattern `"aba"`.

</div>
#### Example 3

<div class="example-block">
**Input:** grid = [["a"]], pattern = "a"

**Output:** 1

</div>
### Constraints

- $m = \text{grid.length}$

- $n = \text{grid}[i].length$

- $1 \le m, n \le 1000$

- $1 \le m * n \le 10^{5}$

- $1 \le \text{pattern.length} \le m * n$

- `grid` and `pattern` consist of only lowercase English letters.