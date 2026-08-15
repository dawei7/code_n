### 1. Description

You are given an integer array `nums`.

You are allowed to replace **at most** one element in the array with any other integer value of your choice.

Return the length of the **longest non-decreasing subarray** that can be obtained after performing at most one replacement.

An array is said to be **non-decreasing** if each element is greater than or equal to its previous one (if it exists).

### 2. Function Contract

**Inputs**

- `nums`: The integer array in which at most one position may be replaced.

The replacement value may be any integer; it is not restricted to values already present in `nums` or to the input-value bounds. The selected result must be a contiguous subarray, not a subsequence.

**Return value**

Return the maximum length of a non-decreasing subarray achievable with zero or one replacement.

### 3. Examples

#### Example 1

- **Input:** nums = [1,2,3,1,2]

- **Output:** 4

- **Explanation:** Replacing $\text{nums}[3] = 1$ with 3 gives the array [1, 2, 3, 3, 2].

The longest non-decreasing subarray is [1, 2, 3, 3], which has a length of 4.

#### Example 2

- **Input:** nums = [2,2,2,2,2]

- **Output:** 5

- **Explanation:** All elements in `nums` are equal, so it is already non-decreasing and the entire `nums` forms a subarray of length 5.

### 4. Constraints

- $1 \le \text{nums.length} \le 10^{5}$

- $-10^{9} \le \text{nums}[i] \le 10^{9}$​​​​​​​
