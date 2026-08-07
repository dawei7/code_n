### 1. Description

You are given an integer array `nums`.

Your task is to choose **exactly three** integers from `nums` such that their sum is divisible by three.

Return the **maximum** possible sum of such a triplet. If no such triplet exists, return 0.

### 2. Function Contract

**Inputs**

- `nums`: An integer array containing at least three positive values.

Let $N=\lvert\texttt{nums}\rvert$. A selection uses three distinct array positions; equal numeric values may all be selected when they occur at different positions.

**Return value**

Return the largest sum of exactly three selected elements that is congruent to zero modulo three, or `0` when no such triplet exists.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [4,2,3,1]

**Output:** 9

**Explanation:**

The valid triplets whose sum is divisible by 3 are:

- `(4, 2, 3)` with a sum of $4 + 2 + 3 = 9$.

- `(2, 3, 1)` with a sum of $2 + 3 + 1 = 6$.

Thus, the answer is 9.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [2,1,5]

**Output:** 0

**Explanation:**

No triplet forms a sum divisible by 3, so the answer is 0.

</div>

### 4. Constraints

- $3 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{5}$