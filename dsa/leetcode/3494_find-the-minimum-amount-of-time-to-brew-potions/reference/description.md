### 1. Description

You are given two integer arrays, `skill` and `mana`, of length `n` and `m`, respectively.

In a laboratory, `n` wizards must brew `m` potions *in order*. Each potion has a mana capacity $\text{mana}[j]$ and **must** pass through **all** the wizards sequentially to be brewed properly. The time taken by the $$i^{\text{th}}$$ wizard on the $$j^{\text{th}}$$ potion is $\text{time}_{ij} = \text{skill}[i] * \text{mana}[j]$.

Since the brewing process is delicate, a potion **must** be passed to the next wizard immediately after the current wizard completes their work. This means the timing must be *synchronized* so that each wizard begins working on a potion **exactly** when it arrives. ​

Return the **minimum** amount of time required for the potions to be brewed properly.

### 2. Function Contract

**Inputs**

- `skill`: Input parameter (`List[int]`).
- `mana`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** skill = [1,5,2,4], mana = [5,1,4,2]

- **Output:** 110

- **Explanation:** <table style="border: 1px solid black;">
	<tbody>
		<tr>
			<th style="border: 1px solid black;">Potion Number</th>
			<th style="border: 1px solid black;">Start time</th>
			<th style="border: 1px solid black;">Wizard 0 done by</th>
			<th style="border: 1px solid black;">Wizard 1 done by</th>
			<th style="border: 1px solid black;">Wizard 2 done by</th>
			<th style="border: 1px solid black;">Wizard 3 done by</th>
		</tr>
		<tr>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">0</td>
			<td style="border: 1px solid black;">5</td>
			<td style="border: 1px solid black;">30</td>
			<td style="border: 1px solid black;">40</td>
			<td style="border: 1px solid black;">60</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">1</td>
			<td style="border: 1px solid black;">52</td>
			<td style="border: 1px solid black;">53</td>
			<td style="border: 1px solid black;">58</td>
			<td style="border: 1px solid black;">60</td>
			<td style="border: 1px solid black;">64</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">2</td>
			<td style="border: 1px solid black;">54</td>
			<td style="border: 1px solid black;">58</td>
			<td style="border: 1px solid black;">78</td>
			<td style="border: 1px solid black;">86</td>
			<td style="border: 1px solid black;">102</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">3</td>
			<td style="border: 1px solid black;">86</td>
			<td style="border: 1px solid black;">88</td>
			<td style="border: 1px solid black;">98</td>
			<td style="border: 1px solid black;">102</td>
			<td style="border: 1px solid black;">110</td>
		</tr>
	</tbody>
</table>

As an example for why wizard 0 cannot start working on the 1^st potion before time $t = 52$, consider the case where the wizards started preparing the 1^st potion at time $t = 50$. At time $t = 58$, wizard 2 is done with the 1^st potion, but wizard 3 will still be working on the 0^th potion till time $t = 60$.

#### Example 2

- **Input:** skill = [1,1,1], mana = [1,1,1]

- **Output:** 5

- **Explanation:** 

- Preparation of the 0^th potion begins at time $t = 0$, and is completed by time $t = 3$.

- Preparation of the 1^st potion begins at time $t = 1$, and is completed by time $t = 4$.

- Preparation of the 2^nd potion begins at time $t = 2$, and is completed by time $t = 5$.

#### Example 3

- **Input:** skill = [1,2,3,4], mana = [1,2]

- **Output:** 21

### 4. Constraints

- $n = \text{skill.length}$

- $m = \text{mana.length}$

- $1 \le n, m \le 5000$

- $1 \le \text{mana}[i], \text{skill}[i] \le 5000$
