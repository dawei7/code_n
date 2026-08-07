### 1. Description

You are given an integer array `nums` and a **positive** integer `k`.

The **value** of a sequence `seq` of size $2 * x$ is defined as:

- $(\text{seq}[0] OR \text{seq}[1] OR ... OR seq[x - 1]) XOR (\text{seq}[x] OR seq[x + 1] OR ... OR seq[2 * x - 1])$.

Return the **maximum** **value** of any subsequence of `nums` having size $2 * k$.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [2,6,7], k = 1

**Output:** 5

**Explanation:**

The subsequence `[2, 7]` has the maximum value of $2 XOR 7 = 5$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [4,2,5,6,7], k = 2

**Output:** 2

**Explanation:**

The subsequence `[4, 5, 6, 7]` has the maximum value of $(4 OR 5) XOR (6 OR 7) = 2$.

</div>

### 4. Constraints

- $2 \le \text{nums.length} \le 400$

- $1 \le \text{nums}[i] < 2^{7}$

- $1 \le k \le \text{nums.length} / 2$