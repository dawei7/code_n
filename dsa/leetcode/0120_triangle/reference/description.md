### 1. Description

Given a `triangle` array, return *the minimum path sum from top to bottom*.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index `i` on the current row, you may move to either index `i` or index $i + 1$ on the next row.

### 2. Function Contract

**Inputs**

- `triangle`: The integer rows of the triangle.

**Return value**

Return the smallest sum obtainable by a valid adjacent path from the top entry to the bottom row.

### 3. Examples

#### Example 1

- **Input:** $triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]$
- **Output:** `11`
- **Explanation:** The triangle looks like:
<u>2</u>
<u>3</u> 4
6 <u>5</u> 7
4 <u>1</u> 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
#### Example 2

- **Input:** $triangle = [[-10]]$
- **Output:** `-10`

### 4. Constraints

- $1 \le \text{triangle.length} \le 200$

- $\text{triangle}[0].length = 1$

- $\text{triangle}[i].length = triangle[i - 1].length + 1$

- $-10^{4} \le \text{triangle}[i][j] \le 10^{4}$

**Follow up:** Could you do this using only `O(n)` extra space, where `n` is the total number of rows in the triangle?