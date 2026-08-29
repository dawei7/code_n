### 1. Description

You are given two categories of theme park attractions: **land rides** and **water rides**.

- **Land rides**

		- $\text{landStartTime}[i]$ – the earliest time the $i^{\text{th}}$ land ride can be boarded.

- $\text{landDuration}[i]$ – how long the $i^{\text{th}}$ land ride lasts.

- **Water rides**

		- $\text{waterStartTime}[j]$ – the earliest time the $j^{\text{th}}$ water ride can be boarded.

- $\text{waterDuration}[j]$ – how long the $j^{\text{th}}$ water ride lasts.

A tourist must experience **exactly one** ride from **each** category, in **either order**.

- A ride may be started at its opening time or **any later moment**.

- If a ride is started at time `t`, it finishes at time $t + duration$.

- Immediately after finishing one ride the tourist may board the other (if it is already open) or wait until it opens.

Return the **earliest possible time** at which the tourist can finish both rides.

### 2. Function Contract

**Inputs**

- `landStartTime`: Input parameter (`List[int]`).
- `landDuration`: Input parameter (`List[int]`).
- `waterStartTime`: Input parameter (`List[int]`).
- `waterDuration`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** landStartTime = [2,8], landDuration = [4,1], waterStartTime = [6], waterDuration = [3]

- **Output:** 9

- **Explanation:** 

- Plan A (land ride 0 → water ride 0):

		- Start land ride 0 at time $\text{landStartTime}[0] = 2$. Finish at $2 + \text{landDuration}[0] = 6$.

- Water ride 0 opens at time $\text{waterStartTime}[0] = 6$. Start immediately at `6`, finish at $6 + \text{waterDuration}[0] = 9$.

- Plan B (water ride 0 → land ride 1):

		- Start water ride 0 at time $\text{waterStartTime}[0] = 6$. Finish at $6 + \text{waterDuration}[0] = 9$.

- Land ride 1 opens at $\text{landStartTime}[1] = 8$. Start at time `9`, finish at $9 + \text{landDuration}[1] = 10$.

- Plan C (land ride 1 → water ride 0):

		- Start land ride 1 at time $\text{landStartTime}[1] = 8$. Finish at $8 + \text{landDuration}[1] = 9$.

- Water ride 0 opened at $\text{waterStartTime}[0] = 6$. Start at time `9`, finish at $9 + \text{waterDuration}[0] = 12$.

- Plan D (water ride 0 → land ride 0):

		- Start water ride 0 at time $\text{waterStartTime}[0] = 6$. Finish at $6 + \text{waterDuration}[0] = 9$.

- Land ride 0 opened at $\text{landStartTime}[0] = 2$. Start at time `9`, finish at $9 + \text{landDuration}[0] = 13$.

Plan A gives the earliest finish time of 9.

#### Example 2

- **Input:** landStartTime = [5], landDuration = [3], waterStartTime = [1], waterDuration = [10]

- **Output:** 14

- **Explanation:** 

- Plan A (water ride 0 → land ride 0):

		- Start water ride 0 at time $\text{waterStartTime}[0] = 1$. Finish at $1 + \text{waterDuration}[0] = 11$.

- Land ride 0 opened at $\text{landStartTime}[0] = 5$. Start immediately at `11` and finish at $11 + \text{landDuration}[0] = 14$.

- Plan B (land ride 0 → water ride 0):

		- Start land ride 0 at time $\text{landStartTime}[0] = 5$. Finish at $5 + \text{landDuration}[0] = 8$.

- Water ride 0 opened at $\text{waterStartTime}[0] = 1$. Start immediately at `8` and finish at $8 + \text{waterDuration}[0] = 18$.

Plan A provides the earliest finish time of 14.****

### 4. Constraints

- $1 \le n, m \le 5 * 10^{4}$

- $\text{landStartTime.length} = \text{landDuration.length} = n$

- $\text{waterStartTime.length} = \text{waterDuration.length} = m$

- $1 \le \text{landStartTime}[i], \text{landDuration}[i], \text{waterStartTime}[j], \text{waterDuration}[j] \le 10^{5}$
