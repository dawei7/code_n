### 1. Description

You are given an undirected tree rooted at node 0 with `n` nodes numbered from 0 to $n - 1$, represented by an array `parent` where $\text{parent}[i]$ is the parent of node `i`.

Each node `i` has three types of gates, given in a 2D array `gates` where $\text{gates}[i] = [\text{red}_{i}, \text{blue}_{i}, \text{white}_{i}]$ which represents the number of **red**, **blue**, and **white** gates at node `i`.

- **Red** gate: usable only with a **red** card.

- **Blue** gate: usable only with a **blue** card.

- **White** gate: usable with **either** card, but **flips** the card color when used.

Alice and Bob start at given nodes with either a red or blue card (`1` = red, `0` = blue). They must **independently** move **upward** to their **lowest common ancestor (LCA)**.

At each node, a person may move to their parent **only if** they can use **at least** one gate at that node with their current card. **White** gates may be used any number of times to flip the card color.

**Movement rules (one move = from `u` to $\text{parent}[u]$):**

- Movement is only upward toward the root.

- At node `u`, pick **exactly** one specific gate instance. Identical gates are treated as **separate** and counted individually.

- If holding a **red** card: use a red gate to remain red, or a white gate to **change** to blue.

- If holding a **blue** card: use a blue gate to remain blue, or a white gate to **change** to red.

- If no usable gate exists at `u`, the sequence ends.

You are also given a 2D array `queries` where $\text{queries}[i] = [\text{aNode}_{i}, \text{aCard}_{i}, \text{bNode}_{i}, \text{bCard}_{i}]$:

- $\text{aNode}_{i}$, $\text{aCard}_{i}$: Alice's starting node and card.

- $\text{bNode}_{i}$, $\text{bCard}_{i}$: Bob's starting node and card.

For each query, count the number of **distinct** valid ways **modulo** $10^{9} + 7$ for both to reach their **LCA**.

After computing the result for all queries, return the **bitwise XOR** of those values.

### 2. Function Contract

`solve(n, parent, gates, queries) -> int`

**Inputs**

- `n`: The number of nodes in the rooted tree.
- `parent`: An array describing each node's parent; the root uses $\text{parent}[0] = -1$.
- `gates`: For each node, `[red, blue, white]` gives the number of separate gate instances of each color.
- `queries`: Query quadruples `[alice_node, alice_card, bob_node, bob_card]`, where card `0` is blue and card `1` is red.

Let $q = \lvert\texttt{queries}\rvert$. The arrays describe one valid tree, and every query node is a valid node index.

**Output**

Return one integer: the bitwise XOR of the $q$ per-query joint route counts after each count has been reduced modulo $10^9 + 7$.

For one query, Alice's and Bob's route counts are independent and are multiplied modulo $10^9 + 7$. A zero-length route from a starting node already equal to the LCA has count one.

### 3. Note

- Two ways are distinct if the set of gates used **differs** for either Alice or Bob.

- If any person is already at the **LCA**, then the number of ways for them is 1.

- The **lowest common ancestor (LCA)** is defined between two nodes `a` and `b` as the lowest node in a tree that has both `a` and `b` as descendants (where a node is allowed to be a descendant of itself).

### 4. Examples

#### Example 1

- **Input:** n = 3, parent = [-1,0,0], gates = [[1,0,1],[0,1,1],[1,1,0]], queries = [[1,0,2,0],[1,1,2,0],[1,0,2,1]]

- **Output:** 1

