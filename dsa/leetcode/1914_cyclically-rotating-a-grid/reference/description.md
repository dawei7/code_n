### 1. Description

You are given an `m x n` integer matrix `grid`​​​, where `m` and `n` are both **even** integers, and an integer `k`.

The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:

![](images/ringofgrid.png)

A cyclic rotation of the matrix is done by cyclically rotating **each layer** in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent element in the **counter-clockwise** direction. An example rotation is shown below:

![](images/explanation_grid.jpg)

Return *the matrix after applying *`k` *cyclic rotations to it*.

### 2. Function Contract

**Inputs**

- `grid`: Input parameter (`List[List[int]]`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `List[List[int]]`.

### 3. Examples

#### Example 1

![](images/rod2.png)

- **Input:** `grid = [[40,10],[30,20]], k = 1`
- **Output:** `[[10,20],[40,30]]`
- **Explanation:** The figures above represent the grid at every state.

#### Example 2

**

![](images/ringofgrid5.png)

** **

![](images/ringofgrid6.png)

** **

![](images/ringofgrid7.png)

**

- **Input:** `grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2`
- **Output:** `[[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]`
- **Explanation:** The figures above represent the grid at every state.

### 4. Constraints

- $m = \text{grid.length}$

- $n = \text{grid}[i].length$

- $2 \le m, n \le 50$

- Both `m` and `n` are **even** integers.

- $1 \le \text{grid}[i][j] \le ^ 5000$

- $1 \le k \le 10^{9}$
