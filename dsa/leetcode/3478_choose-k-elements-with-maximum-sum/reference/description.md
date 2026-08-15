### 1. Description

You are given two integer arrays, `nums1` and `nums2`, both of length `n`, along with a positive integer `k`.

For each index `i` from `0` to $n - 1$, perform the following:

- Find **all** indices `j` where $\text{nums1}[j]$ is less than $\text{nums1}[i]$.

- Choose **at most** `k` values of $\text{nums2}[j]$ at these indices to **maximize** the total sum.

Return an array `answer` of size `n`, where $\text{answer}[i]$ represents the result for the corresponding index `i`.

### 2. Function Contract

**Inputs**

- `nums1`: Input parameter (`List[int]`).
- `nums2`: Input parameter (`List[int]`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `List[int]`.

### 3. Examples

#### Example 1

- **Input:** nums1 = [4,2,1,5,3], nums2 = [10,20,30,40,50], k = 2

- **Output:** [80,30,0,80,50]

- **Explanation:** 

- For $i = 0$: Select the 2 largest values from `nums2` at indices `[1, 2, 4]` where $\text{nums1}[j] < \text{nums1}[0]$, resulting in $50 + 30 = 80$.

- For $i = 1$: Select the 2 largest values from `nums2` at index `[2]` where $\text{nums1}[j] < \text{nums1}[1]$, resulting in 30.

- For $i = 2$: No indices satisfy $\text{nums1}[j] < \text{nums1}[2]$, resulting in 0.

- For $i = 3$: Select the 2 largest values from `nums2` at indices `[0, 1, 2, 4]` where $\text{nums1}[j] < \text{nums1}[3]$, resulting in $50 + 30 = 80$.

- For $i = 4$: Select the 2 largest values from `nums2` at indices `[1, 2]` where $\text{nums1}[j] < \text{nums1}[4]$, resulting in $30 + 20 = 50$.

#### Example 2

- **Input:** nums1 = [2,2,2,2], nums2 = [3,1,2,3], k = 1

- **Output:** [0,0,0,0]

- **Explanation:** Since all elements in `nums1` are equal, no indices satisfy the condition $\text{nums1}[j] < \text{nums1}[i]$ for any `i`, resulting in 0 for all positions.

### 4. Constraints

- $n = \text{nums1.length} = \text{nums2.length}$

- $1 \le n \le 10^{5}$

- $1 \le \text{nums1}[i], \text{nums2}[i] \le 10^{6}$

- $1 \le k \le n$
