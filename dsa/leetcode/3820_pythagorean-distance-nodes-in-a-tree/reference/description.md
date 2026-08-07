### 1. Description

You are given an integer `n` and an undirected tree with `n` nodes numbered from 0 to $n - 1$. The tree is represented by a 2D array `edges` of length $n - 1$, where $\text{edges}[i] = [u_{i}, v_{i}]$ indicates an undirected edge between $u_{i}$ and $v_{i}$.

You are also given three **distinct** target nodes `x`, `y`, and `z`.

For any node `u` in the tree:

- Let `dx` be the distance from `u` to node `x`

- Let `dy` be the distance from `u` to node `y`

- Let `dz` be the distance from `u` to node `z`

The node `u` is called **special** if the three distances form a **Pythagorean Triplet**.

Return an integer denoting the number of special nodes in the tree.

A **Pythagorean triplet** consists of three integers `a`, `b`, and `c` which, when sorted in **ascending** order, satisfy $a^{2} + b^{2} = c^{2}$.

The **distance** between two nodes in a tree is the number of edges on the unique path between them.

### 2. Function Contract

**Inputs**

- `n`: The number of nodes in the tree.
- `edges`: The $n - 1$ undirected edges, each represented by a two-element array $[u_{i}, v_{i}]$.
- `x`: The first target node.
- `y`: The second target node.
- `z`: The third target node.

The nodes are labeled from `0` through $n - 1$. The edge list forms one valid tree, and `x`, `y`, and `z` are pairwise distinct.

For any node, compute its three edge-count distances to the targets. After arranging those distances as $a\le b\le c$, the node qualifies exactly when $a^2+b^2=c^2$. A distance may be zero; the definition does not require a positive Pythagorean triplet.

**Return value**

Return the number of nodes whose three target distances satisfy the Pythagorean equation.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** n = 4, edges = [[0,1],[0,2],[0,3]], x = 1, y = 2, z = 3

**Output:** 3

**Explanation:**

For each node, we compute its distances to nodes $x = 1$, $y = 2$, and $z = 3$.

- Node 0 has distances 1, 1, and 1. After sorting, the distances are 1, 1, and 1, which do not satisfy the Pythagorean condition.

- Node 1 has distances 0, 2, and 2. After sorting, the distances are 0, 2, and 2. Since $0^{2} + 2^{2} = 2^{2}$, node 1 is special.

- Node 2 has distances 2, 0, and 2. After sorting, the distances are 0, 2, and 2. Since $0^{2} + 2^{2} = 2^{2}$, node 2 is special.

- Node 3 has distances 2, 2, and 0. After sorting, the distances are 0, 2, and 2. This also satisfies the Pythagorean condition.

Therefore, nodes 1, 2, and 3 are special, and the answer is 3.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 4, edges = [[0,1],[1,2],[2,3]], x = 0, y = 3, z = 2

**Output:** 0

**Explanation:**

For each node, we compute its distances to nodes $x = 0$, $y = 3$, and $z = 2$.

- Node 0 has distances 0, 3, and 2. After sorting, the distances are 0, 2, and 3, which do not satisfy the Pythagorean condition.

- Node 1 has distances 1, 2, and 1. After sorting, the distances are 1, 1, and 2, which do not satisfy the Pythagorean condition.

- Node 2 has distances 2, 1, and 0. After sorting, the distances are 0, 1, and 2, which do not satisfy the Pythagorean condition.

- Node 3 has distances 3, 0, and 1. After sorting, the distances are 0, 1, and 3, which do not satisfy the Pythagorean condition.

No node satisfies the Pythagorean condition. Therefore, the answer is 0.

</div>
#### Example 3

<div class="example-block">
**Input:** n = 4, edges = [[0,1],[1,2],[1,3]], x = 1, y = 3, z = 0

**Output:** 1

**Explanation:**

For each node, we compute its distances to nodes $x = 1$, $y = 3$, and $z = 0$.

- Node 0 has distances 1, 2, and 0. After sorting, the distances are 0, 1, and 2, which do not satisfy the Pythagorean condition.

- Node 1 has distances 0, 1, and 1. After sorting, the distances are 0, 1, and 1. Since $0^{2} + 1^{2} = 1^{2}$, node 1 is special.

- Node 2 has distances 1, 2, and 2. After sorting, the distances are 1, 2, and 2, which do not satisfy the Pythagorean condition.

- Node 3 has distances 1, 0, and 2. After sorting, the distances are 0, 1, and 2, which do not satisfy the Pythagorean condition.

Therefore, the answer is 1.

</div>

### 4. Constraints

- $4 \le n \le 10^{5}$

- $\text{edges.length} = n - 1$

- $\text{edges}[i] = [u_{i}, v_{i}]$

- $0 \le u_{i}, v_{i}, x, y, z \le n - 1$

- `x`, `y`, and `z` are pairwise **distinct**.

- The input is generated such that `edges` represent a valid tree.