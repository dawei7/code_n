### 1. Description

You are given a string `road`, consisting only of characters `"x"` and `"."`, where each `"x"` denotes a *pothole* and each `"."` denotes a smooth road, and an integer `budget`.

In one repair operation, you can repair `n` **consecutive** potholes for a price of $n + 1$.

Return the **maximum** number of potholes that can be fixed such that the sum of the prices of all of the fixes **doesn't go over** the given budget.

### 2. Function Contract

- Refer to method signature.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** road = "..", budget = 5

**Output:** 0

**Explanation:**

There are no potholes to be fixed.

</div>
#### Example 2

<div class="example-block">
**Input:** road = "..xxxxx", budget = 4

**Output:** 3

**Explanation:**

We fix the first three potholes (they are consecutive). The budget needed for this task is $3 + 1 = 4$.

</div>
#### Example 3

<div class="example-block">
**Input:** road = "x.x.xxx...x", budget = 14

**Output:** 6

**Explanation:**

We can fix all the potholes. The total cost would be $(1 + 1) + (1 + 1) + (3 + 1) + (1 + 1) = 10$ which is within our budget of 14.

</div>

### 4. Constraints

- $1 \le \text{road.length} \le 10^{5}$

- $1 \le budget \le 10^{5} + 1$

- `road` consists only of characters `'.'` and `'x'`.