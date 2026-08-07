### 1. Description

You are given an array of positive integers `nums` and an integer `k`.

You may perform at most `k` operations. In each operation, you can choose one element in the array and **double** its value. Each element can be doubled **at most** once.

The **score** of a contiguous **subarray** is defined as the **product** of its length and the *greatest common divisor (GCD)* of all its elements.

Your task is to return the **maximum** **score** that can be achieved by selecting a contiguous subarray from the modified array.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Note

- The **greatest common divisor (GCD)** of an array is the largest integer that evenly divides all the array elements.

### 4. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [2,4], k = 1

**Output:** 8

**Explanation:**

- Double $\text{nums}[0]$ to 4 using one operation. The modified array becomes `[4, 4]`.

- The GCD of the subarray `[4, 4]` is 4, and the length is 2.

- Thus, the maximum possible score is $2 × 4 = 8$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [3,5,7], k = 2

**Output:** 14

**Explanation:**

- Double $\text{nums}[2]$ to 14 using one operation. The modified array becomes `[3, 5, 14]`.

- The GCD of the subarray `[14]` is 14, and the length is 1.

- Thus, the maximum possible score is $1 × 14 = 14$.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [5,5,5], k = 1

**Output:** 15

**Explanation:**

- The subarray `[5, 5, 5]` has a GCD of 5, and its length is 3.

- Since doubling any element doesn't improve the score, the maximum score is $3 × 5 = 15$.

</div>

### 5. Constraints

- $1 \le n = \text{nums.length} \le 1500$

- $1 \le \text{nums}[i] \le 10^{9}$

- $1 \le k \le n$