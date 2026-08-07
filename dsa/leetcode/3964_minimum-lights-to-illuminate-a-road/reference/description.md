### 1. Description

You are given an integer array `lights` of length `n`, representing positions 0 through $n - 1$ on a road.

For each position `i`:

- If $\text{lights}[i] = v$, where `v > 0`, there is a working bulb at position `i` that **illuminates** every position from $max(0, i - v)$ to $min(n - 1, i + v)$, inclusive.

- If $\text{lights}[i] = 0$, there is no working bulb at position `i`.

A position is **visible** if it is illuminated by **at least** one working bulb.

You may install **additional** bulbs at **any** positions. Each additional bulb installed at position `j` **illuminates** positions from $max(0, j - 1)$ to $min(n - 1, j + 1)$, inclusive.

Return the minimum number of additional bulbs required to make **every** position on the road visible.

### 2. Function Contract

**Inputs**

- `lights`: A nonempty list of nonnegative integers; index `i` is a road position, and a positive value is the illumination radius of the existing bulb at that position.

Let $n$ be the number of road positions.

**Return value**

Return the smallest number of additional radius-one bulbs whose combined coverage, together with the existing working bulbs, makes all `n` positions visible.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** lights = [0,0,0,0]

**Output:** 2

**Explanation:**

One optimal placement is:

- Install an additional bulb at position 1, illuminating positions `[0, 1, 2]`.

- Install an additional bulb at position 3, illuminating positions `[2, 3]`.

Therefore, the minimum number of additional bulbs required is 2.

</div>
#### Example 2

<div class="example-block">
**Input:** lights = [0,0,0,2,0]

**Output:** 1

**Explanation:**

- Since $\text{lights}[3] = 2$, the working bulb at position 3 illuminates positions `[1, 2, 3, 4]`.

- Installing an additional bulb at position 1 illuminates positions `[0, 1, 2]`, making every position visible.

- Therefore, the minimum number of additional bulbs required is 1.

</div>

### 4. Constraints

- $1 \le n = \text{lights.length} \le 10^{5}$

- $0 \le \text{lights}[i] \le n$