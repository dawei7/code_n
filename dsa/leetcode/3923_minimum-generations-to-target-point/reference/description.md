### 1. Description

You are given a 2D integer array `points` where $\text{points}[i] = [x_{i}, y_{i}, z_{i}]$ represents a point in 3D space, and an integer array `target` representing a target point.

Define **generation** 0 as the initial list of points. For each integer $k \ge 1$, form generation `k` as follows:

- Consider every pair of two **distinct** points $a = [x_{1}, y_{1}, z_{1}]$ and $b = [x_{2}, y_{2}, z_{2}]$ taken from all points produced in generations 0 through $k - 1$.

- For each such pair, compute $c = [floor((x_{1} + x_{2}) / 2), floor((y_{1} + y_{2}) / 2), floor((z_{1} + z_{2}) / 2)]$ and collect every such `c` into a generation `k`.

- All points in the generation `k` are produced **simultaneously** from points in generations 0 through $k - 1$.

- After generation `k` is formed, the points in the generation `k` are considered available for forming later generations.

Return the **smallest** integer `k` such that the `target` appears in one of the generations 0 through `k`. If the `target` is already in the initial points, return 0. If it is impossible to obtain the `target`, return -1.

Notes:

- **floor** denotes rounding **down** to the nearest integer.

- "Two **distinct** points" means the two chosen points must have **different** `(x, y, z)` coordinates. A point cannot be paired with itself, and pairing two points with **identical** coordinates is not possible.

### 2. Function Contract

**Inputs**

- `points`: A non-empty list of distinct three-element integer lists representing the generation-$0$ points.
- `target`: A three-element integer list representing the point to find.

Let $n=\lvert\texttt{points}\rvert$. Let $U$ be the number of distinct coordinate triples that eventually enter the reachable closure; the coordinate limits guarantee $U\le7^3=343$.

**Return value**

Return the smallest generation number in which `target` is available. Return `-1` if the closure stabilizes without the target.

### 3. Examples

#### Example 1

- **Input:** points = [[0,0,0],[6,6,6]], target = [3,3,3]

- **Output:** 1

- **Explanation:** 

- **Generation 0:** The initial $points = [[0, 0, 0], [6, 6, 6]]$.

- The $target = [3, 3, 3]$ does not exist in generation 0.

- **Generation 1:** For each pair of points in generation 0, we create new points.

		- Using `[0, 0, 0]` and `[6, 6, 6]`, we generate `[3, 3, 3]`.

- After generation 1, $points = [[0, 0, 0], [6, 6, 6], [3, 3, 3]]$.

- The $target = [3, 3, 3]$ is found in generation 1, so the smallest `k` is 1.

#### Example 2

- **Input:** points = [[0,0,0],[5,5,5]], target = [1,1,1]

- **Output:** 2

- **Explanation:** 

- **Generation 0:** The initial $points = [[0, 0, 0], [5, 5, 5]]$.

- The $target = [1, 1, 1]$ does not exist in generation 0.

- **Generation 1:** For each pair of points in generation 0, we create new points.

		- Using `[0, 0, 0]` and `[5, 5, 5]`, we generate `[2, 2, 2]`.

- After generation 1, $points = [[0, 0, 0], [5, 5, 5], [2, 2, 2]]$.

- **Generation 2:** For each pair of points available after generation 1, we create new points.

		- Using `[0, 0, 0]` and `[5, 5, 5]`, we generate `[2, 2, 2]`.

- Using `[0, 0, 0]` and `[2, 2, 2]`, we generate `[1, 1, 1]`.

- Using `[5, 5, 5]` and `[2, 2, 2]`, we generate `[3, 3, 3]`.

- After generation 2, $points = [[0, 0, 0], [5, 5, 5], [2, 2, 2], [1, 1, 1], [3, 3, 3]]$.

- The $target = [1, 1, 1]$ is found in generation 2, so the smallest `k` is 2.

#### Example 3

- **Input:** points = [[0,0,0],[2,2,2],[3,3,3]], target = [2,2,2]

- **Output:** 0

- **Explanation:** 

- **Generation 0:** The initial $points = [[0, 0, 0], [2, 2, 2], [3, 3, 3]]$.

- The $target = [2, 2, 2]$ already exists in generation 0, so the smallest `k` is 0.

#### Example 4

- **Input:** points = [[1,2,3]], target = [5,5,5]

- **Output:** -1

- **Explanation:** 

- Only one initial point is available, so no new points can be generated.

- Therefore, the target cannot be obtained, and the answer is -1.

### 4. Constraints

- $1 \le \text{points.length} \le 20$

- $\text{points}[i] = [x_{i}, y_{i}, z_{i}]$

- $0 \le x_{i}, y_{i}, z_{i} \le 6$

- $\text{target.length} = 3$

- $0 \le \text{target}[i] \le 6$

- The initial set of points contains no duplicates.
