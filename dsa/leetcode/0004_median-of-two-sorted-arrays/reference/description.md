## Description

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be `O(log (m+n))`.
### Function Contract

**Inputs**

- `nums1`: The first ascending-sorted integer array.
- `nums2`: The second ascending-sorted integer array.

Let $m = \lvert\texttt{nums1}\rvert$ and $n = \lvert\texttt{nums2}\rvert$.

**Return value**

Return the median of all values from both arrays as a floating-point number.

### Examples

#### Example 1

- **Input:** $nums1 = [1,3], nums2 = [2]$
- **Output:** `2.00000`
- **Explanation:** merged array = [1,2,3] and median is 2.
#### Example 2

- **Input:** $nums1 = [1,2], nums2 = [3,4]$
- **Output:** `2.50000`
- **Explanation:** merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
### Constraints

- $\text{nums1.length} = m$

- $\text{nums2.length} = n$

- $0 \le m \le 1000$

- $0 \le n \le 1000$

- $1 \le m + n \le 2000$

- $-10^{6} \le \text{nums1}[i], \text{nums2}[i] \le 10^{6}$