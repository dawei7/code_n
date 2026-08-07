### 1. Description

You are given an integer array `nums` consisting of `n` elements, and an integer `k`.

Find a contiguous subarray whose **length is greater than or equal to** `k` that has the maximum average value and return *this value*. Any answer with a calculation error less than $10^{-5}$ will be accepted.

### 2. Function Contract

**Inputs**

- `nums`: The integer array in which the contiguous subarray is selected.
- `k`: The minimum permitted subarray length.

**Return value**

Return the maximum value of

$\frac{\text{sum of the selected contiguous subarray}}{\text{length of that subarray}}$

over all contiguous subarrays of length at least `k`. The returned floating-point value must have calculation error less than $10^{-5}$.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,12,-5,-6,50,3], k = 4`
- **Output:** `12.75000`
- **Explanation:**
**- When the length is 4, averages are [0.5, 12.75, 10.5] and the maximum average is 12.75
- When the length is 5, averages are [10.4, 10.8] and the maximum average is 10.8
- When the length is 6, averages are [9.16667] and the maximum average is 9.16667
The maximum average is when we choose a subarray of length 4 (i.e., the sub array [12, -5, -6, 50]) which has the max average 12.75, so we return 12.75
Note that we do not consider the subarrays of length < 4.
#### Example 2

- **Input:** `nums = [5], k = 1`
- **Output:** `5.00000`

### 4. Constraints

- $n = \text{nums.length}$

- $1 \le k \le n \le 10^{4}$

- $-10^{4} \le \text{nums}[i] \le 10^{4}$