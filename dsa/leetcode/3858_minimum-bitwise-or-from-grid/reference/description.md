### 1. Description

You are given a 2D integer array `grid` of size `m x n`.

You must select **exactly one** integer from each row of the grid.

Return an integer denoting the **minimum possible bitwise OR** of the selected integers from each row.

### 2. Function Contract

**Inputs**

- `grid`: A nonempty rectangular matrix of positive integers, with at least one value in every row.

If row $i$ contributes the selected value $x_i$, a valid selection contains exactly $m$ values and produces

$x_0\mathbin{\vert}x_1\mathbin{\vert}\cdots\mathbin{\vert}x_{m-1}.$

No column consistency is required: each row may contribute a value from any of its columns.

**Return value**

Return the minimum numerical value of the combined bitwise OR among all selections.

### 3. Examples

#### Example 1

- **Input:** grid = [[1,5],[2,4]]

- **Output:** 3

- **Explanation:** 

- Choose 1 from the first row and 2 from the second row.

- The bitwise OR of $1 | 2 = 3$​​​​​​​, which is the minimum possible.

#### Example 2

- **Input:** grid = [[3,5],[6,4]]

- **Output:** 5

- **Explanation:** 

- Choose 5 from the first row and 4 from the second row.

- The bitwise OR of $5 | 4 = 5$​​​​​​​, which is the minimum possible.

#### Example 3

- **Input:** grid = [[7,9,8]]

- **Output:** 7

- **Explanation:** 

- Choosing 7 gives the minimum bitwise OR.

### 4. Constraints

- $1 \le m = \text{grid.length} \le 10^{5}$

- $1 \le n = \text{grid}[i].length \le 10^{5}$

- $m * n \le 10^{5}$

- $1 \le \text{grid}[i][j] \le 10^{5}​​​​​​​$
