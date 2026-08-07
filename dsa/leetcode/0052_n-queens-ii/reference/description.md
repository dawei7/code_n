### 1. Description

The **n-queens** puzzle is the problem of placing `n` queens on an `n x n` chessboard such that no two queens attack each other.

Given an integer `n`, return *the number of distinct solutions to the **n-queens puzzle***.

### 2. Function Contract

**Inputs**

- `n`: The board dimension and the number of queens.

**Return value**

Return the number of distinct valid n-queens configurations.

### 3. Examples

#### Example 1

![](images/queens.jpg)

- **Input:** $n = 4$
- **Output:** `2`
- **Explanation:** There are two distinct solutions to the 4-queens puzzle as shown.
#### Example 2

- **Input:** $n = 1$
- **Output:** `1`

### 4. Constraints

- $1 \le n \le 9$