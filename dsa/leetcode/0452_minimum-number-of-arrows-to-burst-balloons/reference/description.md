## Description

There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array `points` where $\text{points}[i] = [x_{start}, x_{end}]$ denotes a balloon whose **horizontal diameter** stretches between $x_{start}$ and $x_{end}$. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up **directly vertically** (in the positive y-direction) from different points along the x-axis. A balloon with $x_{start}$ and $x_{end}$ is **burst** by an arrow shot at `x` if $x_{start} \le x \le x_{end}$. There is **no limit** to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array `points`, return *the **minimum** number of arrows that must be shot to burst all balloons*.
### Function Contract

**Inputs**

- `points`: A nonempty list of two-element integer intervals `[x_start, x_end]`, one for each balloon's horizontal diameter.

**Return value**

- Return the minimum number of vertical arrows whose $x$-coordinates intersect all balloon intervals.

Each interval is closed: an arrow fired at either endpoint bursts that balloon.

### Examples
#### Example 1

- **Input:** $points = [[10,16],[2,8],[1,6],[7,12]]$
- **Output:** `2`
- **Explanation:** The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
#### Example 2

- **Input:** $points = [[1,2],[3,4],[5,6],[7,8]]$
- **Output:** `4`
- **Explanation:** One arrow needs to be shot for each balloon for a total of 4 arrows.
#### Example 3

- **Input:** $points = [[1,2],[2,3],[3,4],[4,5]]$
- **Output:** `2`
- **Explanation:** The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].
### Constraints

- $1 \le \text{points.length} \le 10^{5}$

- $\text{points}[i].length = 2$

- $-2^{31} \le x_{start} < x_{end} \le 2^{31} - 1$