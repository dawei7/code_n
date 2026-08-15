### 1. Description

On a campus represented as a 2D grid, there are `n` workers and `m` bikes, with $n \le m$. Each worker and bike is a 2D coordinate on this grid.

We assign one unique bike to each worker so that the sum of the **Manhattan distances** between each worker and their assigned bike is minimized.

Return *the minimum possible sum of Manhattan distances between each worker and their assigned bike*.

The **Manhattan distance** between two points `p1` and `p2` is $Manhattan(p1, p2) = |\text{p1.x} - \text{p2.x}| + |\text{p1.y} - \text{p2.y}|$.

### 2. Function Contract

**Inputs**

- `workers`: a non-empty array of two-coordinate worker locations.
- `bikes`: a non-empty array of two-coordinate bike locations.

Let $n=\lvert\texttt{workers}\rvert$ and $m=\lvert\texttt{bikes}\rvert$. The input guarantees $n \le m$, so every worker can receive a different bike. Coordinate pairs and array indices remain distinct concepts: the worker or bike index identifies an entity, while its pair identifies the entity's grid location.

**Return value**

- The minimum sum of Manhattan distances obtained by assigning a distinct bike to every worker.

### 3. Examples

#### Example 1

![](images/1261_example_1_v2.png)

- **Input:** $workers = [[0,0],[2,1]], bikes = [[1,2],[3,3]]$
- **Output:** `6`
- **Explanation:** We assign bike 0 to worker 0, bike 1 to worker 1. The Manhattan distance of both assignments is 3, so the output is 6.

#### Example 2

![](images/1261_example_2_v2.png)

- **Input:** $workers = [[0,0],[1,1],[2,0]], bikes = [[1,0],[2,2],[2,1]]$
- **Output:** `4`
- **Explanation:** We first assign bike 0 to worker 0, then assign bike 1 to worker 1 or worker 2, bike 2 to worker 2 or worker 1. Both assignments lead to sum of the Manhattan distances as 4.

#### Example 3

- **Input:** $workers = [[0,0],[1,0],[2,0],[3,0],[4,0]], bikes = [[0,999],[1,999],[2,999],[3,999],[4,999]]$
- **Output:** `4995`

### 4. Constraints

- $n = \text{workers.length}$

- $m = \text{bikes.length}$

- $1 \le n \le m \le 10$

- $\text{workers}[i].length = 2$

- $\text{bikes}[i].length = 2$

- $0 \le \text{workers}[i][0], \text{workers}[i][1], \text{bikes}[i][0], \text{bikes}[i][1] < 1000$

- All the workers and the bikes locations are **unique**.
