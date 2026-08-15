### 1. Description

You are given three integers `n`, `s`, and `m`.

A sequence `seq` of integers of length `n` is considered **valid** if:

- $\text{seq}[0] = s$.

- The sequence is **alternating**, meaning that either:

		- $\text{seq}[0] > \text{seq}[1] < \text{seq}[2] > ...$, or

- $\text{seq}[0] < \text{seq}[1] > \text{seq}[2] < ...$.

- For every adjacent pair, $|\text{seq}[i] - seq[i - 1]| \le m$.

A sequence of length 1 is considered alternating.

Return the **maximum** possible element that can appear in any valid sequence.

### 2. Function Contract

**Inputs**

- `n`: The number of elements in the sequence.
- `s`: The required value of the first element.
- `m`: The maximum permitted absolute difference between adjacent elements.

All sequence elements are integers. Alternation is strict, so adjacent values cannot be equal even though their absolute difference is allowed to be less than or equal to `m`.

**Return value**

Return the maximum integer that can appear in any valid length-`n` alternating sequence beginning with `s` and respecting the adjacent-difference limit.

### 3. Examples

#### Example 1

- **Input:** n = 4, s = 3, m = 5

- **Output:** 12

- **Explanation:** 

- One valid sequence is `[3, 8, 7, 12]`.

- The maximum element in the sequence is 12.

#### Example 2

- **Input:** n = 2, s = 4, m = 3

- **Output:** 7

- **Explanation:** 

- One valid sequence is `[4, 7]`.

- The maximum element in the sequence is 7.

### 4. Constraints

- $1 \le n, s \le 10^{9}$

- $1 \le m \le 10^{5}$
