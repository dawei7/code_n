## Description

<div data-docx-has-block-data="false" data-lark-html-role="root" data-page-id="Rax8d6clvoFeVtx7bzXcvkVynwf">
<div class="old-record-id-Y5dGdSKIMoNTttxGhHLccrpEnaf">There is an endless straight line populated with some robots and walls. You are given integer arrays `robots`, `distance`, and `walls`:</div>
</div>

- $\text{robots}[i]$ is the position of the $$i^{\text{th}}$$ robot.

- $\text{distance}[i]$ is the **maximum** distance the $$i^{\text{th}}$$ robot's bullet can travel.

- $\text{walls}[j]$ is the position of the $$j^{\text{th}}$$ wall.

Every robot has **one** bullet that can either fire to the left or the right **at most **$\text{distance}[i]$ meters.

A bullet destroys every wall in its path that lies within its range. Robots are fixed obstacles: if a bullet hits another robot before reaching a wall, it **immediately stops** at that robot and cannot continue.

Return the **maximum** number of **unique** walls that can be destroyed by the robots.

Notes:

- A wall and a robot may share the same position; the wall can be destroyed by the robot at that position.

- Robots are not destroyed by bullets.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** robots = [4], distance = [3], walls = [1,10]

**Output:** 1

**Explanation:**

- $\text{robots}[0] = 4$ fires **left** with $\text{distance}[0] = 3$, covering `[1, 4]` and destroys $\text{walls}[0] = 1$.

- Thus, the answer is 1.

</div>
#### Example 2

<div class="example-block">
**Input:** robots = [10,2], distance = [5,1], walls = [5,2,7]

**Output:** 3

**Explanation:**

- $\text{robots}[0] = 10$ fires **left** with $\text{distance}[0] = 5$, covering `[5, 10]` and destroys $\text{walls}[0] = 5$ and $\text{walls}[2] = 7$.

- $\text{robots}[1] = 2$ fires **left** with $\text{distance}[1] = 1$, covering `[1, 2]` and destroys $\text{walls}[1] = 2$.

- Thus, the answer is 3.

</div>
#### Example 3

<div class="example-block">
**Input:** robots = [1,2], distance = [100,1], walls = [10]

**Output:** 0

**Explanation:**

In this example, only $\text{robots}[0]$ can reach the wall, but its shot to the **right** is blocked by $\text{robots}[1]$; thus the answer is 0.

</div>
### Constraints

- $1 \le \text{robots.length} = \text{distance.length} \le 10^{5}$

- $1 \le \text{walls.length} \le 10^{5}$

- $1 \le \text{robots}[i], \text{walls}[j] \le 10^{9}$

- $1 \le \text{distance}[i] \le 10^{5}$

- All values in `robots` are **unique**

- All values in `walls` are **unique**