- **Explanation:** <table border="1" bordercolor="#ccc" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
	<thead>
		<tr>
			<th align="center">`i`</th>
			<th align="center">Alice

			[Node, Card]</th>
			<th align="center">Bob

			[Node, Card]</th>
			<th align="center">LCA</th>
			<th align="center">Alice

			Path</th>
			<th align="center">Bob

			Path</th>
			<th align="center">Alice Ways</th>
			<th align="center">Bob Ways</th>
			<th align="center">Total Ways</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center">0</td>
			<td align="center">[1, 0]: Blue</td>
			<td align="center">[2, 0]: Blue</td>
			<td align="center">0</td>
			<td align="center">1 → 0</td>
			<td align="center">2 → 0</td>
			<td align="center">2 (1 Blue + 1 White at node 1)</td>
			<td align="center">1 (1 Blue at node 2)</td>
			<td align="center">2 × 1 = 2</td>
		</tr>
		<tr>
			<td align="center">1</td>
			<td align="center">[1, 1]: Red</td>
			<td align="center">[2, 0]: Blue</td>
			<td align="center">0</td>
			<td align="center">1 → 0</td>
			<td align="center">2 → 0</td>
			<td align="center">1 (1 White at node 1)</td>
			<td align="center">1 (1 Blue at node 2)</td>
			<td align="center">1 × 1 = 1</td>
		</tr>
		<tr>
			<td align="center">2</td>
			<td align="center">[1, 0]: Blue</td>
			<td align="center">[2, 1]: Red</td>
			<td align="center">0</td>
			<td align="center">1 → 0</td>
			<td align="center">2 → 0</td>
			<td align="center">2 (1 Blue + 1 White at node 1)</td>
			<td align="center">1 (1 Red at node 2)</td>
			<td align="center">2 × 1 = 2</td>
		</tr>
	</tbody>
</table>

Thus, the XOR of all values: $2 XOR 1 XOR 2 = 1$.

#### Example 2

- **Input:** n = 3, parent = [-1,0,1], gates = [[0,1,2],[1,0,1],[0,0,3]], queries = [[2,0,1,0],[2,1,0,0],[1,1,2,1]]

- **Output:** 3

- **Explanation:** <table border="1" bordercolor="#ccc" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
	<thead>
		<tr>
			<th align="center">`i`</th>
			<th align="center">Alice

			[Node, Card]</th>
			<th align="center">Bob

			[Node, Card]</th>
			<th align="center">LCA</th>
			<th align="center">Alice Path</th>
			<th align="center">Bob Path</th>
			<th align="center">Alice Ways</th>
			<th align="center">Bob Ways</th>
			<th align="center">Total Ways</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center">0</td>
			<td align="center">[2, 0]: Blue</td>
			<td align="center">[1, 0]: Blue</td>
			<td align="center">1</td>
			<td align="center">2 → 1</td>
			<td align="center">1</td>
			<td align="center">3 (3 White at node 2)</td>
			<td align="center">1 (no move)</td>
			<td align="center">3 × 1 = 3</td>
		</tr>
		<tr>
			<td align="center">1</td>
			<td align="center">[2, 1]: Red</td>
			<td align="center">[0, 0]: Blue</td>
			<td align="center">0</td>
			<td align="center">2 → 1 → 0</td>
			<td align="center">0</td>
			<td align="center">3 (3 White at node 2) × 1 (1 White at node 1) = 3</td>
			<td align="center">1 (no move)</td>
			<td align="center">3 × 1 = 3</td>
		</tr>
		<tr>
			<td align="center">2</td>
			<td align="center">[1, 1]: Red</td>
			<td align="center">[2, 1]: Red</td>
			<td align="center">1</td>
			<td align="center">1</td>
			<td align="center">2 → 1</td>
			<td align="center">1 (no move)</td>
			<td align="center">3 (3 White at node 2)</td>
			<td align="center">1 × 3 = 3</td>
		</tr>
	</tbody>
</table>

Thus, the XOR of all values: $3 XOR 3 XOR 3 = 3$.

### 5. Constraints



- $2 \le n \le 2 * 10^{4}$

- $n = \text{parent.length} = \text{gates.length}$

- $\text{parent}[0] = -1$

- $0 \le \text{parent}[i] < n$ for `i` in `[1, n - 1]`

- $\text{gates}[i] = [\text{red}_{i}, \text{blue}_{i}, \text{white}_{i}]$

- $0 \le \text{red}_{i}, \text{blue}_{i}, \text{white}_{i} \le 10$

- $1 \le \text{queries.length} \le 2 * 10^{4}$

- $\text{queries}[i] = [\text{aNode}_{i}, \text{aCard}_{i}, \text{bNode}_{i}, \text{bCard}_{i}]$

- $0 \le \text{aNode}_{i}, \text{bNode}_{i} \le n - 1$

- $0 \le \text{aCard}_{i}, \text{bCard}_{i} \le 1$

- The input is generated such that the array `parent` represents a valid tree.
