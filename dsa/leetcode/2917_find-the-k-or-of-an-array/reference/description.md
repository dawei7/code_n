## Description

You are given an integer array `nums`, and an integer `k`. Let's introduce **K-or** operation by extending the standard bitwise OR. In K-or, a bit position in the result is set to `1` if at least `k` numbers in `nums` have a `1` in that position.

Return *the K-or of* `nums`.

**Example 1: **

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input:** nums = [7,12,9,8,9,15], k = 4

**Output:** 9

**Explanation: **

Represent numbers in binary:

<table style="text-indent:10px; margin-bottom=20px;">
	<tbody>
		<tr>
			<th>**Number**</th>
			<th>Bit 3</th>
			<th>Bit 2</th>
			<th>Bit 1</th>
			<th>Bit 0</th>
		</tr>
		<tr>
			<td>**7**</td>
			<td>0</td>
			<td>1</td>
			<td>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>**12**</td>
			<td>1</td>
			<td>1</td>
			<td>0</td>
			<td>0</td>
		</tr>
		<tr>
			<td>**9**</td>
			<td>1</td>
			<td>0</td>
			<td>0</td>
			<td>1</td>
		</tr>
		<tr>
			<td>**8**</td>
			<td>1</td>
			<td>0</td>
			<td>0</td>
			<td>0</td>
		</tr>
		<tr>
			<td>**9**</td>
			<td>1</td>
			<td>0</td>
			<td>0</td>
			<td>1</td>
		</tr>
		<tr>
			<td>**15**</td>
			<td>1</td>
			<td>1</td>
			<td>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>**Result = 9**</td>
			<td>1</td>
			<td>0</td>
			<td>0</td>
			<td>1</td>
		</tr>
	</tbody>
</table>

Bit 0 is set in 7, 9, 9, and 15. Bit 3 is set in 12, 9, 8, 9, and 15.

Only bits 0 and 3 qualify. The result is $(1001)_2 = 9$.

</div>

**Example 2: **

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input:** nums = [2,12,1,11,4,5], k = 6

**Output:** 0

**Explanation: **No bit appears as 1 in all six array numbers, as required for K-or with $k = 6$. Thus, the result is 0.

</div>

**Example 3: **

<div class="example-block" style="border-color: var(--border-tertiary); border-left-width: 2px; color: var(--text-secondary); font-size: .875rem; margin-bottom: 1rem; margin-top: 1rem; overflow: visible; padding-left: 1rem;">
**Input:** nums = [10,8,5,9,11,6,8], k = 1

**Output:** 15

**Explanation: ** Since $k = 1$, the 1-or of the array is equal to the bitwise OR of all its elements. Hence, the answer is $10 OR 8 OR 5 OR 9 OR 11 OR 6 OR 8 = 15$.

</div>
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Constraints

- $1 \le \text{nums.length} \le 50$

- $0 \le \text{nums}[i] < 2^{31}$

- $1 \le k \le \text{nums.length}$