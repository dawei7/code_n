### 1. Description

You are given an integer array `nums`, and an integer `k`.

Start with an initial value $val = 1$ and process `nums` from left to right. At each index `i`, you must choose **exactly one** of the following actions:

- Multiply `val` by $\text{nums}[i]$.

- Divide `val` by $\text{nums}[i]$.

- Leave `val` unchanged.

After processing all elements, `val` is considered **equal** to `k` only if its final rational value **exactly** equals `k`.

Return the count of **distinct** sequences of choices that result in $val = k$.

### 2. Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers, processed once in its given left-to-right order.
- `k`: The positive integer that the final exact rational value must equal.

Every index contributes one of three distinct choices: multiplication, division, or no change. Two sequences are distinct when they choose different actions at any index, even if those actions happen to produce the same value, as multiplication and division by `1` do.

Let $N=\lvert\texttt{nums}\rvert$. Represent a reachable rational value by its signed exponents of the only possible prime factors $2$, $3$, and $5$. Let $S$ be the maximum number of distinct exponent triples reachable after any processed prefix.

**Return value**

Return the number of distinct length-$N$ action sequences whose final rational value is exactly `k`.

### 3. Note

Division is rational (exact), not integer division. For example, $2 / 4 = 1 / 2$.

### 4. Examples

#### Example 1

- **Input:** nums = [2,3,2], k = 6

- **Output:** 2

- **Explanation:** The following 2 distinct sequences of choices result in $val = k$:

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Sequence</th>
			<th style="border: 1px solid black;">Operation on $\text{nums}[0]$</th>
			<th style="border: 1px solid black;">Operation on $\text{nums}[1]$</th>
			<th style="border: 1px solid black;">Operation on $\text{nums}[2]$</th>
			<th style="border: 1px solid black;">Final `val`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">Multiply: $val = 1 * 2 = 2$</td>
			<td style="border: 1px solid black;">Multiply: $val = 2 * 3 = 6$</td>
			<td style="border: 1px solid black;">Leave `val` unchanged</td>
			<td style="border: 1px solid black;">6</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">Leave `val` unchanged</td>
			<td style="border: 1px solid black;">Multiply: $val = 1 * 3 = 3$</td>
			<td style="border: 1px solid black;">Multiply: $val = 3 * 2 = 6$</td>
			<td style="border: 1px solid black;">6</td>
		</tr>
	</tbody>
</table>

#### Example 2

- **Input:** nums = [4,6,3], k = 2

- **Output:** 2

- **Explanation:** The following 2 distinct sequences of choices result in $val = k$:

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Sequence</th>
			<th style="border: 1px solid black;">Operation on $\text{nums}[0]$</th>
			<th style="border: 1px solid black;">Operation on $\text{nums}[1]$</th>
			<th style="border: 1px solid black;">Operation on $\text{nums}[2]$</th>
			<th style="border: 1px solid black;">Final `val`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">Multiply: $val = 1 * 4 = 4$</td>
			<td style="border: 1px solid black;">Divide: $val = 4 / 6 = 2 / 3$</td>
			<td style="border: 1px solid black;">Multiply: $val = (2 / 3) * 3 = 2$</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">Leave `val` unchanged</td>
			<td style="border: 1px solid black;">Multiply: $val = 1 * 6 = 6$</td>
			<td style="border: 1px solid black;">Divide: $val = 6 / 3 = 2$</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
	</tbody>
</table>

#### Example 3

- **Input:** nums = [1,5], k = 1

- **Output:** 3

- **Explanation:** The following 3 distinct sequences of choices result in $val = k$:

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">Sequence</th>
			<th style="border: 1px solid black;">Operation on $\text{nums}[0]$</th>
			<th style="border: 1px solid black;">Operation on $\text{nums}[1]$</th>
			<th style="border: 1px solid black;">Final `val`</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">Multiply: $val = 1 * 1 = 1$</td>
			<td style="border: 1px solid black;">Leave `val` unchanged</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">Divide: $val = 1 / 1 = 1$</td>
			<td style="border: 1px solid black;">Leave `val` unchanged</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">Leave `val` unchanged</td>
			<td style="border: 1px solid black;">Leave `val` unchanged</td>
			<td style="border: 1px solid black;">1</td>
		</tr>
	</tbody>
</table>

### 5. Constraints

- $1 \le \text{nums.length} \le 19$

- $1 \le \text{nums}[i] \le 6$

- $1 \le k \le 10^{15}$
