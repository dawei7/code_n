### 1. Description

An array `A` is larger than some array `B` if for the first index `i` where $A[i] \neq B[i]$, $A[i] > B[i]$.

For example, consider `0`-indexing:

- `[1,3,2,4] > [1,2,2,4]`, since at index `1`, `3 > 2`.

- `[1,4,4,4] < [2,1,1,1]`, since at index `0`, `1 < 2`.

A subarray is a contiguous subsequence of the array.

Given an integer array `nums` of **distinct** integers, return the **largest** subarray of `nums` of length `k`.

### 2. Function Contract

**Inputs**

- `nums`: An array of distinct integers ($1 \le \text{nums.length} \le 10^5$, $1 \le \text{nums}[i] \le 10^9$).
- `k`: An integer representing the target subarray length ($1 \le k \le \text{nums.length}$).

**Return value**

Return an integer array representing the lexicographically largest contiguous subarray of `nums` of length `k`.

### 3. Examples

#### Example 1

- **Input:** `nums = [1,4,5,2,3], k = 3`
- **Output:** `[5,2,3]`
- **Explanation:** The subarrays of size 3 are: [1,4,5], [4,5,2], and [5,2,3].
Of these, [5,2,3] is the largest.

#### Example 2

- **Input:** `nums = [1,4,5,2,3], k = 4`
- **Output:** `[4,5,2,3]`
- **Explanation:** The subarrays of size 4 are: [1,4,5,2], and [4,5,2,3].
Of these, [4,5,2,3] is the largest.

#### Example 3

- **Input:** `nums = [1,4,5,2,3], k = 1`
- **Output:** `[5]`

### 4. Constraints

- $1 \le k \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$

- All the integers of `nums` are **unique**.

**Follow up:** What if the integers in `nums` are not distinct?
