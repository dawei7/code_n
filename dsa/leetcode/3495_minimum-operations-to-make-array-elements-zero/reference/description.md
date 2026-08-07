## Description

You are given a 2D array `queries`, where $\text{queries}[i]$ is of the form `[l, r]`. Each $\text{queries}[i]$ defines an array of integers `nums` consisting of elements ranging from `l` to `r`, both **inclusive**.

In one operation, you can:

- Select two integers `a` and `b` from the array.

- Replace them with $floor(a / 4)$ and $floor(b / 4)$.

Your task is to determine the **minimum** number of operations required to reduce all elements of the array to zero for each query. Return the sum of the results for all queries.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** queries = [[1,2],[2,4]]

**Output:** 3

**Explanation:**

For $\text{queries}[0]$:

- The initial array is `nums = [1, 2]`.

- In the first operation, select $\text{nums}[0]$ and $\text{nums}[1]$. The array becomes `[0, 0]`.

- The minimum number of operations required is 1.

For $\text{queries}[1]$:

- The initial array is `nums = [2, 3, 4]`.

- In the first operation, select $\text{nums}[0]$ and $\text{nums}[2]$. The array becomes `[0, 3, 1]`.

- In the second operation, select $\text{nums}[1]$ and $\text{nums}[2]$. The array becomes `[0, 0, 0]`.

- The minimum number of operations required is 2.

The output is $1 + 2 = 3$.

</div>
#### Example 2

<div class="example-block">
**Input:** queries = [[2,6]]

**Output:** 4

**Explanation:**

For $\text{queries}[0]$:

- The initial array is `nums = [2, 3, 4, 5, 6]`.

- In the first operation, select $\text{nums}[0]$ and $\text{nums}[3]$. The array becomes `[0, 3, 4, 1, 6]`.

- In the second operation, select $\text{nums}[2]$ and $\text{nums}[4]$. The array becomes `[0, 3, 1, 1, 1]`.

- In the third operation, select $\text{nums}[1]$ and $\text{nums}[2]$. The array becomes `[0, 0, 0, 1, 1]`.

- In the fourth operation, select $\text{nums}[3]$ and $\text{nums}[4]$. The array becomes `[0, 0, 0, 0, 0]`.

- The minimum number of operations required is 4.

The output is 4.

</div>
### Constraints

- $1 \le \text{queries.length} \le 10^{5}$

- $\text{queries}[i].length = 2$

- $\text{queries}[i] = [l, r]$

- $1 \le l < r \le 10^{9}$