### 1. Description

A parentheses string is a **non-empty** string consisting only of `'('` and `')'`. It is **valid** if **any** of the following conditions is **true**:

- It is `()`.

- It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid parentheses strings.

- It can be written as `(A)`, where `A` is a valid parentheses string.

You are given an `m x n` matrix of parentheses `grid`. A **valid parentheses string path** in the grid is a path satisfying **all** of the following conditions:

- The path starts from the upper left cell `(0, 0)`.

- The path ends at the bottom-right cell $(m - 1, n - 1)$.

- The path only ever moves **down** or **right**.

- The resulting parentheses string formed by the path is **valid**.

Return `true` *if there exists a **valid parentheses string path** in the grid.* Otherwise, return `false`.

### 2. Function Contract

**Inputs**

- `grid`: Input parameter (`List[List[str]]`).

**Return value**

- Returns `bool`.

### 3. Examples

#### Example 1

![](images/example1drawio.png)

- **Input:** `grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]`
- **Output:** `true`
- **Explanation:** The above diagram shows two possible paths that form valid parentheses strings.
The first path shown results in the valid parentheses string "()(())".
The second path shown results in the valid parentheses string "((()))".
Note that there may be other valid parentheses string paths.

#### Example 2

![](images/example2drawio.png)

- **Input:** `grid = [[")",")"],["(","("]]`
- **Output:** `false`
- **Explanation:** The two possible paths form the parentheses strings "))(" and ")((". Since neither of them are valid parentheses strings, we return false.

### 4. Constraints

- $m = \text{grid.length}$

- $n = \text{grid}[i].length$

- $1 \le m, n \le 100$

- $\text{grid}[i][j]$ is either `'('` or `')'`.
