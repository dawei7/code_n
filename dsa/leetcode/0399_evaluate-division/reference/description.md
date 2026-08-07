### 1. Description

You are given an array of variable pairs `equations` and an array of real numbers `values`, where $\text{equations}[i] = [A_{i}, B_{i}]$ and $\text{values}[i]$ represent the equation $A_{i} / B_{i} = \text{values}[i]$. Each $A_{i}$ or $B_{i}$ is a string that represents a single variable.

You are also given some `queries`, where $\text{queries}[j] = [C_{j}, D_{j}]$ represents the $$j^{\text{th}}$$ query where you must find the answer for $C_{j} / D_{j} = ?$.

Return *the answers to all queries*. If a single answer cannot be determined, return `-1.0`.

### 2. Function Contract

**Inputs**

- `equations`: Variable-name pairs describing known divisions.
- `values`: The positive real quotient corresponding to each equation.
- `queries`: Variable-name pairs whose quotients must be evaluated.

**Return value**

Return the quotient for each query in order, using `-1.0` when either variable is undefined or no relationship determines the quotient.

### 3. Note

The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

### 4. Note

The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

### 5. Examples

#### Example 1

- **Input:** `equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]`
- **Output:** `[6.00000,0.50000,-1.00000,1.00000,-1.00000]`
- **Explanation:**
Given: *a / b = 2.0*, *b / c = 3.0*
queries are: *a / c = ?*, *b / a = ?*, *a / e = ?*, *a / a = ?*, *x / x = ? *
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
#### Example 2

- **Input:** `equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]`
- **Output:** `[3.75000,0.40000,5.00000,0.20000]`
#### Example 3

- **Input:** `equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]`
- **Output:** `[0.50000,2.00000,-1.00000,-1.00000]`

### 6. Constraints

- $1 \le \text{equations.length} \le 20$

- $\text{equations}[i].length = 2$

- $1 \le A_{i}.length, B_{i}.length \le 5$

- $\text{values.length} = \text{equations.length}$

- $0.0 < \text{values}[i] \le 20.0$

- $1 \le \text{queries.length} \le 20$

- $\text{queries}[i].length = 2$

- $1 \le C_{j}.length, D_{j}.length \le 5$

- $A_{i}, B_{i}, C_{j}, D_{j}$ consist of lower case English letters and digits.