## Description

You are given an array `maximumHeight`, where $\text{maximumHeight}[i]$ denotes the **maximum** height the $$i^{\text{th}}$$ tower can be assigned.

Your task is to assign a height to each tower so that:

- The height of the $$i^{\text{th}}$$tower is a positive integer and does not exceed$\text{maximumHeight}[i]$.

- No two towers have the same height.

Return the **maximum** possible total sum of the tower heights. If it's not possible to assign heights, return `-1`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** maximumHeight = [2,3,4,3]

**Output:** 10

**Explanation:**

We can assign heights in the following way: `[1, 2, 4, 3]`.

</div>
#### Example 2

<div class="example-block">
**Input:** maximumHeight = [15,10]

**Output:** 25

**Explanation:**

We can assign heights in the following way: `[15, 10]`.

</div>
#### Example 3

<div class="example-block">
**Input:** maximumHeight = [2,2,1]

**Output:** -1

**Explanation:**

It's impossible to assign positive heights to each index so that no two towers have the same height.

</div>
### Constraints

- $1 \le \text{maximumHeight.length} \le 10^{5}$

- $1 \le \text{maximumHeight}[i] \le 10^{9}$