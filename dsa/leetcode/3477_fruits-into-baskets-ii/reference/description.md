## Description

You are given two arrays of integers, `fruits` and `baskets`, each of length `n`, where $\text{fruits}[i]$ represents the **quantity** of the $$i^{\text{th}}$$type of fruit, and$\text{baskets}[j]$represents the **capacity** of the$$j^{\text{th}}$$ basket.

From left to right, place the fruits according to these rules:

- Each fruit type must be placed in the **leftmost available basket** with a capacity **greater than or equal** to the quantity of that fruit type.

- Each basket can hold **only one** type of fruit.

- If a fruit type **cannot be placed** in any basket, it remains **unplaced**.

Return the number of fruit types that remain unplaced after all possible allocations are made.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** fruits = [4,2,5], baskets = [3,5,4]

**Output:** 1

**Explanation:**

- $\text{fruits}[0] = 4$ is placed in $\text{baskets}[1] = 5$.

- $\text{fruits}[1] = 2$ is placed in $\text{baskets}[0] = 3$.

- $\text{fruits}[2] = 5$ cannot be placed in $\text{baskets}[2] = 4$.

Since one fruit type remains unplaced, we return 1.

</div>
#### Example 2

<div class="example-block">
**Input:** fruits = [3,6,1], baskets = [6,4,7]

**Output:** 0

**Explanation:**

- $\text{fruits}[0] = 3$ is placed in $\text{baskets}[0] = 6$.

- $\text{fruits}[1] = 6$ cannot be placed in $\text{baskets}[1] = 4$ (insufficient capacity) but can be placed in the next available basket, $\text{baskets}[2] = 7$.

- $\text{fruits}[2] = 1$ is placed in $\text{baskets}[1] = 4$.

Since all fruits are successfully placed, we return 0.

</div>
### Constraints

- $n = \text{fruits.length} = \text{baskets.length}$

- $1 \le n \le 100$

- $1 \le \text{fruits}[i], \text{baskets}[i] \le 1000$