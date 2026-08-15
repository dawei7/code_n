### 1. Description

You are given two integer arrays `x` and `y`, each of length `n`. You must choose three **distinct** indices `i`, `j`, and `k` such that:

- $x[i] \neq x[j]$

- $x[j] \neq x[k]$

- $x[k] \neq x[i]$

Your goal is to **maximize** the value of $y[i] + y[j] + y[k]$ under these conditions. Return the **maximum** possible sum that can be obtained by choosing such a triplet of indices.

If no such triplet exists, return -1.

### 2. Function Contract

**Inputs**

- `x`: Input parameter (`List[int]`).
- `y`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** x = [1,2,1,3,2], y = [5,3,4,6,2]

- **Output:** 14

- **Explanation:** 

- Choose $i = 0$ ($x[i] = 1$, $y[i] = 5$), $j = 1$ ($x[j] = 2$, $y[j] = 3$), $k = 3$ ($x[k] = 3$, $y[k] = 6$).

- All three values chosen from `x` are distinct. $5 + 3 + 6 = 14$ is the maximum we can obtain. Hence, the output is 14.

#### Example 2

- **Input:** x = [1,2,1,2], y = [4,5,6,7]

- **Output:** -1

- **Explanation:** 

- There are only two distinct values in `x`. Hence, the output is -1.

### 4. Constraints

- $n = \text{x.length} = \text{y.length}$

- $3 \le n \le 10^{5}$

- $1 \le x[i], y[i] \le 10^{6}$
