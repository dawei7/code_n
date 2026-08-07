## Description

You are given a 2D integer array `units` of size `m × n` where $\text{units}[i][j]$ represents the capacity of the $$j^{\text{th}}$$ unit in the $$i^{\text{th}}$$ device. Each device contains **exactly** `n` units.

The **rating** of a device is the **minimum** capacity among all its units.

You may perform the following operation any number of times (including zero):

- Choose a device `i` that has **not been** used as a source before.

- Remove **exactly** one unit from device `i` and add it to **any** different device.

- Then mark device `i` as used, so it cannot be chosen again as a source.

Return the **maximum** possible sum of the ratings of all devices after any number of such operations.

**Note:**

- Devices can receive units from multiple devices, regardless of whether they have been selected.

- The rating of an empty device is 0.
### Function Contract

**Inputs**

- `units`: A nonempty rectangular matrix of positive capacities; every row represents one device and has the same length.

Let $m$ be the number of devices, $n$ the units per device, and $U=mn$ the total number of initially supplied units.

**Return value**

Return the maximum possible sum of final device ratings after zero or more legal transfers. The total may exceed the range of a signed 32-bit integer.

### Examples

#### Example 1

<div class="example-block">
**Input:** units = [[1,3],[2,2]]

**Output:** 4

**Explanation:**

- ​​​​​​​​​​​​​​Select device $i = 0$ and transfer $\text{units}[0][0] = 1$ to device $i = 1$.

- After the transfer, the ratings are:

		<li>Device $0 = [3]$: $\text{rating}[0] = 3$

- Device $1 = [2, 2, <u>1</u>]$: $\text{rating}[1] = 1$

	</li>
- Thus, the sum of ratings is $3 + 1 = 4$.

</div>
#### Example 2

<div class="example-block">
**Input:** units = [[1,2,3],[4,5,6]]

**Output:** 6

**Explanation:**

- Select device $i = 1$ and transfer $\text{units}[1][0] = 4$ to device $i = 0$.

- After the transfer, the ratings are:

		<li>Device $0 = [1, 2, 3, <u>4</u>]$: $\text{rating}[0] = 1$

- Device $1 = [5, 6]$: $\text{rating}[1] = 5$

	</li>
- Thus, the sum of ratings is $1 + 5 = 6$.

</div>
#### Example 3

<div class="example-block">
**Input:** units = [[5,5,5],[1,1,1]]

**Output:** 6

**Explanation:**

- No transfers increase the sum of ratings. Thus, the sum of ratings is $5 + 1 = 6$.

</div>
### Constraints

- $1 \le m = \text{units.length} \le 10^{5}$

- $1 \le n = \text{units}[i].length \le 10^{5}$

- $m * n \le 2 * 10^{5}$

- $1 \le \text{units}[i][j] \le 10^{5}$