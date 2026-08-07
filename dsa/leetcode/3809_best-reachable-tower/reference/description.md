### 1. Description

You are given a 2D integer array `towers`, where $\text{towers}[i] = [x_{i}, y_{i}, q_{i}]$ represents the coordinates $(x_{i}, y_{i})$ and quality factor $q_{i}$ of the $$i^{\text{th}}$$ tower.

You are also given an integer array $center = [cx, cy​​​​​​​]$ representing your location, and an integer `radius`.

A tower is **reachable** if its **Manhattan distance** from `center` is **less than or equal** to `radius`.

Among all reachable towers:

- Return the coordinates of the tower with the **maximum** quality factor.

- If there is a tie, return the tower with the **lexicographically smallest** coordinate. If no tower is reachable, return `[-1, -1]`.

The **Manhattan Distance** between two cells $(x_{i}, y_{i})$ and $(x_{j}, y_{j})$ is $|x_{i} - x_{j}| + |y_{i} - y_{j}|$.

A coordinate $[x_{i}, y_{i}]$ is **lexicographically smaller** than $[x_{j}, y_{j}]$ if $x_{i} < x_{j}$, or $x_{i} = x_{j}$ and $y_{i} < y_{j}$.

`|x|` denotes the **absolute** **value** of `x`.

### 2. Function Contract

**Inputs**

- `towers`: A non-empty list of triples $[x_{i}, y_{i}, q_{i}]$, giving one tower's coordinates and quality factor per entry.
- `center`: A two-element list `[cx, cy]` representing your location.
- `radius`: The inclusive maximum Manhattan distance at which a tower is reachable.

Let $N=\lvert\texttt{towers}\rvert$. For each tower, reachability is determined by

$\lvert x_i-cx\rvert+\lvert y_i-cy\rvert\le\texttt{radius}.$

**Return value**

Return $[x_{i}, y_{i}]$ for the reachable tower with greatest $q_i$. Among equal greatest qualities, return the smallest coordinate under ordinary list lexicographic order. Return `[-1, -1]` if the reachable set is empty.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** towers = [[1,2,5], [2,1,7], [3,1,9]], center = [1,1], radius = 2

**Output:** [3,1]

**Explanation:**

- Tower `[1, 2, 5]`: Manhattan distance = $|1 - 1| + |2 - 1| = 1$, reachable.

- Tower `[2, 1, 7]`: Manhattan distance = $|2 - 1| + |1 - 1| = 1$, reachable.

- Tower `[3, 1, 9]`: Manhattan distance = $|3 - 1| + |1 - 1| = 2$, reachable.

All towers are reachable. The maximum quality factor is 9, which corresponds to tower `[3, 1]`.

</div>
#### Example 2

<div class="example-block">
**Input:** towers = [[1,3,4], [2,2,4], [4,4,7]], center = [0,0], radius = 5

**Output:** [1,3]

**Explanation:**

- Tower `[1, 3, 4]`: Manhattan distance = $|1 - 0| + |3 - 0| = 4$, reachable.

- Tower `[2, 2, 4]`: Manhattan distance = $|2 - 0| + |2 - 0| = 4$, reachable.

- Tower `[4, 4, 7]`: Manhattan distance = $|4 - 0| + |4 - 0| = 8$, not reachable.

Among the reachable towers, the maximum quality factor is 4. Both `[1, 3]` and `[2, 2]` have the same quality, so the lexicographically smaller coordinate is `[1, 3]`.

</div>
#### Example 3

<div class="example-block">
**Input:** towers = [[5,6,8], [0,3,5]], center = [1,2], radius = 1

**Output:** [-1,-1]

**Explanation:**

- Tower `[5, 6, 8]`: Manhattan distance = $|5 - 1| + |6 - 2| = 8$, not reachable.

- Tower `[0, 3, 5]`: Manhattan distance = $|0 - 1| + |3 - 2| = 2$, not reachable.

No tower is reachable within the given radius, so `[-1, -1]` is returned.

</div>

### 4. Constraints

- $1 \le \text{towers.length} \le 10^{5}$

- $\text{towers}[i] = [x_{i}, y_{i}, q_{i}]$

- $center = [cx, cy]$

- $0 \le x_{i}, y_{i}, q_{i}, cx, cy \le 10^{5}$​​​​​​​

- $0 \le radius \le 10^{5}$