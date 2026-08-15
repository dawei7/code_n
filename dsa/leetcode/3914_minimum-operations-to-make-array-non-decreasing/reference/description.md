### 1. Description

You are given an integer array `nums` of length `n`.

In one operation, you may choose any **subarray** `nums[l..r]` and **increase** each element in that **subarray** by `x`, where `x` is any **positive** integer.

Return the **minimum** possible **sum** of the values of `x` across all operations required to make the array **non-decreasing**.

An array is **non-decreasing** if $\text{nums}[i] \le nums[i + 1]$ for all $0 \le i < n - 1$.

### 2. Function Contract

**Inputs**

- `nums`: A non-empty array of positive integers that may be increased through contiguous-subarray operations.

Let $n = \lvert\texttt{nums}\rvert$.

**Return value**

Return the minimum sum of all positive increment values `x` needed to reach an array satisfying $\texttt{\text{nums}[i]} \le \texttt{nums[i + 1]}$ for every $0 \le i < n-1$. Return `0` when the input is already non-decreasing.

### 3. Examples

#### Example 1

- **Input:** nums = [3,3,2,1]

- **Output:** 2

- **Explanation:** One optimal set of operations:

- Choose subarray `[2..3]` and add $x = 1$ resulting in `[3, 3, 3, 2]`

- Choose subarray `[3..3]` and add $x = 1$ resulting in `[3, 3, 3, 3]`

The array becomes non-decreasing, and the total sum of chosen `x` values is $1 + 1 = 2$.

#### Example 2

- **Input:** nums = [5,1,2,3]

- **Output:** 4

- **Explanation:** One optimal set of operations:

- Choose subarray `[1..3]` and add $x = 4$ resulting in `[5, 5, 6, 7]`

The array becomes non-decreasing, and the total sum of chosen `x` values is `4`.

### 4. Constraints

- $1 \le n = \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$
