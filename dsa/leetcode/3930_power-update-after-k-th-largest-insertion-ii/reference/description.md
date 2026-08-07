## Description

You are given an integer array `nums` and an integer `p`.

You are also given a 2D integer array `queries`, where each $\text{queries}[i] = [\text{val}_{i}, k_{i}]$.

For each query:

- Insert $\text{val}_{i}$ into `nums`.

- Let `x` be the $k_{i}^th$ **largest** element in the current `nums`.

- **Update** `p` to $p^x \% (10^{9} + 7)$.

Return an array `ans` where the $\text{ans}[i]$ represents the value of `p` after processing the $$i^{\text{th}}$$ query.
### Function Contract

**Inputs**

- `nums`: The nonempty initial list of positive integer values.
- `p`: The positive initial state used as the base of the first modular power.
- `queries`: A nonempty list of pairs $[\text{val}_{i}, k_{i}]$; each pair inserts $\text{val}_{i}$ and requests the $k_{i}$th largest value after that insertion.

Let $N=\lvert\texttt{nums}\rvert$, $Q=\lvert\texttt{queries}\rvert$, and let $V$ be the largest value appearing initially or as an insertion. For zero-based query index $i$, the current multiset contains $N+i+1$ elements after insertion, and $k_{i}$ is guaranteed to be a valid one-based rank in that multiset. Equal values occupy separate rank positions.

All state updates use the modulus

$M=$10^{9}$+7.$

**Return value**

Return a list of length $Q$. Its entry at index $i$ is the updated `p` after inserting $\text{val}_{i}$, selecting the requested order statistic, and computing the modular power. Processing a query never resets `p` to its original value.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [2], p = 4, queries = [[3,1],[1,2]]

**Output:** [64,4096]

**Explanation:**

<table border="1" bordercolor="#ccc" cellpadding="5" cellspacing="0">
	<thead>
		<tr>
			<th>`i`</th>
			<th>$\text{val}_{i}$</th>
			<th>Current

			`nums`</th>
			<th>$k_{i}$</th>
			<th>$k_{i}^th$

			largest</th>
			<th>p</th>
			<th>New $p = p^k \% (10^{9} + 7)$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>0</td>
			<td>3</td>
			<td>[2, 3]</td>
			<td>1</td>
			<td>3</td>
			<td>4</td>
			<td>$4^{3}$ % ($10^{9}$ + 7) = 64</td>
		</tr>
		<tr>
			<td>1</td>
			<td>1</td>
			<td>[2, 3, 1]</td>
			<td>2</td>
			<td>2</td>
			<td>64</td>
			<td>$64^{2}$ % ($10^{9}$ + 7) = 4096</td>
		</tr>
	</tbody>
</table>

Thus, $ans = [64, 4096]$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [7,5], p = 6, queries = [[4,3],[7,2]]

**Output:** [1296,220296870]

**Explanation:**

<table border="1" bordercolor="#ccc" cellpadding="5" cellspacing="0">
	<thead>
		<tr>
			<th>`i`</th>
			<th>$\text{val}_{i}$</th>
			<th>Current​​​​​​​

			`nums`</th>
			<th>$k_{i}$</th>
			<th>$k_{i}^th$

			largest</th>
			<th>`p`</th>
			<th>New $p = p^k \% (10^{9} + 7)$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>0</td>
			<td>4</td>
			<td>[7, 5, 4]</td>
			<td>3</td>
			<td>4</td>
			<td>6</td>
			<td>$6^{4}$ % ($10^{9}$ + 7) = 1296</td>
		</tr>
		<tr>
			<td>1</td>
			<td>7</td>
			<td>[7, 5, 4, 7]</td>
			<td>2</td>
			<td>7</td>
			<td>1296</td>
			<td>$1296^{7}$ % ($10^{9}$ + 7) = 220296870</td>
		</tr>
	</tbody>
</table>

Thus, $ans = [1296, 220296870]$

</div>
### Constraints

- $1 \le \text{nums.length} \le 2 * 10^{4}$

- $1 \le \text{nums}[i] \le 10^{9}$

- $​​​​​​​1 \le p \le 10^{9}$

- $1 \le \text{queries.length} \le 2 * 10^{4}$

- $^​​​​​​​1 \le \text{val}_{i} \le 10^{9}$

- $1 \le k_{i} \le n + i + 1$​​​​​​​