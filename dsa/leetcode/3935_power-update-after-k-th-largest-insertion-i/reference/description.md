## Description

You are given an integer array `nums` and an integer `p`.

You are also given a 2D integer array `queries`, where each $\text{queries}[i] = [\text{val}_{i}, k_{i}]$ and the difference between **consecutive** $k_{i}$ values is always **less** than 10.

For each query:

- Insert $\text{val}_{i}$ into `nums`.

- Let `x` be the $k_{i}^th$ **largest** element in the current `nums`.

- **Update** `p` to $p^x \% (10^{9} + 7)$.

Return an array `ans` where the $\text{ans}[i]$ represents the value of `p` after processing the $$i^{\text{th}}$$ query.
### Function Contract

**Inputs**

- `nums`: The nonempty initial multiset, represented as an integer array.
- `p`: The initial positive integer state.
- `queries`: An ordered array whose element `i` is $[\text{val}_{i}, k_{i}]$, giving the value to insert and the requested largest rank after that insertion.

Let $N$ be the initial length, $Q$ the query count, and $V$ the maximum inserted or initial array value. The insertion for query `i` happens before rank $k_{i}$ is selected. Duplicate values occupy separate ranks. Every query's rank is valid for the current length, and adjacent ranks obey $\lvert k_i-k_{i-1}\rvert<10$ for $i>0$.

**Return value**

Return an array of length $Q$ whose element `i` is the updated `p` after query `i` has been processed.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [2], p = 4, queries = [[3,1],[1,2]]

**Output:** [64,4096]

**Explanation:**

<table border="1" bordercolor="#ccc" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
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

<div class="example-block">
<table border="1" bordercolor="#ccc" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
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
</div>
### Constraints

- $1 \le \text{nums.length} \le 2 × 10^{4}$

- $1 \le \text{nums}[i] \le 10^{6}$

- $​​​​​​​1 \le p \le 10^{6}$

- $1 \le \text{queries.length} \le 2 × 10^{4}$

- $^​​​​​​​1 \le \text{val}_{i} \le 10^{6}$

- $1 \le k_{i} \le n + i + 1$

- $|k_{i} - k_{i} - 1| < 10$ for `i > 0`