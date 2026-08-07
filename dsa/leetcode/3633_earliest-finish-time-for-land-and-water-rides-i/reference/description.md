## Description

You are given two categories of theme park attractions: **land rides** and **water rides**.

- **Land rides**

		<li data-end="245" data-start="168">$\text{landStartTime}[i]$ – the earliest time the $$i^{\text{th}}$$ land ride can be boarded.

- $\text{landDuration}[i]$ – how long the $$i^{\text{th}}$$ land ride lasts.

	</li>
- **Water rides**

		<li>$\text{waterStartTime}[j]$ – the earliest time the $$j^{\text{th}}$$ water ride can be boarded.

- $\text{waterDuration}[j]$ – how long the $$j^{\text{th}}$$ water ride lasts.

	</li>

A tourist must experience **exactly one** ride from **each** category, in **either order**.

- A ride may be started at its opening time or **any later moment**.

- If a ride is started at time `t`, it finishes at time $t + duration$.

- Immediately after finishing one ride the tourist may board the other (if it is already open) or wait until it opens.

Return the **earliest possible time** at which the tourist can finish both rides.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** landStartTime = [2,8], landDuration = [4,1], waterStartTime = [6], waterDuration = [3]

**Output:** 9

**Explanation:**​​​​​​​

- Plan A (land ride 0 → water ride 0):

		<li data-end="272" data-start="186">Start land ride 0 at time $\text{landStartTime}[0] = 2$. Finish at $2 + \text{landDuration}[0] = 6$.

- Water ride 0 opens at time $\text{waterStartTime}[0] = 6$. Start immediately at `6`, finish at $6 + \text{waterDuration}[0] = 9$.

	</li>
- Plan B (water ride 0 → land ride 1):

		<li data-end="526" data-start="437">Start water ride 0 at time $\text{waterStartTime}[0] = 6$. Finish at $6 + \text{waterDuration}[0] = 9$.

- Land ride 1 opens at $\text{landStartTime}[1] = 8$. Start at time `9`, finish at $9 + \text{landDuration}[1] = 10$.

	</li>
- Plan C (land ride 1 → water ride 0):

		<li data-end="763" data-start="677">Start land ride 1 at time $\text{landStartTime}[1] = 8$. Finish at $8 + \text{landDuration}[1] = 9$.

- Water ride 0 opened at $\text{waterStartTime}[0] = 6$. Start at time `9`, finish at $9 + \text{waterDuration}[0] = 12$.

	</li>
- Plan D (water ride 0 → land ride 0):

		<li data-end="1007" data-start="918">Start water ride 0 at time $\text{waterStartTime}[0] = 6$. Finish at $6 + \text{waterDuration}[0] = 9$.

- Land ride 0 opened at $\text{landStartTime}[0] = 2$. Start at time `9`, finish at $9 + \text{landDuration}[0] = 13$.

	</li>

Plan A gives the earliest finish time of 9.

</div>
#### Example 2

<div class="example-block">
**Input:** landStartTime = [5], landDuration = [3], waterStartTime = [1], waterDuration = [10]

**Output:** 14

**Explanation:**​​​​​​​

- Plan A (water ride 0 → land ride 0):

		<li data-end="1219" data-start="1129">Start water ride 0 at time $\text{waterStartTime}[0] = 1$. Finish at $1 + \text{waterDuration}[0] = 11$.

- Land ride 0 opened at $\text{landStartTime}[0] = 5$. Start immediately at `11` and finish at $11 + \text{landDuration}[0] = 14$.

	</li>
- Plan B (land ride 0 → water ride 0):

		<li data-end="1469" data-start="1383">Start land ride 0 at time $\text{landStartTime}[0] = 5$. Finish at $5 + \text{landDuration}[0] = 8$.

- Water ride 0 opened at $\text{waterStartTime}[0] = 1$. Start immediately at `8` and finish at $8 + \text{waterDuration}[0] = 18$.

	</li>

Plan A provides the earliest finish time of 14.**​​​​​​​**

</div>
### Constraints

- $1 \le n, m \le 100$

- $\text{landStartTime.length} = \text{landDuration.length} = n$

- $\text{waterStartTime.length} = \text{waterDuration.length} = m$

- $1 \le \text{landStartTime}[i], \text{landDuration}[i], \text{waterStartTime}[j], \text{waterDuration}[j] \le 1000$