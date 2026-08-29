### 1. Description

There is an infinite 2D plane.

You are given a positive integer `k`. You are also given a 2D array `queries`, which contains the following queries:

- $\text{queries}[i] = [x, y]$: Build an obstacle at coordinate `(x, y)` in the plane. It is guaranteed that there is **no** obstacle at this coordinate when this query is made.

After each query, you need to find the **distance** of the $k^{\text{th}}$ **nearest** obstacle from the origin.

Return an integer array `results` where $\text{results}[i]$ denotes the $k^{\text{th}}$ nearest obstacle after query `i`, or $\text{results}[i] = -1$ if there are less than `k` obstacles.

### 2. Function Contract

**Inputs**

- `queries`: Input parameter (`List[List[int]]`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `List[int]`.

### 3. Note

that initially there are **no** obstacles anywhere.

The **distance** of an obstacle at coordinate `(x, y)` from the origin is given by $|x| + |y|$.

### 4. Examples

#### Example 1

- **Input:** queries = [[1,2],[3,4],[2,3],[-3,0]], k = 2

- **Output:** [-1,7,5,3]

- **Explanation:** 

- Initially, there are 0 obstacles.

- After $\text{queries}[0]$, there are less than 2 obstacles.

- After $\text{queries}[1]$, there are obstacles at distances 3 and 7.

- After $\text{queries}[2]$, there are obstacles at distances 3, 5, and 7.

- After $\text{queries}[3]$, there are obstacles at distances 3, 3, 5, and 7.

#### Example 2

- **Input:** queries = [[5,5],[4,4],[3,3]], k = 1

- **Output:** [10,8,6]

- **Explanation:** 

- After $\text{queries}[0]$, there is an obstacle at distance 10.

- After $\text{queries}[1]$, there are obstacles at distances 8 and 10.

- After $\text{queries}[2]$, there are obstacles at distances 6, 8, and 10.

### 5. Constraints

- $1 \le \text{queries.length} \le 2 * 10^{5}$

- All $\text{queries}[i]$ are unique.

- $-10^{9} \le \text{queries}[i][0], \text{queries}[i][1] \le 10^{9}$

- $1 \le k \le 10^{5}$
