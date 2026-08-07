## Description

There are n points on an infinite plane. You are given two integer arrays `xCoord` and `yCoord` where $(\text{xCoord}[i], \text{yCoord}[i])$ represents the coordinates of the $$i^{\text{th}}$$ point.

Your task is to find the **maximum **area of a rectangle that:

- Can be formed using **four** of these points as its corners.

- Does **not** contain any other point inside or on its border.

- Has its edges **parallel** to the axes.

Return the **maximum area** that you can obtain or -1 if no such rectangle is possible.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** xCoord = [1,1,3,3], yCoord = [1,3,1,3]

**Output:** 4

**Explanation:**

**

![Example 1 diagram](images/example1.png)

**

We can make a rectangle with these 4 points as corners and there is no other point that lies inside or on the border. Hence, the maximum possible area would be 4.

</div>
#### Example 2

<div class="example-block">
**Input:** xCoord = [1,1,3,3,2], yCoord = [1,3,1,3,2]

**Output:** -1

**Explanation:**

**

![Example 2 diagram](images/example2.png)

**

There is only one rectangle possible is with points `[1,1], [1,3], [3,1]` and `[3,3]` but `[2,2]` will always lie inside it. Hence, returning -1.

</div>
#### Example 3

<div class="example-block">
**Input:** xCoord = [1,1,3,3,1,3], yCoord = [1,3,1,3,2,2]

**Output:** 2

**Explanation:**

**

![Example 3 diagram](images/example3.png)

**

The maximum area rectangle is formed by the points `[1,3], [1,2], [3,2], [3,3]`, which has an area of 2. Additionally, the points `[1,1], [1,2], [3,1], [3,2]` also form a valid rectangle with the same area.

</div>
### Constraints

- $1 \le \text{xCoord.length} = \text{yCoord.length} \le 2 * 10^{5}$

- $0 \le \text{xCoord}[i], \text{yCoord}[i] \le 8 * 10^{7}$

- All the given points are **unique**.