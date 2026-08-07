## Description

There are `n` mountains in a row, and each mountain has a height. You are given an integer array `height` where $\text{height}[i]$ represents the height of mountain `i`, and an integer `threshold`.

A mountain is called **stable** if the mountain just before it (**if it exists**) has a height **strictly greater** than `threshold`. **Note** that mountain 0 is **not** stable.

Return an array containing the indices of *all* **stable** mountains in **any** order.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** height = [1,2,3,4,5], threshold = 2

**Output:** [3,4]

**Explanation:**

- Mountain 3 is stable because $\text{height}[2] = 3$ is greater than $threshold = 2$.

- Mountain 4 is stable because $\text{height}[3] = 4$ is greater than $threshold = 2$.

</div>
#### Example 2

<div class="example-block">
**Input:** height = [10,1,10,1,10], threshold = 3

**Output:** [1,3]

</div>
#### Example 3

<div class="example-block">
**Input:** height = [10,1,10,1,10], threshold = 10

**Output:** []

</div>
### Constraints

- $2 \le n = \text{height.length} \le 100$

- $1 \le \text{height}[i] \le 100$

- $1 \le threshold \le 100$