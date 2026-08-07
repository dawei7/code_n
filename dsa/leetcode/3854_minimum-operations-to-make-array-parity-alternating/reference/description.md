## Description

You are given an integer array `nums`.

An array is called **parity alternating** if for every index `i` where $0 \le i < n - 1$, $\text{nums}[i]$ and $nums[i + 1]$ have different parity (one is even and the other is odd).

In one operation, you may choose any index `i` and either increase $\text{nums}[i]$ by 1 or decrease $\text{nums}[i]$ by 1.

Return an integer array `answer` of length 2 where:

- $\text{answer}[0]$ is the **minimum** number of operations required to make the array parity alternating.

- $\text{answer}[1]$ is the **minimum** possible value of $max(nums) - min(nums)$ taken over all arrays that are parity alternating and can be obtained by performing **exactly** $\text{answer}[0]$ operations.

An array of length 1 is considered parity alternating.
### Function Contract

**Inputs**

- `nums`: A nonempty array of integers.

If $N=\lvert\texttt{nums}\rvert$, the resulting array must satisfy

$$
\texttt{nums[i]}\bmod 2 \ne \texttt{nums[i+1]}\bmod 2
$$

for every $0\le i<N-1$. Each operation adds either `1` or `-1` to one chosen element.

The operation count is optimized first. Only arrays obtained with exactly that optimal count participate in the separate minimization of the final range.

**Return value**

Return `[minimum operations, minimum final range]`, where the range is the final maximum element minus the final minimum element.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [-2,-3,1,4]

**Output:** [2,6]

**Explanation:**

Applying the following operations:

- Increase $\text{nums}[2]$ by 1, resulting in `nums = [-2, -3, 2, 4]`.

- Decrease $\text{nums}[3]$ by 1, resulting in `nums = [-2, -3, 2, 3]`.

The resulting array is parity alternating, and the value of $max(nums) - min(nums) = 3 - (-3) = 6$ is the minimum possible among all parity alternating arrays obtainable using exactly 2 operations.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [0,2,-2]

**Output:** [1,3]

**Explanation:**

Applying the following operation:

- Decrease $\text{nums}[1]$ by 1, resulting in `nums = [0, 1, -2]`.

The resulting array is parity alternating, and the value of $max(nums) - min(nums) = 1 - (-2) = 3$ is the minimum possible among all parity alternating arrays obtainable using exactly 1 operation.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [7]

**Output:** [0,0]

**Explanation:**

No operations are required. The array is already parity alternating, and the value of $max(nums) - min(nums) = 7 - 7 = 0$, which is the minimum possible.

</div>
### Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $-10^{9} \le \text{nums}[i] \le 10^{9}$