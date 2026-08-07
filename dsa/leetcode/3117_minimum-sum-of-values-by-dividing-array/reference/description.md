### 1. Description

You are given two arrays `nums` and `andValues` of length `n` and `m` respectively.

The **value** of an array is equal to the **last** element of that array.

You have to divide `nums` into `m` **disjoint contiguous** subarrays such that for the $$i^{\text{th}}$$ subarray $[l_{i}, r_{i}]$, the bitwise `AND` of the subarray elements is equal to $\text{andValues}[i]$, in other words, $nums[l_{i}] \& nums[l_{i} + 1] \& ... \& nums[r_{i}] = \text{andValues}[i]$ for all $1 \le i \le m$, where `&` represents the bitwise `AND` operator.

Return *the **minimum** possible sum of the **values** of the *`m`* subarrays *`nums`* is divided into*. *If it is not possible to divide *`nums`* into *`m`* subarrays satisfying these conditions, return* `-1`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,4,3,3,2], andValues = [0,3,3,2]

**Output:** 12

**Explanation:**

The only possible way to divide `nums` is:

- `[1,4]` as $1 \& 4 = 0$.

- `[3]` as the bitwise `AND` of a single element subarray is that element itself.

- `[3]` as the bitwise `AND` of a single element subarray is that element itself.

- `[2]` as the bitwise `AND` of a single element subarray is that element itself.

The sum of the values for these subarrays is $4 + 3 + 3 + 2 = 12$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [2,3,5,7,7,7,5], andValues = [0,7,5]

**Output:** 17

**Explanation:**

There are three ways to divide `nums`:

- `[[2,3,5],[7,7,7],[5]]` with the sum of the values $5 + 7 + 5 = 17$.

- `[[2,3,5,7],[7,7],[5]]` with the sum of the values $7 + 7 + 5 = 19$.

- `[[2,3,5,7,7],[7],[5]]` with the sum of the values $7 + 7 + 5 = 19$.

The minimum possible sum of the values is `17`.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1,2,3,4], andValues = [2]

**Output:** -1

**Explanation:**

The bitwise `AND` of the entire array `nums` is `0`. As there is no possible way to divide `nums` into a single subarray to have the bitwise `AND` of elements `2`, return `-1`.

</div>

### 4. Constraints

- $1 \le n = \text{nums.length} \le 10^{4}$

- $1 \le m = \text{andValues.length} \le min(n, 10)$

- $1 \le \text{nums}[i] < 10^{5}$

- $0 \le \text{andValues}[j] < 10^{5}$