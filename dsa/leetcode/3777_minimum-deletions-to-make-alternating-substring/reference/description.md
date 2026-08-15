### 1. Description

You are given a string `s` of length `n` consisting only of the characters `'A'` and `'B'`.

You are also given a 2D integer array `queries` of length `q`, where each $\text{queries}[i]$ is one of the following:

- `[1, j]`: **Flip** the character at index `j` of `s` i.e. `'A'` changes to `'B'` (and vice versa). This operation mutates `s` and affects subsequent queries.

- `[2, l, r]`: **Compute** the **minimum** number of character deletions required to make the **substring** `s[l..r]` **alternating**. This operation does not modify `s`; the length of `s` remains `n`.

A **substring** is **alternating** if no two **adjacent** characters are **equal**. A substring of length 1 is always alternating.

Return an integer array `answer`, where $\text{answer}[i]$ is the result of the $$i^{\text{th}}$$ query of type `[2, l, r]`.

### 2. Function Contract

**Inputs**

- `s`: A nonempty binary-alphabet string containing only `'A'` and `'B'`.
- `queries`: A nonempty sequence of flip queries `[1, j]` and range queries `[2, l, r]`.

Let $N=\lvert s\rvert$ and $Q=\lvert\texttt{queries}\rvert$. All indices are zero-based, and both endpoints of `s[l..r]` are included. Queries are stateful: each flip affects all queries that follow it.

**Return value**

Return one integer for each type-2 query, in the same relative order as those queries. Each integer is the fewest deletions needed to leave an alternating subsequence of the requested current substring.

### 3. Examples

#### Example 1

- **Input:** s = "ABA", queries = [[2,1,2],[1,1],[2,0,2]]

- **Output:** [0,2]

- **Explanation:** <table style="border: 1px solid black;">
	<thead>
		<tr>
			<th align="center" style="border: 1px solid black;">`**i**`</th>
			<th align="center" style="border: 1px solid black;">$**\text{queries}[i]**$</th>
			<th align="center" style="border: 1px solid black;">`**j**`</th>
			<th align="center" style="border: 1px solid black;">`**l**`</th>
			<th align="center" style="border: 1px solid black;">`**r**`</th>
			<th align="center" style="border: 1px solid black;">**`s` before query**</th>
			<th align="center" style="border: 1px solid black;">`**s[l..r]**`</th>
			<th align="center" style="border: 1px solid black;">**Result**</th>
			<th align="center" style="border: 1px solid black;">**Answer**</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">[2, 1, 2]</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">`"ABA"`</td>
			<td align="center" style="border: 1px solid black;">`"BA"`</td>
			<td align="center" style="border: 1px solid black;">Already alternating</td>
			<td align="center" style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">[1, 1]</td>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">`"ABA"`</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">Flip $s[1]$ from `'B'` to `'A'`</td>
			<td align="center" style="border: 1px solid black;">-</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">[2, 0, 2]</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">`"AAA"`</td>
			<td align="center" style="border: 1px solid black;">`"AAA"`</td>
			<td align="center" style="border: 1px solid black;">Delete any two `'A'`s to get `"A"`</td>
			<td align="center" style="border: 1px solid black;">2</td>
		</tr>
	</tbody>
</table>

Thus, the answer is `[0, 2]`.

#### Example 2

- **Input:** s = "ABB", queries = [[2,0,2],[1,2],[2,0,2]]

- **Output:** [1,0]

- **Explanation:** <table style="border: 1px solid black;">
	<thead>
		<tr>
			<th align="center" style="border: 1px solid black;">`**i**`</th>
			<th align="center" style="border: 1px solid black;">$**\text{queries}[i]**$</th>
			<th align="center" style="border: 1px solid black;">`**j**`</th>
			<th align="center" style="border: 1px solid black;">`**l**`</th>
			<th align="center" style="border: 1px solid black;">`**r**`</th>
			<th align="center" style="border: 1px solid black;">**`s` before query**</th>
			<th align="center" style="border: 1px solid black;">`**s[l..r]**`</th>
			<th align="center" style="border: 1px solid black;">**Result**</th>
			<th align="center" style="border: 1px solid black;">**Answer**</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">[2, 0, 2]</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">`"ABB"`</td>
			<td align="center" style="border: 1px solid black;">`"ABB"`</td>
			<td align="center" style="border: 1px solid black;">Delete one `'B'` to get `"AB"`</td>
			<td align="center" style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">[1, 2]</td>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">`"ABB"`</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">Flip $s[2]$ from `'B'` to `'A'`</td>
			<td align="center" style="border: 1px solid black;">-</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">[2, 0, 2]</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">`"ABA"`</td>
			<td align="center" style="border: 1px solid black;">`"ABA"`</td>
			<td align="center" style="border: 1px solid black;">Already alternating</td>
			<td align="center" style="border: 1px solid black;">0</td>
		</tr>
	</tbody>
</table>

Thus, the answer is `[1, 0]`.

#### Example 3

- **Input:** s = "BABA", queries = [[2,0,3],[1,1],[2,1,3]]

- **Output:** [0,1]

- **Explanation:** <table style="border: 1px solid black;">
	<thead>
		<tr>
			<th align="center" style="border: 1px solid black;">`**i**`</th>
			<th align="center" style="border: 1px solid black;">$**\text{queries}[i]**$</th>
			<th align="center" style="border: 1px solid black;">`**j**`</th>
			<th align="center" style="border: 1px solid black;">`**l**`</th>
			<th align="center" style="border: 1px solid black;">`**r**`</th>
			<th align="center" style="border: 1px solid black;">**`s` before query**</th>
			<th align="center" style="border: 1px solid black;">`**s[l..r]**`</th>
			<th align="center" style="border: 1px solid black;">**Result**</th>
			<th align="center" style="border: 1px solid black;">**Answer**</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">[2, 0, 3]</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">0</td>
			<td align="center" style="border: 1px solid black;">3</td>
			<td align="center" style="border: 1px solid black;">`"BABA"`</td>
			<td align="center" style="border: 1px solid black;">`"BABA"`</td>
			<td align="center" style="border: 1px solid black;">Already alternating</td>
			<td align="center" style="border: 1px solid black;">0</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">[1, 1]</td>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">`"BABA"`</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">Flip $s[1]$ from `'A'` to `'B'`</td>
			<td align="center" style="border: 1px solid black;">-</td>
		</tr>
		<tr>
			<td align="center" style="border: 1px solid black;">2</td>
			<td align="center" style="border: 1px solid black;">[2, 1, 3]</td>
			<td align="center" style="border: 1px solid black;">-</td>
			<td align="center" style="border: 1px solid black;">1</td>
			<td align="center" style="border: 1px solid black;">3</td>
			<td align="center" style="border: 1px solid black;">`"BBBA"`</td>
			<td align="center" style="border: 1px solid black;">`"BBA"`</td>
			<td align="center" style="border: 1px solid black;">Delete one `'B'` to get `"BA"`</td>
			<td align="center" style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>

Thus, the answer is `[0, 1]`.

### 4. Constraints

- $1 \le n = \text{s.length} \le 10^{5}$

- $s[i]$ is either `'A'` or `'B'`.

- $1 \le q = \text{queries.length} \le 10^{5}$

- $\text{queries}[i].length = 2$ or `3`

		- $\text{queries}[i] = [1, j]$ or,

- $\text{queries}[i] = [2, l, r]$

- $0 \le j \le n - 1$

- $0 \le l \le r \le n - 1$
