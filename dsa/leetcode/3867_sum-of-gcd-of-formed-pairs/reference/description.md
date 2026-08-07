## Description

You are given an integer array `nums` of length `n`.

Construct an array `prefixGcd` where for each index `i`:

- Let $\text{mx}_{i} = max(\text{nums}[0], \text{nums}[1], ..., \text{nums}[i])$.

- $\text{prefixGcd}[i] = gcd(\text{nums}[i], \text{mx}_{i})$.

After constructing `prefixGcd`:

- Sort `prefixGcd` in **non-decreasing** order.

- Form pairs by taking the **smallest unpaired** element and the **largest unpaired** element.

- Repeat this process until no more pairs can be formed.

- For each formed pair, **compute** the `gcd` of the two elements.

- If `n` is odd, the **middle** element in the `prefixGcd` array remains **unpaired** and should be ignored.

Return an integer denoting the **sum of the GCD** values of all formed pairs.

The term `gcd(a, b)` denotes the **greatest common divisor** of `a` and `b`.
### Function Contract

**Inputs**

- `nums`: An array of positive integers.

Let $N=\lvert\texttt{nums}\rvert$ and $V=\max(\texttt{nums})$. For each index $i$, the inclusive prefix maximum and derived value are

$$
M_i = \max_{0 \le j \le i}\texttt{nums[j]},
\qquad
P_i = \gcd(\texttt{nums[i]}, M_i).
$$

The pairing rule applies to the non-decreasing ordering of all $P_i$ values, not to the original `nums` values. Pair the first with the last, the second with the second-to-last, and so on for exactly $\lfloor N/2 \rfloor$ pairs.

**Return value**

Return an integer equal to the sum of the GCD of every formed pair. A singleton input forms no pair and therefore returns `0`.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [2,6,4]

**Output:** 2

**Explanation:**

Construct `prefixGcd`:

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">$\text{nums}[i]$</th>
			<th style="border: 1px solid black;">$\text{mx}_{i}$</th>
			<th style="border: 1px solid black;">$\text{prefixGcd}[i]$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">6</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">4</td>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
	</tbody>
</table>

$prefixGcd = [2, 6, 2]$. After sorting, it forms `[2, 2, 6]`.

Pair the smallest and largest elements: $gcd(2, 6) = 2$. The remaining middle element 2 is ignored. Thus, the sum is 2.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [3,6,2,8]

**Output:** 5

**Explanation:**

Construct `prefixGcd`:

<table style="border: 1px solid black;">
	<thead>
		<tr>
			<th style="border: 1px solid black;">`i`</th>
			<th style="border: 1px solid black;">$\text{nums}[i]$</th>
			<th style="border: 1px solid black;">$\text{mx}_{i}$</th>
			<th style="border: 1px solid black;">$\text{prefixGcd}[i]$</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">3</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">6</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">6</td>
			<td style="border: 1px solid black;">2</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">8</td>
			<td style="border: 1px solid black;">8</td>
			<td style="border: 1px solid black;">8</td>
		</tr>
	</tbody>
</table>

$prefixGcd = [3, 6, 2, 8]$. After sorting, it forms `[2, 3, 6, 8]`.

Form pairs: $gcd(2, 8) = 2$ and $gcd(3, 6) = 3$. Thus, the sum is $2 + 3 = 5$.

</div>
### Constraints

- $1 \le n = \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^​​​​​​​9$