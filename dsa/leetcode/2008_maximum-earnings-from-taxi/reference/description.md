### 1. Description

There are `n` points on a road you are driving your taxi on. The `n` points on the road are labeled from `1` to `n` in the direction you are going, and you want to drive from point `1` to point `n` to make money by picking up passengers. You cannot change the direction of the taxi.

The passengers are represented by a **0-indexed** 2D integer array `rides`, where $\text{rides}[i] = [\text{start}_{i}, \text{end}_{i}, \text{tip}_{i}]$ denotes the $$i^{\text{th}}$$ passenger requesting a ride from point $\text{start}_{i}$ to point $\text{end}_{i}$ who is willing to give a $\text{tip}_{i}$ dollar tip.

For** each **passenger `i` you pick up, you **earn** $\text{end}_{i} - \text{start}_{i} + \text{tip}_{i}$ dollars. You may only drive **at most one **passenger at a time.

Given `n` and `rides`, return *the **maximum** number of dollars you can earn by picking up the passengers optimally.*

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Note

You may drop off a passenger and pick up a different passenger at the same point.

### 4. Examples

#### Example 1

- **Input:** $n = 5, rides = [<u>[2,5,4]</u>,[1,5,1]]$
- **Output:** `7`
- **Explanation:** We can pick up passenger 0 to earn 5 - 2 + 4 = 7 dollars.
#### Example 2

- **Input:** $n = 20, rides = [[1,6,1],<u>[3,10,2]</u>,<u>[10,12,3]</u>,[11,12,2],[12,15,2],<u>[13,18,1]</u>]$
- **Output:** `20`
- **Explanation:** We will pick up the following passengers:
- Drive passenger 1 from point 3 to point 10 for a profit of 10 - 3 + 2 = 9 dollars.
- Drive passenger 2 from point 10 to point 12 for a profit of 12 - 10 + 3 = 5 dollars.
- Drive passenger 5 from point 13 to point 18 for a profit of 18 - 13 + 1 = 6 dollars.
We earn 9 + 5 + 6 = 20 dollars in total.

### 5. Constraints

- $1 \le n \le 10^{5}$

- $1 \le \text{rides.length} \le 3 * 10^{4}$

- $\text{rides}[i].length = 3$

- $1 \le \text{start}_{i} < \text{end}_{i} \le n$

- $1 \le \text{tip}_{i} \le 10^{5}$