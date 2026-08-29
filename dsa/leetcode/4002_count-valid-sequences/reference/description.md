### 1. Description

You are given two **positive** integers `n` and `k`.

A **valid sequence** is a sequence of `k` positive integers such that:

- The **sum** of all integers in the sequence is equal to `n`.

- The **product** of all integers in the sequence is **even**.

Return the number of valid sequences. Since the answer may be very large, return it **modulo** $10^{9} + 7$.

Two sequences are considered **different** if they differ at any index. For example, `[1, 1, 2]` and `[1, 2, 1]` are considered different sequences.

### 2. Function Contract

**Inputs**

- `n`: The required sum of the sequence.
- `k`: The exact number of positive integers in the sequence.

A candidate sequence $(a_1,a_2,\ldots,a_k)$ is valid when every $a_i$ is positive,

$\sum_{i=1}^{k} a_i=n,$

and $\prod_{i=1}^{k}a_i$ is even.

**Return value**

Return the number of distinct valid ordered sequences, reduced modulo $10^9+7$.

### 3. Examples

#### Example 1

- **Input:** n = 5, k = 3

- **Output:** 3

- **Explanation:** The sequences of length $k = 3$ whose sum is 5 are:

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Sequence</th>
			<th style="border: 1px solid black;">Product</th>
			<th style="border: 1px solid black;">Parity</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[1, 1, 3]`</td>
			<td style="border: 1px solid black;">$1 * 1 * 3 = 3$</td>
			<td style="border: 1px solid black;">Odd</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[1, 2, 2]`</td>
			<td style="border: 1px solid black;">$1 * 2 * 2 = 4$</td>
			<td style="border: 1px solid black;">Even</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[2, 1, 2]`</td>
			<td style="border: 1px solid black;">$2 * 1 * 2 = 4$</td>
			<td style="border: 1px solid black;">Even</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[2, 2, 1]`</td>
			<td style="border: 1px solid black;">$2 * 2 * 1 = 4$</td>
			<td style="border: 1px solid black;">Even</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[1, 3, 1]`</td>
			<td style="border: 1px solid black;">$1 * 3 * 1 = 3$</td>
			<td style="border: 1px solid black;">Odd</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[3, 1, 1]`</td>
			<td style="border: 1px solid black;">$3 * 1 * 1 = 3$</td>
			<td style="border: 1px solid black;">Odd</td>
		</tr>
	</tbody>
</table>

There are 3 sequences with an even product, thus the answer is 3.

#### Example 2

- **Input:** n = 3, k = 2

- **Output:** 2

- **Explanation:** The sequences of length $k = 2$ whose sum is 3 are:

<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Sequence</th>
			<th style="border: 1px solid black;">Product</th>
			<th style="border: 1px solid black;">Parity</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[1, 2]`</td>
			<td style="border: 1px solid black;">$1 * 2 = 2$</td>
			<td style="border: 1px solid black;">Even</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">`[2, 1]`</td>
			<td style="border: 1px solid black;">$2 * 1 = 2$</td>
			<td style="border: 1px solid black;">Even</td>
		</tr>
	</tbody>
</table>

There are 2 sequences with an even product, thus the answer is 2.

#### Example 3

- **Input:** n = 5, k = 5

- **Output:** 0

- **Explanation:** The only possible sequence of length $k = 5$ whose sum is 5 is `[1, 1, 1, 1, 1]`, which has an odd product. Thus, the answer is 0.

### 4. Constraints

- $1 \le n \le 5 * 10^{5}$

- $1 \le k \le n$
