### 1. Description

You are given an array `routes` representing bus routes where $\text{routes}[i]$ is a bus route that the $$i^{\text{th}}$$ bus repeats forever.

- For example, if $\text{routes}[0] = [1, 5, 7]$, this means that the $0^th$ bus travels in the sequence `1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ...` forever.

You will start at the bus stop `source` (You are not on any bus initially), and you want to go to the bus stop `target`. You can travel between bus stops by buses only.

Return *the least number of buses you must take to travel from *`source`* to *`target`. Return `-1` if it is not possible.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $routes = [[1,2,7],[3,6,7]], source = 1, target = 6$
- **Output:** `2`
- **Explanation:** The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
#### Example 2

- **Input:** $routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12$
- **Output:** `-1`

### 4. Constraints

- $1 \le \text{routes.length} \le 500$.

- $1 \le \text{routes}[i].length \le 10^{5}$

- All the values of $\text{routes}[i]$ are **unique**.

- $sum(\text{routes}[i].length) \le 10^{5}$

- $0 \le \text{routes}[i][j] < 10^{6}$

- $0 \le source, target < 10^{6}$