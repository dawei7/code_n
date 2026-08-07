### 1. Description

You are given an integer array `nums`.

Your task is to find two **distinct** indices `i` and `j` such that the product $\text{nums}[i] * \text{nums}[j]$ is **maximized,** and the binary representations of $\text{nums}[i]$ and $\text{nums}[j]$ do not share any common set bits.

Return the **maximum** possible product of such a pair. If no such pair exists, return 0.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,3,4,5,6,7]

**Output:** 12

**Explanation:**

The best pair is 3 (011) and 4 (100). They share no set bits and $3 * 4 = 12$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [5,6,4]

**Output:** 0

**Explanation:**

Every pair of numbers has at least one common set bit. Hence, the answer is 0.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [64,8,32]

**Output:** 2048

**Explanation:**

No pair of numbers share a common bit, so the answer is the product of the two maximum elements, 64 and 32 ($64 * 32 = 2048$).

</div>

### 4. Constraints

- $2 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{6}$