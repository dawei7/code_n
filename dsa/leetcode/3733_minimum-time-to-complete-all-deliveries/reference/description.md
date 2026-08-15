### 1. Description

You are given two integer arrays of size 2: $d = [d_{1}, d_{2}]$ and $r = [r_{1}, r_{2}]$.

Two delivery drones are tasked with completing a specific number of deliveries. Drone `i` must complete $d_{i}$ deliveries.

Each delivery takes **exactly** one hour and **only one** drone can make a delivery at any given hour.

Additionally, both drones require recharging at specific intervals during which they cannot make deliveries. Drone `i` must recharge every $r_{i}$ hours (i.e. at hours that are multiples of $r_{i}$).

Return an integer denoting the **minimum** total time (in hours) required to complete all deliveries.

### 2. Function Contract

**Inputs**

- `d`: A length-two array where $d[i]$ is drone `i`'s required delivery count.
- `r`: A length-two array where $r[i]$ is drone `i`'s recharge interval.

Hours are numbered from `1`. A drone is unavailable at hours divisible by its recharge interval. The drones may recharge simultaneously, but the single-delivery-per-hour rule applies whenever either could deliver.

**Return value**

Return the smallest final hour by which both delivery quotas can be assigned legally.

### 3. Examples

#### Example 1

- **Input:** d = [3,1], r = [2,3]

- **Output:** 5

- **Explanation:** 

- The first drone delivers at hours 1, 3, 5 (recharges at hours 2, 4).

- The second drone delivers at hour 2 (recharges at hour 3).

#### Example 2

- **Input:** d = [1,3], r = [2,2]

- **Output:** 7

- **Explanation:** 

- The first drone delivers at hour 3 (recharges at hours 2, 4, 6).

- The second drone delivers at hours 1, 5, 7 (recharges at hours 2, 4, 6).

#### Example 3

- **Input:** d = [2,1], r = [3,4]

- **Output:** 3

- **Explanation:** 

- The first drone delivers at hours 1, 2 (recharges at hour 3).

- The second drone delivers at hour 3.

### 4. Constraints

- $d = [d_{1}, d_{2}]$

- $1 \le d_{i} \le 10^{9}$

- $r = [r_{1}, r_{2}]$

- $2 \le r_{i} \le 3 * 10^{4}$
