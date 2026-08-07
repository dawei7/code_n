## Description

There is a circle of red and blue tiles. You are given an array of integers `colors`. The color of tile `i` is represented by $\text{colors}[i]$:

- $\text{colors}[i] = 0$ means that tile `i` is **red**.

- $\text{colors}[i] = 1$ means that tile `i` is **blue**.

Every 3 contiguous tiles in the circle with **alternating** colors (the middle tile has a different color from its **left** and **right** tiles) is called an **alternating** group.

Return the number of **alternating** groups.

**Note** that since `colors` represents a **circle**, the **first** and the **last** tiles are considered to be next to each other.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** colors = [1,1,1]

**Output:** 0

**Explanation:**

![](images/image_2024-05-16_23-53-171.png)

</div>
#### Example 2

<div class="example-block">
**Input:** colors = [0,1,0,0,1]

**Output:** 3

**Explanation:**

![](images/image_2024-05-16_23-47-491.png)

Alternating groups:

**

![](images/image_2024-05-16_23-50-441.png)

**

![](images/image_2024-05-16_23-48-211.png)

**

![](images/image_2024-05-16_23-49-351.png)

**

</div>
### Constraints

- $3 \le \text{colors.length} \le 100$

- $0 \le \text{colors}[i] \le 1$