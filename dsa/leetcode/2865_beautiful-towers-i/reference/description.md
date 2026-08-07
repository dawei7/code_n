### 1. Description

You are given an array `heights` of `n` integers representing the number of bricks in `n` consecutive towers. Your task is to remove some bricks to form a **mountain-shaped** tower arrangement. In this arrangement, the tower heights are non-decreasing, reaching a maximum peak value with one or multiple consecutive towers and then non-increasing.

Return the **maximum possible sum** of heights of a mountain-shaped tower arrangement.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** heights = [5,3,4,1,1]

**Output:** 13

**Explanation:**

We remove some bricks to make $heights = [5,3,3,1,1]$, the peak is at index 0.

</div>
#### Example 2

<div class="example-block">
**Input:** heights = [6,5,3,9,2,7]

**Output:** 22

**Explanation:**

We remove some bricks to make $heights = [3,3,3,9,2,2]$, the peak is at index 3.

</div>
#### Example 3

<div class="example-block">
**Input:** heights = [3,2,5,5,2,3]

**Output:** 18

**Explanation:**

We remove some bricks to make $heights = [2,2,5,5,2,2]$, the peak is at index 2 or 3.

</div>

### 4. Constraints

- $1 \le n = \text{heights.length} \le 10^{3}$

- $1 \le \text{heights}[i] \le 10^{9}$