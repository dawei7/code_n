## Description

You are given two integer arrays of the same length `nums1` and `nums2`. In one operation, you are allowed to swap $\text{nums1}[i]$ with $\text{nums2}[i]$.

- For example, if $nums1 = [1,2,3,<u>8</u>]$, and $nums2 = [5,6,7,<u>4</u>]$, you can swap the element at $i = 3$ to obtain $nums1 = [1,2,3,4]$ and $nums2 = [5,6,7,8]$.

Return *the minimum number of needed operations to make *`nums1`* and *`nums2`* **strictly increasing***. The test cases are generated so that the given input always makes it possible.

An array `arr` is **strictly increasing** if and only if $\text{arr}[0] < \text{arr}[1] < \text{arr}[2] < ... < arr[\text{arr.length} - 1]$.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** $nums1 = [1,3,5,4], nums2 = [1,2,3,7]$
- **Output:** `1`
- **Explanation:**
Swap nums1[3] and nums2[3]. Then the sequences are:
nums1 = [1, 3, 5, 7] and nums2 = [1, 2, 3, 4]
which are both strictly increasing.
#### Example 2

- **Input:** $nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]$
- **Output:** `1`
### Constraints

- $2 \le \text{nums1.length} \le 10^{5}$

- $\text{nums2.length} = \text{nums1.length}$

- $0 \le \text{nums1}[i], \text{nums2}[i] \le 2 * 10^{5}$