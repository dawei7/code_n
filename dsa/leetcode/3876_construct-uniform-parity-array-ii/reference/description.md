## Description

You are given an array `nums1` of `n` **distinct** integers.

You want to construct another array `nums2` of length `n` such that the elements in `nums2` are either **all odd or all even**.

For each index `i`, you must choose **exactly one** of the following (in any order):

- $\text{nums2}[i] = \text{nums1}[i]$​​​​​​​

- $\text{nums2}[i] = \text{nums1}[i] - \text{nums1}[j]$, for an index $j \neq i$, such that $\text{nums1}[i] - \text{nums1}[j] \ge 1$

Return `true` if it is possible to construct such an array, otherwise return `false`.
### Function Contract

**Inputs**

- `nums1`: A non-empty array of distinct positive integers from which every `nums2` entry must be formed.

Each output position may retain its corresponding input value or subtract the value at a different input index. A subtraction is legal only when its result is positive, so the minuend must be strictly greater than the selected subtrahend.

Let $n=\lvert\texttt{nums1}\rvert$.

**Return value**

Return `true` if one legal choice per index can make every constructed value odd or every constructed value even. Return `false` if neither common parity is achievable.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums1 = [1,4,7]

**Output:** true

**Explanation:**​​​​​​​​​​​​​​

- Set $\text{nums2}[0] = \text{nums1}[0] = 1$.

- Set $\text{nums2}[1] = \text{nums1}[1] - \text{nums1}[0] = 4 - 1 = 3$.

- Set $\text{nums2}[2] = \text{nums1}[2] = 7$.

- $nums2 = [1, 3, 7]$, and all elements are odd. Thus, the answer is `true`.

</div>
#### Example 2

<div class="example-block">
**Input:** nums1 = [2,3]

**Output:** false

**Explanation:**

It is not possible to construct `nums2` such that all elements have the same parity. Thus, the answer is `false`.

</div>
#### Example 3

<div class="example-block">
**Input:** nums1 = [4,6]

**Output:** true

**Explanation:**

- Set $\text{nums2}[0] = \text{nums1}[0] = 4$.

- Set $\text{nums2}[1] = \text{nums1}[1] = 6$.

- $nums2 = [4, 6]$, and all elements are even. Thus, the answer is `true`.

</div>
### Constraints

- $1 \le n = \text{nums1.length} \le 10^{5}$

- $1 \le \text{nums1}[i] \le 10^{9}$

- `nums1` consists of distinct integers.