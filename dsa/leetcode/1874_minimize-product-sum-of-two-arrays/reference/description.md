## Description

The **product sum **of two equal-length arrays `a` and `b` is equal to the sum of $a[i] * b[i]$ for all $0 \le i < \text{a.length}$ (**0-indexed**).

- For example, if $a = [1,2,3,4]$ and $b = [5,2,3,1]$, the **product sum** would be $1*5 + 2*2 + 3*3 + 4*1 = 22$.

Given two arrays `nums1` and `nums2` of length `n`, return *the **minimum product sum** if you are allowed to **rearrange** the **order** of the elements in *`nums1`.
### Function Contract

- Refer to method signature.

### Examples

#### Example 1

- **Input:** $nums1 = [5,3,4,2], nums2 = [4,2,2,5]$
- **Output:** `40`
- **Explanation:** We can rearrange nums1 to become [3,5,4,2]. The product sum of [3,5,4,2] and [4,2,2,5] is 3*4 + 5*2 + 4*2 + 2*5 = 40.
#### Example 2

- **Input:** $nums1 = [2,1,4,5,7], nums2 = [3,2,4,8,6]$
- **Output:** `65`
- **Explanation:** We can rearrange nums1 to become [5,7,4,1,2]. The product sum of [5,7,4,1,2] and [3,2,4,8,6] is 5*3 + 7*2 + 4*4 + 1*8 + 2*6 = 65.
### Constraints

- $n = \text{nums1.length} = \text{nums2.length}$

- $1 \le n \le 10^{5}$

- $1 \le \text{nums1}[i], \text{nums2}[i] \le 100$