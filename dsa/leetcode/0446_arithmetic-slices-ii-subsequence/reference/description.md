## Description

Given an integer array `nums`, return *the number of all the **arithmetic subsequences** of* `nums`.

A sequence of numbers is called arithmetic if it consists of **at least three elements** and if the difference between any two consecutive elements is the same.

- For example, `[1, 3, 5, 7, 9]`, `[7, 7, 7, 7]`, and `[3, -1, -5, -9]` are arithmetic sequences.

- For example, `[1, 1, 2, 5, 7]` is not an arithmetic sequence.

A **subsequence** of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

- For example, `[2,5,10]` is a subsequence of `[1,2,1,**<u>2</u>**,4,1,<u>**5**</u>,<u>**10**</u>]`.

The test cases are generated so that the answer fits in **32-bit** integer.
### Function Contract

**Inputs**

- `nums`: An integer array whose subsequences preserve the original index order.

**Return value**

- Return the number of arithmetic subsequences containing at least three elements.

Different selections of indices count as different subsequences, even if they produce the same values.

### Examples

#### Example 1

- **Input:** `nums = [2,4,6,8,10]`
- **Output:** `7`
- **Explanation:** All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
#### Example 2

- **Input:** `nums = [7,7,7,7,7]`
- **Output:** `16`
- **Explanation:** Any subsequence of this array is arithmetic.
### Constraints

- $1 \le \text{nums.length} \le 1000$

- $-2^{31} \le \text{nums}[i] \le 2^{31} - 1$