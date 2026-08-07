### 1. Description

You are given an integer `n` and an undirected tree rooted at node 0 with `n` nodes numbered from 0 to $n - 1$. This is represented by a 2D array `edges` of length $n - 1$, where $\text{edges}[i] = [u_{i}, v_{i}]$ indicates an edge from node $u_{i}$ to $v_{i}$ .

Each node `i` has an associated cost given by $\text{cost}[i]$, representing the cost to traverse that node.

The **score** of a path is defined as the sum of the costs of all nodes along the path.

Your goal is to make the scores of all **root-to-leaf** paths **equal** by **increasing** the cost of any number of nodes by **any non-negative** amount.

Return the **minimum** number of nodes whose cost must be increased to make all root-to-leaf path scores equal.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** n = 3, edges = [[0,1],[0,2]], cost = [2,1,3]

**Output:** 1

**Explanation:**

![](images/screenshot-2025-05-28-at-134018.png)

There are two root-to-leaf paths:

- Path `0 → 1` has a score of $2 + 1 = 3$.

- Path `0 → 2` has a score of $2 + 3 = 5$.

To make all root-to-leaf path scores equal to 5, increase the cost of node 1 by 2.

Only one node is increased, so the output is 1.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 3, edges = [[0,1],[1,2]], cost = [5,1,4]

**Output:** 0

**Explanation:**

![](images/screenshot-2025-05-28-at-134249.png)

There is only** **one root-to-leaf path:

- Path `0 → 1 → 2` has a score of $5 + 1 + 4 = 10$.

Since only one root-to-leaf path exists, all path costs are trivially equal, and the output is 0.

</div>
#### Example 3

<div class="example-block">
**Input:** n = 5, edges = [[0,4],[0,1],[1,2],[1,3]], cost = [3,4,1,1,7]

**Output:** 1

**Explanation:**

![](images/screenshot-2025-05-28-at-135704.png)

There are three root-to-leaf paths:

- Path `0 → 4` has a score of $3 + 7 = 10$.

- Path `0 → 1 → 2` has a score of $3 + 4 + 1 = 8$.

- Path `0 → 1 → 3` has a score of $3 + 4 + 1 = 8$.

To make all root-to-leaf path scores equal to 10, increase the cost of node 1 by 2. Thus, the output is 1.

</div>

### 4. Constraints

- $2 \le n \le 10^{5}$

- $\text{edges.length} = n - 1$

- $\text{edges}[i] = [u_{i}, v_{i}]$

- $0 \le u_{i}, v_{i} < n$

- $\text{cost.length} = n$

- $1 \le \text{cost}[i] \le 10^{9}$

- The input is generated such that `edges` represents a valid tree.