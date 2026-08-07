## Description

You are given two integer arrays `nums1` and `nums2` of size `n`.

You can perform the following two operations any number of times on these two arrays:

- **Swap within the same array**: Choose two indices `i` and `j`. Then, choose either to swap $\text{nums1}[i]$ and $\text{nums1}[j]$, or $\text{nums2}[i]$ and $\text{nums2}[j]$. This operation is **free of charge**.

- **Swap between two arrays**: Choose an index `i`. Then, swap $\text{nums1}[i]$ and $\text{nums2}[i]$. This operation **incurs a cost of 1**.

Return an integer denoting the **minimum cost** to make `nums1` and `nums2` **identical**. If this is not possible, return -1.
### Function Contract

**Inputs**

- `nums1`: The first array of positive integers.
- `nums2`: The second array of positive integers, with the same length as `nums1`.

Let $N=\lvert\texttt{nums1}\rvert=\lvert\texttt{nums2}\rvert$. A free operation may reorder either array independently. A paid operation exchanges the two values currently occupying one shared index; the free operations may be used before or after it to position any desired pair of values at that index.

**Return value**

Return the minimum number of paid between-array swaps required to make the two arrays identical. Return `-1` if equality is impossible. Free swaps do not contribute to the returned cost.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums1 = [10,20], nums2 = [20,10]

**Output:** 0

**Explanation:**

- Swap $\text{nums2}[0] = 20$ and $\text{nums2}[1] = 10$.

		<li>`nums2` becomes `[10, 20]`.

- This operation is free of charge.

	</li>
- `nums1` and `nums2` are now identical. The cost is 0.

</div>
#### Example 2

<div class="example-block">
**Input:** nums1 = [10,10], nums2 = [20,20]

**Output:** 1

**Explanation:**

- Swap $\text{nums1}[0] = 10$ and $\text{nums2}[0] = 20$.

		<li>`nums1` becomes `[20, 10]`.

- `nums2` becomes `[10, 20]`.

- This operation costs 1.

	</li>
- Swap $\text{nums2}[0] = 10$ and $\text{nums2}[1] = 20$.

		<li>`nums2` becomes `[20, 10]`.

- This operation is free of charge.

	</li>
- `nums1` and `nums2` are now identical. The cost is 1.

</div>
#### Example 3

<div class="example-block">
**Input:** nums1 = [10,20], nums2 = [30,40]

**Output:** -1

**Explanation:**

It is impossible to make the two arrays identical. Therefore, the answer is -1.

</div>
### Constraints

- $2 \le n = \text{nums1.length} = \text{nums2.length} \le 8 * 10^{4}$

- $1 \le \text{nums1}[i], \text{nums2}[i] \le 8 * 10^{4}$