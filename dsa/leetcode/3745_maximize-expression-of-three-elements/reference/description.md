### 1. Description

You are given an integer array `nums`.

Choose three elements `a`, `b`, and `c` from `nums` at **distinct** indices such that the value of the expression $a + b - c$ is maximized.

Return an integer denoting the **maximum possible value** of this expression.

### 2. Function Contract

**Inputs**

- `nums`: The integer array supplying the three distinctly indexed selections.

The same index cannot fill two roles. Duplicate values at separate indices remain separate eligible elements.

**Return value**

Return the maximum value of $a + b - c$ over all choices of three distinct indices.

### 3. Examples

#### Example 1

- **Input:** nums = [1,4,2,5]

- **Output:** 8

- **Explanation:** We can choose $a = 4$, $b = 5$, and $c = 1$. The expression value is $4 + 5 - 1 = 8$, which is the maximum possible.

#### Example 2

- **Input:** nums = [-2,0,5,-2,4]

- **Output:** 11

- **Explanation:** We can choose $a = 5$, $b = 4$, and $c = -2$. The expression value is $5 + 4 - (-2) = 11$, which is the maximum possible.

### 4. Constraints

- $3 \le \text{nums.length} \le 100$

- $-100 \le \text{nums}[i] \le 100$
