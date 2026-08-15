### 1. Description

You are given an integer `n` representing the number of nodes in a **directed weighted** graph, numbered from 0 to $n - 1$. This is represented by a 2D integer array `edges`, where $\text{edges}[i] = [u_{i}, v_{i}, w_{i}]$ represents a directed edge from node $u_{i}$ to node $v_{i}$ with weight $w_{i}$.

You are also given a string `labels` of length `n`, where $\text{labels}[i]$ is the character assigned to node `i`, and an integer `k`.

Return the **minimum** **total** edge weight of a path from node 0 to node $n - 1$ such that the concatenation of the labels of the nodes along the path contains **at most** `k` **consecutive** **identical** characters. If no valid path exists, return -1.

### 2. Function Contract

**Inputs**

- `n`: The number of graph nodes, numbered from `0` to $n - 1$.
- `edges`: A list of triples `[u, v, w]`, each representing a directed edge from node `u` to node `v` with positive weight `w`.
- `labels`: A lowercase string of length `n`; $\text{labels}[i]$ is the character assigned to node `i`.
- `k`: The maximum permitted length of any consecutive run of one character in the route's node-label string.

Let $m = \lvert\texttt{edges}\rvert$. The cost of a route is the sum of the weights of all directed edges it takes. The route consisting only of node `0` has cost zero, so when $n = 1$ the answer is `0`.

**Return value**

Return the minimum cost of a valid route from node `0` to node $n - 1$. Return `-1` if no such route exists.

### 3. Examples

#### Example 1

- **Input:** n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1

- **Output:** 3

- **Explanation:** The optimal valid path from node 0 to node 2 is as follows:

- Use $\text{edges}[2] = [0, 2, 3]$ to reach node 2 with a weight $w_{i} = 3$.

The corresponding concatenation of labels is `"ab"`, which satisfies at most $k = 1$ consecutive identical characters. Thus, the answer is 3.

#### Example 2

- **Input:** n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 2

- **Output:** 2

- **Explanation:** The optimal valid path from node 0 to node 2 is as follows:

- Use $\text{edges}[0] = [0, 1, 1]$ to reach node 1 with weight $w_{i} = 1$.

- Use $\text{edges}[1] = [1, 2, 1]$ to reach node 2 with weight $w_{i} = 1$.

The corresponding concatenation of labels is `"aab"`, which satisfies at most $k = 2$ consecutive identical characters. Thus, the answer is 2.

#### Example 3

- **Input:** n = 3, edges = [[0,1,1],[1,2,1]], labels = "aaa", k = 2

- **Output:** -1

- **Explanation:** There is no valid path from node 0 to node 2 that satisfies at most $k = 2$ consecutive identical characters. Thus, the answer is -1.

### 4. Constraints

- $1 \le n = \text{labels.length} \le 5 * 10^{4}$

- $0 \le \text{edges.length} \le 5 * 10^{4}$

- $\text{edges}[i] = [u_{i}, v_{i}, w_{i}]$

- $0 \le u_{i}, v_{i} \le n - 1$

- $u_{i} \neq v_{i}$

- $1 \le w_{i} \le 10^{4}$

- `labels` consists of lowercase English letters

- $1 \le k \le 50$
