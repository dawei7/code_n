### 1. Description

You are given a binary array `nums` (**0-indexed**).

We define $x_{i}$ as the number whose binary representation is the subarray `nums[0..i]` (from most-significant-bit to least-significant-bit).

- For example, if `nums = [1,0,1]`, then $x_{0} = 1$, $x_{1} = 2$, and $x_{2} = 5$.

Return *an array of booleans *`answer`* where *$\text{answer}[i]$* is *`true`* if *$x_{i}$* is divisible by *`5`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `nums = [0,1,1]`
- **Output:** `[true,false,false]`
- **Explanation:** The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.
Only the first number is divisible by 5, so answer[0] is true.
#### Example 2

- **Input:** `nums = [1,1,1]`
- **Output:** `[false,false,false]`

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $\text{nums}[i]$ is either `0` or `1`.