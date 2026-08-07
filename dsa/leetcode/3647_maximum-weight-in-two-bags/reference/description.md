### 1. Description

You are given an integer array `weights` and two integers `w1` and `w2` representing the **maximum** capacities of two bags.

Each item may be placed in **at most** one bag such that:

- Bag 1 holds **at most** `w1` total weight.

- Bag 2 holds **at most** `w2` total weight.

Return the **maximum** total weight that can be packed into the two bags.

### 2. Function Contract

- Refer to method signature.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** weights = [1,4,3,2], w1 = 5, w2 = 4

**Output:** 9

**Explanation:**

- Bag 1: Place $\text{weights}[2] = 3$ and $\text{weights}[3] = 2$ as $3 + 2 = 5 \le w1$

- Bag 2: Place $\text{weights}[1] = 4$ as $4 \le w2$

- Total weight: $5 + 4 = 9$

</div>
#### Example 2

<div class="example-block">
**Input:** weights = [3,6,4,8], w1 = 9, w2 = 7

**Output:** 15

**Explanation:**

- Bag 1: Place $\text{weights}[3] = 8$ as $8 \le w1$

- Bag 2: Place $\text{weights}[0] = 3$ and $\text{weights}[2] = 4$ as $3 + 4 = 7 \le w2$

- Total weight: $8 + 7 = 15$

</div>
#### Example 3

<div class="example-block">
**Input:** weights = [5,7], w1 = 2, w2 = 3

**Output:** 0

**Explanation:**

No weight fits in either bag, thus the answer is 0.

</div>

### 4. Constraints

- $1 \le \text{weights.length} \le 100$

- $1 \le \text{weights}[i] \le 100$

- $1 \le w1, w2 \le 300$