### 1. Description

You are given an integer array `nums`.

Return the maximum possible sum of a subarray of `nums` that is a palindrome.

### 2. Function Contract

`solve(nums) -> int`

Let $n = \lvert\texttt{nums}\rvert$.

**Inputs**

- `nums`: A nonempty array of positive integers.

For indices $0 \le l \le r < n$, the subarray `nums[l..r]` is palindromic exactly when $nums[l + j] = nums[r - j]$ for every valid offset $j$.

**Output**

Return the maximum element sum among all palindromic subarrays of `nums`. The result may exceed a 32-bit signed integer.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [10,10]

**Output:** 20

**Explanation:**

The whole array `[10,10]` is a palindrome. Therefore, the maximum sum is $10 + 10 = 20$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,2,3,2,1,5,6]

**Output:** 9

**Explanation:**

The contiguous subarray `[1,2,3,2,1]` is a palindrome. Its sum is $1 + 2 + 3 + 2 + 1 = 9$ and it is the maximum sum.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [7,1,2,1,7,3,4,3,4]

**Output:** 18

**Explanation:**

The contiguous subarray `[7,1,2,1,7]` is a palindrome. Its sum is $7 + 1 + 2 + 1 + 7 = 18$ and it is the maximum sum.

</div>
#### Example 4

<div class="example-block">
**Input:** nums = [1,2,3,4,5]

**Output:** 5

**Explanation:**

No subarray with length greater than 1 is a palindrome. The largest element in the array is 5. Therefore, the answer is 5.

</div>
#### Example 5

<div class="example-block">
**Input:** nums = [1000]

**Output:** 1000

**Explanation:**

The subarray with only one element is a palindrome. Therefore, the answer is 1000.

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^​​​​​​​9$