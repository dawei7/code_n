## Description

You are given an integer array `nums`.

Choose three elements `a`, `b`, and `c` from `nums` at **distinct** indices such that the value of the expression $a + b - c$ is maximized.

Return an integer denoting the **maximum possible value** of this expression.
### Function Contract

**Inputs**

- `nums`: The integer array supplying the three distinctly indexed selections.

The same index cannot fill two roles. Duplicate values at separate indices remain separate eligible elements.

**Return value**

Return the maximum value of `a + b - c` over all choices of three distinct indices.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,4,2,5]

**Output:** 8

**Explanation:**

We can choose $a = 4$, $b = 5$, and $c = 1$. The expression value is $4 + 5 - 1 = 8$, which is the maximum possible.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [-2,0,5,-2,4]

**Output:** 11

**Explanation:**

We can choose $a = 5$, $b = 4$, and $c = -2$. The expression value is $5 + 4 - (-2) = 11$, which is the maximum possible.

</div>
### Constraints

- $3 \le \text{nums.length} \le 100$

- $-100 \le \text{nums}[i] \le 100$