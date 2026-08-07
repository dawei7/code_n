## Description

You are given an integer `n` and an undirected tree rooted at node 0 with `n` nodes numbered from 0 to $n - 1$. This is represented by a 2D array `edges` of length $n - 1$, where $\text{edges}[i] = [u_{i}, v_{i}]$ indicates an undirected edge between nodes $u_{i}$ and $v_{i}$.

You are also given an integer array `nums`, where $\text{nums}[i]$ is the positive integer assigned to node `i`.

Define a value $t_{i}$ as the number of **ancestors** of node `i` such that the product $\text{nums}[i] * \text{nums}[ancestor]$ is a **perfect square**.

Return the sum of all $t_{i}$ values for all nodes `i` in range `[1, n - 1]`.

**Note**:

- In a rooted tree, the **ancestors** of node `i` are all nodes on the path from node `i` to the root node 0, **excluding** `i` itself.
### Function Contract

**Inputs**

- `n`: The number of nodes in the rooted tree.
- `edges`: The `n - 1` undirected edges of the valid tree.
- `nums`: The positive value assigned to each node, in node-index order.

The undirected edges are interpreted after rooting the tree at node `0`. For node `i` and one of its ancestors `a`, the pair contributes exactly when `nums[i] * nums[a]` is a perfect square.

**Return value**

Return the total number of qualifying ordered descendant-ancestor pairs. Node `0` contributes no $t_i$ term because it has no ancestor.

### Examples
#### Example 1

<div class="example-block">
**Input:** n = 3, edges = [[0,1],[1,2]], nums = [2,8,2]

**Output:** 3

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`**i**`</th>
			<th style="border: 1px solid black;">**Ancestors**</th>
			<th style="border: 1px solid black;">$**\text{nums}[i] * \text{nums}[ancestor]**$</th>
			<th style="border: 1px solid black;">Square Check</th>
			<th style="border: 1px solid black;">$**t_{i}**$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[0]</td>
			<td style="border: 1px solid black;">$\text{nums}[1] * \text{nums}[0] = 8 * 2 = 16$</td>
			<td style="border: 1px solid black;">16 is a perfect square</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[1, 0]</td>
			<td style="border: 1px solid black;">$\text{nums}[2] * \text{nums}[1] = 2 * 8 = 16$

			$\text{nums}[2] * \text{nums}[0] = 2 * 2 = 4$</td>
			<td style="border: 1px solid black;">Both 4 and 16 are perfect squares</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
	</tbody>
</table>

Thus, the total number of valid ancestor pairs across all non-root nodes is $1 + 2 = 3$.

</div>
#### Example 2

<div class="example-block">
**Input:** n = 3, edges = [[0,1],[0,2]], nums = [1,2,4]

**Output:** 1

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`**i**`</th>
			<th style="border: 1px solid black;">**Ancestors**</th>
			<th style="border: 1px solid black;">$**\text{nums}[i] * \text{nums}[ancestor]**$</th>
			<th style="border: 1px solid black;">Square Check</th>
			<th style="border: 1px solid black;">$**t_{i}**$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[0]</td>
			<td style="border: 1px solid black;">$\text{nums}[1] * \text{nums}[0] = 2 * 1 = 2$</td>
			<td style="border: 1px solid black;">2 is **not** a perfect square</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[0]</td>
			<td style="border: 1px solid black;">$\text{nums}[2] * \text{nums}[0] = 4 * 1 = 4$</td>
			<td style="border: 1px solid black;">4 is a perfect square</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>

Thus, the total number of valid ancestor pairs across all non-root nodes is 1.

</div>
#### Example 3

<div class="example-block">
**Input:** n = 4, edges = [[0,1],[0,2],[1,3]], nums = [1,2,9,4]

**Output:** 2

**Explanation:**

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">**Ancestors**</th>
			<th style="border: 1px solid black;">$**\text{nums}[i] * \text{nums}[ancestor]**$</th>
			<th style="border: 1px solid black;">Square Check</th>
			<th style="border: 1px solid black;">$**t_{i}**$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">[0]</td>
			<td style="border: 1px solid black;">$\text{nums}[1] * \text{nums}[0] = 2 * 1 = 2$</td>
			<td style="border: 1px solid black;">2 is **not** a perfect square</td>
			<td style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">[0]</td>
			<td style="border: 1px solid black;">$\text{nums}[2] * \text{nums}[0] = 9 * 1 = 9$</td>
			<td style="border: 1px solid black;">9 is a perfect square</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">[1, 0]</td>
			<td style="border: 1px solid black;">$\text{nums}[3] * \text{nums}[1] = 4 * 2 = 8$

			$\text{nums}[3] * \text{nums}[0] = 4 * 1 = 4$</td>
			<td style="border: 1px solid black;">Only 4 is a perfect square</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>

Thus, the total number of valid ancestor pairs across all non-root nodes is $0 + 1 + 1 = 2$.

</div>
### Constraints

- $1 \le n \le 10^{5}$

- $\text{edges.length} = n - 1$

- $\text{edges}[i] = [u_{i}, v_{i}]$

- $0 \le u_{i}, v_{i} \le n - 1$

- $\text{nums.length} = n$

- $1 \le \text{nums}[i] \le 10^{5}$

- The input is generated such that `edges` represents a valid tree.